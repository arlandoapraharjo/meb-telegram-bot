"""
Unit tests for input quality guardrails and anti-sugarcoat validation.
"""

from __future__ import annotations

import unittest
import content_bank


class TestQualityGuard(unittest.TestCase):
    def test_empty_and_whitespace(self) -> None:
        status, msg = content_bank.check_submission_quality("   ")
        self.assertEqual(status, "empty_punct")
        self.assertIsNotNone(msg)

    def test_pure_dots_and_punctuation(self) -> None:
        dots = [".", "...", "..", "???", "!!!", "....", "...?"]
        for item in dots:
            status, msg = content_bank.check_submission_quality(item)
            self.assertEqual(status, "empty_punct", f"Failed for '{item}'")
            self.assertIn("tanda baca atau titik", msg)

    def test_too_short(self) -> None:
        short_inputs = ["a", "z", "?"]
        for item in short_inputs:
            status, msg = content_bank.check_submission_quality(item)
            self.assertIn(status, ("too_short", "empty_punct"))

    def test_excessive_repetition_and_mash(self) -> None:
        repeats = ["aaaaaa", "zzzzzzzz", "ddddd"]
        for item in repeats:
            status, msg = content_bank.check_submission_quality(item)
            self.assertEqual(status, "gibberish", f"Failed for '{item}'")

        mash = ["asdfghjk", "qwertyuiop", "zxcvbnm"]
        for item in mash:
            status, msg = content_bank.check_submission_quality(item)
            self.assertEqual(status, "gibberish", f"Failed for '{item}'")

    def test_valid_input(self) -> None:
        valid_inputs = [
            "Good morning!",
            "I am fine, thank you.",
            "My name is Budi.",
            "Yes, I can.",
            "Cat",
        ]
        for item in valid_inputs:
            status, msg = content_bank.check_submission_quality(item)
            self.assertEqual(status, "valid", f"Failed for valid text '{item}'")
            self.assertIsNone(msg)


if __name__ == "__main__":
    unittest.main()
