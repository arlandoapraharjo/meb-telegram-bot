"""
Unit tests for the SlidingWindowRateLimiter.
"""

from __future__ import annotations

import asyncio
import unittest
from rate_limiter import SlidingWindowRateLimiter


class TestRateLimiter(unittest.IsolatedAsyncioTestCase):
    async def test_sliding_window_allows_within_limit(self) -> None:
        limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=2.0)
        user_id = 12345

        self.assertTrue(await limiter.is_allowed(user_id))
        self.assertTrue(await limiter.is_allowed(user_id))
        self.assertTrue(await limiter.is_allowed(user_id))
        # 4th request exceeds max_requests of 3
        self.assertFalse(await limiter.is_allowed(user_id))

    async def test_sliding_window_resets_after_window(self) -> None:
        limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=0.1)
        user_id = 99999

        self.assertTrue(await limiter.is_allowed(user_id))
        self.assertTrue(await limiter.is_allowed(user_id))
        self.assertFalse(await limiter.is_allowed(user_id))

        # Wait for window to expire
        await asyncio.sleep(0.12)
        self.assertTrue(await limiter.is_allowed(user_id))

    async def test_different_users_are_isolated(self) -> None:
        limiter = SlidingWindowRateLimiter(max_requests=1, window_seconds=1.0)
        user_a = 101
        user_b = 202

        self.assertTrue(await limiter.is_allowed(user_a))
        self.assertFalse(await limiter.is_allowed(user_a))

        # User B should still be allowed
        self.assertTrue(await limiter.is_allowed(user_b))
        self.assertFalse(await limiter.is_allowed(user_b))


if __name__ == "__main__":
    unittest.main()
