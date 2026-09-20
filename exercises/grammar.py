"""
Curated Grammar exercises for English Buddy Bot.
Total: 200 exercises (67 Beginner, 67 Intermediate, 66 Advanced).
"""
from typing import Any, Dict, List
import config

GRAMMAR_EXERCISES: Dict[str, List[Dict[str, Any]]] = {
    config.LEVEL_BEGINNER: [
    {
        "id": "grm_beg_01",
        "badge": "📝 To Be: I am",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek I)</b>\n\nGunakan <b>am</b> untuk subjek <b>I</b>.\nContoh: <i>I am a student.</i> (Saya seorang murid.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I ___ happy today.\"",
        "expected": [
            "am",
            "i am happy today",
            "i am",
            "am happy today"
        ],
        "primary_answer": "am"
    },
    {
        "id": "grm_beg_02",
        "badge": "📝 To Be: You are",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek You)</b>\n\nGunakan <b>are</b> untuk subjek <b>You</b>.\nContoh: <i>You are smart.</i> (Kamu pintar.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"You ___ my best friend.\"",
        "expected": [
            "are",
            "you are my best friend",
            "you are",
            "are my best friend"
        ],
        "primary_answer": "are"
    },
    {
        "id": "grm_beg_03",
        "badge": "📝 To Be: He is",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek He)</b>\n\nGunakan <b>is</b> untuk <b>He</b> (dia laki-laki).\nContoh: <i>He is tall.</i> (Dia tinggi.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He ___ a doctor.\"",
        "expected": [
            "is",
            "he is a doctor",
            "he is",
            "is a doctor"
        ],
        "primary_answer": "is"
    },
    {
        "id": "grm_beg_04",
        "badge": "📝 To Be: She is",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek She)</b>\n\nGunakan <b>is</b> untuk <b>She</b> (dia perempuan).\nContoh: <i>She is kind.</i> (Dia baik hati.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She ___ a teacher.\"",
        "expected": [
            "is",
            "she is a teacher",
            "she is",
            "is a teacher"
        ],
        "primary_answer": "is"
    },
    {
        "id": "grm_beg_05",
        "badge": "📝 To Be: It is",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek It)</b>\n\nGunakan <b>is</b> untuk <b>It</b> (benda atau hewan tunggal).\nContoh: <i>It is a cat.</i> (Itu seekor kucing.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"It ___ a cute rabbit.\"",
        "expected": [
            "is",
            "it is a cute rabbit",
            "it is",
            "is a cute rabbit"
        ],
        "primary_answer": "is"
    },
    {
        "id": "grm_beg_06",
        "badge": "📝 To Be: We are",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek We)</b>\n\nGunakan <b>are</b> untuk subjek <b>We</b> (kami/kita).\nContoh: <i>We are ready.</i> (Kita sudah siap.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We ___ good friends.\"",
        "expected": [
            "are",
            "we are good friends",
            "we are",
            "are good friends"
        ],
        "primary_answer": "are"
    },
    {
        "id": "grm_beg_07",
        "badge": "📝 To Be: They are",
        "prompt": "✨ <b>Grammar Dasar: To Be (Subjek They)</b>\n\nGunakan <b>are</b> untuk subjek <b>They</b> (mereka).\nContoh: <i>They are happy.</i> (Mereka bahagia.)\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"They ___ students.\"",
        "expected": [
            "are",
            "they are students",
            "they are",
            "are students"
        ],
        "primary_answer": "are"
    },
    {
        "id": "grm_beg_08",
        "badge": "📝 Kata Kerja: I eat",
        "prompt": "🍚 <b>Simple Present: Subjek I</b>\n\nUntuk subjek <b>I</b>, kata kerja bentuk dasar tanpa akhiran 's'.\n\n👉 <b>Pilih kata yang benar (eat / eats):</b>\n\"I (eat/eats) rice every morning.\"",
        "expected": [
            "eat",
            "i eat",
            "i eat rice every morning",
            "eat rice every morning"
        ],
        "primary_answer": "eat"
    },
    {
        "id": "grm_beg_09",
        "badge": "📝 Kata Kerja: He eats",
        "prompt": "🍎 <b>Simple Present: Subjek He</b>\n\nUntuk subjek <b>He/She/It</b>, kata kerja ditambah akhiran <b>-s</b> atau <b>-es</b>.\n\n👉 <b>Pilih kata yang tepat (eat / eats):</b>\n\"Budi (eat/eats) an apple.\"",
        "expected": [
            "eats",
            "budi eats an apple",
            "he eats",
            "eats an apple"
        ],
        "primary_answer": "eats"
    },
    {
        "id": "grm_beg_10",
        "badge": "📝 Kata Kerja: She drinks",
        "prompt": "🥛 <b>Simple Present: Subjek She</b>\n\nSubjek tunggal perempuan (She/Siti) membutuhkan akhiran <b>-s</b> pada verb.\n\n👉 <b>Pilih kata yang tepat (drink / drinks):</b>\n\"She (drink/drinks) fresh milk.\"",
        "expected": [
            "drinks",
            "she drinks fresh milk",
            "she drinks",
            "drinks fresh milk"
        ],
        "primary_answer": "drinks"
    },
    {
        "id": "grm_beg_11",
        "badge": "📝 Kata Kerja Jamak: They play",
        "prompt": "⚽ <b>Simple Present: Subjek They</b>\n\nUntuk subjek jamak <b>They/We</b>, kata kerja kembali ke bentuk dasar tanpa 's'.\n\n👉 <b>Pilih kata yang tepat (play / plays):</b>\n\"They (play/plays) soccer in the yard.\"",
        "expected": [
            "play",
            "they play soccer in the yard",
            "they play",
            "play soccer"
        ],
        "primary_answer": "play"
    },
    {
        "id": "grm_beg_12",
        "badge": "📝 Kata Kerja Jamak: We study",
        "prompt": "📖 <b>Simple Present: Subjek We</b>\n\nUntuk <b>We</b>, gunakan kata kerja dasar.\n\n👉 <b>Pilih kata yang tepat (study / studies):</b>\n\"We (study/studies) English together.\"",
        "expected": [
            "study",
            "we study english together",
            "we study",
            "study english"
        ],
        "primary_answer": "study"
    },
    {
        "id": "grm_beg_13",
        "badge": "📍 Preposisi: in",
        "prompt": "🎒 <b>Preposisi Tempat: in (di dalam)</b>\n\nGunakan <b>in</b> untuk menunjukkan posisi di dalam ruangan/wadah.\n\n👉 <b>Lengkapi dengan preposisi yang tepat (in / on):</b>\n\"The pencil is ___ the bag.\"",
        "expected": [
            "in",
            "the pencil is in the bag",
            "is in the bag"
        ],
        "primary_answer": "in"
    },
    {
        "id": "grm_beg_14",
        "badge": "📍 Preposisi: on",
        "prompt": "🪑 <b>Preposisi Tempat: on (di atas permukaan)</b>\n\nGunakan <b>on</b> untuk benda yang menempel di atas permukaan meja, lantai, dll.\n\n👉 <b>Lengkapi kalimat ini (in / on):</b>\n\"The book is ___ the table.\"",
        "expected": [
            "on",
            "the book is on the table",
            "is on the table"
        ],
        "primary_answer": "on"
    },
    {
        "id": "grm_beg_15",
        "badge": "📍 Preposisi: under",
        "prompt": "🐱 <b>Preposisi Tempat: under (di bawah)</b>\n\nGunakan <b>under</b> bila letak benda berada di bawah sesuatu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The cat is sleeping ___ the bed.\" (di bawah ranjang)",
        "expected": [
            "under",
            "the cat is sleeping under the bed",
            "sleeping under the bed"
        ],
        "primary_answer": "under"
    },
    {
        "id": "grm_beg_16",
        "badge": "📍 Preposisi: at",
        "prompt": "🏫 <b>Preposisi Tempat: at (di titik lokasi tertentu)</b>\n\nGunakan <b>at</b> untuk lokasi spesifik seperti rumah atau sekolah.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I am ___ school right now.\"",
        "expected": [
            "at",
            "i am at school right now",
            "at school"
        ],
        "primary_answer": "at"
    },
    {
        "id": "grm_beg_17",
        "badge": "👉 Penunjuk Tunggal Dekat: This",
        "prompt": "✏️ <b>Kata Tunjuk Tunggal: This is (Ini)</b>\n\nGunakan <b>This is</b> untuk satu benda yang berada dekat.\n\n👉 <b>Pilih kata yang tepat (This / These):</b>\n\"___ is my new pen.\"",
        "expected": [
            "this",
            "this is my new pen",
            "this is"
        ],
        "primary_answer": "This"
    },
    {
        "id": "grm_beg_18",
        "badge": "👉 Penunjuk Tunggal Jauh: That",
        "prompt": "🏠 <b>Kata Tunjuk Tunggal: That is (Itu)</b>\n\nGunakan <b>That is</b> untuk satu benda yang berjarak jauh.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ is my house over there.\" (Itu rumahku)",
        "expected": [
            "that",
            "that is my house over there",
            "that is"
        ],
        "primary_answer": "That"
    },
    {
        "id": "grm_beg_19",
        "badge": "👉 Penunjuk Jamak Dekat: These",
        "prompt": "👟 <b>Kata Tunjuk Jamak: These are (Ini banyak)</b>\n\nGunakan <b>These are</b> untuk lebih dari satu benda di dekat kita.\n\n👉 <b>Pilih kata yang tepat (This / These):</b>\n\"___ are my shoes.\"",
        "expected": [
            "these",
            "these are my shoes",
            "these are"
        ],
        "primary_answer": "These"
    },
    {
        "id": "grm_beg_20",
        "badge": "👉 Penunjuk Jamak Jauh: Those",
        "prompt": "🐦 <b>Kata Tunjuk Jamak: Those are (Itu banyak)</b>\n\nGunakan <b>Those are</b> untuk banyak benda yang jauh.\n\n👉 <b>Pilih kata yang tepat (That / Those):</b>\n\"___ are beautiful birds in the sky.\"",
        "expected": [
            "those",
            "those are beautiful birds in the sky",
            "those are"
        ],
        "primary_answer": "Those"
    },
    {
        "id": "grm_beg_21",
        "badge": "❌ Kalimat Negatif: is not",
        "prompt": "🚫 <b>Kalimat Negatif: is not (bukan/tidak)</b>\n\nTambahkan <b>not</b> setelah to be untuk menyatakan penyangkalan.\n\n👉 <b>Lengkapi kalimat negatif ini:</b>\n\"He is ___ tired today.\"",
        "expected": [
            "not",
            "he is not tired today",
            "is not tired"
        ],
        "primary_answer": "not"
    },
    {
        "id": "grm_beg_22",
        "badge": "❌ Kalimat Negatif: are not",
        "prompt": "🚫 <b>Kalimat Negatif: are not</b>\n\nPenyangkalan untuk subjek jamak: are + not (aren't).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We are ___ late for class.\"",
        "expected": [
            "not",
            "we are not late for class",
            "are not late"
        ],
        "primary_answer": "not"
    },
    {
        "id": "grm_beg_23",
        "badge": "❓ Kalimat Tanya: Do you...?",
        "prompt": "❓ <b>Pertanyaan Present Tense: Do you</b>\n\nGunakan kata bantu <b>Do</b> untuk bertanya pada subjek You/They/We.\n\n👉 <b>Lengkapi pertanyaan ini (Do / Does):</b>\n\"___ you like ice cream?\"",
        "expected": [
            "do",
            "do you like ice cream",
            "do you like ice cream?"
        ],
        "primary_answer": "Do"
    },
    {
        "id": "grm_beg_24",
        "badge": "❓ Kalimat Tanya: Does he...?",
        "prompt": "❓ <b>Pertanyaan Present Tense: Does</b>\n\nGunakan kata bantu <b>Does</b> untuk bertanya pada subjek He/She/It.\n\n👉 <b>Pilih kata bantu yang tepat (Do / Does):</b>\n\"___ he have a bicycle?\"",
        "expected": [
            "does",
            "does he have a bicycle",
            "does he have a bicycle?"
        ],
        "primary_answer": "Does"
    },
    {
        "id": "grm_beg_25",
        "badge": "📝 Kata Kerja: have",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>have</b> untuk subjek I, You, We, They.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I ___ two new pencils.\"",
        "expected": [
            "have",
            "i have"
        ],
        "primary_answer": "have"
    },
    {
        "id": "grm_beg_26",
        "badge": "📝 Kata Kerja: has",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>has</b> untuk subjek He, She, It (tunggal).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Budi ___ a red bicycle.\"",
        "expected": [
            "has",
            "he has"
        ],
        "primary_answer": "has"
    },
    {
        "id": "grm_beg_27",
        "badge": "📝 Kata Kerja: likes",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nSubjek tunggal (She) membutuhkan akhiran -s pada verb 'like'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She ___ sweet apples.\"",
        "expected": [
            "likes",
            "she likes"
        ],
        "primary_answer": "likes"
    },
    {
        "id": "grm_beg_28",
        "badge": "📝 Kata Kerja: like",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nSubjek jamak (We/They) menggunakan kata kerja dasar 'like'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We ___ fresh milk.\"",
        "expected": [
            "like",
            "we like"
        ],
        "primary_answer": "like"
    },
    {
        "id": "grm_beg_29",
        "badge": "📝 Artikel Kata: an apple",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>an</b> sebelum kata yang diawali bunyi vokal (a, i, u, e, o).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I eat ___ apple every morning.\" (a / an)",
        "expected": [
            "an",
            "an apple"
        ],
        "primary_answer": "an"
    },
    {
        "id": "grm_beg_30",
        "badge": "📝 Artikel Kata: a book",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>a</b> sebelum kata yang diawali bunyi konsonan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"There is ___ book on the table.\" (a / an)",
        "expected": [
            "a",
            "a book"
        ],
        "primary_answer": "a"
    },
    {
        "id": "grm_beg_31",
        "badge": "📝 Artikel Kata: an orange",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nKata 'orange' diawali huruf vokal O, gunakan <b>an</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Mother gave me ___ orange.\" (a / an)",
        "expected": [
            "an",
            "an orange"
        ],
        "primary_answer": "an"
    },
    {
        "id": "grm_beg_32",
        "badge": "📝 Artikel Kata: a pencil",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nKata 'pencil' diawali bunyi konsonan P, gunakan <b>a</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He buys ___ sharp pencil.\" (a / an)",
        "expected": [
            "a",
            "a pencil"
        ],
        "primary_answer": "a"
    },
    {
        "id": "grm_beg_33",
        "badge": "📝 Jamak Beraturan: cats",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nTambahkan akhiran <b>-s</b> untuk mengubah benda menjadi jamak (lebih dari satu).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I see three (cat) ___ playing in the yard.\"",
        "expected": [
            "cats",
            "three cats"
        ],
        "primary_answer": "cats"
    },
    {
        "id": "grm_beg_34",
        "badge": "📝 Jamak Berakhiran -es: boxes",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nKata berakhiran -x ditambah <b>-es</b> dalam bentuk jamak.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Put these two (box) ___ in the corner.\"",
        "expected": [
            "boxes",
            "two boxes"
        ],
        "primary_answer": "boxes"
    },
    {
        "id": "grm_beg_35",
        "badge": "📝 Jamak Berakhiran -es: watches",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nKata berakhiran -ch ditambah <b>-es</b> dalam bentuk jamak.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Father has two wrist (watch) ___.\"",
        "expected": [
            "watches",
            "two watches"
        ],
        "primary_answer": "watches"
    },
    {
        "id": "grm_beg_36",
        "badge": "📝 Jamak Tidak Beraturan: children",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nChild (satu anak) berubah menjadi <b>children</b> (banyak anak).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Five (child) ___ are playing in the garden.\"",
        "expected": [
            "children",
            "five children"
        ],
        "primary_answer": "children"
    },
    {
        "id": "grm_beg_37",
        "badge": "📝 Jamak Tidak Beraturan: men",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nMan (satu pria) berubah menjadi <b>men</b> (banyak pria).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Two (man) ___ are standing near the gate.\"",
        "expected": [
            "men",
            "two men"
        ],
        "primary_answer": "men"
    },
    {
        "id": "grm_beg_38",
        "badge": "📝 Kepemilikan: my",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>my</b> untuk menyatakan kepunyaan saya.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"This is ___ new school bag.\" (punyaku: my / your)",
        "expected": [
            "my",
            "my bag"
        ],
        "primary_answer": "my"
    },
    {
        "id": "grm_beg_39",
        "badge": "📝 Kepemilikan: your",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>your</b> untuk menyatakan kepunyaanmu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Is that ___ water bottle?\" (punyamu: my / your)",
        "expected": [
            "your",
            "your bottle"
        ],
        "primary_answer": "your"
    },
    {
        "id": "grm_beg_40",
        "badge": "📝 Kepemilikan: his",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>his</b> untuk kepunyaan dia laki-laki.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Ahmad is riding ___ bicycle.\" (his / her)",
        "expected": [
            "his",
            "his bicycle"
        ],
        "primary_answer": "his"
    },
    {
        "id": "grm_beg_41",
        "badge": "📝 Kepemilikan: her",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>her</b> untuk kepunyaan dia perempuan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Siti is combing ___ long hair.\" (his / her)",
        "expected": [
            "her",
            "her hair"
        ],
        "primary_answer": "her"
    },
    {
        "id": "grm_beg_42",
        "badge": "📝 Kepemilikan: their",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>their</b> untuk kepunyaan mereka.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The students are cleaning ___ classroom.\" (their / our)",
        "expected": [
            "their",
            "their classroom"
        ],
        "primary_answer": "their"
    },
    {
        "id": "grm_beg_43",
        "badge": "📝 Kepemilikan: our",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>our</b> untuk kepunyaan kami / kita.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We love ___ beautiful country.\" (our / their)",
        "expected": [
            "our",
            "our country"
        ],
        "primary_answer": "our"
    },
    {
        "id": "grm_beg_44",
        "badge": "📍 Preposisi: behind",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>behind</b> untuk posisi di belakang sesuatu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The cat is hiding ___ the door.\" (di belakang)",
        "expected": [
            "behind",
            "behind the door"
        ],
        "primary_answer": "behind"
    },
    {
        "id": "grm_beg_45",
        "badge": "📍 Preposisi: in front of",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>in front of</b> untuk posisi di depan sesuatu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The teacher stands ___ the class.\" (di depan)",
        "expected": [
            "in front of",
            "in front of the class"
        ],
        "primary_answer": "in front of"
    },
    {
        "id": "grm_beg_46",
        "badge": "📍 Preposisi: next to",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>next to</b> untuk posisi di samping/sebelah.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Budi sits ___ Ahmad in the classroom.\" (di sebelah)",
        "expected": [
            "next to",
            "beside"
        ],
        "primary_answer": "next to"
    },
    {
        "id": "grm_beg_47",
        "badge": "📍 Preposisi: between",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>between</b> untuk posisi di antara dua benda.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The ball is ___ the two chairs.\" (di antara)",
        "expected": [
            "between",
            "between the chairs"
        ],
        "primary_answer": "between"
    },
    {
        "id": "grm_beg_48",
        "badge": "❓ Kata Tanya: Where",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>Where</b> untuk menanyakan tempat / lokasi.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ is your school located?\" (Where / When)",
        "expected": [
            "where",
            "where is your school located"
        ],
        "primary_answer": "Where"
    },
    {
        "id": "grm_beg_49",
        "badge": "❓ Kata Tanya: When",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>When</b> untuk menanyakan waktu kegiatan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ does the movie start?\" (When / Who)",
        "expected": [
            "when",
            "when does the movie start"
        ],
        "primary_answer": "When"
    },
    {
        "id": "grm_beg_50",
        "badge": "❓ Kata Tanya: Who",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>Who</b> untuk menanyakan sosok / orang.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ is the president of Indonesia?\" (Who / What)",
        "expected": [
            "who",
            "who is the president"
        ],
        "primary_answer": "Who"
    },
    {
        "id": "grm_beg_51",
        "badge": "❓ Kata Tanya: Why",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>Why</b> untuk menanyakan alasan / mengapa.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ are you crying, little sister?\" (Why / Where)",
        "expected": [
            "why",
            "why are you crying"
        ],
        "primary_answer": "Why"
    },
    {
        "id": "grm_beg_52",
        "badge": "🚫 Penyangkal Present: do not",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nSubjek I / You / We / They menggunakan <b>do not</b> (don't).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I ___ like bitter medicine.\" (do not / does not)",
        "expected": [
            "do not",
            "don't",
            "dont"
        ],
        "primary_answer": "do not"
    },
    {
        "id": "grm_beg_53",
        "badge": "🚫 Penyangkal Present: does not",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nSubjek tunggal He / She / It menggunakan <b>does not</b> (doesn't).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He ___ eat spicy food.\" (do not / does not)",
        "expected": [
            "does not",
            "doesn't",
            "doesnt"
        ],
        "primary_answer": "does not"
    },
    {
        "id": "grm_beg_54",
        "badge": "🚫 Penyangkal Present: does not",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nSubjek tunggal Nina menggunakan <b>does not</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Nina ___ watch horror movies.\" (do not / does not)",
        "expected": [
            "does not",
            "doesn't"
        ],
        "primary_answer": "does not"
    },
    {
        "id": "grm_beg_55",
        "badge": "❓ Tanya To Be: Are you",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nMulai pertanyaan dengan <b>Are</b> untuk subjek You.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ you ready for school today?\" (Are / Is)",
        "expected": [
            "are",
            "are you ready"
        ],
        "primary_answer": "Are"
    },
    {
        "id": "grm_beg_56",
        "badge": "❓ Tanya To Be: Is he",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nMulai pertanyaan dengan <b>Is</b> untuk subjek He tunggal.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ he your older brother?\" (Are / Is)",
        "expected": [
            "is",
            "is he your older brother"
        ],
        "primary_answer": "Is"
    },
    {
        "id": "grm_beg_57",
        "badge": "❓ Tanya To Be: Is it",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nMulai pertanyaan dengan <b>Is</b> untuk subjek It.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ it raining outside?\" (Are / Is)",
        "expected": [
            "is",
            "is it raining"
        ],
        "primary_answer": "Is"
    },
    {
        "id": "grm_beg_58",
        "badge": "⏰ Preposisi Waktu: in the morning",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>in</b> untuk rentang waktu morning/afternoon/evening.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We wake up early ___ the morning.\" (in / on)",
        "expected": [
            "in",
            "in the morning"
        ],
        "primary_answer": "in"
    },
    {
        "id": "grm_beg_59",
        "badge": "📅 Preposisi Hari: on Monday",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>on</b> sebelum nama-nama hari (Monday, Sunday, etc.).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The flag ceremony is held ___ Monday.\" (in / on)",
        "expected": [
            "on",
            "on monday"
        ],
        "primary_answer": "on"
    },
    {
        "id": "grm_beg_60",
        "badge": "⏰ Preposisi Jam: at seven",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>at</b> untuk jam yang spesifik.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"School starts ___ seven o'clock.\" (at / on)",
        "expected": [
            "at",
            "at seven"
        ],
        "primary_answer": "at"
    },
    {
        "id": "grm_beg_61",
        "badge": "📝 Kata Kerja: run",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nUntuk subjek jamak 'They', kata kerja bentuk dasar tanpa akhiran -s.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"They ___ fast on the running track.\" (run / runs)",
        "expected": [
            "run",
            "they run"
        ],
        "primary_answer": "run"
    },
    {
        "id": "grm_beg_62",
        "badge": "📝 Kata Kerja: runs",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nUntuk subjek tunggal 'The dog', tambahkan akhiran -s.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The dog ___ after the red ball.\" (run / runs)",
        "expected": [
            "runs",
            "the dog runs"
        ],
        "primary_answer": "runs"
    },
    {
        "id": "grm_beg_63",
        "badge": "📝 Kata Kerja: study",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nUntuk subjek 'We', gunakan bentuk dasar 'study'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We ___ English together every day.\" (study / studies)",
        "expected": [
            "study",
            "we study"
        ],
        "primary_answer": "study"
    },
    {
        "id": "grm_beg_64",
        "badge": "📝 Kata Kerja: studies",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nUntuk subjek tunggal 'Siti', study berubah menjadi <b>studies</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Siti ___ diligently every night.\" (study / studies)",
        "expected": [
            "studies",
            "siti studies"
        ],
        "primary_answer": "studies"
    },
    {
        "id": "grm_beg_65",
        "badge": "📝 Kata Kerja: watch",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nUntuk subjek 'I', gunakan bentuk dasar 'watch'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I ___ funny cartoon videos.\" (watch / watches)",
        "expected": [
            "watch",
            "i watch"
        ],
        "primary_answer": "watch"
    },
    {
        "id": "grm_beg_66",
        "badge": "📝 Kata Kerja: watches",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nUntuk subjek tunggal 'He', watch ditambah -es menjadi <b>watches</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He ___ television after dinner.\" (watch / watches)",
        "expected": [
            "watches",
            "he watches"
        ],
        "primary_answer": "watches"
    },
    {
        "id": "grm_beg_67",
        "badge": "💪 Modal Kemampuan: can",
        "prompt": "✨ <b>Grammar Dasar:</b>\n\nGunakan <b>can</b> untuk menyatakan kemampuan melakukan sesuatu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I ___ swim very well across the river.\" (can / am)",
        "expected": [
            "can",
            "i can"
        ],
        "primary_answer": "can"
    }
],
    config.LEVEL_INTERMEDIATE: [
    {
        "id": "grm_int_01",
        "badge": "⏳ Regular Past Tense: played",
        "prompt": "⚽ <b>Simple Past Tense: Regular Verb (-ed)</b>\n\nKata kerja beraturan di masa lampau diakhiri <b>-ed</b>.\nContoh: play ➔ played.\n\n👉 <b>Ubah kata 'play' ke bentuk lampau:</b>\n\"Yesterday, they (play) ___ football in the stadium.\"",
        "expected": [
            "played",
            "they played",
            "played football"
        ],
        "primary_answer": "played"
    },
    {
        "id": "grm_int_02",
        "badge": "⏳ Regular Past Tense: watched",
        "prompt": "📺 <b>Simple Past Tense: Regular Verb (-ed)</b>\n\nWatch ➔ Watched (menonton).\n\n👉 <b>Tulis bentuk lampau dari kata 'watch':</b>\n\"Last night, I ___ an interesting movie.\"",
        "expected": [
            "watched",
            "i watched",
            "watched an interesting movie"
        ],
        "primary_answer": "watched"
    },
    {
        "id": "grm_int_03",
        "badge": "⏳ Regular Past Tense: cooked",
        "prompt": "🍳 <b>Simple Past Tense: Regular Verb (-ed)</b>\n\nCook ➔ Cooked (memasak).\n\n👉 <b>Lengkapi kalimat bentuk lampau ini:</b>\n\"Mother ___ delicious fried chicken this morning.\"",
        "expected": [
            "cooked",
            "mother cooked",
            "cooked delicious fried chicken"
        ],
        "primary_answer": "cooked"
    },
    {
        "id": "grm_int_04",
        "badge": "🔄 Irregular Past: went",
        "prompt": "🚗 <b>Simple Past: Irregular Verb (Go ➔ Went)</b>\n\nKata kerja tidak beraturan berubah bentuk.\nContoh: Go ➔ Went (pergi).\n\n👉 <b>Tulis bentuk lampau dari 'go':</b>\n\"Two days ago, we ___ to the beach.\"",
        "expected": [
            "went",
            "we went",
            "went to the beach"
        ],
        "primary_answer": "went"
    },
    {
        "id": "grm_int_05",
        "badge": "🔄 Irregular Past: ate",
        "prompt": "🍜 <b>Simple Past: Irregular Verb (Eat ➔ Ate)</b>\n\nEat ➔ Ate (makan di masa lampau).\n\n👉 <b>Lengkapi dengan bentuk lampau dari 'eat':</b>\n\"Budi ___ noodles for breakfast this morning.\"",
        "expected": [
            "ate",
            "budi ate",
            "ate noodles"
        ],
        "primary_answer": "ate"
    },
    {
        "id": "grm_int_06",
        "badge": "🔄 Irregular Past: bought",
        "prompt": "🛍️ <b>Simple Past: Irregular Verb (Buy ➔ Bought)</b>\n\nBuy ➔ Bought (membeli).\n\n👉 <b>Ubah kata kerja 'buy' ke past tense:</b>\n\"She ___ a new backpack yesterday.\"",
        "expected": [
            "bought",
            "she bought",
            "bought a new backpack"
        ],
        "primary_answer": "bought"
    },
    {
        "id": "grm_int_07",
        "badge": "🔄 Irregular Past: saw",
        "prompt": "👀 <b>Simple Past: Irregular Verb (See ➔ Saw)</b>\n\nSee ➔ Saw (melihat).\n\n👉 <b>Lengkapi kalimat ini dengan past tense dari 'see':</b>\n\"We ___ a beautiful rainbow after the rain.\"",
        "expected": [
            "saw",
            "we saw",
            "saw a beautiful rainbow"
        ],
        "primary_answer": "saw"
    },
    {
        "id": "grm_int_08",
        "badge": "🕰️ Past To Be: was",
        "prompt": "🛌 <b>Past To Be: was</b>\n\nGunakan <b>was</b> untuk subjek I, He, She, It di masa lampau.\n\n👉 <b>Pilih to be lampau yang tepat (was / were):</b>\n\"I ___ very tired yesterday.\"",
        "expected": [
            "was",
            "i was",
            "i was very tired yesterday"
        ],
        "primary_answer": "was"
    },
    {
        "id": "grm_int_09",
        "badge": "🕰️ Past To Be: were",
        "prompt": "👥 <b>Past To Be: were</b>\n\nGunakan <b>were</b> untuk subjek You, We, They di masa lampau.\n\n👉 <b>Pilih to be lampau yang tepat (was / were):</b>\n\"They ___ at the library yesterday afternoon.\"",
        "expected": [
            "were",
            "they were",
            "they were at the library"
        ],
        "primary_answer": "were"
    },
    {
        "id": "grm_int_10",
        "badge": "🕰️ Past To Be Negatif: was not",
        "prompt": "🏥 <b>Past To Be Negatif: was not</b>\n\nBentuk negatif lampau tunggal: was not / wasn't.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She was ___ at school yesterday because she visited her grandmother.\"",
        "expected": [
            "not",
            "was not",
            "she was not"
        ],
        "primary_answer": "not"
    },
    {
        "id": "grm_int_11",
        "badge": "💪 Modal Verb: can",
        "prompt": "🏊 <b>Modal: can (bisa / mampu)</b>\n\nModal 'can' diikuti kata kerja bentuk dasar tanpa 'to'.\n\n👉 <b>Lengkapi dengan kata modal 'can':</b>\n\"He ___ swim across the pool easily.\"",
        "expected": [
            "can",
            "he can",
            "can swim"
        ],
        "primary_answer": "can"
    },
    {
        "id": "grm_int_12",
        "badge": "💪 Modal Negatif: cannot",
        "prompt": "🚫 <b>Modal Negatif: cannot / can't (tidak bisa)</b>\n\nMenyatakan ketidakmampuan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Penguins ___ fly in the air, but they swim very fast.\"",
        "expected": [
            "cannot",
            "can't",
            "cant",
            "cannot fly",
            "can't fly"
        ],
        "primary_answer": "cannot"
    },
    {
        "id": "grm_int_13",
        "badge": "📋 Modal Kewajiban: must",
        "prompt": "🚦 <b>Modal Kewajiban: must (harus / wajib)</b>\n\nGunakan <b>must</b> untuk menyatakan keharusan mutlak.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Drivers ___ stop when the traffic light is red.\"",
        "expected": [
            "must",
            "drivers must",
            "must stop"
        ],
        "primary_answer": "must"
    },
    {
        "id": "grm_int_14",
        "badge": "💡 Modal Saran: should",
        "prompt": "💤 <b>Modal Saran: should (sebaiknya)</b>\n\nGunakan <b>should</b> untuk memberi nasihat atau anjuran.\n\n👉 <b>Lengkapi kalimat nasihat ini:</b>\n\"You ___ drink plenty of water when doing sports.\"",
        "expected": [
            "should",
            "you should",
            "should drink"
        ],
        "primary_answer": "should"
    },
    {
        "id": "grm_int_15",
        "badge": "⚖️ Perbandingan: taller than",
        "prompt": "🦒 <b>Comparative Adjective (-er than)</b>\n\nUntuk membandingkan 2 hal dengan kata sifat pendek: kata sifat + er + than.\n\n👉 <b>Ubah kata 'tall' menjadi bentuk perbandingan:</b>\n\"A giraffe is (tall) ___ than a horse.\"",
        "expected": [
            "taller",
            "taller than",
            "is taller than"
        ],
        "primary_answer": "taller"
    },
    {
        "id": "grm_int_16",
        "badge": "⚖️ Perbandingan: faster than",
        "prompt": "🐆 <b>Comparative Adjective: faster than</b>\n\nFast ➔ Faster than (lebih cepat daripada).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"A cheetah runs ___ than a lion.\" (lebih cepat)",
        "expected": [
            "faster",
            "faster than"
        ],
        "primary_answer": "faster"
    },
    {
        "id": "grm_int_17",
        "badge": "💎 Perbandingan Panjang: more expensive",
        "prompt": "🚗 <b>Comparative Adjective: more + adjective</b>\n\nUntuk kata sifat panjang (3 suku kata atau lebih), gunakan <b>more</b>.\n\n👉 <b>Lengkapi kalimat perbandingan ini:</b>\n\"A car is ___ expensive than a bicycle.\"",
        "expected": [
            "more",
            "more expensive",
            "more expensive than"
        ],
        "primary_answer": "more"
    },
    {
        "id": "grm_int_18",
        "badge": "🌺 Perbandingan Panjang: more beautiful",
        "prompt": "🌸 <b>Comparative Adjective: more beautiful</b>\n\nBeautiful ➔ More beautiful than.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"This flower garden is ___ beautiful than before.\"",
        "expected": [
            "more",
            "more beautiful"
        ],
        "primary_answer": "more"
    },
    {
        "id": "grm_int_19",
        "badge": "⚡ Sedang Terjadi: is reading",
        "prompt": "📚 <b>Present Continuous Tense (am/is/are + V-ing)</b>\n\nMenyatakan aktivitas yang sedang berlangsung saat ini.\n\n👉 <b>Lengkapi bentuk verb 'read':</b>\n\"Rani is ___ a storybook in the living room right now.\"",
        "expected": [
            "reading",
            "is reading",
            "reading a storybook"
        ],
        "primary_answer": "reading"
    },
    {
        "id": "grm_int_20",
        "badge": "⚡ Sedang Terjadi: are playing",
        "prompt": "⚽ <b>Present Continuous: are playing</b>\n\nSubjek jamak (They/The boys) menggunakan <b>are</b> + V-ing.\n\n👉 <b>Lengkapi bentuk verb 'play':</b>\n\"The children are ___ games outside.\"",
        "expected": [
            "playing",
            "are playing"
        ],
        "primary_answer": "playing"
    },
    {
        "id": "grm_int_21",
        "badge": "⚡ Sedang Terjadi: is cooking",
        "prompt": "🍳 <b>Present Continuous: is cooking</b>\n\nGunakan is + cooking untuk subjek tunggal yang sedang memasak.\n\n👉 <b>Lengkapi dengan kata kerja bentuk -ing dari 'cook':</b>\n\"Mother is ___ lunch in the kitchen.\"",
        "expected": [
            "cooking",
            "is cooking"
        ],
        "primary_answer": "cooking"
    },
    {
        "id": "grm_int_22",
        "badge": "🔗 Kata Hubung Sebab: because",
        "prompt": "💧 <b>Conjunction: because (karena)</b>\n\nGunakan <b>because</b> untuk menjelaskan alasan/sebab.\n\n👉 <b>Lengkapi kalimat ini (because / but):</b>\n\"I drink plenty of water ___ I feel thirsty.\"",
        "expected": [
            "because",
            "because i feel thirsty"
        ],
        "primary_answer": "because"
    },
    {
        "id": "grm_int_23",
        "badge": "🔗 Kata Hubung Kontras: but",
        "prompt": "⚖️ <b>Conjunction: but (tetapi / namun)</b>\n\nGunakan <b>but</b> untuk menghubungkan dua pernyataan yang berlawanan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He studied diligently, ___ he still needs more practice.\"",
        "expected": [
            "but",
            "but he still"
        ],
        "primary_answer": "but"
    },
    {
        "id": "grm_int_24",
        "badge": "🔗 Kata Hubung Akibat: so",
        "prompt": "☔ <b>Conjunction: so (sehingga / maka)</b>\n\nGunakan <b>so</b> untuk menunjukkan hasil atau akibat logis.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"It is raining heavily outside, ___ I brought an umbrella.\"",
        "expected": [
            "so",
            "so i brought an umbrella"
        ],
        "primary_answer": "so"
    },
    {
        "id": "grm_int_25",
        "badge": "⏳ Bentuk Lampau Irregular: went",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'go' adalah <b>went</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Yesterday, our family ___ to the city zoo.\" (go / went)",
        "expected": [
            "went",
            "we went"
        ],
        "primary_answer": "went"
    },
    {
        "id": "grm_int_26",
        "badge": "⏳ Bentuk Lampau Irregular: took",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'take' adalah <b>took</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He ___ many beautiful photographs during the trip.\" (take / took)",
        "expected": [
            "took",
            "he took"
        ],
        "primary_answer": "took"
    },
    {
        "id": "grm_int_27",
        "badge": "⏳ Bentuk Lampau Irregular: gave",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'give' adalah <b>gave</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Grandmother ___ me a shiny silver coin.\" (give / gave)",
        "expected": [
            "gave",
            "she gave"
        ],
        "primary_answer": "gave"
    },
    {
        "id": "grm_int_28",
        "badge": "⏳ Bentuk Lampau Irregular: made",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'make' adalah <b>made</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Mother ___ delicious chocolate cake yesterday.\" (make / made)",
        "expected": [
            "made",
            "mother made"
        ],
        "primary_answer": "made"
    },
    {
        "id": "grm_int_29",
        "badge": "⏳ Bentuk Lampau Irregular: wrote",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'write' adalah <b>wrote</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The student ___ a wonderful poem for the teacher.\" (write / wrote)",
        "expected": [
            "wrote",
            "the student wrote"
        ],
        "primary_answer": "wrote"
    },
    {
        "id": "grm_int_30",
        "badge": "⏳ Bentuk Lampau Irregular: drank",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'drink' adalah <b>drank</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"After jogging, he ___ two glasses of cold water.\" (drink / drank)",
        "expected": [
            "drank",
            "he drank"
        ],
        "primary_answer": "drank"
    },
    {
        "id": "grm_int_31",
        "badge": "⏳ Bentuk Lampau Irregular: slept",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'sleep' adalah <b>slept</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The tired baby ___ soundly throughout the night.\" (sleep / slept)",
        "expected": [
            "slept",
            "the baby slept"
        ],
        "primary_answer": "slept"
    },
    {
        "id": "grm_int_32",
        "badge": "⏳ Bentuk Lampau Irregular: found",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'find' adalah <b>found</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Yesterday, Sarah ___ her missing watch under the desk.\" (find / found)",
        "expected": [
            "found",
            "sarah found"
        ],
        "primary_answer": "found"
    },
    {
        "id": "grm_int_33",
        "badge": "⏳ Bentuk Lampau Irregular: came",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau (V2) dari 'come' adalah <b>came</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"My uncle ___ to our house last night.\" (come / came)",
        "expected": [
            "came",
            "uncle came"
        ],
        "primary_answer": "came"
    },
    {
        "id": "grm_int_34",
        "badge": "🚫 Penyangkal Lampau: did not",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nDalam kalimat lampau negatif, gunakan <b>did not</b> + V1.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She ___ come to school yesterday because of fever.\" (did not / was not)",
        "expected": [
            "did not",
            "didn't",
            "didnt"
        ],
        "primary_answer": "did not"
    },
    {
        "id": "grm_int_35",
        "badge": "❓ Tanya Lampau: Did you",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nPertanyaan lampau diawali kata bantu <b>Did</b> + V1.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ you finish your mathematics homework last night?\" (Did / Do)",
        "expected": [
            "did",
            "did you finish"
        ],
        "primary_answer": "Did"
    },
    {
        "id": "grm_int_36",
        "badge": "🚀 Masa Depan: will",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>will</b> + V1 untuk menyatakan rencana masa depan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Next year, our school ___ build a new science lab.\" (will / was)",
        "expected": [
            "will",
            "will build"
        ],
        "primary_answer": "will"
    },
    {
        "id": "grm_int_37",
        "badge": "🚀 Masa Depan: is going to",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>is going to</b> untuk rencana yang sudah pasti.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Budi ___ buy a new pair of shoes this Sunday.\" (is going to / will be)",
        "expected": [
            "is going to",
            "going to"
        ],
        "primary_answer": "is going to"
    },
    {
        "id": "grm_int_38",
        "badge": "🏆 Superlatif: tallest",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nUntuk kata sifat pendek paling tinggi: the + adjective + -est.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Mount Everest is the ___ mountain in the world.\" (tall / tallest)",
        "expected": [
            "tallest",
            "the tallest"
        ],
        "primary_answer": "tallest"
    },
    {
        "id": "grm_int_39",
        "badge": "🏆 Superlatif: fastest",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nFastest = paling cepat.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The cheetah is the ___ land mammal.\" (fast / fastest)",
        "expected": [
            "fastest",
            "the fastest"
        ],
        "primary_answer": "fastest"
    },
    {
        "id": "grm_int_40",
        "badge": "🏆 Superlatif Panjang: most beautiful",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nUntuk kata sifat panjang: the + <b>most</b> + adjective.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"This is the ___ beautiful garden in our town.\" (more / most)",
        "expected": [
            "most",
            "the most beautiful",
            "most beautiful"
        ],
        "primary_answer": "most"
    },
    {
        "id": "grm_int_41",
        "badge": "🏆 Superlatif Panjang: most expensive",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nThe most expensive = paling mahal.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"That luxury watch is the ___ expensive item in the shop.\" (more / most)",
        "expected": [
            "most",
            "the most expensive",
            "most expensive"
        ],
        "primary_answer": "most"
    },
    {
        "id": "grm_int_42",
        "badge": "⏳ Past Continuous: was reading",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nMenyatakan aksi yang sedang berlangsung di masa lampau: was + V-ing.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"At eight o'clock last night, Maya was ___ a novel.\" (read / reading)",
        "expected": [
            "reading",
            "was reading"
        ],
        "primary_answer": "reading"
    },
    {
        "id": "grm_int_43",
        "badge": "⏳ Past Continuous: were playing",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nSubjek jamak (They) di masa lampau menggunakan were + V-ing.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The boys were ___ soccer when it started to rain.\" (play / playing)",
        "expected": [
            "playing",
            "were playing"
        ],
        "primary_answer": "playing"
    },
    {
        "id": "grm_int_44",
        "badge": "🔗 Kata Hubung: while",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>while</b> untuk menghubungkan dua kejadian bersamaan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I fell asleep ___ mother was reading a story.\" (while / because)",
        "expected": [
            "while"
        ],
        "primary_answer": "while"
    },
    {
        "id": "grm_int_45",
        "badge": "🔗 Kata Hubung: although",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>although</b> (meskipun) untuk menyatakan kontras pertentangan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ it was raining heavily, the students still arrived on time.\" (Although / Because)",
        "expected": [
            "although"
        ],
        "primary_answer": "Although"
    },
    {
        "id": "grm_int_46",
        "badge": "🔗 Kata Hubung: so that",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>so that</b> (agar / supaya) untuk menyatakan tujuan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Eat healthy vegetables ___ you stay strong.\" (so that / but)",
        "expected": [
            "so that",
            "in order that"
        ],
        "primary_answer": "so that"
    },
    {
        "id": "grm_int_47",
        "badge": "🔮 Modal Peluang: might",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>might</b> (mungkin) untuk menyatakan kemungkinan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Take an umbrella with you, it ___ rain later.\" (might / must)",
        "expected": [
            "might"
        ],
        "primary_answer": "might"
    },
    {
        "id": "grm_int_48",
        "badge": "🙋 Modal Izin: May I",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>May I</b> untuk meminta izin secara sopan kepada guru/orang tua.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ I ask a question about this math problem, Teacher?\" (May / Must)",
        "expected": [
            "may",
            "may i"
        ],
        "primary_answer": "May"
    },
    {
        "id": "grm_int_49",
        "badge": "💪 Modal Kemampuan Lampau: could",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nBentuk lampau dari 'can' adalah <b>could</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"When he was six years old, he ___ already swim.\" (could / can)",
        "expected": [
            "could",
            "he could"
        ],
        "primary_answer": "could"
    },
    {
        "id": "grm_int_50",
        "badge": "⏱️ Frekuensi: always",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nAlways = selalu (100% dari waktu).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I ___ brush my teeth before going to sleep.\" (always / never)",
        "expected": [
            "always"
        ],
        "primary_answer": "always"
    },
    {
        "id": "grm_int_51",
        "badge": "⏱️ Frekuensi: never",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nNever = tidak pernah (0% dari waktu).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"An honest person ___ tells lies.\" (never / always)",
        "expected": [
            "never"
        ],
        "primary_answer": "never"
    },
    {
        "id": "grm_int_52",
        "badge": "⏱️ Frekuensi: usually",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nUsually = biasanya / pada umumnya.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We ___ have breakfast together at seven.\" (usually / rarely)",
        "expected": [
            "usually"
        ],
        "primary_answer": "usually"
    },
    {
        "id": "grm_int_53",
        "badge": "🏃 Keterangan Cara: quickly",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nQuick (adjective) ➔ <b>quickly</b> (adverb: dengan cepat).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The firefighter ran ___ toward the burning house.\" (quick / quickly)",
        "expected": [
            "quickly"
        ],
        "primary_answer": "quickly"
    },
    {
        "id": "grm_int_54",
        "badge": "🚗 Keterangan Cara: carefully",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nCareful ➔ <b>carefully</b> (dengan hati-hati).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Always cross the busy road ___.\" (careful / carefully)",
        "expected": [
            "carefully"
        ],
        "primary_answer": "carefully"
    },
    {
        "id": "grm_int_55",
        "badge": "🔔 Keterangan Cara: loudly",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nLoud ➔ <b>loudly</b> (dengan keras/nyaring).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The school bell rang ___ across the courtyard.\" (loud / loudly)",
        "expected": [
            "loudly"
        ],
        "primary_answer": "loudly"
    },
    {
        "id": "grm_int_56",
        "badge": "⚡ Keterangan Khusus: fast",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nKata keterangan untuk cepat tetap <b>fast</b> (bukan fastly).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He runs very ___ in the sprint competition.\" (fast / fastly)",
        "expected": [
            "fast"
        ],
        "primary_answer": "fast"
    },
    {
        "id": "grm_int_57",
        "badge": "🌟 Keterangan Khusus: well",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nKata keterangan untuk 'good' adalah <b>well</b> (dengan baik).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She plays the acoustic piano very ___.\" (good / well)",
        "expected": [
            "well"
        ],
        "primary_answer": "well"
    },
    {
        "id": "grm_int_58",
        "badge": "❓ Question Tag: isn't it",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nUntuk kalimat positif to be is, tag-nya adalah <b>isn't it?</b>\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Today is very hot, ___?\" (isn't it / is it)",
        "expected": [
            "isn't it",
            "isnt it"
        ],
        "primary_answer": "isn't it"
    },
    {
        "id": "grm_int_59",
        "badge": "❓ Question Tag: aren't they",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nUntuk kalimat positif are, tag-nya <b>aren't they?</b>\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"They are our new classmates, ___?\" (aren't they / are they)",
        "expected": [
            "aren't they",
            "arent they"
        ],
        "primary_answer": "aren't they"
    },
    {
        "id": "grm_int_60",
        "badge": "❓ Question Tag: don't you",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nUntuk kalimat present verb You, tag-nya <b>don't you?</b>\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"You speak English well, ___?\" (don't you / do you)",
        "expected": [
            "don't you",
            "dont you"
        ],
        "primary_answer": "don't you"
    },
    {
        "id": "grm_int_61",
        "badge": "🪞 Refleksif: myself",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>myself</b> untuk subjek 'I'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I painted this landscape canvas all by ___.\" (myself / himself)",
        "expected": [
            "myself"
        ],
        "primary_answer": "myself"
    },
    {
        "id": "grm_int_62",
        "badge": "🪞 Refleksif: himself",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>himself</b> untuk subjek 'He'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He looked at ___ in the large mirror.\" (himself / herself)",
        "expected": [
            "himself"
        ],
        "primary_answer": "himself"
    },
    {
        "id": "grm_int_63",
        "badge": "🪞 Refleksif: herself",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>herself</b> untuk subjek 'She'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Siti prepared lunch for ___ this morning.\" (herself / itself)",
        "expected": [
            "herself"
        ],
        "primary_answer": "herself"
    },
    {
        "id": "grm_int_64",
        "badge": "🔢 Hitung Banyak: many",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>many</b> untuk kata benda yang dapat dihitung (countable).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"There are ___ interesting books in the library.\" (many / much)",
        "expected": [
            "many"
        ],
        "primary_answer": "many"
    },
    {
        "id": "grm_int_65",
        "badge": "💧 Tak Terhitung: much",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>much</b> untuk kata benda yang tidak dapat dihitung (uncountable).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"How ___ water should we drink each day?\" (much / many)",
        "expected": [
            "much"
        ],
        "primary_answer": "much"
    },
    {
        "id": "grm_int_66",
        "badge": "🍎 Sedikit Terhitung: a few",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>a few</b> untuk sedikit benda yang dapat dihitung.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I have ___ sweet apples in my basket.\" (a few / a little)",
        "expected": [
            "a few",
            "few"
        ],
        "primary_answer": "a few"
    },
    {
        "id": "grm_int_67",
        "badge": "🍯 Sedikit Tak Terhitung: a little",
        "prompt": "⏳ <b>Grammar Menengah:</b>\n\nGunakan <b>a little</b> untuk sedikit benda cair/bubuk tak terhitung.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Please add ___ sugar to my hot coffee.\" (a few / a little)",
        "expected": [
            "a little",
            "little"
        ],
        "primary_answer": "a little"
    }
],
    config.LEVEL_ADVANCED: [
    {
        "id": "grm_adv_01",
        "badge": "🏆 Present Perfect: has lived",
        "prompt": "🏡 <b>Present Perfect Tense (have/has + V3)</b>\n\nMenyatakan kejadian masa lalu yang dampaknya terasa hingga kini.\n\n👉 <b>Pilih kata bantu yang benar (have / has):</b>\n\"She ___ lived in this town for five years.\"",
        "expected": [
            "has",
            "she has",
            "has lived"
        ],
        "primary_answer": "has"
    },
    {
        "id": "grm_adv_02",
        "badge": "🏆 Present Perfect: have visited",
        "prompt": "✈️ <b>Present Perfect: have + V3</b>\n\nSubjek I, You, We, They menggunakan <b>have</b>.\n\n👉 <b>Lengkapi kalimat pengalaman ini:</b>\n\"I ___ visited the National Museum three times.\"",
        "expected": [
            "have",
            "i have",
            "have visited"
        ],
        "primary_answer": "have"
    },
    {
        "id": "grm_adv_03",
        "badge": "🏆 Present Perfect: have finished",
        "prompt": "📝 <b>Present Perfect: have finished</b>\n\nFinish ➔ Finished (V3).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We ___ already finished our science project.\"",
        "expected": [
            "have",
            "we have",
            "have already finished"
        ],
        "primary_answer": "have"
    },
    {
        "id": "grm_adv_04",
        "badge": "🏆 Present Perfect: has eaten",
        "prompt": "🍽️ <b>Present Perfect: irregular V3 (eaten)</b>\n\nEat ➔ Ate (V2) ➔ Eaten (V3).\n\n👉 <b>Tulis bentuk V3 dari kata 'eat':</b>\n\"He has ___ breakfast already.\"",
        "expected": [
            "eaten",
            "has eaten"
        ],
        "primary_answer": "eaten"
    },
    {
        "id": "grm_adv_05",
        "badge": "🔄 Kalimat Pasif: is cleaned",
        "prompt": "🧹 <b>Passive Voice (Present: is/are + V3)</b>\n\nFokus pada objek yang menerima tindakan.\n\n👉 <b>Lengkapi bentuk pasif dari 'clean':</b>\n\"The classroom is ___ by students every afternoon.\"",
        "expected": [
            "cleaned",
            "is cleaned"
        ],
        "primary_answer": "cleaned"
    },
    {
        "id": "grm_adv_06",
        "badge": "🔄 Kalimat Pasif Jamak: are made",
        "prompt": "🍰 <b>Passive Voice: are made</b>\n\nObjek jamak (These cakes) menggunakan <b>are</b> + V3.\n\n👉 <b>Lengkapi dengan to be yang tepat (is / are):</b>\n\"These delicious cookies ___ made with organic honey.\"",
        "expected": [
            "are",
            "are made"
        ],
        "primary_answer": "are"
    },
    {
        "id": "grm_adv_07",
        "badge": "🔄 Kalimat Pasif Lampau: was written",
        "prompt": "📜 <b>Past Passive Voice: was/were + V3</b>\n\nWrite ➔ Wrote ➔ Written (V3).\n\n👉 <b>Tulis bentuk V3 dari 'write' dalam kalimat pasif ini:</b>\n\"The historic novel was ___ by a renowned author in 1945.\"",
        "expected": [
            "written",
            "was written"
        ],
        "primary_answer": "written"
    },
    {
        "id": "grm_adv_08",
        "badge": "🔄 Kalimat Pasif Lampau: was built",
        "prompt": "🌉 <b>Past Passive: was built</b>\n\nBuild ➔ Built (V3).\n\n👉 <b>Lengkapi kalimat pasif lampau ini:</b>\n\"The suspension bridge ___ built ten years ago.\" (was / were)",
        "expected": [
            "was",
            "was built"
        ],
        "primary_answer": "was"
    },
    {
        "id": "grm_adv_09",
        "badge": "🌧️ Pengandaian Tipe 1: First Conditional",
        "prompt": "☔ <b>First Conditional (If + Present, will + V1)</b>\n\nMenyatakan kemungkinan nyata di masa depan.\n\n👉 <b>Lengkapi klausa hasil dengan modal masa depan (will):</b>\n\"If it rains tomorrow, I ___ stay at home.\"",
        "expected": [
            "will",
            "will stay",
            "i will"
        ],
        "primary_answer": "will"
    },
    {
        "id": "grm_adv_10",
        "badge": "🎓 Pengandaian Tipe 1: If you study",
        "prompt": "📚 <b>First Conditional: Klausa Syarat</b>\n\nBagian setelah 'if' menggunakan Simple Present Tense.\n\n👉 <b>Pilih bentuk verb yang tepat (study / studied):</b>\n\"If you ___ diligently, you will pass the scholarship examination.\"",
        "expected": [
            "study",
            "if you study"
        ],
        "primary_answer": "study"
    },
    {
        "id": "grm_adv_11",
        "badge": "⏰ Pengandaian Tipe 1: will not miss",
        "prompt": "🚌 <b>First Conditional: Negasi</b>\n\nWill not = won't.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"If we leave early, we ___ not arrive late.\"",
        "expected": [
            "will",
            "will not",
            "won't",
            "wont"
        ],
        "primary_answer": "will"
    },
    {
        "id": "grm_adv_12",
        "badge": "💭 Pengandaian Tipe 2: would fly",
        "prompt": "🦅 <b>Second Conditional (If + Past, would + V1)</b>\n\nMenyatakan imajinasi/khayalan yang tidak nyata saat ini.\n\n👉 <b>Lengkapi klausa hasil dengan kata 'would':</b>\n\"If I had wings, I ___ travel across the continents.\"",
        "expected": [
            "would",
            "i would",
            "would travel"
        ],
        "primary_answer": "would"
    },
    {
        "id": "grm_adv_13",
        "badge": "💭 Pengandaian Tipe 2: If she were",
        "prompt": "🩺 <b>Second Conditional: To Be 'were'</b>\n\nDalam pengandaian formal tipe 2, semua subjek menggunakan <b>were</b>.\n\n👉 <b>Lengkapi dengan to be pengandaian:</b>\n\"If she ___ the president, she would build more free hospitals.\"",
        "expected": [
            "were",
            "was",
            "if she were"
        ],
        "primary_answer": "were"
    },
    {
        "id": "grm_adv_14",
        "badge": "👤 Relative Pronoun: who (orang)",
        "prompt": "👩‍🏫 <b>Relative Pronoun: who</b>\n\nGunakan <b>who</b> untuk merujuk pada subjek manusia.\n\n👉 <b>Lengkapi kalimat ini (who / which):</b>\n\"The young girl ___ won the English speech contest is my sister.\"",
        "expected": [
            "who",
            "who won"
        ],
        "primary_answer": "who"
    },
    {
        "id": "grm_adv_15",
        "badge": "📦 Relative Pronoun: which (benda)",
        "prompt": "💻 <b>Relative Pronoun: which / that</b>\n\nGunakan <b>which</b> atau <b>that</b> untuk merujuk pada benda/hewan.\n\n👉 <b>Lengkapi dengan 'which':</b>\n\"The laptop ___ broke down yesterday has been repaired.\"",
        "expected": [
            "which",
            "that"
        ],
        "primary_answer": "which"
    },
    {
        "id": "grm_adv_16",
        "badge": "🏷️ Relative Pronoun: whose (kepemilikan)",
        "prompt": "🎒 <b>Relative Pronoun: whose (milik siapa)</b>\n\nGunakan <b>whose</b> untuk menunjukkan kepemilikan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The student ___ project received first prize gave an inspiring speech.\"",
        "expected": [
            "whose",
            "whose project"
        ],
        "primary_answer": "whose"
    },
    {
        "id": "grm_adv_17",
        "badge": "❓ Question Tag Positif-Negatif: isn't he?",
        "prompt": "👨‍⚕️ <b>Question Tag: Kalimat Positif ➔ Tag Negatif</b>\n\nContoh: He is kind, <i>isn't he?</i>\n\n👉 <b>Lengkapi tag pertanyaan ini:</b>\n\"Mr. Hendra is a surgeon, ___ he?\"",
        "expected": [
            "isn't",
            "is not",
            "isnt",
            "isn't he",
            "isnt he?"
        ],
        "primary_answer": "isn't"
    },
    {
        "id": "grm_adv_18",
        "badge": "❓ Question Tag: aren't you?",
        "prompt": "😊 <b>Question Tag: You are</b>\n\nYou are ready, <i>aren't you?</i>\n\n👉 <b>Lengkapi question tag ini:</b>\n\"You are enjoying this learning journey, ___ you?\"",
        "expected": [
            "aren't",
            "are not",
            "arent",
            "aren't you",
            "arent you?"
        ],
        "primary_answer": "aren't"
    },
    {
        "id": "grm_adv_19",
        "badge": "❓ Question Tag Lampau: didn't they?",
        "prompt": "🚌 <b>Question Tag: Simple Past</b>\n\nKalimat past tense menggunakan kata bantu 'did'. Tag negatifnya: <b>didn't</b>.\n\n👉 <b>Lengkapi question tag ini:</b>\n\"They arrived on time, ___ they?\"",
        "expected": [
            "didn't",
            "did not",
            "didnt",
            "didn't they",
            "didnt they?"
        ],
        "primary_answer": "didn't"
    },
    {
        "id": "grm_adv_20",
        "badge": "🌅 Kebiasaan Masa Lalu: used to",
        "prompt": "🚴 <b>Habitual Past: used to (dulu terbiasa)</b>\n\nMenyatakan kebiasaan masa lalu yang sudah tidak dilakukan lagi sekarang.\n\n👉 <b>Lengkapi kalimat kebiasaan ini:</b>\n\"I ___ to ride my bicycle to school every morning.\"",
        "expected": [
            "used",
            "used to"
        ],
        "primary_answer": "used"
    },
    {
        "id": "grm_adv_21",
        "badge": "🌅 Kebiasaan Tinggal: used to live",
        "prompt": "🏙️ <b>Used to + Verb dasar</b>\n\nDiikuti kata kerja bentuk pertama.\n\n👉 <b>Lengkapi kata kerja dasar 'live':</b>\n\"She used to ___ in Surabaya before moving to Jakarta.\"",
        "expected": [
            "live",
            "used to live"
        ],
        "primary_answer": "live"
    },
    {
        "id": "grm_adv_22",
        "badge": "🎨 Gerund: enjoy + V-ing",
        "prompt": "📖 <b>Gerund setelah kata kerja tertentu (enjoy)</b>\n\nKata 'enjoy' harus diikuti kata kerja bentuk <b>-ing</b>.\n\n👉 <b>Ubah kata kerja 'read' menjadi gerund:</b>\n\"I truly enjoy ___ mystery novels on rainy weekends.\"",
        "expected": [
            "reading",
            "enjoy reading"
        ],
        "primary_answer": "reading"
    },
    {
        "id": "grm_adv_23",
        "badge": "🎯 Infinitive: decided to",
        "prompt": "🎓 <b>Infinitive setelah kata kerja (decide)</b>\n\nKata 'decide' diikuti <b>to + V1</b>.\n\n👉 <b>Lengkapi dengan 'to':</b>\n\"She decided ___ enroll in an advanced public speaking workshop.\"",
        "expected": [
            "to",
            "decided to"
        ],
        "primary_answer": "to"
    },
    {
        "id": "grm_adv_24",
        "badge": "🛡️ Gerund Larangan: avoid + V-ing",
        "prompt": "🥗 <b>Gerund: avoid + V-ing</b>\n\nKata 'avoid' (menghindari) diikuti gerund (-ing).\n\n👉 <b>Ubah kata 'eat' ke bentuk gerund:</b>\n\"Athletes strictly avoid ___ excessive processed sugars before a match.\"",
        "expected": [
            "eating",
            "avoid eating"
        ],
        "primary_answer": "eating"
    },
    {
        "id": "grm_adv_25",
        "badge": "🏆 Past Perfect: had left",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPast Perfect (had + V3) menyatakan kejadian yang sudah selesai sebelum kejadian lampau lainnya.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"When we arrived at the platform, the morning train ___ already left.\" (had / has)",
        "expected": [
            "had",
            "had left"
        ],
        "primary_answer": "had"
    },
    {
        "id": "grm_adv_26",
        "badge": "🏆 Past Perfect: had finished",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nFinish ➔ Finished (V3) dengan had untuk waktu lampau terdahulu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"By the time the bell rang, the students ___ finished their examination.\" (had / have)",
        "expected": [
            "had",
            "had finished"
        ],
        "primary_answer": "had"
    },
    {
        "id": "grm_adv_27",
        "badge": "⏳ Present Perfect Continuous: has been studying",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nTelah dan masih terus berlangsung: has/have + been + V-ing.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He has been ___ English for three consecutive hours.\" (study / studying)",
        "expected": [
            "studying",
            "been studying"
        ],
        "primary_answer": "studying"
    },
    {
        "id": "grm_adv_28",
        "badge": "⏳ Present Perfect Continuous: have been living",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nSubjek 'We' menggunakan have been + V-ing.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We ___ been living in this peaceful village since 2015.\" (have / has)",
        "expected": [
            "have",
            "have been"
        ],
        "primary_answer": "have"
    },
    {
        "id": "grm_adv_29",
        "badge": "🔄 Pasif Sedang Terjadi: is being repaired",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPassive Continuous: is/are + being + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The old wooden bridge is currently ___ repaired by local workers.\" (being / been)",
        "expected": [
            "being",
            "is being"
        ],
        "primary_answer": "being"
    },
    {
        "id": "grm_adv_30",
        "badge": "🔄 Pasif Masa Depan: will be held",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nFuture Passive: will be + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The international conference will ___ held in Jakarta next month.\" (be / been)",
        "expected": [
            "be",
            "will be"
        ],
        "primary_answer": "be"
    },
    {
        "id": "grm_adv_31",
        "badge": "🔄 Pasif Modal: must be protected",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nModal Passive: must be + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Endangered animals must ___ protected from illegal poaching.\" (be / being)",
        "expected": [
            "be",
            "must be"
        ],
        "primary_answer": "be"
    },
    {
        "id": "grm_adv_32",
        "badge": "🔄 Pasif Present Perfect: has been discovered",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPresent Perfect Passive: has/have + been + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"A new medicinal orchid species has ___ discovered in Borneo.\" (been / being)",
        "expected": [
            "been",
            "has been"
        ],
        "primary_answer": "been"
    },
    {
        "id": "grm_adv_33",
        "badge": "🌧️ Pengandaian Tipe 3: had known",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nThird Conditional (penyesalan masa lampau): If + had + V3, would have + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"If I ___ known the schedule earlier, I would have joined the field trip.\" (had / have)",
        "expected": [
            "had",
            "had known"
        ],
        "primary_answer": "had"
    },
    {
        "id": "grm_adv_34",
        "badge": "🌧️ Pengandaian Tipe 3: would have passed",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nThird Conditional klausa hasil: would have + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"If she had studied diligently, she ___ have passed the scholarship exam.\" (would / will)",
        "expected": [
            "would",
            "would have"
        ],
        "primary_answer": "would"
    },
    {
        "id": "grm_adv_35",
        "badge": "🌧️ Pengandaian Tipe 3 Negatif: had not rained",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nBentuk penolakan syarat lampau: had not + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"If it had ___ rained yesterday, we would have hiked to the summit.\" (not / no)",
        "expected": [
            "not",
            "had not"
        ],
        "primary_answer": "not"
    },
    {
        "id": "grm_adv_36",
        "badge": "👤 Relative Pronoun: whose (kepemilikan)",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGunakan <b>whose</b> untuk menggantikan kepunyaan seseorang.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The talented boy ___ painting won first prize is my neighbor.\" (whose / who)",
        "expected": [
            "whose"
        ],
        "primary_answer": "whose"
    },
    {
        "id": "grm_adv_37",
        "badge": "👤 Relative Pronoun: whom (objek manusia)",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGunakan <b>whom</b> bila merujuk pada objek manusia formal.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The distinguished professor ___ we met at the symposium gave an inspiring lecture.\" (whom / which)",
        "expected": [
            "whom"
        ],
        "primary_answer": "whom"
    },
    {
        "id": "grm_adv_38",
        "badge": "👤 Relative Pronoun: which (benda/konsep)",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGunakan <b>which</b> untuk merujuk pada hewan atau benda non-manusia.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The solar panel system ___ was installed on our roof generates clean electricity.\" (which / who)",
        "expected": [
            "which"
        ],
        "primary_answer": "which"
    },
    {
        "id": "grm_adv_39",
        "badge": "📍 Relative Adverb: where (tempat)",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGunakan <b>where</b> untuk menghubungkan keterangan tempat.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"This is the serene lakeside village ___ my grandparents grew up.\" (where / when)",
        "expected": [
            "where"
        ],
        "primary_answer": "where"
    },
    {
        "id": "grm_adv_40",
        "badge": "⏰ Relative Adverb: when (waktu)",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGunakan <b>when</b> untuk menghubungkan keterangan waktu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I vividly remember the historic day ___ our team won the championship.\" (when / where)",
        "expected": [
            "when"
        ],
        "primary_answer": "when"
    },
    {
        "id": "grm_adv_41",
        "badge": "🗣️ Kalimat Tidak Langsung: was",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nDirect: \"I am happy.\" ➔ Indirect: He said that he ___ happy.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He explained that he ___ delighted with the test results.\" (was / is)",
        "expected": [
            "was"
        ],
        "primary_answer": "was"
    },
    {
        "id": "grm_adv_42",
        "badge": "🗣️ Kalimat Tidak Langsung: had finished",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nDirect: \"I finished my task.\" ➔ Indirect: She told me she ___ finished her task.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She mentioned that she ___ already completed the research proposal.\" (had / has)",
        "expected": [
            "had",
            "had completed"
        ],
        "primary_answer": "had"
    },
    {
        "id": "grm_adv_43",
        "badge": "🗣️ Pertanyaan Tidak Langsung: if / whether",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGunakan <b>if</b> atau <b>whether</b> untuk pertanyaan Yes/No tidak langsung.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The teacher asked ___ we had understood the mathematical theorem.\" (if / that)",
        "expected": [
            "if",
            "whether"
        ],
        "primary_answer": "if"
    },
    {
        "id": "grm_adv_44",
        "badge": "🏊 Gerund Sebagai Subjek: Swimming",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nKata kerja berakhiran -ing yang bertindak sebagai kata benda subjek.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ in the open ocean is both exhilarating and challenging.\" (Swimming / To swim)",
        "expected": [
            "swimming"
        ],
        "primary_answer": "Swimming"
    },
    {
        "id": "grm_adv_45",
        "badge": "🎨 Gerund Setelah Preposisi: learning",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nSetelah preposisi (in, at, of, for, about), kata kerja harus berupa gerund (-ing).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"She is genuinely interested in ___ foreign languages.\" (learn / learning)",
        "expected": [
            "learning",
            "in learning"
        ],
        "primary_answer": "learning"
    },
    {
        "id": "grm_adv_46",
        "badge": "📖 Kata Kerja Diikuti Gerund: reading",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nKata kerja seperti 'enjoy' wajib diikuti gerund (V-ing).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"They thoroughly enjoy ___ historical fables together.\" (reading / to read)",
        "expected": [
            "reading"
        ],
        "primary_answer": "reading"
    },
    {
        "id": "grm_adv_47",
        "badge": "🎯 Kata Kerja Diikuti Infinitive: to visit",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nKata kerja seperti 'decide' diikuti to-infinitive (to + V1).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We decided ___ the ancient temple next Saturday.\" (to visit / visiting)",
        "expected": [
            "to visit"
        ],
        "primary_answer": "to visit"
    },
    {
        "id": "grm_adv_48",
        "badge": "🤝 Kata Kerja Diikuti Infinitive: to help",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nKata kerja 'promise' diikuti to-infinitive.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"He promised ___ me with my science presentation.\" (to help / helping)",
        "expected": [
            "to help"
        ],
        "primary_answer": "to help"
    },
    {
        "id": "grm_adv_49",
        "badge": "🔄 Inversi Kalimat Negatif: have I",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nJika kalimat diawali adverb negatif (Seldom/Rarely), susunan to be / aux dibalik.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Seldom ___ I witnessed such breathtaking natural beauty.\" (have / I have)",
        "expected": [
            "have",
            "have i"
        ],
        "primary_answer": "have"
    },
    {
        "id": "grm_adv_50",
        "badge": "🔄 Inversi Kalimat Negatif: had she",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nNever + had + subjek + V3.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Never ___ she imagined that she would become an astronomer.\" (had / did)",
        "expected": [
            "had",
            "had she"
        ],
        "primary_answer": "had"
    },
    {
        "id": "grm_adv_51",
        "badge": "📜 Subjunctive Mood: be",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nSetelah kata 'recommend/insist that', gunakan kata kerja bentuk dasar 'be'.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The principal recommended that every student ___ punctual tomorrow.\" (be / is)",
        "expected": [
            "be"
        ],
        "primary_answer": "be"
    },
    {
        "id": "grm_adv_52",
        "badge": "📜 Subjunctive Mood: submit",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nSubjunctive: suggest that he + V dasar tanpa -s.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The advisor suggested that the researcher ___ the report immediately.\" (submit / submits)",
        "expected": [
            "submit"
        ],
        "primary_answer": "submit"
    },
    {
        "id": "grm_adv_53",
        "badge": "🔧 Kausatif: repaired",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nHave something done (have + objek + V3) = menyuruh orang lain memperbaiki.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I went to the garage to have my motorcycle ___.\" (repaired / repair)",
        "expected": [
            "repaired"
        ],
        "primary_answer": "repaired"
    },
    {
        "id": "grm_adv_54",
        "badge": "🔧 Kausatif: clean",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nMake someone do something (make + orang + V1 dasar).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"The coach made the athletes ___ up the sports hall.\" (clean / cleaned)",
        "expected": [
            "clean"
        ],
        "primary_answer": "clean"
    },
    {
        "id": "grm_adv_55",
        "badge": "🤝 Phrasal Verb: forward to meeting",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nFrasa 'look forward to' wajib diikuti gerund (-ing).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"We look forward to ___ you at the conference.\" (meeting / meet)",
        "expected": [
            "meeting",
            "meeting you"
        ],
        "primary_answer": "meeting"
    },
    {
        "id": "grm_adv_56",
        "badge": "🚫 Phrasal Verb: give up",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nGive up = menyerah / menghentikan kebiasaan.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Never ___ up on your lifelong dreams despite difficulties.\" (give / take)",
        "expected": [
            "give",
            "give up"
        ],
        "primary_answer": "give"
    },
    {
        "id": "grm_adv_57",
        "badge": "🧩 Phrasal Verb: figure out",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nFigure out = memecahkan atau memahami masalah rumit.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"It took scientists years to ___ out the genetic structure.\" (figure / look)",
        "expected": [
            "figure",
            "figure out"
        ],
        "primary_answer": "figure"
    },
    {
        "id": "grm_adv_58",
        "badge": "⚖️ Penyangkal Ganda: Neither ... nor",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPasangan <b>Neither</b> adalah <b>nor</b> (tidak ... dan juga tidak ...).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ the teacher nor the students were late for the lecture.\" (Neither / Either)",
        "expected": [
            "neither"
        ],
        "primary_answer": "Neither"
    },
    {
        "id": "grm_adv_59",
        "badge": "⚖️ Pilihan Ganda: Either ... or",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPasangan <b>Either</b> adalah <b>or</b> (salah satu dari).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"You can choose ___ the blue backpack or the green one.\" (either / neither)",
        "expected": [
            "either"
        ],
        "primary_answer": "either"
    },
    {
        "id": "grm_adv_60",
        "badge": "🌟 Bukan Hanya Tapi Juga: Not only",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPasangan <b>Not only ... but also</b>.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ only is he exceptionally kind, but he is also hardworking.\" (Not / No)",
        "expected": [
            "not",
            "not only"
        ],
        "primary_answer": "Not"
    },
    {
        "id": "grm_adv_61",
        "badge": "🕰️ Kebiasaan Masa Lalu: used to",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nUsed to + V1 = kebiasaan masa lalu yang sekarang sudah tidak lagi.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"Grandfather ___ to walk ten miles to school every morning.\" (used / was)",
        "expected": [
            "used",
            "used to"
        ],
        "primary_answer": "used"
    },
    {
        "id": "grm_adv_62",
        "badge": "🌅 Terbiasa Saat Ini: is used to waking",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nBe used to + V-ing = sudah terbiasa dengan kondisi tertentu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"A farmer is used to ___ up before dawn.\" (waking / wake)",
        "expected": [
            "waking"
        ],
        "primary_answer": "waking"
    },
    {
        "id": "grm_adv_63",
        "badge": "🚶 Participle Clause Aktif: Walking",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nKlausa partisipel aksi aktif: V-ing di awal kalimat.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ along the riverbank, the botanist discovered a rare flower.\" (Walking / Walked)",
        "expected": [
            "walking"
        ],
        "primary_answer": "Walking"
    },
    {
        "id": "grm_adv_64",
        "badge": "📜 Participle Clause Lampau: Having finished",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nSetelah menyelesaikan (Having + V3).\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"___ completed the experiment, the scientist documented the observations.\" (Having / Have)",
        "expected": [
            "having",
            "having completed"
        ],
        "primary_answer": "Having"
    },
    {
        "id": "grm_adv_65",
        "badge": "🔀 Mixed Conditional: would be",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nPengandaian syarat masa lalu berdampak pada kondisi saat ini.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"If I had accepted that scholarship, I ___ be studying abroad right now.\" (would / will)",
        "expected": [
            "would",
            "would be"
        ],
        "primary_answer": "would"
    },
    {
        "id": "grm_adv_66",
        "badge": "💭 Ungkapan Penyesalan: I wish I had studied",
        "prompt": "🏆 <b>Grammar Tingkat Lanjut:</b>\n\nWish + Past Perfect untuk menyatakan penyesalan masa lalu.\n\n👉 <b>Lengkapi kalimat ini:</b>\n\"I wish I ___ studied harder for yesterday's final test.\" (had / have)",
        "expected": [
            "had",
            "had studied"
        ],
        "primary_answer": "had"
    }
],
}
