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
GEMINI_TIMEOUT_SECONDS: Final[float] = 7.0

# --- Difficulty Levels (CEFR) ---
LEVEL_BEGINNER: Final[str] = "beginner"
LEVEL_INTERMEDIATE: Final[str] = "intermediate"
LEVEL_ADVANCED: Final[str] = "advanced"
DEFAULT_LEVEL: Final[str] = LEVEL_INTERMEDIATE

LEVEL_INFO: Final[dict[str, dict[str, str]]] = {

    LEVEL_BEGINNER: {
        "title": "Beginner (A1–A2)",
        "badge": "🟢 Beginner (A1–A2)",
        "icon": "🟢",
        "description": "Essential daily words, simple present/past, and foundational phrases.",
    },
    LEVEL_INTERMEDIATE: {
        "title": "Intermediate (B1–B2)",
        "badge": "🟡 Intermediate (B1–B2)",
        "icon": "🟡",
        "description": "Conversational fluency, idioms, phrasal verbs, and varied tenses.",
    },
    LEVEL_ADVANCED: {
        "title": "Advanced (C1–C2)",
        "badge": "🔴 Advanced (C1–C2)",
        "icon": "🔴",
        "description": "Subtle nuances, complex grammar, academic vocabulary, and professional flow.",
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
        "button_text": "💬 Daily Conversation",
        "title": "Daily Conversation Practice",
        "badge": "💬 Topic: Ordering Coffee & Light Lunch",
        "prompt": (
            "<b>☕ Scenario:</b> You are at a cozy neighborhood café in London.\n\n"
            "<b>Barista:</b> <i>\"Hi there! Welcome to The Daily Roast. What can I get started for you today?\"</i>\n\n"
            "👉 <b>Your Turn:</b> Reply with what you would say to order your drink, ask for almond milk, or ask about pastries!"
        ),
    },
    MODE_VOCABULARY: {
        "button_text": "📚 Vocabulary",
        "title": "Vocabulary Builder",
        "badge": "📚 Word of the Day",
        "prompt": (
            "🌟 <b>Word:</b> <code>Serendipity</code> <i>/ˌser.ənˈdɪp.ə.ti/</i> (noun)\n\n"
            "<b>Definition:</b> The occurrence and development of events by chance in a happy or beneficial way.\n\n"
            "<b>Example Sentence:</b> <i>\"Finding my dream apartment while lost in the city was pure serendipity.\"</i>\n\n"
            "👉 <b>Your Turn:</b> Send a sentence using <b>serendipity</b> or ask for 3 real-world synonyms!"
        ),
    },
    MODE_GRAMMAR: {
        "button_text": "✏️ Grammar",
        "title": "Grammar Clinic",
        "badge": "✏️ Spot & Fix the Mistake",
        "prompt": (
            "🔍 <b>Spot the grammatical error in this sentence:</b>\n\n"
            "❌ <code>\"Neither of the managers were aware of the updated security policy.\"</code>\n\n"
            "👉 <b>Your Turn:</b> Send the corrected sentence and explain why the original was incorrect!"
        ),
    },
    MODE_READING: {
        "button_text": "📖 Reading",
        "title": "Reading Comprehension",
        "badge": "📖 Mini-Reading Passage",
        "prompt": (
            "📄 <b>Passage:</b>\n"
            "<i>\"Bioluminescent organisms, such as deep-sea anglerfish and fireflies, produce light through a chemical reaction involving luciferin and luciferase. Unlike incandescent bulbs that waste 90% of their energy generating heat, bioluminescence is almost 100% efficient cold light.\"</i>\n\n"
            "❓ <b>Question:</b> In what way is bioluminescence superior to traditional incandescent lighting?\n\n"
            "👉 <b>Your Turn:</b> Reply with your answer in your own words!"
        ),
    },
    MODE_SPEAKING: {
        "button_text": "🗣️ Speaking",
        "title": "Speaking & Pronunciation Lab",
        "badge": "🗣️ Pronunciation & Fluency",
        "prompt": (
            "🎙️ <b>Tongue Twister & Rhythm Challenge:</b>\n"
            "<i>\"Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked.\"</i>\n\n"
            "🎯 <b>Focus:</b> Clear plosive /p/ sounds and consistent speaking rhythm.\n\n"
            "👉 <b>Your Turn:</b> Record and send a voice message practicing this line, or write down any questions about natural linking sounds!"
        ),
    },
    MODE_CHALLENGE: {
        "button_text": "🎮 English Challenge",
        "title": "English Challenge Arena",
        "badge": "🎮 Level 1: Sentence Unscramble",
        "prompt": (
            "🧩 <b>Unscramble the words into a natural English idiom:</b>\n\n"
            "<code>[ weather / under / feeling / today / a / bit / the / I'm ]</code>\n\n"
            "👉 <b>Your Turn:</b> Send the unscrambled sentence and explain what the idiom means!"
        ),
    },
}
