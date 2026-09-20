"""
Unit tests for offline Content Bank (1,000 curated exercises).
"""

from __future__ import annotations

import unittest
from typing import Any, Dict, List

import config
import content_bank


class TestContentBank(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = content_bank.EXERCISE_BANK
        self.all_exercises: List[Dict[str, Any]] = [
            ex
            for mode_dict in self.bank.values()
            for level_list in mode_dict.values()
            for ex in level_list
        ]

    def test_total_exercise_count(self) -> None:
        """Verify the content bank contains exactly 1,000 exercises."""
        self.assertEqual(len(self.all_exercises), 1000)
        self.assertEqual(content_bank.TOTAL_EXERCISES, 1000)

    def test_track_distribution(self) -> None:
        """Verify each of the 5 tracks has exactly 200 exercises."""
        expected_modes = [
            config.MODE_DAILY_CONVERSATION,
            config.MODE_VOCABULARY,
            config.MODE_GRAMMAR,
            config.MODE_READING,
            config.MODE_CHALLENGE,
        ]
        self.assertEqual(set(self.bank.keys()), set(expected_modes))

        for mode in expected_modes:
            mode_total = sum(len(items) for items in self.bank[mode].values())
            self.assertEqual(
                mode_total,
                200,
                f"Mode {mode} should have exactly 200 exercises, found {mode_total}",
            )

    def test_level_distribution(self) -> None:
        """Verify each track has 67 Beginner, 67 Intermediate, and 66 Advanced exercises."""
        for mode, levels in self.bank.items():
            self.assertEqual(
                len(levels[config.LEVEL_BEGINNER]),
                67,
                f"Mode {mode} beginner count mismatch",
            )
            self.assertEqual(
                len(levels[config.LEVEL_INTERMEDIATE]),
                67,
                f"Mode {mode} intermediate count mismatch",
            )
            self.assertEqual(
                len(levels[config.LEVEL_ADVANCED]),
                66,
                f"Mode {mode} advanced count mismatch",
            )

    def test_id_uniqueness(self) -> None:
        """Verify every exercise has a unique ID across all tracks and levels."""
        ids = [ex["id"] for ex in self.all_exercises]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate exercise IDs detected!")

    def test_schema_integrity(self) -> None:
        """Verify every exercise contains valid, non-empty required fields."""
        required_fields = ["id", "badge", "prompt", "expected", "primary_answer"]
        for ex in self.all_exercises:
            for field in required_fields:
                self.assertIn(field, ex, f"Missing field '{field}' in exercise {ex.get('id')}")
                self.assertTrue(ex[field], f"Empty field '{field}' in exercise {ex.get('id')}")
            self.assertIsInstance(ex["expected"], list)
            self.assertGreaterEqual(len(ex["expected"]), 1)

    def test_offline_retrieval_and_exclude(self) -> None:
        """Verify randomized retrieval and consecutive duplicate suppression."""
        for mode in self.bank.keys():
            for level in [config.LEVEL_BEGINNER, config.LEVEL_INTERMEDIATE, config.LEVEL_ADVANCED]:
                first = content_bank.get_offline_exercise(mode, level)
                self.assertIsNotNone(first.get("id"))
                self.assertTrue(first.get("prompt"))

                # With exclude_id provided
                second = content_bank.get_offline_exercise(mode, level, exclude_id=first["id"])
                self.assertNotEqual(
                    first["id"],
                    second["id"],
                    f"Consecutive retrieval returned duplicate ID for {mode}/{level}",
                )

    def test_pedagogical_answer_evaluation(self) -> None:
        """Verify answer grading handles exact match, typo correction, and mistakes."""
        ex = content_bank.get_exercise_by_id("conv_beg_01")
        self.assertIsNotNone(ex)

        # 1. Exact match
        res_exact = content_bank.evaluate_offline_answer(ex["primary_answer"], ex)
        self.assertIn("Tepat Sekali", res_exact)

        # 2. Near-miss typo (ratio >= 0.70)
        res_typo = content_bank.evaluate_offline_answer("God morning! I am fin, thankyou.", ex)
        self.assertIn("Salah Ketik", res_typo)

        # 3. Completely incorrect
        res_wrong = content_bank.evaluate_offline_answer("I want to eat chocolate", ex)
        self.assertIn("Kunci Jawaban yang Benar", res_wrong)


if __name__ == "__main__":
    unittest.main()
