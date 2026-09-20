# 🤖 Mebby — Modular Telegram Learning Bot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vercel](https://img.shields.io/badge/Vercel-black?logo=vercel&logoColor=white)](https://vercel.com/)
[![Telegram Bot API](https://img.shields.io/badge/telegram--bot--api-v21%2B%20(async)-0088cc?logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![Google GenAI](https://img.shields.io/badge/Google%20GenAI-Gemini%20Flash-4285F4?logo=googlegemini&logoColor=white)](https://ai.google.dev/)

A serverless Telegram bot built with **FastAPI** and **python-telegram-bot (v21+ async)**. Configured by default for English practice with **Gemini Flash** and an offline fallback bank (1,000 exercises), designed to be deployed directly to **Vercel** or adapted as a template for other subjects (math, coding, other languages).

## Features

- **5 Practice Tracks:** Daily Conversation, Vocabulary, Grammar, Reading Comprehension, and Challenge.
- **CEFR Level Selection:** Beginner (A1–A2), Intermediate (B1–B2), and Advanced (C1–C2) via inline keyboards.
- **Hybrid Evaluation:** Real-time feedback powered by Gemini Flash; falls back to offline content when unconfigured or rate-limited.
- **Serverless Architecture:** Stateless FastAPI ASGI handler (`api/index.py`) designed for Vercel functions.
- **Security & Abuse Mitigation:**
  - Constant-time verification for `X-Telegram-Bot-Api-Secret-Token`.
  - In-memory sliding window rate limiter (5 requests / 10s per user).
  - Strict payload limits (512 KB) and message input truncation (300 chars).
  - Masked credentials across application logs.

---

## Deployment (Vercel Webhook)

### 1. Configure Environment Variables
Set the following in your Vercel Project Settings:
- `TELEGRAM_BOT_TOKEN`: Token obtained from [@BotFather](https://t.me/BotFather).
- `WEBHOOK_SECRET`: Random string for request validation (generate via `python -c "import secrets; print(secrets.token_urlsafe(32))"`).
- `GEMINI_API_KEY`: *(Optional)* Google AI Studio key. If omitted, the bot runs in offline mode.
- `BOT_NAME` & `BOT_USERNAME`: *(Optional)* Bot branding and handle for the landing portal.

### 2. Deploy
Push to your linked GitHub repository or deploy via CLI:
```bash
vercel --prod

```

### 3. Register Webhook

Point Telegram to your Vercel domain:

```bash
# Using the CLI script
python scripts/set_webhook.py set https://<your-project>.vercel.app

# Or via cURL
curl -F "url=https://<your-project>.vercel.app/api/webhook" \
     -F "secret_token=<YOUR_WEBHOOK_SECRET>" \
     [https://api.telegram.org/bot](https://api.telegram.org/bot)<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook

```

Check status:

```bash
python scripts/set_webhook.py info

```

---

## Local Development (Polling)

To develop locally without webhooks:

```bash
# 1. Clone repository
git clone [https://github.com/arlandoapraharjo/mebby-telegram-bot.git](https://github.com/arlandoapraharjo/mebby-telegram-bot.git)
cd mebby-telegram-bot

# 2. Setup environment
cp .env.example .env
# Fill in TELEGRAM_BOT_TOKEN in .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Remove active webhook (required before polling)
python scripts/set_webhook.py delete

# 5. Start bot
python bot.py

```

---

## Configuration (`.env`)

| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `TELEGRAM_BOT_TOKEN` | **Yes** | — | Telegram Bot API token |
| `WEBHOOK_SECRET` | **Yes (Prod)** | — | Secret token header for webhook validation |
| `BOT_NAME` | No | `Mebby` | Display name in messages and AI persona |
| `BOT_USERNAME` | No | `EnglishBuddy_Practice_Bot` | Telegram handle (without `@`) for portal links |
| `GEMINI_API_KEY` | No | — | Google AI Studio key (runs offline bank if omitted) |
| `GEMINI_MODEL` | No | `gemini-3.8-flash` | Gemini model variant |
| `RATE_LIMIT_MAX_REQUESTS` | No | `5` | Allowed requests per sliding window |
| `RATE_LIMIT_WINDOW_SECONDS` | No | `10.0` | Sliding window duration (seconds) |
| `MAX_MESSAGE_LENGTH` | No | `300` | Max character length for user inputs |

---

## Project Structure

```text
├── api/
│   └── index.py            # FastAPI entrypoint for Vercel serverless webhook
├── exercises/              # Offline exercise bank
│   ├── __init__.py         # Track loader
│   ├── conversation.py     # 200 Conversation exercises
│   ├── vocabulary.py       # 200 Vocabulary exercises
│   ├── grammar.py          # 200 Grammar exercises
│   ├── reading.py          # 200 Reading exercises
│   └── challenge.py        # 200 Challenge exercises
├── frontend/               # Status card preview component (React / Tailwind)
├── public/
│   └── index.html          # Web status portal served at GET /
├── scripts/
│   └── set_webhook.py      # Webhook registration CLI
├── tests/                  # Test suite
├── bot.py                  # Standalone entrypoint for local polling
├── config.py               # Environment configuration
├── content_bank.py         # Offline exercise evaluator
├── gemini_service.py       # Gemini API client & persona prompt
├── handlers.py             # Telegram commands & callback handlers
└── rate_limiter.py         # In-memory sliding window rate limiter

```
