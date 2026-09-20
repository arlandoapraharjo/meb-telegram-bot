"""
Configuration and Environment Module for English Buddy Telegram Bot.

Responsible for:
- Securely loading environment variables via python-dotenv.
- Validating the Telegram bot token and critical settings.
- Defining global rate limits, input caps, and learning mode content.
"""

from __future__ import annotations

import os
import re
from typing import Any, Final

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Security & Validation ---
_TOKEN_ENV_KEY: Final[str] = "TELEGRAM_BOT_TOKEN"
_RAW_TOKEN: str = os.getenv(_TOKEN_ENV_KEY, "").strip()

# Telegram Bot Token regex: <bot_id (7 to 12 digits)>:<token_hash (30 to 50 chars)>
BOT_TOKEN_PATTERN: Final[re.Pattern] = re.compile(r"^\d{7,12}:[A-Za-z0-9_-]{30,50}$")



def validate_bot_token(token: str | None = None) -> str:
    """
    Validates that the Telegram bot token exists and conforms to standard format.
    Terminates startup immediately with a clear, safe error message if invalid.
    """
    candidate = (token if token is not None else _RAW_TOKEN).strip()

    if not candidate:
        raise RuntimeError(
            f"CRITICAL SECURITY ERROR: Environment variable '{_TOKEN_ENV_KEY}' is missing or empty. "
            "Please create a '.env' file from '.env.example' and configure your Telegram bot token."
        )

    if not BOT_TOKEN_PATTERN.match(candidate):
        raise ValueError(
            f"CRITICAL SECURITY ERROR: '{_TOKEN_ENV_KEY}' has an invalid format. "
            "A valid Telegram bot token looks like '1234567890:ABCdefGHIjklMNOpqrsTUVwxyz1234567'. "
            "Check that you copied the complete token from @BotFather without leading or trailing spaces."
        )

    return candidate


# Bot Token placeholder or validated token
# If run directly or imported, we validate only when running the bot or validating explicitly.
TELEGRAM_BOT_TOKEN: str = _RAW_TOKEN

# --- Telegram Bot Identity Settings ---
# Canonical bot username (without @ prefix), used for public portal links & display chips.
_RAW_BOT_USERNAME: Final[str] = (
    os.getenv("BOT_USERNAME")
    or os.getenv("TELEGRAM_BOT_USERNAME")
    or "EnglishBuddy_Practice_Bot"
).strip()

BOT_USERNAME: Final[str] = _RAW_BOT_USERNAME.lstrip("@") or "EnglishBuddy_Practice_Bot"
BOT_DISPLAY_HANDLE: Final[str] = f"@{BOT_USERNAME}"
BOT_TELEGRAM_URL: Final[str] = f"https://t.me/{BOT_USERNAME}"


def format_bot_handle(username: str | None = None) -> str:
    """Returns the bot display handle with a single leading '@' prefix."""
    user = (username or BOT_USERNAME).strip().lstrip("@")
    return f"@{user}" if user else "@EnglishBuddy_Practice_Bot"


def format_telegram_url(username: str | None = None) -> str:
    """Returns the canonical Telegram link URL (without '@')."""
    user = (username or BOT_USERNAME).strip().lstrip("@")
    return f"https://t.me/{user}" if user else "https://t.me/EnglishBuddy_Practice_Bot"


# Webhook Secret Token for Telegram API authentication on serverless endpoints
WEBHOOK_SECRET: Final[str] = os.getenv("WEBHOOK_SECRET", "").strip()


# --- Rate Limiter Settings ---
RATE_LIMIT_MAX_REQUESTS: Final[int] = int(os.getenv("RATE_LIMIT_MAX_REQUESTS", "5"))
RATE_LIMIT_WINDOW_SECONDS: Final[float] = float(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "10.0"))
RATE_LIMIT_MAX_TRACKED_USERS: Final[int] = int(os.getenv("RATE_LIMIT_MAX_TRACKED_USERS", "10000"))
RATE_LIMIT_CLEANUP_INTERVAL_SECONDS: Final[float] = float(
    os.getenv("RATE_LIMIT_CLEANUP_INTERVAL_SECONDS", "60.0")
)

# --- Input Guardrails ---
MAX_MESSAGE_LENGTH: Final[int] = int(os.getenv("MAX_MESSAGE_LENGTH", "300"))

# --- Gemini AI Configuration (Optional Hybrid Mode) ---
GEMINI_API_KEY: Final[str] = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL: Final[str] = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
# Timeout threshold for Gemini Flash calls before falling back to offline bank
GEMINI_TIMEOUT_SECONDS: Final[float] = 9.5

# --- Difficulty Levels (CEFR) ---
LEVEL_BEGINNER: Final[str] = "beginner"
LEVEL_INTERMEDIATE: Final[str] = "intermediate"
LEVEL_ADVANCED: Final[str] = "advanced"
DEFAULT_LEVEL: Final[str] = LEVEL_BEGINNER

LEVEL_INFO: Final[dict[str, dict[str, str]]] = {
    LEVEL_BEGINNER: {
        "title": "Pemula (Beginner)",
        "badge": "🟢 Pemula (Beginner)",
        "short": "Pemula",
        "icon": "🟢",
        "description": "To be (am/is/are), anggota tubuh (body parts), kata kerja dasar, & susun kata mudah.",
    },
    LEVEL_INTERMEDIATE: {
        "title": "Menengah (Intermediate)",
        "badge": "🟡 Menengah (Intermediate)",
        "short": "Menengah",
        "icon": "🟡",
        "description": "Kegiatan sehari-hari (daily activity), kata sifat, cerita pendek fabel, & kuis to be.",
    },
    LEVEL_ADVANCED: {
        "title": "Percaya Diri (Confident)",
        "badge": "🔴 Percaya Diri (Confident)",
        "short": "Percaya Diri",
        "icon": "🔴",
        "description": "Mengenal jenis kata (part of speech), recount text (pengalaman kemarin), & kalimat aktif.",
    },
}

# --- Network Timeouts (Seconds) ---
HTTPX_CONNECT_TIMEOUT: Final[float] = 5.0
HTTPX_READ_TIMEOUT: Final[float] = 15.0
HTTPX_WRITE_TIMEOUT: Final[float] = 10.0
HTTPX_POOL_TIMEOUT: Final[float] = 5.0

# --- Learning Mode Callback Constants ---
MODE_DAILY_CONVERSATION: Final[str] = "mode_daily_conversation"
MODE_VOCABULARY: Final[str] = "mode_vocabulary"
MODE_GRAMMAR: Final[str] = "mode_grammar"
MODE_READING: Final[str] = "mode_reading"
MODE_SPEAKING: Final[str] = "mode_speaking"
MODE_CHALLENGE: Final[str] = "mode_challenge"

# --- Navigation & Action Callback Constants ---
ACTION_MAIN_MENU: Final[str] = "action_main_menu"
ACTION_NEXT_EXERCISE: Final[str] = "action_next_exercise"
ACTION_SELECT_LEVEL: Final[str] = "action_select_level"
ACTION_SET_LEVEL_PREFIX: Final[str] = "action_set_level_"


# --- Learning Modes Display Content ---
LEARNING_MODES: Final[dict[str, dict[str, Any]]] = {
    MODE_DAILY_CONVERSATION: {
        "button_text": "💬 Percakapan",
        "title": "Percakapan Sehari-hari (Daily Conversation)",
        "badge": "💬 Sapaan & Perkenalan Diri",
        "prompt": (
            "👋 <b>Halo! Mari berkenalan! (Let's introduce yourself)</b>\n\n"
            "<b>Teman baru:</b> <i>\"Hello! My name is Budi. What is your name?\"</i>\n"
            "<i>(Halo! Nama saya Budi. Siapa namamu?)</i>\n\n"
            "👉 <b>Giliranmu (Your Turn):</b> Jawab dengan mengetik:\n"
            "<code>My name is [namamu]</code>\n"
            "<i>(Contoh: My name is Siti)</i>"
        ),
    },
    MODE_VOCABULARY: {
        "button_text": "📚 Kosakata",
        "title": "Belajar Kosakata (Vocabularies)",
        "badge": "📚 Body Parts & Daily Activity",
        "prompt": (
            "🌟 <b>Kosakata Anggota Tubuh (Body Parts):</b>\n\n"
            "• <b>Head</b> = Kepala\n"
            "• <b>Eyes</b> = Mata\n"
            "• <b>Nose</b> = Hidung\n"
            "• <b>Mouth</b> = Mulut\n\n"
            "👉 <b>Giliranmu (Your Turn):</b> Tulis 1 kata anggota tubuh di atas beserta artinya!\n"
            "<i>(Contoh: Eyes = mata)</i>"
        ),
    },
    MODE_GRAMMAR: {
        "button_text": "✏️ Tata Bahasa",
        "title": "Tata Bahasa Mudah (Grammar)",
        "badge": "✏️ Belajar 'To Be' (am, is, are)",
        "prompt": (
            "🔍 <b>Aturan Dasar 'To Be' (am / is / are):</b>\n\n"
            "• <b>I</b> pasangannya <b>am</b> ➡️ <i>I am a student.</i> (Saya seorang murid)\n"
            "• <b>He / She</b> pasangannya <b>is</b> ➡️ <i>She is happy.</i> (Dia senang)\n"
            "• <b>They / We / You</b> pasangannya <b>are</b> ➡️ <i>We are friends.</i> (Kami berteman)\n\n"
            "❓ <b>Lengkapi kalimat ini:</b>\n"
            "<code>I ___ a girl.</code> (Pilih: am / is / are)\n\n"
            "👉 <b>Giliranmu (Your Turn):</b> Ketik to be yang tepat!"
        ),
    },
    MODE_READING: {
        "button_text": "📖 Membaca",
        "title": "Membaca Teks Pendek (Reading)",
        "badge": "📖 Descriptive Text: My Cat",
        "prompt": (
            "📄 <b>Teks Deskriptif Sederhana: My Cat (Kucingku)</b>\n\n"
            "<i>\"I have a cat. His name is Milo. He is cute and soft. He likes to eat fish.\"</i>\n\n"
            "💡 <b>Kamus Mini:</b>\n"
            "• cat = kucing | cute = lucu | likes = suka | fish = ikan\n\n"
            "❓ <b>Pertanyaan:</b> Siapa nama kucing itu? (What is the cat's name?)\n\n"
            "👉 <b>Giliranmu (Your Turn):</b> Jawab dengan nama kucing tersebut!"
        ),
    },
    MODE_CHALLENGE: {
        "button_text": "🎮 Tantangan",
        "title": "Tantangan Seru (English Challenge)",
        "badge": "🎮 Susun Kata (Unscramble)",
        "prompt": (
            "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
            "<code>[ girl / a / am / I ]</code>\n\n"
            "💡 <i>Petunjuk: Mulai dengan kata 'I' (Saya)...</i>\n\n"
            "👉 <b>Giliranmu (Your Turn):</b> Ketik susunan kalimat yang benar!"
        ),
    },
}
