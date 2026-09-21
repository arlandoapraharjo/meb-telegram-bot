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


def _strip_conversational_prefixes(text: str) -> str:
    """Strips common answer filler prefixes such as 'the answer is:', 'it is', 'jawabannya:'."""
    clean = re.sub(
        r'^(?:the\s+answer\s+(?:is|was):?|the\s+answer:?|it\s+(?:is|was):?|it\'s:?|its:?|jawabannya:?|jawaban:?|kunci:?|kuncinya:?)\s*',
        '',
        text,
        flags=re.IGNORECASE,
    )
    return clean.strip()



def _strip_articles(text: str) -> str:
    """Strips leading English grammatical articles (the, a, an)."""
    return re.sub(r'^(?:the|a|an)\s+', '', text, flags=re.IGNORECASE).strip()


def _is_valid_match(user_text: str, expected_item: str, prompt_text: str = "") -> bool:
    """
    Intelligently checks whether user_text matches expected_item:
    1. Exact normalized match.
    2. Match ignoring leading conversational prefixes ('the answer is', 'it is', 'jawabannya').
    3. Match ignoring leading articles ('the', 'a', 'an').
    4. Noun phrase extraction: if user answered a valid noun phrase from the prompt
       (e.g. 'the sovereign king' when expected is 'king' and 'sovereign king' is in the prompt).
    """
    norm_u = _normalize_answer(user_text)
    norm_e = _normalize_answer(expected_item)

    if norm_u == norm_e:
        return True

    # Strip conversational prefixes
    core_u = _strip_conversational_prefixes(norm_u)
    core_e = _strip_conversational_prefixes(norm_e)
    if core_u == norm_e or core_u == core_e:
        return True

    # Strip articles ("the king" == "king", "an apple" == "apple")
    u_no_art = _strip_articles(core_u)
    e_no_art = _strip_articles(core_e)
    if u_no_art == e_no_art:
        return True

    # Prompt-grounded noun phrase extraction:
    # If the student's answer contains the expected target keyword (e.g. 'king'),
    # and all additional words in the student's answer appear in the exercise prompt (e.g. 'sovereign'):
    if prompt_text and e_no_art:
        e_words = e_no_art.split()
        u_words = u_no_art.split()

        # Check if e_no_art is in u_no_art (e.g. 'king' in 'sovereign king')
        if all(w in u_words for w in e_words) or (len(e_words) == 1 and e_words[0] in u_words):
            norm_prompt = prompt_text.lower()
            # If the multi-word answer is directly present in the prompt
            if u_no_art in norm_prompt or norm_u in norm_prompt:
                return True
            # Or if every word in the user's answer appears in the prompt
            if all(w in norm_prompt for w in u_words):
                return True

    return False


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
    prompt_text = active_exercise.get("prompt", "")

    # 1. Exact & Intelligent Match (permits case, articles, prefixes, and valid prompt noun phrases)
    for exp in expected_list:
        if _is_valid_match(safe_user_text, exp, prompt_text):
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


def _mask_text_answer(answer: str) -> str:
    """
    Creates a pedagogical mask for single words or short phrases:
    - 'Nine' -> 'N _ _ e'
    - 'is' -> 'i _'
    - 'early diagnosis' -> 'e _ _ _ y   d _ _ _ _ _ _ _ s'
    """
    words = answer.strip().split()
    masked_words = []
    for w in words:
        clean = re.sub(r'^[^\w]+|[^\w]+$', '', w)
        if not clean:
            continue
        if len(clean) == 1:
            masked_words.append(clean.upper())
        elif len(clean) == 2:
            masked_words.append(f"{clean[0]} _")
        elif len(clean) == 3:
            masked_words.append(f"{clean[0]} _ {clean[-1]}")
        else:
            middle = " ".join(["_"] * (len(clean) - 2))
            masked_words.append(f"{clean[0]} {middle} {clean[-1]}")
    return "   ".join(masked_words)


def _extract_exercise_clue(prompt: str, badge: str, primary_answer: str) -> str:
    """Extracts meaningful Indonesian context from exercise prompt or badge for hints."""
    # 1. Look for vocabulary target in quotes
    m = re.search(r"untuk\s+['\"]([^'\"]+)['\"]", prompt, re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # 2. Look for explicit equals translation
    m = re.search(r"•\s*<b>[^<]+</b>\s*=\s*([^<\n]+)", prompt)
    if m:
        return m.group(1).strip()

    # 3. Look for reading question translation in parentheses
    m = re.search(r"\(([^\)]+\?)\)", prompt)
    if m:
        return m.group(1).strip()

    # 4. Look for situation instruction in conversation
    m = re.search(r"Katakan bahwa\s+([^:\n]+):", prompt, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r"Sampaikan bahwa\s+([^:\n]+):", prompt, re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # 5. Look for idiom description in challenge
    m = re.search(r"Ungkapan untuk\s+([^:\n]+):", prompt, re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # 6. Look for Artinya: in prompt
    m = re.search(r"Artinya:\s*([^)\n<]+)", prompt, re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # Clean badge as fallback
    clean_badge = re.sub(r'^[^\w]+', '', badge).strip()
    return clean_badge or "Kosakata bahasa Inggris"


def get_offline_hint(
    active_exercise: Optional[Dict[str, Any]],
    mode: str = config.MODE_DAILY_CONVERSATION,
    level: str = config.DEFAULT_LEVEL,
    query_text: str = "",
) -> str:
    """
    Provides a structured, pedagogical offline hint or explanation when
    the student asks 'apa maksudnya?', 'apa jawabannya?', or requests help (/hint).
    Does not require any Gemini API call (0 API cost, zero downtime).
    """
    level_info = config.LEVEL_INFO.get(level, config.LEVEL_INFO[config.DEFAULT_LEVEL])
    badge = level_info.get("badge", "Level")

    if not active_exercise:
        return (
            f"💡 <b>Petunjuk Belajar ({badge}):</b>\n\n"
            "Kamu sedang berada di menu latihan bahasa Inggris! "
            "Pilihlah salah satu topik di menu atau tekan <b>🔄 Latihan Lain</b> untuk mulai mengerjakan soal bersama Mebby ya! 😊"
        )

    title = active_exercise.get("title", "Latihan")
    ex_badge = active_exercise.get("badge", "Soal")
    prompt = active_exercise.get("prompt", "")
    primary_answer = active_exercise.get("primary_answer", "").strip()

    query_lower = query_text.lower().strip()

    # 1. If the user explicitly asks for the answer key or gives up
    if any(p in query_lower for p in ["kunci jawaban", "kunci", "menyerah", "pasrah", "bocoran", "jawaban asli", "jawaban benar"]):
        if primary_answer:
            return (
                f"🔑 <b>Kunci Jawaban ({badge}):</b>\n\n"
                f"📌 <b>Materi:</b> {ex_badge}\n"
                f"✅ Jawaban yang tepat: <code>{primary_answer}</code>\n\n"
                f"💡 Yuk coba ketik ulang jawaban di atas agar semakin ingat dan terlatih ya! Semangat! 😊"
            )

    context_clue = _extract_exercise_clue(prompt, ex_badge, primary_answer)

    # 2. If the user asks for meaning/explanation ('apa maksudnya', 'artinya apa', 'maksudnya gimana')
    is_explanation = any(p in query_lower for p in [
        "apa maksudnya", "artinya apa", "maksudnya gimana", "maksudnya apa",
        "artinya", "terjemahkan", "terjemahan", "jelaskan", "artikan", "maknanya"
    ])
    if is_explanation:
        return (
            f"💡 <b>Penjelasan Soal ({badge}):</b>\n\n"
            f"📌 <b>Materi:</b> {ex_badge}\n\n"
            f"📖 <b>Inti Pertanyaan / Konteks:</b>\n"
            f"\"{context_clue}\"\n\n"
            f"Perhatikan instruksi pada bagian <i>👉 Giliranmu</i> atau pertanyaan pada soal di atas ya. "
            f"Tuliskan jawaban dalam bahasa Inggris. Jangan takut salah, karena dari kesalahan kita bisa belajar!\n\n"
            f"👉 <b>Yuk coba ketik jawabanmu di bawah ini:</b>"
        )

    # 3. Default Hint Request (triggered by /hint, 'minta petunjuk', 'petunjuk', 'hint', 'clue', 'apa jawabannya', etc.)
    words = primary_answer.split()

    # If it's a long sentence (e.g. Conversation track, 5+ words)
    if len(words) >= 5:
        starter_count = min(4, len(words))
        starter = " ".join(words[:starter_count])
        return (
            f"💡 <b>Petunjuk Jawaban ({badge}):</b>\n\n"
            f"📌 <b>Materi:</b> {ex_badge}\n\n"
            f"🔍 <b>Petunjuk merangkai kalimat:</b>\n"
            f"• Situasi/Maksud: <i>\"{context_clue}\"</i>\n"
            f"• Awali kalimatmu dengan: <code>{starter}...</code>\n"
            f"• Jumlah kata: sekitar <b>{len(words)} kata</b>\n\n"
            f"👉 <b>Yuk coba rangkai dan ketik kalimatmu di bawah ini!</b>\n"
            f"<i>(Ketik <code>kunci jawaban</code> jika ingin melihat kalimat lengkapnya ya 😊)</i>"
        )

    # For single word or short phrase (Vocabulary, Reading, Grammar, Challenge)
    first_char = primary_answer[0].upper() if primary_answer else ""
    clean_ans = re.sub(r'[^\w\s]', '', primary_answer)
    letter_count = len(clean_ans.replace(' ', ''))
    masked = _mask_text_answer(primary_answer)

    details = []
    if context_clue and context_clue.lower() != primary_answer.lower():
        details.append(f"• Petunjuk makna/konteks: <b>{context_clue}</b>")

    if len(words) == 1:
        details.append(f"• Dimulai dengan huruf: <b>{first_char}...</b>")
        details.append(f"• Jumlah huruf: <b>{letter_count} huruf</b>")
    else:
        details.append(f"• Terdiri dari <b>{len(words)} kata</b> ({letter_count} huruf)")
        details.append(f"• Dimulai dengan huruf: <b>{first_char}...</b>")

    if masked:
        details.append(f"• Pola huruf: <code>{masked}</code>")

    details_str = "\n".join(details)
    return (
        f"💡 <b>Petunjuk Jawaban ({badge}):</b>\n\n"
        f"📌 <b>Materi:</b> {ex_badge}\n\n"
        f"🔍 <b>Petunjuk jawaban:</b>\n"
        f"{details_str}\n\n"
        f"👉 <b>Yuk coba ketik tebakanmu di bawah ini!</b>\n"
        f"<i>(Ketik <code>kunci jawaban</code> jika ingin melihat jawabannya langsung ya 😊)</i>"
    )



