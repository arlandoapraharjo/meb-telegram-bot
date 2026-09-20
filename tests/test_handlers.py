"""
Unit tests for bot command handlers and messages.
"""

from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, MagicMock
from telegram import Update, Message, Chat, User, constants
from telegram.ext import ContextTypes

import config
from handlers import help_command, start_command, HELP_MESSAGE, WELCOME_MESSAGE, BOT_DESCRIPTION_EN, BOT_DESCRIPTION_ID


class TestBotHandlers(unittest.IsolatedAsyncioTestCase):
    async def test_help_command_sends_guide(self) -> None:
        """Verify /help sends friendly pedagogical guide and inline keyboard."""
        update = MagicMock(spec=Update)
        message = MagicMock(spec=Message)
        message.reply_text = AsyncMock()
        update.message = message
        user = MagicMock(spec=User)
        user.is_bot = False
        user.id = 123456
        user.username = "testuser"
        update.effective_user = user
        chat = MagicMock(spec=Chat)
        chat.type = constants.ChatType.PRIVATE
        update.effective_chat = chat
        context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

        await help_command(update, context)

        message.reply_text.assert_called_once()
        call_kwargs = message.reply_text.call_args.kwargs
        self.assertIn(f"Panduan & Bantuan {config.BOT_NAME}", call_kwargs["text"])
        self.assertIn(config.BOT_NAME, HELP_MESSAGE)
        self.assertIn(config.BOT_NAME, WELCOME_MESSAGE)
        self.assertIn("Percakapan", call_kwargs["text"])
        self.assertIn("Kosakata", call_kwargs["text"])
        self.assertIn("Tata Bahasa", call_kwargs["text"])
        self.assertIn("Membaca", call_kwargs["text"])
        self.assertIn("Tantangan", call_kwargs["text"])
        self.assertIn("/start", call_kwargs["text"])
        self.assertIn("/help", call_kwargs["text"])
        self.assertIsNotNone(call_kwargs.get("reply_markup"))

    async def test_start_command_sends_welcome(self) -> None:
        """Verify /start sends welcome message and main menu keyboard."""
        update = MagicMock(spec=Update)
        message = MagicMock(spec=Message)
        sent_message = MagicMock(spec=Message)
        sent_message.message_id = 1234
        message.reply_text = AsyncMock(return_value=sent_message)
        update.message = message
        user = MagicMock(spec=User)
        user.is_bot = False
        user.id = 123457
        user.username = "testuser2"
        update.effective_user = user
        chat = MagicMock(spec=Chat)
        chat.type = constants.ChatType.PRIVATE
        update.effective_chat = chat
        context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)
        context.user_data = {}

        await start_command(update, context)

        message.reply_text.assert_called_once()
        call_kwargs = message.reply_text.call_args.kwargs
        self.assertEqual(call_kwargs["text"], WELCOME_MESSAGE)
        self.assertIsNotNone(call_kwargs.get("reply_markup"))

    def test_descriptions_character_limits(self) -> None:
        """Verify Telegram Bot API character constraints (<= 512 characters for descriptions)."""
        self.assertLessEqual(len(BOT_DESCRIPTION_EN), 512)
        self.assertLessEqual(len(BOT_DESCRIPTION_ID), 512)

    def test_dynamic_identity_adaptation(self) -> None:
        """Verify profile descriptions and welcome messages adapt dynamically to any bot username/name."""
        from handlers import (
            get_bot_description_en,
            get_bot_description_id,
            get_bot_short_desc_en,
            get_bot_short_desc_id,
            get_welcome_message,
        )

        test_cases = [
            ("TAPE", "tape_english_bot"),
            ("Mebby", "mebby_tutor_bot"),
            ("Super Long Bot Name That Might Test Limits", "very_long_bot_username_bot"),
            (None, "tape_english_bot"),
            ("CustomBot", None),
        ]

        for b_name, b_user in test_cases:
            desc_en = get_bot_description_en(bot_name=b_name, bot_username=b_user)
            desc_id = get_bot_description_id(bot_name=b_name, bot_username=b_user)
            short_en = get_bot_short_desc_en(bot_name=b_name, bot_username=b_user)
            short_id = get_bot_short_desc_id(bot_name=b_name, bot_username=b_user)
            welcome = get_welcome_message(bot_name=b_name, bot_username=b_user)

            # Strict Telegram API limits
            self.assertLessEqual(len(desc_en), 512)
            self.assertLessEqual(len(desc_id), 512)
            self.assertLessEqual(len(short_en), 120)
            self.assertLessEqual(len(short_id), 120)

            # Check that descriptions contain the dynamic identity
            if b_user:
                clean_user = b_user.lstrip("@")
                self.assertIn(clean_user, desc_en)
                self.assertIn(clean_user, desc_id)
            elif b_name:
                self.assertIn(b_name, desc_en)
                self.assertIn(b_name, desc_id)

            if b_name:
                self.assertIn(b_name, welcome)


if __name__ == "__main__":
    unittest.main()
