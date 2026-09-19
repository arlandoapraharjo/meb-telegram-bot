# 🤖 English Buddy Telegram Bot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vercel](https://img.shields.io/badge/Vercel-Serverless-black?logo=vercel&logoColor=white)](https://vercel.com/)
[![Telegram Bot API](https://img.shields.io/badge/telegram--bot--api-v21%2B%20(async)-0088cc?logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![Google GenAI](https://img.shields.io/badge/Google%20GenAI-Gemini%203.8%20Flash-4285F4?logo=googlegemini&logoColor=white)](https://ai.google.dev/)

An interactive Telegram bot for English learners built with **FastAPI** and **python-telegram-bot (v21+ async)**, featuring **Gemini 3.8 Flash AI coaching**, an instant **curated offline fallback bank** (108 exercises), and ready for zero-maintenance deployment on **Vercel Serverless Functions**.

---

## ✨ Features

- 💬 **6 Practice Tracks:** Daily Conversation, Vocabulary Builder, Grammar Clinic, Reading Comprehension, Speaking Lab, and Challenge Arena.
- 🎯 **3 CEFR Levels:** Beginner (A1–A2), Intermediate (B1–B2), and Advanced (C1–C2)—switchable anytime via inline buttons.
- ⚡ **Hybrid AI Engine:** Real-time feedback and dynamic exercise generation via Google Gemini 3.8 Flash; automatically falls back to offline exercises if offline or unconfigured.
- ☁️ **Serverless Webhook Ready:** Production-ready FastAPI ASGI entrypoint (`api/index.py`) engineered specifically for Vercel's Python runtime.
- 🛡️ **Production Guardrails:**
  - `X-Telegram-Bot-Api-Secret-Token` authentication with constant-time verification.
  - Automatic 300-character input truncation guardrail.
  - In-memory sliding window rate limiter (5 req / 10s).
  - 512KB DoS payload limiter.
  - Automatic credential scrubbing from all logs and output messages.

---

## 🚀 Deployment (Vercel Serverless Webhook)

### 1. Configure Environment Variables
In your Vercel Project Settings (or via `.env` locally), configure:
- `TELEGRAM_BOT_TOKEN`: Your Telegram Bot Token from [@BotFather](https://t.me/BotFather).
- `WEBHOOK_SECRET`: A custom random string for webhook request validation (e.g., generated with `python -c "import secrets; print(secrets.token_urlsafe(32))"`).
- `GEMINI_API_KEY`: *(Optional)* Google AI Studio API key for dynamic AI coaching.
- `GEMINI_MODEL`: *(Optional)* Gemini model name (defaults to `gemini-3.8-flash`).

### 2. Deploy to Vercel
Push to GitHub to trigger automatic deployment, or deploy directly via Vercel CLI:
```bash
vercel --prod
```

### 3. Register Webhook with Telegram
Point Telegram to your Vercel deployment URL using the included helper utility:
```bash
# Option A: Using the CLI helper (Recommended)
python set_webhook.py set https://<your-vercel-domain>.vercel.app

# Option B: Using cURL
curl -F "url=https://<your-vercel-domain>.vercel.app/api/webhook" \
     -F "secret_token=<YOUR_WEBHOOK_SECRET>" \
     https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook
```

Verify webhook registration:
```bash
python set_webhook.py info
# Or via curl:
# curl https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/getWebhookInfo
```

---

## 💻 Local Development (Polling Mode)

If you prefer running the bot locally with long-polling during development:

```bash
# 1. Clone repository
git clone https://github.com/arlandoapraharjo/meb-telegram-bot.git
cd meb-telegram-bot

# 2. Set up environment
cp .env.example .env
# Edit .env and insert your TELEGRAM_BOT_TOKEN

# 3. Install dependencies
pip install -r requirements.txt

# 4. If webhook was previously set, unregister it for local polling:
python set_webhook.py delete

# 5. Run local polling
python bot.py
```

---

## ⚙️ Configuration (`.env`)

| Variable | Required | Default | Description |
| :--- | :---: | :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | **Yes** | — | Bot token from [@BotFather](https://t.me/BotFather) |
| `WEBHOOK_SECRET` | **Yes (Prod)** | — | Secret token header (`X-Telegram-Bot-Api-Secret-Token`) for webhook validation |
| `GEMINI_API_KEY` | No | — | Gemini API key from [Google AI Studio](https://aistudio.google.com/) (runs offline if omitted) |
| `GEMINI_MODEL` | No | `gemini-3.8-flash` | Gemini model name |
| `RATE_LIMIT_MAX_REQUESTS` | No | `5` | Max requests per sliding window |
| `RATE_LIMIT_WINDOW_SECONDS` | No | `10.0` | Sliding window duration in seconds |
| `MAX_MESSAGE_LENGTH` | No | `300` | Max character length for user replies |

---

## 📁 Project Structure

```text
├── api/
│   └── index.py        # FastAPI serverless entrypoint for Vercel Webhook
├── bot.py              # Standalone entrypoint for local polling development
├── set_webhook.py      # CLI utility to register, check, or delete Telegram Webhooks
├── config.py           # Settings, track definitions & validations
├── handlers.py         # Telegram commands, callback queries & text handler
├── gemini_service.py   # Gemini 3.8 Flash AI integration & coach persona
├── content_bank.py     # 108 curated offline exercises & fallback logic
├── rate_limiter.py     # In-memory sliding window rate limiter (LRU)
├── requirements.txt    # Pinned dependencies (fastapi, uvicorn, python-telegram-bot, etc.)
├── vercel.json         # Vercel routing and rewrites configuration
└── .env.example        # Environment variable template
```
