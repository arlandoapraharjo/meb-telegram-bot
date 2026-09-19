"""
Convenience CLI utility to register, inspect, and manage Telegram Webhooks
for the English Buddy Vercel Serverless Deployment.

Usage:
    python set_webhook.py set <VERCEL_URL>
    python set_webhook.py info
    python set_webhook.py delete
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request
import certifi
from dotenv import load_dotenv

# Ensure Windows terminal doesn't crash on emoji characters
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Load credentials from .env
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "").strip()


def get_ssl_context():
    try:
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl._create_unverified_context()


def check_token() -> str:
    if not BOT_TOKEN:
        print("❌ Error: TELEGRAM_BOT_TOKEN is not set in .env")
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


def main():
    parser = argparse.ArgumentParser(description="Manage Telegram Bot Webhook for Vercel")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    set_parser = subparsers.add_parser("set", help="Set the webhook to your Vercel URL")
    set_parser.add_argument("url", nargs="?", help="Your Vercel deployment URL (e.g., https://my-app.vercel.app)")

    subparsers.add_parser("info", help="Check current webhook registration status")
    subparsers.add_parser("delete", help="Delete webhook (use before running local bot.py)")

    args = parser.parse_args()

    if args.action == "set":
        url = args.url
        if not url:
            url = input("Enter your deployed Vercel domain (e.g., https://my-app.vercel.app): ").strip()
        set_webhook(url)
    elif args.action == "info":
        get_info()
    elif args.action == "delete":
        delete_webhook()
    else:
        # If no arguments provided, show menu
        print("\n🤖 English Buddy - Webhook Setup Utility\n")
        print("1. Set Webhook (Connect Vercel to Telegram)")
        print("2. Check Webhook Info (Verify status)")
        print("3. Delete Webhook (Switch back to local polling)")
        print("4. Exit")
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            url = input("Enter your Vercel URL (e.g. https://my-bot.vercel.app): ").strip()
            if url:
                set_webhook(url)
        elif choice == "2":
            get_info()
        elif choice == "3":
            delete_webhook()
        else:
            print("Exiting.")


if __name__ == "__main__":
    main()
