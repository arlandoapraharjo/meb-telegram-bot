"""
Telegram Handlers Module for English Buddy Bot.

Handles:
- /start command with an inline keyboard menu (6 learning modes + level selector).
- Level switching (Beginner, Intermediate, Advanced).
- Dynamic exercise generation (Gemini Flash AI + offline curated fallback).
- "🔄 Next Exercise" button to instantly roll new exercises within a track.
- Conversational English Coach feedback with 300-character input guardrails.
- Global application-level error handling with credential redaction.
"""

from __future__ import annotations

import html
import logging
import os
import re
import traceback
from typing import Any, Dict, Optional

from telegram import (
    Bot,
    BotCommand,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    constants,
)
from telegram.ext import ContextTypes

import config
import content_bank
import gemini_service
from rate_limiter import rate_limited

logger = logging.getLogger(__name__)

# Credential patterns to scrub from all outgoing messages
_SENSITIVE_PATTERNS = [
    re.compile(r"\d{7,12}:[A-Za-z0-9_-]{30,50}"),  # Telegram Bot Token
    re.compile(r"AIza[0-9A-Za-z-_]{30,45}"),      # Google AI API Key (typically AIzaSy... 39 chars)
]


def sanitize_outgoing_text(text: str) -> str:
    """
    Security Barrier: Guarantees zero credential leakage in outgoing messages.
    Strips configured secrets and any token-like patterns before transmission.
    """
    if not text:
        return text

    sanitized = text
    # 1. Scrub exact configured environment secrets
    if config.TELEGRAM_BOT_TOKEN and config.TELEGRAM_BOT_TOKEN in sanitized:
        sanitized = sanitized.replace(config.TELEGRAM_BOT_TOKEN, "[PROTECTED_CREDENTIAL]")
    if config.GEMINI_API_KEY and config.GEMINI_API_KEY in sanitized:
        sanitized = sanitized.replace(config.GEMINI_API_KEY, "[PROTECTED_CREDENTIAL]")

    # 2. Scrub any regex patterns resembling API keys or bot tokens
    for pattern in _SENSITIVE_PATTERNS:
        sanitized = pattern.sub("[PROTECTED_CREDENTIAL]", sanitized)

    return sanitized


def get_main_menu_keyboard(current_level: str = config.DEFAULT_LEVEL) -> InlineKeyboardMarkup:
    """Builds the 5-mode inline keyboard in a clean, bubble-width aligned grid with a level selector."""
    lvl = config.LEVEL_INFO.get(current_level, config.LEVEL_INFO[config.DEFAULT_LEVEL])
    level_short = lvl.get("short", "Pemula")
    level_icon = lvl.get("icon", "🟢")

    keyboard = [
        [
            InlineKeyboardButton(
                config.LEARNING_MODES[config.MODE_DAILY_CONVERSATION]["button_text"],
                callback_data=config.MODE_DAILY_CONVERSATION,
            ),
            InlineKeyboardButton(
                config.LEARNING_MODES[config.MODE_VOCABULARY]["button_text"],
                callback_data=config.MODE_VOCABULARY,
            ),
        ],
        [
            InlineKeyboardButton(
                config.LEARNING_MODES[config.MODE_GRAMMAR]["button_text"],
                callback_data=config.MODE_GRAMMAR,
            ),
            InlineKeyboardButton(
                config.LEARNING_MODES[config.MODE_READING]["button_text"],
                callback_data=config.MODE_READING,
            ),
        ],
        [
            InlineKeyboardButton(
                config.LEARNING_MODES[config.MODE_CHALLENGE]["button_text"],
                callback_data=config.MODE_CHALLENGE,
            ),
        ],
        [
            InlineKeyboardButton(
                f"⚙️ Level: {level_icon} {level_short} ▾",
                callback_data=config.ACTION_SELECT_LEVEL,
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_level_selection_keyboard(current_level: str = config.DEFAULT_LEVEL) -> InlineKeyboardMarkup:
    """Builds the level selection keyboard."""
    levels = [
        (config.LEVEL_BEGINNER, config.LEVEL_INFO[config.LEVEL_BEGINNER]["badge"]),
        (config.LEVEL_INTERMEDIATE, config.LEVEL_INFO[config.LEVEL_INTERMEDIATE]["badge"]),
        (config.LEVEL_ADVANCED, config.LEVEL_INFO[config.LEVEL_ADVANCED]["badge"]),
    ]
    keyboard = []
    for level_key, label in levels:
        prefix = "✅ " if level_key == current_level else ""
        keyboard.append([
            InlineKeyboardButton(
                f"{prefix}{label}",
                callback_data=f"{config.ACTION_SET_LEVEL_PREFIX}{level_key}",
            )
        ])

    keyboard.append([
        InlineKeyboardButton("🔙 Kembali ke Menu", callback_data=config.ACTION_MAIN_MENU)
    ])
    return InlineKeyboardMarkup(keyboard)


def get_mode_keyboard(mode_key: str) -> InlineKeyboardMarkup:
    """Builds inline action buttons: Next Exercise and Return to Main Menu."""
    keyboard = [
        [
            InlineKeyboardButton("🔄 Latihan Lain", callback_data=config.ACTION_NEXT_EXERCISE),
            InlineKeyboardButton("🔙 Menu Utama", callback_data=config.ACTION_MAIN_MENU),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def resolve_bot_identity(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> tuple[str, str]:
    """
    Dynamically resolves a clean bot display name and handle.
    Adapts gracefully to bot_name, bot_username, or falls back to config values.
    Returns: (full_display, short_display)
    """
    uname = (bot_username or "").strip().lstrip("@")
    bname = (bot_name or "").strip()

    # If neither explicitly provided, fallback to environment / config defaults
    if not uname and not bname:
        bname = (os.getenv("BOT_NAME") or config.BOT_NAME or "").strip()
        uname = (os.getenv("BOT_USERNAME") or config.BOT_USERNAME or "").strip().lstrip("@")

    if bname and uname and bname.lower() != uname.lower():
        full_display = f"{bname} (@{uname})"
        short_display = f"@{uname}"
    elif uname:
        full_display = f"@{uname}"
        short_display = f"@{uname}"
    elif bname:
        full_display = bname
        short_display = bname
    else:
        full_display = "English Buddy"
        short_display = "English Buddy"

    return full_display, short_display


def get_welcome_message(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> str:
    """Generates friendly greeting message suitable for all audiences."""
    full_display, short_display = resolve_bot_identity(bot_name, bot_username)
    bname = (bot_name or "").strip() or (os.getenv("BOT_NAME") or config.BOT_NAME or "").strip() or short_display
    return (
        f"Halo! Aku {bname}, teman belajarmu! 👋✨\n\n"
        "Belajar bahasa Inggris itu seru dan menyenangkan! Jangan takut salah ya, di sini kita bisa belajar dan berlatih bersama sesuai kemampuanmu.\n\n"
        "Yuk, pilih materi atau tantangan yang ingin kamu coba di bawah ini:"
    )


WELCOME_MESSAGE: str = get_welcome_message()


def _extract_bot_identity(context: Optional[ContextTypes.DEFAULT_TYPE]) -> tuple[Optional[str], Optional[str]]:
    """Safely extracts bot first_name and username from PTB context if available."""
    bot_name = None
    bot_username = None
    if context and hasattr(context, "bot") and context.bot:
        fname = getattr(context.bot, "first_name", None)
        uname = getattr(context.bot, "username", None)
        if isinstance(fname, str) and fname.strip():
            bot_name = fname.strip()
        if isinstance(uname, str) and uname.strip():
            bot_username = uname.strip()
    return bot_name, bot_username


async def fetch_exercise(
    mode: str,
    level: str,
    exclude_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Hybrid content fetcher:
    Attempts real-time dynamic generation with Gemini Flash AI.
    Falls back cleanly to the offline curated exercise bank if AI is disabled or fails.
    """
    ai_exercise = await gemini_service.generate_dynamic_exercise(mode, level)
    if ai_exercise:
        return ai_exercise

    return content_bank.get_offline_exercise(mode, level, exclude_id)


async def strip_previous_reply_markup(
    context: ContextTypes.DEFAULT_TYPE,
    chat_id: Optional[int],
    message_id: Optional[int],
) -> None:
    """Safely removes inline keyboard from a previous message so old buttons do not dangle."""
    if not chat_id or not message_id:
        return
    try:
        await context.bot.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=None,
        )
    except Exception as exc:
        logger.debug("Could not strip previous reply markup (chat_id=%s, msg_id=%s): %s", chat_id, message_id, exc)


@rate_limited()
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles /start command.
    Sends greeting and displays the 6 learning modes + level selector.
    Cleans up any dangling buttons from previous interactive sessions.
    """
    if update.message is None:
        return

    # Security: Restrict interactions to private chats only
    if update.effective_chat and update.effective_chat.type != constants.ChatType.PRIVATE:
        logger.info("Ignoring /start from non-private chat id=%s", update.effective_chat.id)
        return

    user_data = context.user_data if context.user_data is not None else {}
    current_level = user_data.get("level", config.DEFAULT_LEVEL)

    # Clean buttons from any previous interactive message
    last_msg_id = user_data.get("last_interactive_msg_id")
    if last_msg_id and update.effective_chat:
        await strip_previous_reply_markup(context, update.effective_chat.id, last_msg_id)

    bot_name, bot_username = _extract_bot_identity(context)
    welcome_text = get_welcome_message(bot_name, bot_username) if (bot_name or bot_username) else WELCOME_MESSAGE

    sent_msg = await update.message.reply_text(
        text=welcome_text,
        reply_markup=get_main_menu_keyboard(current_level),
        parse_mode=constants.ParseMode.HTML,
    )
    user_data["last_interactive_msg_id"] = sent_msg.message_id


def get_help_message(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> str:
    """Generates comprehensive guide and help message adapting to bot identity."""
    bname = (bot_name or "").strip() or (os.getenv("BOT_NAME") or config.BOT_NAME or "").strip() or "English Buddy"
    return (
        f"📖 <b>Panduan & Bantuan {bname}</b> 👋✨\n\n"
        f"Halo! Aku {bname}, teman belajarmu untuk menguasai bahasa Inggris dengan cara yang mudah, seru, dan menyenangkan!\n\n"
        "🌟 <b>5 Kategori Pembelajaran:</b>\n"
        "• 💬 <b>Percakapan (Conversation):</b> Latihan dialog nyata situasi sehari-hari.\n"
        "• 📚 <b>Kosakata (Vocabulary):</b> Tambah kosakata, padanan kata, dan frasa baru.\n"
        "• ✍️ <b>Tata Bahasa (Grammar):</b> Pahami pola kalimat, tenses, dan tata bahasa.\n"
        "• 📖 <b>Membaca (Reading):</b> Baca teks pendek dan uji pemahaman bacaanmu.\n"
        "• ⚡ <b>Tantangan (Challenge):</b> Kuis kilat adaptif untuk melatih ketangkasan berpikir!\n\n"
        "⚙️ <b>Tingkat Kemampuan:</b>\n"
        "Kamu bisa memilih level kapan saja di menu utama melalui tombol <b>⚙️ Level</b>:\n"
        "🟢 <b>Pemula (Beginner)</b> • 🟡 <b>Menengah (Intermediate)</b> • 🔴 <b>Mahir (Advanced)</b>\n\n"
        "💡 <b>Cara Belajar:</b>\n"
        "1. Ketik /start atau tekan tombol di bawah untuk membuka menu.\n"
        "2. Pilih topik yang ingin kamu pelajari.\n"
        "3. Ketik jawabanmu langsung di pesan chat saat soal muncul.\n"
        "4. Bot akan mengevaluasi jawabanmu secara ramah dan edukatif!\n"
        "5. Gunakan tombol <b>🔄 Latihan Lain</b> untuk soal baru, atau <b>🔙 Menu Utama</b> untuk ganti materi.\n\n"
        "📌 <b>Perintah Tersedia:</b>\n"
        "• /start - Membuka menu utama pembelajaran\n"
        "• /help - Menampilkan panduan bantuan ini"
    )


HELP_MESSAGE: str = get_help_message()


def get_bot_description_en(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> str:
    """Generates the English bot profile description ('What can this bot do?') adapting to any bot name/username."""
    full_display, _ = resolve_bot_identity(bot_name, bot_username)
    desc = (
        f"Welcome to {full_display}! 👋✨\n"
        "Your interactive English learning companion for all levels with 1,000 curated exercises & smart AI coaching!\n\n"
        "🌟 What can you do?\n"
        "• 💬 Conversation: Real-life dialogues\n"
        "• 📚 Vocabulary: Expand words & phrases\n"
        "• ✍️ Grammar: Master sentence patterns\n"
        "• 📖 Reading: Stories & comprehension\n"
        "• ⚡ Challenge: Rapid-fire adaptive quizzes\n\n"
        "🎯 3 Levels: Beginner, Intermediate, Advanced\n"
        "⚡ 1,000 exercises offline + AI evaluation\n\n"
        "Tap START to begin! 🚀"
    )
    return desc[:512]


def get_bot_description_id(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> str:
    """Generates the Indonesian bot profile description ('What can this bot do?') adapting to any bot name/username."""
    full_display, _ = resolve_bot_identity(bot_name, bot_username)
    desc = (
        f"Selamat datang di {full_display}! 👋✨\n"
        "Teman belajar bahasa Inggris interaktif untuk semua kalangan dengan 1.000 materi kurasi & evaluasi cerdas!\n\n"
        "🌟 Fitur Utama:\n"
        "• 💬 Percakapan: Latihan dialog nyata\n"
        "• 📚 Kosakata: Kosakata & frasa baru\n"
        "• ✍️ Tata Bahasa: Kuasai pola kalimat\n"
        "• 📖 Membaca: Cerita seru & pemahaman\n"
        "• ⚡ Tantangan: Kuis kilat adaptif\n\n"
        "🎯 3 Tingkat: Pemula, Menengah, Mahir\n"
        "⚡ 1.000 latihan offline + evaluasi AI\n\n"
        "Tekan START untuk mulai belajar! 🚀"
    )
    return desc[:512]


def get_bot_short_desc_en(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> str:
    """Generates the English short description adapting to any bot identity."""
    _, short_display = resolve_bot_identity(bot_name, bot_username)
    desc = f"{short_display}: Interactive English companion for all levels with 1,000 exercises & smart AI feedback."
    return desc[:120]


def get_bot_short_desc_id(
    bot_name: Optional[str] = None,
    bot_username: Optional[str] = None,
) -> str:
    """Generates the Indonesian short description adapting to any bot identity."""
    _, short_display = resolve_bot_identity(bot_name, bot_username)
    desc = f"{short_display}: Bot belajar bahasa Inggris untuk semua kalangan dengan 1.000 materi & evaluasi cerdas."
    return desc[:120]


BOT_DESCRIPTION_EN: str = get_bot_description_en()
BOT_DESCRIPTION_ID: str = get_bot_description_id()
BOT_SHORT_DESC_EN: str = get_bot_short_desc_en()
BOT_SHORT_DESC_ID: str = get_bot_short_desc_id()

BOT_COMMANDS = [
    BotCommand("start", "Buka menu utama belajar (Open main menu)"),
    BotCommand("help", "Panduan & bantuan belajar (User guide & help)"),
]


async def setup_bot_profile(bot: Bot) -> None:
    """
    Synchronizes bot description ('What can this bot do?'), short description,
    and menu commands with the Telegram Bot API.
    Dynamically adapts to the bot's configured or actual Telegram name and username.
    """
    try:
        bot_name = ""
        bot_username = ""
        try:
            me = await bot.get_me()
            if me:
                if me.first_name:
                    bot_name = me.first_name.strip()
                if me.username:
                    bot_username = me.username.strip()
        except Exception as get_me_err:
            logger.debug("Could not resolve bot info via get_me(): %s", get_me_err)

        desc_en = get_bot_description_en(bot_name=bot_name, bot_username=bot_username)
        desc_id = get_bot_description_id(bot_name=bot_name, bot_username=bot_username)
        short_en = get_bot_short_desc_en(bot_name=bot_name, bot_username=bot_username)
        short_id = get_bot_short_desc_id(bot_name=bot_name, bot_username=bot_username)

        await bot.set_my_description(description=desc_en)
        await bot.set_my_description(description=desc_id, language_code="id")
        await bot.set_my_short_description(short_description=short_en)
        await bot.set_my_short_description(short_description=short_id, language_code="id")
        await bot.set_my_commands(commands=BOT_COMMANDS)
        logger.info(
            "Successfully updated Telegram bot profile descriptions and commands for '%s' (@%s).",
            bot_name or config.BOT_NAME,
            bot_username or config.BOT_USERNAME,
        )
    except Exception as exc:
        logger.warning("Could not update bot profile descriptions with Telegram API: %s", exc)


@rate_limited()
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles /help command.
    Sends comprehensive user guide and quick navigation back to the main menu.
    """
    if update.message is None:
        return

    # Security: Restrict interactions to private chats only
    if update.effective_chat and update.effective_chat.type != constants.ChatType.PRIVATE:
        logger.info("Ignoring /help from non-private chat id=%s", update.effective_chat.id)
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Buka Menu Belajar (/start)", callback_data=config.ACTION_MAIN_MENU)]
    ])

    bot_name, bot_username = _extract_bot_identity(context)
    help_text = get_help_message(bot_name, bot_username) if (bot_name or bot_username) else HELP_MESSAGE

    await update.message.reply_text(
        text=help_text,
        reply_markup=keyboard,
        parse_mode=constants.ParseMode.HTML,
    )


@rate_limited()
async def menu_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles inline keyboard callbacks:
    - Mode selection & initial dynamic challenge.
    - '🔄 Next Exercise' generation.
    - Level selection & level changes.
    - '🔙 Main Menu' navigation.
    """
    query = update.callback_query
    if query is None or query.data is None:
        return

    # Security: Restrict interactions to private chats only
    if update.effective_chat and update.effective_chat.type != constants.ChatType.PRIVATE:
        return

    await query.answer()
    data = query.data

    user_data = context.user_data if context.user_data is not None else {}
    current_level = user_data.get("level", config.DEFAULT_LEVEL)

    bot_name, bot_username = _extract_bot_identity(context)
    welcome_text = get_welcome_message(bot_name, bot_username) if (bot_name or bot_username) else WELCOME_MESSAGE

    # In-place editing: Keep track of current interactive message
    if query.message:
        user_data["last_interactive_msg_id"] = query.message.message_id

    # 1. Main Menu Navigation
    if data == config.ACTION_MAIN_MENU:
        try:
            await query.edit_message_text(
                text=welcome_text,
                reply_markup=get_main_menu_keyboard(current_level),
                parse_mode=constants.ParseMode.HTML,
            )
        except Exception as exc:
            logger.debug("Error returning to main menu: %s", exc)
        return

    # 2. Level Selection Menu
    if data == config.ACTION_SELECT_LEVEL:
        level_text = (
            "⚙️ <b>Pilih Tingkat Kemampuan (Level):</b>\n\n"
            "• <b>🟢 Pemula (Beginner):</b> To be (am/is/are), anggota tubuh, kata kerja dasar, & susun kata mudah.\n"
            "• <b>🟡 Menengah (Intermediate):</b> Kegiatan sehari-hari, kata sifat, fabel pendek, & kuis to be.\n"
            "• <b>🔴 Percaya Diri (Confident):</b> Mengenal jenis kata (part of speech), teks recount, & kalimat aktif.\n\n"
            "Pilih tingkat belajar di bawah ini ya:"
        )
        try:
            await query.edit_message_text(
                text=level_text,
                reply_markup=get_level_selection_keyboard(current_level),
                parse_mode=constants.ParseMode.HTML,
            )
        except Exception as exc:
            logger.debug("Error displaying level menu: %s", exc)
        return

    # 3. Apply Level Change
    if data.startswith(config.ACTION_SET_LEVEL_PREFIX):
        new_level = data[len(config.ACTION_SET_LEVEL_PREFIX):]
        if new_level in config.LEVEL_INFO:
            user_data["level"] = new_level
            current_level = new_level
            level_name = config.LEVEL_INFO[new_level]["title"]
            logger.info("User %s changed level to %s", update.effective_user.id if update.effective_user else 0, new_level)
            try:
                await query.edit_message_text(
                    text=f"✅ <b>Level berhasil diubah ke {level_name}!</b>\n\n{welcome_text}",
                    reply_markup=get_main_menu_keyboard(current_level),
                    parse_mode=constants.ParseMode.HTML,
                )
            except Exception as exc:
                logger.debug("Error confirming level change: %s", exc)
        return

    # 4. Next Exercise in Current Track
    if data == config.ACTION_NEXT_EXERCISE:
        active_mode = user_data.get("active_mode", config.MODE_DAILY_CONVERSATION)
        last_id = user_data.get("last_exercise_id")

        exercise = await fetch_exercise(active_mode, current_level, exclude_id=last_id)
        user_data["last_exercise_id"] = exercise.get("id")
        user_data["active_prompt"] = exercise.get("prompt", "")
        user_data["active_exercise"] = exercise

        mode_badge = exercise.get("badge", "Practice Challenge")
        level_badge = config.LEVEL_INFO[current_level]["icon"]

        message_text = (
            f"<b>{html.escape(exercise['title'])}</b> [{level_badge}]\n"
            f"<i>{html.escape(mode_badge)}</i>\n\n"
            f"{exercise['prompt']}"
        )
        try:
            await query.edit_message_text(
                text=message_text,
                reply_markup=get_mode_keyboard(active_mode),
                parse_mode=constants.ParseMode.HTML,
            )
        except Exception as exc:
            logger.debug("Error loading next exercise: %s", exc)
        return

    # 5. Selected Learning Mode
    if data in config.LEARNING_MODES:
        user_data["active_mode"] = data
        exercise = await fetch_exercise(data, current_level)
        user_data["last_exercise_id"] = exercise.get("id")
        user_data["active_prompt"] = exercise.get("prompt", "")
        user_data["active_exercise"] = exercise

        level_badge = config.LEVEL_INFO[current_level]["icon"]
        message_text = (
            f"<b>{html.escape(exercise['title'])}</b> [{level_badge}]\n"
            f"<i>{html.escape(exercise['badge'])}</i>\n\n"
            f"{exercise['prompt']}"
        )

        try:
            await query.edit_message_text(
                text=message_text,
                reply_markup=get_mode_keyboard(data),
                parse_mode=constants.ParseMode.HTML,
            )
        except Exception as exc:
            logger.debug("Error opening mode %s: %s", data, exc)


@rate_limited()
async def text_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles student messages with input guardrails:
    - Caps text at MAX_MESSAGE_LENGTH (300 characters).
    - Evaluates student response using the Conversational English Coach persona (Gemini / Offline).
    - Enforces honest, constructive pedagogical feedback without false praise.
    - Provides constructive feedback and inline next-exercise action buttons.
    """
    if update.message is None or not update.message.text:
        return

    # Security: Restrict interactions to private chats only
    if update.effective_chat and update.effective_chat.type != constants.ChatType.PRIVATE:
        return

    raw_text = update.message.text.strip()

    # --- Input Guardrail: Truncate incoming user text to MAX_MESSAGE_LENGTH (300 characters) ---
    if len(raw_text) > config.MAX_MESSAGE_LENGTH:
        logger.info(
            "Input guardrail: Truncating message from user_id=%s (%d chars -> %d chars).",
            update.effective_user.id if update.effective_user else 0,
            len(raw_text),
            config.MAX_MESSAGE_LENGTH,
        )
        user_text = raw_text[:config.MAX_MESSAGE_LENGTH]
    else:
        user_text = raw_text


    user_data = context.user_data if context.user_data is not None else {}
    active_mode = user_data.get("active_mode", config.MODE_DAILY_CONVERSATION)
    current_level = user_data.get("level", config.DEFAULT_LEVEL)
    active_prompt = user_data.get("active_prompt", "English practice exercise")
    active_exercise = user_data.get("active_exercise")

    # Clean buttons from the previous interactive message so old buttons do not dangle
    last_msg_id = user_data.get("last_interactive_msg_id")
    if last_msg_id and update.effective_chat:
        await strip_previous_reply_markup(context, update.effective_chat.id, last_msg_id)

    # 1. Anti-Jailbreak / Prompt Injection Pre-screening (0 API tokens consumed)
    jailbreak_msg = gemini_service.detect_potential_jailbreak(user_text)
    if jailbreak_msg:
        sent_msg = await update.message.reply_text(
            text=sanitize_outgoing_text(jailbreak_msg),
            reply_markup=get_mode_keyboard(active_mode),
            parse_mode=constants.ParseMode.HTML,
        )
        user_data["last_interactive_msg_id"] = sent_msg.message_id
        return

    # Show typing indicator while coach processes
    if update.effective_chat:
        try:
            await context.bot.send_chat_action(
                chat_id=update.effective_chat.id,
                action=constants.ChatAction.TYPING,
            )
        except Exception:
            pass

    # 2. Student Question / Clarification / Hint Intent ('apa maksudnya', 'apa jawabannya')
    if gemini_service.is_student_query_or_hint_request(user_text):
        feedback_text = await gemini_service.explain_or_hint_exercise(
            mode=active_mode,
            level=current_level,
            active_prompt=active_prompt,
            user_text=user_text,
            active_exercise=active_exercise,
        )
    else:
        # 3. Conversational Coach Evaluation for Student Answer Submissions
        feedback_text = await gemini_service.evaluate_student_message(
            mode=active_mode,
            level=current_level,
            active_prompt=active_prompt,
            user_text=user_text,
            active_exercise=active_exercise,
        )

    sent_msg = await update.message.reply_text(
        text=sanitize_outgoing_text(feedback_text),
        reply_markup=get_mode_keyboard(active_mode),
        parse_mode=constants.ParseMode.HTML,
    )
    user_data["last_interactive_msg_id"] = sent_msg.message_id


async def global_error_handler(update: Optional[object], context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Global error handler to catch exceptions cleanly.
    - Sanitizes logs to prevent leaking bot tokens and API keys.
    - Never exposes internal stack traces to end-users.
    """
    error = context.error
    token = config.TELEGRAM_BOT_TOKEN
    api_key = config.GEMINI_API_KEY

    tb_lines = traceback.format_exception(None, error, error.__traceback__) if error else ["No exception info"]
    tb_text = "".join(tb_lines)

    # Redact sensitive credentials
    if token and token in tb_text:
        tb_text = tb_text.replace(token, "***REDACTED_BOT_TOKEN***")
    if api_key and api_key in tb_text:
        tb_text = tb_text.replace(api_key, "***REDACTED_GEMINI_API_KEY***")

    logger.error("Exception while handling update: %s\n%s", error, tb_text)

    if isinstance(update, Update) and update.effective_chat:
        try:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=(
                    "⚠️ <b>An unexpected error occurred.</b>\n\n"
                    "Please tap /start or try again in a few moments."
                ),
                parse_mode=constants.ParseMode.HTML,
            )
        except Exception as notify_err:
            logger.debug("Failed to send error notification to user: %s", notify_err)
