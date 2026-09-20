"""
Convenience CLI utility to register, inspect, and manage Telegram Webhooks
for the English Buddy Vercel Serverless Deployment.

Usage:
    python scripts/set_webhook.py set <VERCEL_URL>
    python scripts/set_webhook.py info
    python scripts/set_webhook.py delete
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import ssl
import sys
import urllib.parse
import urllib.request
import certifi
from dotenv import load_dotenv

# Ensure Windows terminal doesn't crash on emoji characters
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Ensure repository root is accessible and load credentials from root .env
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

load_dotenv(ROOT_DIR / ".env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip().strip("'\"")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "").strip().strip("'\"")


def get_ssl_context():
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx
    except Exception:
        return ssl._create_unverified_context()


def check_token() -> str:
    if not BOT_TOKEN:
        print("❌ Error: TELEGRAM_BOT_TOKEN is not set in .env and not passed via --token")
        sys.exit(1)
    return BOT_TOKEN


def api_request(method: str, params: dict | None = None) -> dict:
    token = check_token()
    base_url = f"https://api.telegram.org/bot{token}/{method}"
    ctx = get_ssl_context()

    if params:
        data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(base_url, data=data, method="POST")
    else:
        req = urllib.request.Request(base_url, method="GET")

    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        err_msg = err.read().decode("utf-8")
        try:
            return json.loads(err_msg)
        except Exception:
            return {"ok": False, "description": err_msg}
    except Exception as exc:
        return {"ok": False, "description": str(exc)}


def set_webhook(vercel_url: str):
    url = vercel_url.strip().rstrip("/")
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    # Ensure it points to the webhook path
    if not url.endswith("/api/webhook"):
        if url.endswith("/api"):
            url = f"{url}/webhook"
        else:
            url = f"{url}/api/webhook"

    print(f"\n📡 Registering Webhook with Telegram...")
    print(f"   Target URL: {url}")
    if WEBHOOK_SECRET:
        print(f"   Secret Token: Configured (X-Telegram-Bot-Api-Secret-Token enabled)")
    else:
        print(f"   Secret Token: ⚠️ None (Consider setting WEBHOOK_SECRET in .env & Vercel)")

    params = {"url": url}
    if WEBHOOK_SECRET:
        params["secret_token"] = WEBHOOK_SECRET

    res = api_request("setWebhook", params)
    if res.get("ok"):
        print(f"✅ SUCCESS: {res.get('description', 'Webhook was set')}\n")
    else:
        print(f"❌ FAILED: {res.get('description', 'Unknown error')}\n")

    # Automatically print status
    get_info()


def get_info():
    print("🔍 Fetching Telegram Webhook Status...")
    res = api_request("getWebhookInfo")
    if res.get("ok"):
        info = res.get("result", {})
        print("--------------------------------------------------")
        print(f"   Status URL:             {info.get('url') or '(none - polling mode)'}")
        print(f"   Custom Certificate:     {info.get('has_custom_certificate')}")
        print(f"   Pending Updates:        {info.get('pending_update_count', 0)}")
        if info.get("last_error_date"):
            print(f"   ⚠️ Last Error:           {info.get('last_error_message')}")
        if info.get("ip_address"):
            print(f"   Resolved IP:            {info.get('ip_address')}")
        print("--------------------------------------------------")
    else:
        print(f"❌ Could not fetch status: {res.get('description')}")


def delete_webhook():
    print("\n🗑️ Deleting Webhook (Switching back to polling mode)...")
    res = api_request("deleteWebhook", {"drop_pending_updates": "false"})
    if res.get("ok"):
        print(f"✅ SUCCESS: {res.get('description', 'Webhook deleted')}")
        print("   You can now run 'python bot.py' locally without conflict.")
    else:
        print(f"❌ FAILED: {res.get('description')}")


def setup_profile():
    print("\n📝 Updating Telegram Bot Profile ('What can this bot do?')...")
    import config
    from handlers import (
        get_bot_description_en,
        get_bot_description_id,
        get_bot_short_desc_en,
        get_bot_short_desc_id,
        BOT_COMMANDS,
    )

    # Determine bot identity dynamically via getMe API call using active token
    bot_name = ""
    bot_username = ""
    me_res = api_request("getMe")
    if me_res.get("ok"):
        result = me_res.get("result", {})
        bot_name = result.get("first_name", "").strip()
        bot_username = result.get("username", "").strip()

    if not bot_name:
        bot_name = os.getenv("BOT_NAME", "").strip() or config.BOT_NAME
    if not bot_username:
        bot_username = os.getenv("BOT_USERNAME", "").strip() or config.BOT_USERNAME

    print(f"🤖 Adapting profile descriptions for bot: '{bot_name}' (@{bot_username})")

    desc_en = get_bot_description_en(bot_name=bot_name, bot_username=bot_username)
    desc_id = get_bot_description_id(bot_name=bot_name, bot_username=bot_username)
    short_en = get_bot_short_desc_en(bot_name=bot_name, bot_username=bot_username)
    short_id = get_bot_short_desc_id(bot_name=bot_name, bot_username=bot_username)

    r1 = api_request("setMyDescription", {"description": desc_en})
    r2 = api_request("setMyDescription", {"description": desc_id, "language_code": "id"})
    r3 = api_request("setMyShortDescription", {"short_description": short_en})
    r4 = api_request("setMyShortDescription", {"short_description": short_id, "language_code": "id"})
    commands = json.dumps([
        {"command": cmd.command, "description": cmd.description}
        for cmd in BOT_COMMANDS
    ])
    r5 = api_request("setMyCommands", {"commands": commands})

    if r1.get("ok") and r2.get("ok") and r3.get("ok") and r4.get("ok") and r5.get("ok"):
        print(f"✅ SUCCESS: Telegram bot profile for '{bot_name}' (@{bot_username}) updated successfully!")
    else:
        errors = []
        for name, r in [("desc_en", r1), ("desc_id", r2), ("short_en", r3), ("short_id", r4), ("commands", r5)]:
            if not r.get("ok"):
                errors.append(f"{name}: {r.get('description', 'failed')}")
        print(f"⚠️ Profile update status: {', '.join(errors) if errors else 'all applied'}")


def main():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--token", help="Override Telegram Bot Token from .env")
    parent_parser.add_argument("--secret", help="Override Webhook Secret Token from .env")

    parser = argparse.ArgumentParser(
        description="Manage Telegram Bot Webhook for Vercel",
        parents=[parent_parser],
    )
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    set_parser = subparsers.add_parser(
        "set",
        help="Set the webhook to your Vercel URL",
        parents=[parent_parser],
    )
    set_parser.add_argument("url", nargs="?", help="Your Vercel deployment URL (e.g., https://my-app.vercel.app)")

    subparsers.add_parser("info", help="Check current webhook registration status", parents=[parent_parser])
    subparsers.add_parser("delete", help="Delete webhook (use before running local bot.py)", parents=[parent_parser])
    subparsers.add_parser("profile", help="Update bot description and commands on Telegram", parents=[parent_parser])

    args = parser.parse_args()

    global BOT_TOKEN, WEBHOOK_SECRET
    if args.token:
        BOT_TOKEN = args.token.strip().strip("'\"")
    if args.secret:
        WEBHOOK_SECRET = args.secret.strip().strip("'\"")

    if args.action == "set":
        url = args.url
        if not url:
            url = input("Enter your deployed Vercel domain (e.g., https://my-app.vercel.app): ").strip()
        set_webhook(url)
    elif args.action == "info":
        get_info()
    elif args.action == "delete":
        delete_webhook()
    elif args.action == "profile":
        setup_profile()
    else:
        # If no arguments provided, show menu
        print("\n🤖 English Buddy - Webhook Setup Utility\n")
        print("1. Set Webhook (Connect Vercel to Telegram)")
        print("2. Check Webhook Info (Verify status)")
        print("3. Delete Webhook (Switch back to local polling)")
        print("4. Update Bot Profile ('What can this bot do?')")
        print("5. Exit")
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            url = input("Enter your Vercel URL (e.g. https://my-bot.vercel.app): ").strip()
            if url:
                set_webhook(url)
        elif choice == "2":
            get_info()
        elif choice == "3":
            delete_webhook()
        elif choice == "4":
            setup_profile()
        else:
            print("Exiting.")


if __name__ == "__main__":
    main()
