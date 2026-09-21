"""
FastAPI Serverless Webhook Entrypoint for English Buddy Telegram Bot.
Configured for Vercel Python Runtime.

Endpoints:
- GET / & GET /api: Health check returning {"status": "healthy"}.
- POST /api/webhook & POST /webhook: Validates X-Telegram-Bot-Api-Secret-Token,
  deserializes Telegram Updates, processes them asynchronously, and returns
  fast HTTP 200 {"status": "ok"} to prevent retry storms.
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
import logging
import os
from pathlib import Path
import secrets
import sys

from fastapi import FastAPI, Header, HTTPException, Request, status
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)
from telegram.request import HTTPXRequest

# Ensure project root directory is in sys.path for serverless imports
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import config  # noqa: E402
import content_bank  # noqa: E402
from bot import TokenRedactingFilter  # noqa: E402
from handlers import (  # noqa: E402
    global_error_handler,
    help_command,
    hint_command,
    menu_callback_handler,
    start_command,
    text_message_handler,
)

# Logging configuration for serverless functions with credential scrubbing
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
root_logger = logging.getLogger()
_token_for_redact = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
_api_key_for_redact = os.getenv("GEMINI_API_KEY", "").strip()
if _token_for_redact or _api_key_for_redact:
    root_logger.addFilter(
        TokenRedactingFilter(token=_token_for_redact, api_key=_api_key_for_redact)
    )

logger = logging.getLogger("english_buddy_webhook")



def create_ptb_application() -> Application:
    """
    Builds and registers handlers on the python-telegram-bot Application instance.
    Does NOT trigger run_polling().
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip().strip("'\"")
    if not token:
        logger.error(
            "CRITICAL: TELEGRAM_BOT_TOKEN is missing or empty! "
            "Configure TELEGRAM_BOT_TOKEN in your Vercel Project Settings."
        )

    # Configure resilient HTTPX timeout parameters
    request_config = HTTPXRequest(
        connection_pool_size=8,
        connect_timeout=config.HTTPX_CONNECT_TIMEOUT,
        read_timeout=config.HTTPX_READ_TIMEOUT,
        write_timeout=config.HTTPX_WRITE_TIMEOUT,
        pool_timeout=config.HTTPX_POOL_TIMEOUT,
    )

    application = (
        ApplicationBuilder()
        .token(token)
        .request(request_config)
        .build()
    )

    # 1. Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("hint", hint_command))
    application.add_handler(CommandHandler("help", help_command))

    # 2. Register callback query handlers (6 learning tracks + level selector)
    application.add_handler(CallbackQueryHandler(menu_callback_handler))

    # 3. Register text message handler with private chat & text filter
    application.add_handler(
        MessageHandler(
            filters.ChatType.PRIVATE & filters.TEXT & (~filters.COMMAND),
            text_message_handler,
        )
    )

    # 4. Register global error handler to prevent unhandled 500 crashes
    application.add_error_handler(global_error_handler)

    return application


# Global application state and async initialization lock
_ptb_app: Application | None = None
_init_lock = asyncio.Lock()


async def get_ptb_app() -> Application:
    """
    Retrieves or lazily initializes the Application instance in an async context.
    Guarantees initialize() and start() are called once before processing updates.
    """
    global _ptb_app
    if _ptb_app is None or not _ptb_app._initialized:
        async with _init_lock:
            if _ptb_app is None:
                _ptb_app = create_ptb_application()

            if not _ptb_app._initialized:
                await _ptb_app.initialize()
                await _ptb_app.start()
                logger.info(
                    "PTB Application initialized and started for webhook processing."
                )

    return _ptb_app



@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    """
    FastAPI lifespan manager to warm up the Telegram bot instance on startup
    and gracefully close connections when the serverless container terminates.
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if bot_token:
        try:
            await get_ptb_app()
        except Exception as exc:
            logger.warning("Bot warmup during startup encountered error: %s", exc)

    yield

    # Shutdown routine
    try:
        if _ptb_app is not None and _ptb_app._initialized:
            await _ptb_app.stop()
            await _ptb_app.shutdown()
            logger.info("PTB Application shutdown complete.")
    except Exception as exc:
        logger.warning("Error during PTB shutdown: %s", exc)


# Initialize FastAPI ASGI App
app = FastAPI(
    title=f"{config.BOT_NAME} Telegram Bot - Vercel Serverless Webhook",
    lifespan=lifespan,
    redirect_slashes=False,
)


INDEX_HTML_PATH = ROOT_DIR / "public" / "index.html"
if not INDEX_HTML_PATH.is_file() and (ROOT_DIR / "index.html").is_file():
    INDEX_HTML_PATH = ROOT_DIR / "index.html"

_raw_html_template: str | None = None


def get_landing_html() -> str:
    """
    Renders the crafted status portal landing page with dynamic bot configuration.
    Dynamically injects the display handle (@<BOT_USERNAME>) into the copy pill,
    the canonical URL (https://t.me/<BOT_USERNAME>) into the CTA button,
    and the configured bot name (<BOT_NAME>) across titles, headings, and meta tags.
    """
    global _raw_html_template
    if _raw_html_template is None:
        if INDEX_HTML_PATH.is_file():
            _raw_html_template = INDEX_HTML_PATH.read_text(encoding="utf-8")
        else:
            _raw_html_template = (
                "<!DOCTYPE html><html><body style='background:#07060a;color:#f4f4f5;"
                "font-family:sans-serif;padding:40px;text-align:center;'>"
                "<h1>{{BOT_NAME}}</h1><p style='color:#10b981;'>● Webhook Active &amp; Operational</p>"
                "</body></html>"
            )

    bot_name = getattr(config, "BOT_NAME", "Mebby").strip() or "Mebby"
    clean_username = getattr(config, "BOT_USERNAME", "").strip().lstrip("@")
    if not clean_username:
        clean_username = (
            os.getenv("BOT_USERNAME")
            or os.getenv("TELEGRAM_BOT_USERNAME")
            or "EnglishBuddy_Practice_Bot"
        ).strip().lstrip("@")
    if not clean_username:
        clean_username = "EnglishBuddy_Practice_Bot"

    display_handle = f"@{clean_username}"
    telegram_url = f"https://t.me/{clean_username}"

    # Perform on-the-fly injection on template before returning HTMLResponse
    content = _raw_html_template
    # 1. Update canonical Telegram deep-links
    content = content.replace("https://t.me/EnglishBuddy_Practice_Bot", telegram_url)
    content = content.replace("https://t.me/EnglishBuddyBot", telegram_url)
    # 2. Update display chips and labels with @ prefix
    content = content.replace("@EnglishBuddy_Practice_Bot", display_handle)
    content = content.replace("@EnglishBuddyBot", display_handle)
    # 3. Update template placeholders if present
    content = content.replace("{{BOT_NAME}}", bot_name)
    content = content.replace("{{BOT_USERNAME}}", clean_username)
    # 4. Update any remaining plain identifiers
    content = content.replace("EnglishBuddy_Practice_Bot", clean_username)
    content = content.replace("EnglishBuddyBot", clean_username)
    # 5. Update specific bot name occurrences
    content = content.replace("<title>Mebby — Status & Portal</title>", f"<title>{bot_name} — Status & Portal</title>")
    content = content.replace("Operational status for Mebby", f"Operational status for {bot_name}")
    content = content.replace('alt="Mebby Mascot"', f'alt="{bot_name} Mascot"')
    content = content.replace("<span>Mebby</span>", f"<span>{bot_name}</span>")
    content = content.replace("<h1>Mebby</h1>", f"<h1>{bot_name}</h1>")

    return content


@app.get("/")
@app.get("/api")
@app.get("/api/index")
@app.get("/api/index.py")
@app.get("/api/webhook")
async def health_check(request: Request):
    """
    Health check & status dashboard:
    - Returns rich 21st.dev craft HTML landing page when opened in a web browser (Accept: text/html).
    - Returns fast JSON {"status": "healthy"} for automated uptime monitoring and API clients.
    """
    accept = request.headers.get("accept", "").lower()
    fmt = request.query_params.get("format", "").lower()

    # Dedicated JSON response for monitoring probes, curl, or format=json
    if fmt == "json" or "application/json" in accept or "curl" in request.headers.get("user-agent", "").lower():
        gemini_key = os.getenv("GEMINI_API_KEY", "").strip()
        bot_name = getattr(config, "BOT_NAME", "Mebby").strip() or "Mebby"
        clean_username = getattr(config, "BOT_USERNAME", "").strip().lstrip("@")
        if not clean_username:
            clean_username = (
                os.getenv("BOT_USERNAME")
                or os.getenv("TELEGRAM_BOT_USERNAME")
                or "EnglishBuddy_Practice_Bot"
            ).strip().lstrip("@")
        if not clean_username:
            clean_username = "EnglishBuddy_Practice_Bot"

        return {
            "status": "healthy",
            "bot_name": bot_name,
            "gemini_active": bool(gemini_key),
            "gemini_model": (os.getenv("GEMINI_MODEL", "").strip() or "gemini-3.8-flash") if gemini_key else None,
            "bot_username": clean_username,
            "bot_handle": f"@{clean_username}",
            "telegram_url": f"https://t.me/{clean_username}",
            "content_bank_exercises": content_bank.TOTAL_EXERCISES,
        }

    # Browser navigation: return crafted minimal landing page
    if "text/html" in accept or request.url.path in ("/", "/api"):
        return HTMLResponse(content=get_landing_html(), status_code=200)

    gemini_key = os.getenv("GEMINI_API_KEY", "").strip()
    return {
        "status": "healthy",
        "gemini_active": bool(gemini_key),
    }


@app.get("/mascot.png")
@app.get("/icon.png")
@app.get("/favicon.png")
@app.get("/favicon.ico")
async def get_brand_icon(request: Request):
    """Serves brand mascot & favicon assets."""
    filename = Path(request.url.path).name
    target = ROOT_DIR / "public" / filename
    if not target.is_file():
        target = ROOT_DIR / "public" / "icon.png"
    if target.is_file():
        media_type = "image/x-icon" if target.suffix == ".ico" else "image/png"
        return FileResponse(target, media_type=media_type)
    raise HTTPException(status_code=404, detail="Asset not found")


@app.post("/api/webhook")
@app.post("/api/webhook/")
@app.post("/webhook")
@app.post("/webhook/")
@app.post("/api/index")
@app.post("/api/index.py")
@app.post("/")
async def telegram_webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str | None = Header(
        None, alias="X-Telegram-Bot-Api-Secret-Token"
    ),
):

    """
    POST /api/webhook: Main Telegram Webhook endpoint.
    - Validates X-Telegram-Bot-Api-Secret-Token against WEBHOOK_SECRET.
    - Deserializes Update payload via Update.de_json(data, bot).
    - Processes update asynchronously via await app.process_update(update).
    - Returns HTTP 200 {"status": "ok"} immediately to prevent retry storms.
    """
    webhook_secret = os.getenv("WEBHOOK_SECRET", "").strip().strip("'\"")

    # 1. Security check: Validate Telegram secret token
    if webhook_secret:
        token_header = (
            x_telegram_bot_api_secret_token
            or request.headers.get("x-telegram-bot-api-secret-token")
        )
        if not token_header or not secrets.compare_digest(token_header, webhook_secret):
            logger.warning(
                "Rejected unauthorized webhook request: "
                "invalid or missing secret token."
            )

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid secret token",
            )
    else:
        logger.warning(
            "WEBHOOK_SECRET is not configured in environment variables. "
            "Proceeding without secret token validation."
        )

    # 2. Guard against oversized payloads (DoS protection: max 512KB)
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > 524288:
        logger.warning("Rejected payload exceeding max size limit (512KB).")
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Payload too large",
        )

    # 3. Parse incoming JSON payload
    try:
        payload = await request.json()

    except Exception as exc:
        logger.error("Failed to parse JSON from incoming webhook request: %s", exc)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Invalid JSON payload"},
        )

    # 3. Retrieve or initialize the PTB Application instance
    try:
        ptb_instance = await get_ptb_app()
    except Exception as exc:
        logger.critical("Failed to retrieve initialized PTB application: %s", exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Bot initialization failure"},
        )

    # 4. Deserialize and process the Telegram Update safely
    try:
        update = Update.de_json(data=payload, bot=ptb_instance.bot)
        if update is not None:
            await ptb_instance.process_update(update)
        else:
            logger.warning(
                "Payload could not be deserialized into a Telegram Update: %s", payload
            )
    except Exception as exc:
        logger.exception("Unhandled exception during update processing: %s", exc)
        # Return HTTP 200 so Telegram will not trigger repeated retry loops
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": "ok", "error": "Internal update error caught"},
        )

    # 5. Immediate 200 OK response
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})

