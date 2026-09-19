"""
In-Memory Sliding Window Rate Limiter for English Buddy Telegram Bot.

Features:
- Thread/async-safe sliding window algorithm per user ID.
- LRU eviction cap to prevent unbounded memory growth from arbitrary user IDs.
- Periodic cleanup of expired timestamps to avoid memory leaks.
- Reusable @rate_limited decorator for Telegram handler functions.
- Non-blocking execution with user alerts on violation.
"""

from __future__ import annotations

import asyncio
import functools
import logging
import time
from collections import OrderedDict, deque
from typing import Any, Callable, Coroutine, Deque, Dict, Optional, TypeVar

from telegram import Update
from telegram.ext import ContextTypes

import config

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Coroutine[Any, Any, Any]])


class SlidingWindowRateLimiter:
    """
    In-memory, bounded sliding window rate limiter.
    Maintains a deque of request timestamps per user.
    """

    def __init__(
        self,
        max_requests: int = config.RATE_LIMIT_MAX_REQUESTS,
        window_seconds: float = config.RATE_LIMIT_WINDOW_SECONDS,
        max_tracked_users: int = config.RATE_LIMIT_MAX_TRACKED_USERS,
    ) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.max_tracked_users = max_tracked_users

        # user_id -> deque of request timestamps
        self._user_requests: OrderedDict[int, Deque[float]] = OrderedDict()
        # user_id -> timestamp of last warning sent (prevents bot from spamming back)
        self._last_warning_sent: Dict[int, float] = {}
        self._lock = asyncio.Lock()

    async def is_allowed(self, user_id: int) -> bool:
        """
        Check if a request from user_id is permitted under the sliding window.
        Returns True if allowed, False if rate limited.
        """
        now = time.monotonic()
        cutoff = now - self.window_seconds

        async with self._lock:
            # Retrieve or initialize user's deque
            if user_id in self._user_requests:
                # Move to end for LRU tracking
                self._user_requests.move_to_end(user_id)
                timestamps = self._user_requests[user_id]
            else:
                # Enforce max capacity by evicting oldest tracked user if limit reached
                if len(self._user_requests) >= self.max_tracked_users:
                    oldest_user, _ = self._user_requests.popitem(last=False)
                    self._last_warning_sent.pop(oldest_user, None)

                timestamps = deque()
                self._user_requests[user_id] = timestamps

            # Purge timestamps outside the sliding window
            while timestamps and timestamps[0] <= cutoff:
                timestamps.popleft()

            # Check capacity
            if len(timestamps) < self.max_requests:
                timestamps.append(now)
                return True
            else:
                return False

    async def should_notify_user(self, user_id: int) -> bool:
        """
        Rate limits the bot's own warnings so repeat spam does not trigger
        a flood of outbound warning messages back to the user.
        """
        now = time.monotonic()
        async with self._lock:
            last_notified = self._last_warning_sent.get(user_id, 0.0)
            # Only notify at most once every 3 seconds per user
            if now - last_notified > 3.0:
                self._last_warning_sent[user_id] = now
                return True
            return False

    async def cleanup_stale(self) -> int:
        """
        Removes users who have no active requests in the current window.
        Returns the number of cleaned entries.
        """
        now = time.monotonic()
        cutoff = now - self.window_seconds
        removed_count = 0

        async with self._lock:
            users_to_remove = []
            for user_id, timestamps in self._user_requests.items():
                while timestamps and timestamps[0] <= cutoff:
                    timestamps.popleft()
                if not timestamps:
                    users_to_remove.append(user_id)

            for user_id in users_to_remove:
                del self._user_requests[user_id]
                self._last_warning_sent.pop(user_id, None)
                removed_count += 1

        if removed_count > 0:
            logger.debug("Rate limiter cleaned up %d stale user records.", removed_count)
        return removed_count

    async def get_tracked_count(self) -> int:
        """Returns the number of currently tracked active users."""
        async with self._lock:
            return len(self._user_requests)


# Singleton rate limiter instance for handlers
global_rate_limiter = SlidingWindowRateLimiter()


def rate_limited(limiter: Optional[SlidingWindowRateLimiter] = None) -> Callable[[F], F]:
    """
    Decorator for python-telegram-bot handler functions:
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE)
    """
    active_limiter = limiter or global_rate_limiter

    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args: Any, **kwargs: Any) -> Any:
            effective_user = update.effective_user
            if effective_user is None or effective_user.is_bot:
                # Drop updates from unknown entities or fellow bots
                return None

            user_id = effective_user.id
            allowed = await active_limiter.is_allowed(user_id)

            if not allowed:
                logger.warning(
                    "Rate limit exceeded for user_id=%d (@%s). Request dropped.",
                    user_id,
                    effective_user.username or "unknown",
                )

                should_notify = await active_limiter.should_notify_user(user_id)

                if update.callback_query:
                    # Callback queries can pop an alert banner
                    try:
                        await update.callback_query.answer(
                            text="⏳ Please slow down! (Max 5 requests per 10s)",
                            show_alert=True,
                        )
                    except Exception as ex:
                        logger.debug("Could not answer callback query on rate limit: %s", ex)

                elif update.message and should_notify:
                    # Send a polite inline rate limit message
                    try:
                        await update.message.reply_text(
                            "⏳ <b>Slow down!</b> You're sending requests too fast. "
                            "Please wait a few seconds before trying again.",
                            parse_mode="HTML",
                        )
                    except Exception as ex:
                        logger.debug("Could not send rate limit message: %s", ex)

                return None

            return await func(update, context, *args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator
