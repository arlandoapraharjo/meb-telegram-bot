"""
Integration tests for FastAPI Serverless Webhook entrypoints.
"""

from __future__ import annotations

import os
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from api.index import app


class TestFastAPIEndpoints(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_json_health_endpoint(self) -> None:
        """Verify GET /api?format=json returns healthy status and 1000 exercises."""
        response = self.client.get("/api?format=json")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["content_bank_exercises"], 1000)
        self.assertIn("bot_username", data)

    def test_landing_page_html(self) -> None:
        """Verify GET / returns 200 HTML content."""
        response = self.client.get("/", headers={"Accept": "text/html"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers.get("content-type", ""))
        self.assertIn("English Buddy", response.text)

    def test_webhook_unauthorized_without_secret(self) -> None:
        """Verify webhook rejects POST requests without valid secret token when configured."""
        with patch.dict(os.environ, {"WEBHOOK_SECRET": "super_secret_token_123"}):
            # Missing secret header
            res_no_header = self.client.post("/api/webhook", json={"update_id": 1})
            self.assertEqual(res_no_header.status_code, 403)

            # Invalid secret header
            res_bad_header = self.client.post(
                "/api/webhook",
                json={"update_id": 1},
                headers={"X-Telegram-Bot-Api-Secret-Token": "wrong_secret"},
            )
            self.assertEqual(res_bad_header.status_code, 403)


if __name__ == "__main__":
    unittest.main()
