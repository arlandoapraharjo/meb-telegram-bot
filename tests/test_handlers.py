"""
Unit tests for bot command handlers and messages.
"""

from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, MagicMock
from telegram import Update, Message, Chat, User, constants
from telegram.ext import ContextTypes

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
        self.assertIn("Panduan & Bantuan Mebby", call_kwargs["text"])
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


if __name__ == "__main__":
    unittest.main()
