"""
Main Application Entrypoint for English Buddy Telegram Bot.

Features:
- Validates bot token on startup and terminates safely if missing or invalid.
- Custom logging filter to redact bot tokens from all log outputs.
- Configures HTTPXRequest timeouts for network resilience.
- Registers command, callback query, and text message handlers.
- Runs periodic rate-limiter cleanup in an asyncio background task.
- Initializes long polling with graceful shutdown handling.
"""

from __future__ import annotations

import asyncio
import logging
import re
import sys

from telegram.error import InvalidToken
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)
from telegram.request import HTTPXRequest

import config
from handlers import (
    global_error_handler,
    help_command,
    menu_callback_handler,
    setup_bot_profile,
    start_command,
    text_message_handler,
)
from rate_limiter import global_rate_limiter

_LOG_CREDENTIAL_PATTERNS = [
    (re.compile(r"\d{7,12}:[A-Za-z0-9_-]{30,50}"), "***REDACTED_BOT_TOKEN***"),
    (re.compile(r"AIza[0-9A-Za-z-_]{30,45}"), "***REDACTED_GEMINI_API_KEY***"),
]


class TokenRedactingFilter(logging.Filter):
    """
    Security logging filter that redacts both Telegram bot tokens
    and Gemini API keys (exact matches and regex patterns) from any log message or URL.
    """

    def __init__(self, token: str | None = None, api_key: str | None = None) -> None:
        super().__init__()
        self.token = token.strip() if token else ""
        self.api_key = api_key.strip() if api_key else ""


    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()

        # 1. Exact string matches
        if self.token and self.token in msg:
            record.msg = str(record.msg).replace(self.token, "***REDACTED_BOT_TOKEN***")
        if self.api_key and self.api_key in msg:
            record.msg = str(record.msg).replace(
                self.api_key, "***REDACTED_GEMINI_API_KEY***"
            )

        # 2. Pattern matches for tokens embedded in URLs or debug dumps
        for pattern, replacement in _LOG_CREDENTIAL_PATTERNS:
            if pattern.search(str(record.msg)):
                record.msg = pattern.sub(replacement, str(record.msg))

        return True


def setup_logging(
    token: str | None = None,
    api_key: str | None = None,
) -> logging.Logger:
    """Configures structured application logging with credential redaction."""

    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    # Attach credential redaction filter to root logger
    root_logger = logging.getLogger()
    if token or api_key:
        root_logger.addFilter(TokenRedactingFilter(token=token, api_key=api_key))

    # Reduce noisy logs from external libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("google").setLevel(logging.WARNING)
    logging.getLogger("telegram.ext.Application").setLevel(logging.INFO)

    return logging.getLogger("english_buddy_bot")


async def post_init(application: Application) -> None:
    """
    Called after application is initialized and before polling starts.
    Starts background maintenance tasks.
    """
    logger = logging.getLogger(__name__)

    async def periodic_rate_limit_cleanup() -> None:
        """Background coroutine to periodically purge stale rate limit records."""
        logger.info(
            "Rate limiter cleanup task started (Interval: %.1fs).",
            config.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS,
        )
        while True:
            try:
                await asyncio.sleep(config.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS)
                await global_rate_limiter.cleanup_stale()
            except asyncio.CancelledError:
                logger.info("Rate limiter cleanup task received cancellation.")
                break
            except Exception as exc:
                logger.error("Unexpected error in rate limiter cleanup task: %s", exc)

    cleanup_task = asyncio.create_task(
        periodic_rate_limit_cleanup(),
        name="rate_limiter_stale_cleanup",
    )
    application.bot_data["cleanup_task"] = cleanup_task

    # Synchronize 'What can this bot do?' profile description and commands with Telegram
    await setup_bot_profile(application.bot)


async def post_shutdown(application: Application) -> None:
    """
    Gracefully cleans up background tasks upon application shutdown.
    """
    logger = logging.getLogger(__name__)
    cleanup_task: asyncio.Task | None = application.bot_data.get("cleanup_task")

    if cleanup_task and not cleanup_task.done():
        logger.info("Canceling rate limiter background task...")
        cleanup_task.cancel()
        try:
            await cleanup_task
        except asyncio.CancelledError:
            pass
    logger.info("English Buddy Bot shutdown completed.")


def create_bot_application(token: str) -> Application:
    """
    Builds and configures the python-telegram-bot Application instance.
    Configures network timeouts and registers all handlers.
    """
    # 1. Network Resilience: Configure HTTPX timeouts
    request_config = HTTPXRequest(
        connection_pool_size=8,
        connect_timeout=config.HTTPX_CONNECT_TIMEOUT,
        read_timeout=config.HTTPX_READ_TIMEOUT,
        write_timeout=config.HTTPX_WRITE_TIMEOUT,
        pool_timeout=config.HTTPX_POOL_TIMEOUT,
    )

    # 2. Build application with security hooks
    app = (
        ApplicationBuilder()
        .token(token)
        .request(request_config)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    # 3. Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # 4. Register callback query handlers (for learning modes and back to menu)
    app.add_handler(CallbackQueryHandler(menu_callback_handler))

    # 5. Register text message handler with private chat & text filter
    app.add_handler(
        MessageHandler(
            filters.ChatType.PRIVATE & filters.TEXT & (~filters.COMMAND),
            text_message_handler,
        )
    )

    # 6. Register global error handler
    app.add_error_handler(global_error_handler)

    return app


def main() -> None:
    """Startup routine."""
    # Step 1: Validate bot token before doing anything else
    try:
        validated_token = config.validate_bot_token()
    except (RuntimeError, ValueError) as err:
        # Secure exit without leaking trace
        print(f"\n[STARTUP ERROR] {err}\n", file=sys.stderr)
        sys.exit(1)

    # Step 2: Set up logging with credential redaction
    logger = setup_logging(token=validated_token, api_key=config.GEMINI_API_KEY)
    logger.info("Initializing English Buddy Telegram Bot...")

    if config.GEMINI_API_KEY:
        logger.info("Hybrid AI Mode: Enabled (Gemini Model: %s)", config.GEMINI_MODEL)
    else:
        logger.info(
            "Hybrid AI Mode: Running in offline curated bank mode "
            "(GEMINI_API_KEY not set)."
        )


    # Step 3: Create and configure Application
    try:
        app = create_bot_application(validated_token)
    except Exception as exc:
        logger.critical("Failed to build Telegram bot application: %s", exc)
        sys.exit(1)

    # Step 4: Run long polling
    logger.info("Bot successfully initialized. Starting long polling...")
    try:
        app.run_polling(
            allowed_updates=["message", "callback_query"],
            drop_pending_updates=True,  # Discards outdated updates during downtime
        )
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot execution terminated by user.")
    except InvalidToken:
        logger.critical(
            "Telegram rejected the bot token (Unauthorized). "
            "Please verify that you copied the correct, active token "
            "from @BotFather into your '.env' file."
        )
        sys.exit(1)

    except Exception as exc:
        logger.critical("Fatal error while running bot polling: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
