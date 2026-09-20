# Mebby

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vercel](https://img.shields.io/badge/Vercel-black?logo=vercel&logoColor=white)](https://vercel.com/)
[![Telegram Bot API](https://img.shields.io/badge/telegram--bot--api-v21%2B%20(async)-0088cc?logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![Google GenAI](https://img.shields.io/badge/Google%20GenAI-Gemini%20Flash-4285F4?logo=googlegemini&logoColor=white)](https://ai.google.dev/)

A serverless Telegram learning bot built with FastAPI and python-telegram-bot. Includes a 1,000-exercise offline bank across five learning tracks and dynamic evaluation via Google Gemini Flash. Deployable on Vercel Serverless Functions or via local polling.

---

## Features

- **5 Learning Tracks:** Daily Conversation, Vocabulary, Grammar, Reading Comprehension, and Challenge.
- **3 Skill Levels:** Beginner (A1–A2), Intermediate (B1–B2), and Advanced (C1–C2) selectable via inline keyboards.
- **Hybrid Evaluation:** Real-time feedback via Gemini Flash with automatic fallback to the 1,000-exercise offline bank when unconfigured or unreachable.
- **Serverless Webhook Handler:** Stateless FastAPI ASGI endpoint (`api/index.py`) designed for Vercel Python runtime.
- **Security & Rate Limiting:**
  - Constant-time verification of `X-Telegram-Bot-Api-Secret-Token`.
  - In-memory sliding window rate limiter (5 requests / 10s per user).
  - 512 KB payload size limit and 300-character input truncation.
  - Secret masking across application logs.
- **Status Dashboard:** Landing page served at `GET /`.

---

## Deployment (Vercel Webhook)

### 1. Configure Environment Variables
Set the following in your Vercel project settings or `.env`:
- `TELEGRAM_BOT_TOKEN`: Bot token from [@BotFather](https://t.me/BotFather).
- `WEBHOOK_SECRET`: Secret token for request verification (`python -c "import secrets; print(secrets.token_urlsafe(32))"`).
- `GEMINI_API_KEY`: *(Optional)* Google AI Studio key. If omitted, the bot runs in offline mode.
- `BOT_NAME` & `BOT_USERNAME`: *(Optional)* Display name and handle for the status page.

### 2. Deploy
Deploy using the Vercel CLI:
```bash
vercel --prod
```

### 3. Register Webhook
Set the Telegram webhook endpoint:
```bash
# Using CLI script
python scripts/set_webhook.py set https://<your-project>.vercel.app

# Using cURL
curl -F "url=https://<your-project>.vercel.app/api/webhook" \
     -F "secret_token=<YOUR_WEBHOOK_SECRET>" \
     https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook
```

Verify webhook status:
```bash
python scripts/set_webhook.py info
```

---

## Local Development

Run the bot locally using long-polling:

```bash
# 1. Clone repository
git clone https://github.com/arlandoapraharjo/mebby-telegram-bot.git
cd mebby-telegram-bot

# 2. Configure environment
cp .env.example .env
# Set TELEGRAM_BOT_TOKEN in .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Unregister active webhook (required before polling)
python scripts/set_webhook.py delete

# 5. Start bot
python bot.py
```

---

## Testing

Run the test suite:
```bash
python -m unittest discover tests
```

---

## Configuration

| Variable | Required | Default | Description |
| :--- | :---: | :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | Yes | — | Telegram Bot API token from [@BotFather](https://t.me/BotFather) |
| `WEBHOOK_SECRET` | Yes (Prod) | — | Secret token header (`X-Telegram-Bot-Api-Secret-Token`) for webhook verification |
| `BOT_NAME` | No | `Mebby` | Display name in messages and coach persona |
| `BOT_USERNAME` | No | `mebby_tutor_bot` | Telegram handle for landing page links |
| `GEMINI_API_KEY` | No | — | Google AI Studio API key (offline bank used if omitted) |
| `GEMINI_MODEL` | No | `gemini-3.8-flash` | Gemini model variant |
| `GEMINI_TIMEOUT_SECONDS` | No | `9.5` | Timeout before fallback to offline bank |
| `RATE_LIMIT_MAX_REQUESTS` | No | `5` | Maximum requests per sliding window |
| `RATE_LIMIT_WINDOW_SECONDS` | No | `10.0` | Sliding window duration in seconds |
| `MAX_MESSAGE_LENGTH` | No | `300` | Maximum character length for user inputs |

---

## Project Structure

```text
├── api/
│   └── index.py            # FastAPI entrypoint for Vercel serverless webhook
├── exercises/              # Offline exercise bank (1,000 exercises)
│   ├── __init__.py
│   ├── conversation.py     # 200 Conversation exercises
│   ├── vocabulary.py       # 200 Vocabulary exercises
│   ├── grammar.py          # 200 Grammar exercises
│   ├── reading.py          # 200 Reading exercises
│   └── challenge.py        # 200 Challenge exercises
├── frontend/               # Status card UI preview (React / Tailwind)
├── public/
│   └── index.html          # Status dashboard served at GET /
├── scripts/
│   └── set_webhook.py      # Webhook management CLI
├── tests/                  # Unit and integration test suite
├── bot.py                  # Polling entrypoint for local development
├── config.py               # Application configuration and environment loader
├── content_bank.py         # Offline bank loader and deterministic evaluator
├── gemini_service.py       # Gemini API client and evaluation logic
├── handlers.py             # Telegram commands, callbacks, and message handlers
└── rate_limiter.py         # In-memory sliding window rate limiter
```
