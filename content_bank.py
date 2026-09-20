"""
Curated Offline Exercise Bank & Random Generator for English Buddy Bot.

Specially designed for Indonesian children and students from rural areas
who are starting English from ground zero.

Features:
- Exactly 1,000 curated, bite-sized exercises (5 tracks x 200 exercises).
- Track 1: 💬 Daily Conversation (200 exercises: 67 Beg, 67 Int, 66 Adv)
- Track 2: 📚 Vocabulary Builder (200 exercises: 67 Beg, 67 Int, 66 Adv)
- Track 3: 📝 Grammar Master (200 exercises: 67 Beg, 67 Int, 66 Adv)
- Track 4: 📖 Reading Comprehension (200 exercises: 67 Beg, 67 Int, 66 Adv)
- Track 5: 🎮 Weekly Challenge & Word Quizzes (200 exercises: 67 Beg, 67 Int, 66 Adv)
- Sub-millisecond O(1) in-memory retrieval.
- Consecutive duplicate suppression with exclude_id tracking.
- Deterministic answer keys (expected & primary_answer) for accurate offline evaluation.
- Intelligent anti-sugarcoat validation: catches punctuation, dots, spam, and incorrect answers
  with polite, constructive feedback.
"""

from __future__ import annotations

import difflib
import random
import re
import string
from typing import Any, Dict, List, Optional, Tuple

import config
from exercises import (
    CHALLENGE_EXERCISES,
    CONVERSATION_EXERCISES,
    GRAMMAR_EXERCISES,
    READING_EXERCISES,
    VOCABULARY_EXERCISES,
)

EXERCISE_BANK: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    config.MODE_DAILY_CONVERSATION: CONVERSATION_EXERCISES,
    config.MODE_VOCABULARY: VOCABULARY_EXERCISES,
    config.MODE_GRAMMAR: GRAMMAR_EXERCISES,
    config.MODE_READING: READING_EXERCISES,
    config.MODE_CHALLENGE: CHALLENGE_EXERCISES,
}

TOTAL_EXERCISES: int = sum(
    len(items) for levels in EXERCISE_BANK.values() for items in levels.values()
)


def get_exercise_by_id(exercise_id: str) -> Optional[Dict[str, Any]]:
    """Lookup an exercise by its unique ID across all modes and levels."""
    for mode_dict in EXERCISE_BANK.values():
        for level_list in mode_dict.values():
            for ex in level_list:
                if ex.get("id") == exercise_id:
                    return ex
    return None


def get_offline_exercise(
    mode: str,
    level: str = config.DEFAULT_LEVEL,
    exclude_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Selects a randomized exercise from the curated offline bank.
    Ensures that, whenever possible, the returned exercise differs from exclude_id
    so consecutive taps never repeat the exact same challenge.
    """
    level_dict = EXERCISE_BANK.get(mode, {}).get(level)
    if not level_dict:
        level_dict = EXERCISE_BANK.get(mode, {}).get(config.DEFAULT_LEVEL, [])

    if not level_dict:
        return {
            "id": "default_fallback",
            "title": config.LEARNING_MODES.get(mode, {}).get("title", "Latihan Bahasa Inggris"),
            "badge": "Latihan Seru",
            "prompt": "Yuk coba buat kalimat pendek dalam bahasa Inggris dan kirim ke sini!",
            "expected": [],
            "primary_answer": "",
        }

    candidates = [ex for ex in level_dict if ex.get("id") != exclude_id]
    chosen = random.choice(candidates if candidates else level_dict)

    mode_info = config.LEARNING_MODES.get(mode, {})
    return {
        "id": chosen.get("id"),
        "title": mode_info.get("title", "Latihan Bahasa Inggris"),
        "badge": chosen.get("badge", "Latihan"),
        "prompt": chosen.get("prompt", ""),
        "expected": chosen.get("expected", []),
        "primary_answer": chosen.get("primary_answer", ""),
    }


def check_submission_quality(user_text: str) -> Tuple[str, Optional[str]]:
    """
    Evaluates raw user input to guard against false praise.
    Returns a tuple of (status, polite_guidance_message).
    
    Status values:
    - 'empty_punct': string is empty or contains only punctuation/dots (e.g. '.', '...', '??')
    - 'too_short': string length is less than 2 alphanumeric characters
    - 'gibberish': keyboard mash or unnatural character repetition (e.g. 'asdfgh', 'aaaaa')
    - 'valid': normal text submission suitable for pedagogical evaluation
    """
    stripped = user_text.strip()
    if not stripped:
        return (
            "empty_punct",
            (
                "Halo! Sepertinya pesanmu kosong. 😊\n\n"
                "Yuk coba ketik jawaban untuk soal latihan di atas ya! Jangan khawatir salah, mari kita coba sama-sama."
            )
        )

    # Check if text consists exclusively of punctuation, symbols, or whitespace
    punct_set = set(string.punctuation + " \t\n\r…•—–-~`!@#$%^&*()_+={}[]|\\:;\"'<>,.?/")
    if all(ch in punct_set for ch in stripped):
        return (
            "empty_punct",
            (
                "Halo! Sepertinya kamu hanya mengetik tanda baca atau titik (<code>.</code>). 😊\n\n"
                "Yuk coba jawab soal latihan di atas dengan kata atau kalimat bahasa Inggris. Jangan ragu ya!"
            )
        )

    # Extract alphanumeric characters only
    alphanumeric_only = re.sub(r'[^a-zA-Z0-9]', '', stripped)
    if len(alphanumeric_only) < 2 and not stripped.isdigit():
        return (
            "too_short",
            (
                "Halo! Jawabanmu terlalu singkat. 😊\n\n"
                "Yuk coba ketik kata atau kalimat lengkap sesuai latihan di atas agar belajarmu semakin maksimal!"
            )
        )

    # Check for excessive character repetition (e.g. 'aaaaa', 'zzzzzz', 'dddd')
    if re.search(r'(.)\1{4,}', stripped.lower()):
        return (
            "gibberish",
            (
                "Halo! Jawaban yang kamu ketik terlihat seperti pengulangan huruf acak. 😊\n\n"
                "Yuk baca kembali petunjuk soal di atas dan coba ketik kata bahasa Inggris yang sesuai ya!"
            )
        )

    # Check for keyboard mash patterns
    mash_patterns = [
        r'^[asdfghjkl]{5,}$',
        r'^[qwertyuiop]{5,}$',
        r'^[zxcvbnm]{5,}$',
    ]
    for pat in mash_patterns:
        if re.match(pat, stripped.lower()):
            return (
                "gibberish",
                (
                    "Halo! Jawaban yang kamu ketik belum terbaca sebagai kata bahasa Inggris. 😊\n\n"
                    "Yuk coba ketik jawaban sesuai instruksi soal di atas!"
                )
            )

    return ("valid", None)


def _normalize_answer(text: str) -> str:
    """Helper to clean string for comparison."""
    clean = text.lower().strip()
    clean = re.sub(r'^[^\w]+|[^\w]+$', '', clean)
    clean = re.sub(r'\s+', ' ', clean)
    return clean


def evaluate_offline_answer(
    user_text: str,
    active_exercise: Optional[Dict[str, Any]],
    mode: str = config.MODE_DAILY_CONVERSATION,
    level: str = config.DEFAULT_LEVEL,
) -> str:
    """
    Pedagogically evaluates a student's answer without sugarcoating.
    - If user enters '.', spam, or gibberish: politely reminds without praise.
    - If user gives wrong answer: clearly states it is not yet correct, shows the answer key, and motivates.
    - If user is correct: praises accurately.
    """
    quality_status, quality_msg = check_submission_quality(user_text)
    if quality_msg:
        return quality_msg

    level_info = config.LEVEL_INFO.get(level, config.LEVEL_INFO[config.DEFAULT_LEVEL])
    badge = level_info.get("badge", "Level")
    safe_user_text = user_text.strip()

    # If no active exercise or no expected keys provided, give constructive fallback
    if not active_exercise or not active_exercise.get("expected"):
        return (
            f"✨ <b>Catatan Belajar ({badge}):</b>\n\n"
            f"Jawabanmu: <i>\"{safe_user_text}\"</i>\n\n"
            f"👍 Terima kasih sudah mencoba berlatih! "
            f"Yuk tekan <b>🔄 Next Exercise</b> untuk melanjutkan latihan dengan soal terarah."
        )

    expected_list = active_exercise.get("expected", [])
    primary_answer = active_exercise.get("primary_answer", expected_list[0] if expected_list else "")
    norm_user = _normalize_answer(safe_user_text)

    # 1. Exact Match (permits case differences and surrounding punctuation)
    for exp in expected_list:
        norm_exp = _normalize_answer(exp)
        if norm_user == norm_exp:
            return (
                f"🎉 <b>Jawabanmu Tepat Sekali! ({badge})</b>\n\n"
                f"📝 Jawabanmu: <code>{safe_user_text}</code>\n"
                f"✅ Kunci: <b>{primary_answer}</b>\n\n"
                f"🌟 Kerja bagus! Ejaan dan kalimatmu sudah 100% tepat. "
                f"Tekan <b>🔄 Next Exercise</b> untuk tantangan berikutnya!"
            )

    # 2. Minor Mistake & Typo Guard (detects near-misses, typos, extra letters, pronoun slips)
    best_ratio = 0.0
    best_exp_str = _normalize_answer(primary_answer)
    for exp in expected_list:
        n_exp = _normalize_answer(exp)
        ratio = difflib.SequenceMatcher(None, norm_user, n_exp).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_exp_str = n_exp

    if best_ratio >= 0.70:
        u_words = norm_user.split()
        e_words = best_exp_str.split()
        diff_points: List[str] = []

        if len(u_words) == len(e_words):
            for u_w, e_w in zip(u_words, e_words):
                if u_w != e_w:
                    diff_points.append(f"• Gunakan kata <b>{e_w}</b> (bukan <i>{u_w}</i>).")
        elif len(u_words) > 0 and len(e_words) > 0:
            diff_points.append(f"• Perhatikan ejaan yang benar: <b>{primary_answer}</b>.")

        diff_text = "\n".join(diff_points)
        if diff_text:
            diff_text = f"💡 <b>Perhatikan koreksi agar tidak salah kaprah ya:</b>\n{diff_text}\n\n"

        return (
            f"⚠️ <b>Hampir Benar, Tapi Ada Sedikit Typo / Salah Ketik! ({badge})</b>\n\n"
            f"📝 Jawabanmu: <code>{safe_user_text}</code>\n"
            f"✅ Kunci yang Benar: <b>{primary_answer}</b>\n\n"
            f"{diff_text}"
            f"Yuk coba ketik sekali lagi jawaban yang benar di atas agar tidak menjadi kebiasaan salah ketik ya! Semangat! 😊"
        )

    # 3. Completely Incorrect or Far Off
    return (
        f"💡 <b>Sedikit Lagi, Yuk Kita Koreksi! ({badge})</b>\n\n"
        f"📝 Jawabanmu: <i>\"{safe_user_text}\"</i>\n"
        f"🔑 <b>Kunci Jawaban yang Benar:</b> <code>{primary_answer}</code>\n\n"
        f"Jawabanmu masih belum tepat untuk soal ini. Jangan berkecil hati ya, salah itu wajar saat belajar! 😊\n"
        f"Yuk coba ketik kunci jawaban di atas, atau tekan <b>🔄 Next Exercise</b> untuk mencoba soal baru!"
    )


def get_offline_feedback(
    mode: str,
    level: str,
    safe_user_text: str,
    active_exercise: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Backwards-compatible wrapper delegating to evaluate_offline_answer.
    """
    return evaluate_offline_answer(safe_user_text, active_exercise, mode, level)
