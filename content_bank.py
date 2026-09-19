"""
Curated Offline Exercise Bank & Random Generator for English Buddy Bot.

Specially designed for Indonesian children and students from rural areas
who are starting English from ground zero.

Features:
- Exactly 108 bite-sized, ultra-accessible exercises (6 tracks x 3 levels x 6 exercises).
- Grammar: to be (am/is/are), verbs, adjectives, part of speech.
- Vocabs: body parts (anggota tubuh), daily activities (kegiatan sehari-hari).
- Reading: descriptive text, narrative text (fables), recount text (pengalaman lampau).
- English Challenge (dimudahkan): easy unscramble ('I am a girl') & 'to be' fill-in-the-blank quizzes.
- Sub-millisecond O(1) in-memory retrieval.
- Consecutive duplicate suppression with exclude_id tracking.
- Contextual, encouraging Indonesian offline feedback.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

import config

EXERCISE_BANK: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    # =========================================================================
    # 1. 💬 DAILY CONVERSATION (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # Sapaan & percakapan sehari-hari yang mudah untuk anak sekolah di Indonesia
    # =========================================================================
    config.MODE_DAILY_CONVERSATION: {
        config.LEVEL_BEGINNER: [
            {
                "id": "conv_beg_01",
                "badge": "💬 Sapaan Pagi (Morning Greeting)",
                "prompt": (
                    "<b>☀️ Situasi:</b> Kamu bertemu teman di depan gerbang sekolah pada pagi hari.\n\n"
                    "<b>Teman:</b> <i>\"Good morning! How are you today?\"</i>\n"
                    "<i>(Selamat pagi! Apa kabarmu hari ini?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Balas dengan mengetik:\n"
                    "<code>Good morning! I am fine, thank you.</code>\n"
                    "<i>(Artinya: Selamat pagi! Saya baik-baik saja, terima kasih.)</i>"
                ),
            },
            {
                "id": "conv_beg_02",
                "badge": "💬 Berkenalan Nama (Introducing Yourself)",
                "prompt": (
                    "<b>👋 Situasi:</b> Ada murid baru di kelasmu yang ingin berkenalan.\n\n"
                    "<b>Murid Baru:</b> <i>\"Hello! My name is Budi. What is your name?\"</i>\n"
                    "<i>(Halo! Nama saya Budi. Siapa namamu?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik namamu dalam bahasa Inggris:\n"
                    "<code>My name is [namamu]</code>\n"
                    "<i>(Contoh: My name is Siti)</i>"
                ),
            },
            {
                "id": "conv_beg_03",
                "badge": "💬 Menanyakan Umur (Asking Age)",
                "prompt": (
                    "<b>🎂 Situasi:</b> Temanmu bertanya berapa umurmu sekarang.\n\n"
                    "<b>Teman:</b> <i>\"How old are you?\"</i>\n"
                    "<i>(Berapa usiamu?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Jawab dengan angka umurmu:\n"
                    "<code>I am 10 years old.</code>\n"
                    "<i>(Ganti angka 10 sesuai umurmu ya!)</i>"
                ),
            },
            {
                "id": "conv_beg_04",
                "badge": "💬 Meminjam Pensil (Borrowing a Pencil)",
                "prompt": (
                    "<b>✏️ Situasi:</b> Pensilmu tertinggal di rumah, kamu ingin meminjam pensil teman.\n\n"
                    "<b>Kamu:</b> <i>\"Can I borrow your pencil, please?\"</i>\n"
                    "<i>(Bolehkah saya meminjam pensilmu?)</i>\n\n"
                    "<b>Teman:</b> <i>\"Sure! Here you are.\"</i> <i>(Tentu! Ini dia.)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan terima kasih dengan mengetik:\n"
                    "<code>Thank you very much!</code>"
                ),
            },
            {
                "id": "conv_beg_05",
                "badge": "💬 Sama-sama (You're Welcome)",
                "prompt": (
                    "<b>🤝 Situasi:</b> Kamu membantu teman mengambilkan buku yang jatuh.\n\n"
                    "<b>Teman:</b> <i>\"Thank you for helping me!\"</i>\n"
                    "<i>(Terima kasih sudah membantuku!)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Jawab 'sama-sama' dengan mengetik:\n"
                    "<code>You are welcome!</code>"
                ),
            },
            {
                "id": "conv_beg_06",
                "badge": "💬 Berpamitan (Saying Goodbye)",
                "prompt": (
                    "<b>🔔 Situasi:</b> Bel pulang sekolah berbunyi, kamu berpamitan pada teman.\n\n"
                    "<b>Teman:</b> <i>\"Goodbye! See you tomorrow!\"</i>\n"
                    "<i>(Selamat tinggal! Sampai jumpa besok!)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Balas ucapan perpisahan dengan mengetik:\n"
                    "<code>Goodbye! See you!</code>"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "conv_int_01",
                "badge": "💬 Warna Kesukaan (Favorite Color)",
                "prompt": (
                    "<b>🎨 Situasi:</b> Kamu dan teman sedang mewarnai gambar di kelas.\n\n"
                    "<b>Teman:</b> <i>\"What is your favorite color?\"</i>\n"
                    "<i>(Apa warna kesukaanmu?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Jawab warna kesukaanmu (blue/red/green/yellow):\n"
                    "<code>My favorite color is blue.</code>"
                ),
            },
            {
                "id": "conv_int_02",
                "badge": "💬 Makanan Kesukaan (Favorite Food)",
                "prompt": (
                    "<b>🍛 Situasi:</b> Waktu istirahat makan siang di sekolah.\n\n"
                    "<b>Teman:</b> <i>\"What do you like to eat?\"</i>\n"
                    "<i>(Kamu suka makan apa?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Beritahu makanan kesukaanmu:\n"
                    "<code>I like fried rice.</code> <i>(Saya suka nasi goreng)</i>\n"
                    "<i>Atau: I like noodles / chicken.</i>"
                ),
            },
            {
                "id": "conv_int_03",
                "badge": "💬 Hobi Bermain (Hobbies)",
                "prompt": (
                    "<b>⚽ Situasi:</b> Mengobrol tentang kegemaran di sore hari.\n\n"
                    "<b>Teman:</b> <i>\"What is your hobby?\"</i>\n"
                    "<i>(Apa hobimu?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Pilih salah satu hobi dan ketik:\n"
                    "<code>My hobby is playing football.</code> <i>(Sepak bola)</i>\n"
                    "<i>Atau: My hobby is reading books / drawing.</i>"
                ),
            },
            {
                "id": "conv_int_04",
                "badge": "💬 Saudara di Rumah (Family)",
                "prompt": (
                    "<b>👨‍👩‍👧 Situasi:</b> Bercerita tentang keluarga.\n\n"
                    "<b>Teman:</b> <i>\"Do you have a brother or sister?\"</i>\n"
                    "<i>(Apakah kamu punya saudara laki-laki atau perempuan?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Jawab dengan mudah:\n"
                    "<code>I have one brother.</code> <i>(1 saudara laki-laki)</i>\n"
                    "<i>Atau: I have one sister.</i>"
                ),
            },
            {
                "id": "conv_int_05",
                "badge": "💬 Beli Jajan di Kantin (Canteen)",
                "prompt": (
                    "<b>🍞 Situasi:</b> Kamu membeli roti di kantin sekolah.\n\n"
                    "<b>Ibu Kantin:</b> <i>\"Hello! What do you want to buy?\"</i>\n"
                    "<i>(Halo! Kamu mau beli apa?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Pesan satu roti dengan sopan:\n"
                    "<code>One bread, please. Thank you!</code>"
                ),
            },
            {
                "id": "conv_int_06",
                "badge": "💬 Pulang Bersama (Walking Home)",
                "prompt": (
                    "<b>🚶 Situasi:</b> Mengajak teman pulang jalan kaki bersama.\n\n"
                    "<b>Kamu:</b> <i>\"Let's walk home together!\"</i>\n"
                    "<i>(Ayo kita jalan pulang bersama!)</i>\n\n"
                    "<b>Teman:</b> <i>\"Okay, let's go!\"</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat ajakan di atas untuk latihan:\n"
                    "<code>Let's go home together!</code>"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "conv_adv_01",
                "badge": "💬 Hewan Peliharaan (Pets)",
                "prompt": (
                    "<b>🐱 Situasi:</b> Temanmu bertanya tentang hewan di rumahmu.\n\n"
                    "<b>Teman:</b> <i>\"Do you have a pet at home?\"</i>\n"
                    "<i>(Apakah kamu punya hewan peliharaan di rumah?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ceritakan hewanmu:\n"
                    "<code>Yes, I have a cute cat. His name is Milo.</code>\n"
                    "<i>(Atau: I have a cute bird / rabbit.)</i>"
                ),
            },
            {
                "id": "conv_adv_02",
                "badge": "💬 Kegiatan Hari Minggu (Sunday Routine)",
                "prompt": (
                    "<b>🌱 Situasi:</b> Menceritakan kegiatan di hari libur.\n\n"
                    "<b>Teman:</b> <i>\"What do you do on Sunday?\"</i>\n"
                    "<i>(Apa yang kamu lakukan di hari Minggu?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Jawab kegiatan membantumu di rumah:\n"
                    "<code>I help my parents in the garden.</code>\n"
                    "<i>(Saya membantu orang tua di kebun.)</i>"
                ),
            },
            {
                "id": "conv_adv_03",
                "badge": "💬 Belajar PR Bersama (Study Together)",
                "prompt": (
                    "<b>📚 Situasi:</b> Kamu mengajak teman belajar PR bahasa Inggris bersama.\n\n"
                    "<b>Teman:</b> <i>\"This English homework is a bit difficult.\"</i>\n"
                    "<i>(PR bahasa Inggris ini agak sulit.)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ajak teman belajar bareng:\n"
                    "<code>Don't worry, let's study together!</code>"
                ),
            },
            {
                "id": "conv_adv_04",
                "badge": "💬 Cuaca Hari Ini (The Weather)",
                "prompt": (
                    "<b>🌧️ Situasi:</b> Hujan mulai turun saat pulang sekolah.\n\n"
                    "<b>Teman:</b> <i>\"Oh, look! It is raining outside.\"</i>\n"
                    "<i>(Oh, lihat! Di luar sedang hujan.)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ingatkan tentang payung:\n"
                    "<code>Yes, bring your umbrella!</code> <i>(Bawa payungmu!)</i>"
                ),
            },
            {
                "id": "conv_adv_05",
                "badge": "💬 Bertamu ke Rumah Teman (Visiting a Friend)",
                "prompt": (
                    "<b>🏡 Situasi:</b> Kamu berkunjung ke rumah temanmu di desa.\n\n"
                    "<b>Teman:</b> <i>\"Welcome to my house! Please come in.\"</i>\n"
                    "<i>(Selamat datang di rumahku! Silakan masuk.)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Puji rumahnya dengan sopan:\n"
                    "<code>Thank you! Your house is very clean.</code>"
                ),
            },
            {
                "id": "conv_adv_06",
                "badge": "💬 Cita-citaku (My Dream)",
                "prompt": (
                    "<b>⭐ Situasi:</b> Guru bertanya cita-citamu saat besar nanti.\n\n"
                    "<b>Guru:</b> <i>\"What do you want to be when you grow up?\"</i>\n"
                    "<i>(Kamu ingin jadi apa saat sudah besar nanti?)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Sebutkan cita-citamu (teacher/doctor/policeman/farmer):\n"
                    "<code>I want to be a teacher.</code> <i>(Guru)</i>\n"
                    "<i>Atau: I want to be a doctor. (Dokter)</i>"
                ),
            },
        ],
    },

    # =========================================================================
    # 2. 📚 VOCABULARY (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # Sesuai revisi: Body Parts & Daily Activity
    # =========================================================================
    config.MODE_VOCABULARY: {
        config.LEVEL_BEGINNER: [
            {
                "id": "voc_beg_01",
                "badge": "📚 Body Parts: Kepala & Rambut",
                "prompt": (
                    "🌟 <b>Anggota Tubuh (Body Parts):</b>\n\n"
                    "• <b>Head</b> <i>[hed]</i> = Kepala\n"
                    "• <b>Hair</b> <i>[her]</i> = Rambut\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I have black hair.\"</i> (Saya punya rambut hitam)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Kepala'</b>!"
                ),
            },
            {
                "id": "voc_beg_02",
                "badge": "📚 Body Parts: Mata & Hidung",
                "prompt": (
                    "🌟 <b>Anggota Tubuh (Body Parts):</b>\n\n"
                    "• <b>Eyes</b> <i>[ais]</i> = Mata (dua mata)\n"
                    "• <b>Nose</b> <i>[nous]</i> = Hidung\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I see with my eyes.\"</i> (Saya melihat dengan mata)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Mata'</b>!"
                ),
            },
            {
                "id": "voc_beg_03",
                "badge": "📚 Body Parts: Mulut & Gigi",
                "prompt": (
                    "🌟 <b>Anggota Tubuh (Body Parts):</b>\n\n"
                    "• <b>Mouth</b> <i>[maut]</i> = Mulut\n"
                    "• <b>Teeth</b> <i>[tiit]</i> = Gigi\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I brush my teeth.\"</i> (Saya menggosok gigi)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Gigi'</b>!"
                ),
            },
            {
                "id": "voc_beg_04",
                "badge": "📚 Body Parts: Telinga & Leher",
                "prompt": (
                    "🌟 <b>Anggota Tubuh (Body Parts):</b>\n\n"
                    "• <b>Ears</b> <i>[irs]</i> = Telinga\n"
                    "• <b>Neck</b> <i>[nek]</i> = Leher\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I hear sounds with my ears.\"</i> (Saya mendengar dengan telinga)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Telinga'</b>!"
                ),
            },
            {
                "id": "voc_beg_05",
                "badge": "📚 Body Parts: Tangan & Jari",
                "prompt": (
                    "🌟 <b>Anggota Tubuh (Body Parts):</b>\n\n"
                    "• <b>Hands</b> <i>[hends]</i> = Tangan\n"
                    "• <b>Fingers</b> <i>[fing-gers]</i> = Jari tangan\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I wash my hands with soap.\"</i> (Saya mencuci tangan dengan sabun)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Tangan'</b>!"
                ),
            },
            {
                "id": "voc_beg_06",
                "badge": "📚 Body Parts: Kaki & Lutut",
                "prompt": (
                    "🌟 <b>Anggota Tubuh (Body Parts):</b>\n\n"
                    "• <b>Legs</b> <i>[legs]</i> = Kaki (tungkai kaki)\n"
                    "• <b>Foot</b> <i>[fut]</i> = Telapak kaki\n"
                    "• <b>Knees</b> <i>[niis]</i> = Lutut\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I kick the ball with my foot.\"</i> (Saya menendang bola dengan kaki)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Kaki'</b>!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "voc_int_01",
                "badge": "📚 Daily Activity: Bangun Pagi",
                "prompt": (
                    "🌟 <b>Kegiatan Sehari-hari (Daily Activity):</b>\n\n"
                    "• <b>Wake up</b> = Bangun tidur\n"
                    "• <b>Wash face</b> = Cuci muka\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I wake up at five in the morning.\"</i> (Saya bangun jam 5 pagi)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik bahasa Inggris untuk <b>'Bangun tidur'</b>!"
                ),
            },
            {
                "id": "voc_int_02",
                "badge": "📚 Daily Activity: Mandi & Sarapan",
                "prompt": (
                    "🌟 <b>Kegiatan Sehari-hari (Daily Activity):</b>\n\n"
                    "• <b>Take a bath</b> = Mandi\n"
                    "• <b>Eat breakfast</b> = Sarapan (makan pagi)\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I eat breakfast with my family.\"</i> (Saya sarapan bersama keluarga)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik bahasa Inggris untuk <b>'Sarapan'</b>!"
                ),
            },
            {
                "id": "voc_int_03",
                "badge": "📚 Daily Activity: Pergi ke Sekolah",
                "prompt": (
                    "🌟 <b>Kegiatan Sehari-hari (Daily Activity):</b>\n\n"
                    "• <b>Go to school</b> = Pergi ke sekolah\n"
                    "• <b>Study English</b> = Belajar bahasa Inggris\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"We go to school on foot.\"</i> (Kami pergi ke sekolah jalan kaki)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik bahasa Inggris untuk <b>'Pergi ke sekolah'</b>!"
                ),
            },
            {
                "id": "voc_int_04",
                "badge": "📚 Daily Activity: Bermain Sore",
                "prompt": (
                    "🌟 <b>Kegiatan Sehari-hari (Daily Activity):</b>\n\n"
                    "• <b>Play football</b> = Bermain sepak bola\n"
                    "• <b>Ride a bicycle</b> = Naik sepeda\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"In the afternoon, I play football.\"</i> (Di sore hari, saya main bola)\n\n"
                    "👉 <b>Giliranmu:</b> Tulis kegiatan yang kamu suka lakukan di sore hari!"
                ),
            },
            {
                "id": "voc_int_05",
                "badge": "📚 Daily Activity: Mengerjakan PR",
                "prompt": (
                    "🌟 <b>Kegiatan Sehari-hari (Daily Activity):</b>\n\n"
                    "• <b>Do homework</b> = Mengerjakan PR\n"
                    "• <b>Read a book</b> = Membaca buku\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I do my homework at seven o'clock.\"</i> (Saya mengerjakan PR jam 7)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik bahasa Inggris untuk <b>'Membaca buku'</b>!"
                ),
            },
            {
                "id": "voc_int_06",
                "badge": "📚 Daily Activity: Tidur Malam",
                "prompt": (
                    "🌟 <b>Kegiatan Sehari-hari (Daily Activity):</b>\n\n"
                    "• <b>Go to sleep</b> = Pergi tidur\n"
                    "• <b>Good night</b> = Selamat malam / selamat tidur\n\n"
                    "<b>Contoh Kalimat:</b> <i>\"I go to sleep at nine o'clock.\"</i> (Saya tidur jam 9 malam)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik bahasa Inggris untuk <b>'Selamat malam'</b>!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "voc_adv_01",
                "badge": "📚 Kalimat: Mencuci Tangan",
                "prompt": (
                    "🌟 <b>Gabungan Kata (Body & Activity):</b>\n\n"
                    "<i>\"Before eating, I wash my <b>hands</b>.\"</i>\n"
                    "<i>(Sebelum makan, saya mencuci tangan saya.)</i>\n\n"
                    "• wash = mencuci\n"
                    "• hands = tangan\n\n"
                    "👉 <b>Giliranmu:</b> Ketik ulang kalimat bahasa Inggris di atas!"
                ),
            },
            {
                "id": "voc_adv_02",
                "badge": "📚 Kalimat: Menggosok Gigi",
                "prompt": (
                    "🌟 <b>Gabungan Kata (Body & Activity):</b>\n\n"
                    "<i>\"Before sleeping, we brush our <b>teeth</b>.\"</i>\n"
                    "<i>(Sebelum tidur, kita menggosok gigi.)</i>\n\n"
                    "• brush = menyikat / menggosok\n"
                    "• teeth = gigi\n\n"
                    "👉 <b>Giliranmu:</b> Ketik ulang kalimat bahasa Inggris di atas!"
                ),
            },
            {
                "id": "voc_adv_03",
                "badge": "📚 Kalimat: Menyisir Rambut",
                "prompt": (
                    "🌟 <b>Gabungan Kata (Body & Activity):</b>\n\n"
                    "<i>\"Every morning, she combs her <b>hair</b>.\"</i>\n"
                    "<i>(Setiap pagi, dia menyisir rambutnya.)</i>\n\n"
                    "• combs = menyisir\n"
                    "• hair = rambut\n\n"
                    "👉 <b>Giliranmu:</b> Kata <b>'hair'</b> artinya apa dalam bahasa Indonesia?"
                ),
            },
            {
                "id": "voc_adv_04",
                "badge": "📚 Kalimat: Membaca dengan Mata",
                "prompt": (
                    "🌟 <b>Gabungan Kata (Body & Activity):</b>\n\n"
                    "<i>\"We use our <b>eyes</b> to read storybooks.\"</i>\n"
                    "<i>(Kita menggunakan mata kita untuk membaca buku cerita.)</i>\n\n"
                    "• eyes = mata\n"
                    "• read = membaca\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'Mata'</b>!"
                ),
            },
            {
                "id": "voc_adv_05",
                "badge": "📚 Kalimat: Berlari di Lapangan",
                "prompt": (
                    "🌟 <b>Gabungan Kata (Body & Activity):</b>\n\n"
                    "<i>\"The boys run with their <b>legs</b> in the field.\"</i>\n"
                    "<i>(Anak-anak laki-laki berlari dengan kaki mereka di lapangan.)</i>\n\n"
                    "• run = berlari\n"
                    "• legs = kaki\n\n"
                    "👉 <b>Giliranmu:</b> Kata <b>'run'</b> artinya apa dalam bahasa Indonesia?"
                ),
            },
            {
                "id": "voc_adv_06",
                "badge": "📚 Kalimat: Berbicara Bahasa Inggris",
                "prompt": (
                    "🌟 <b>Gabungan Kata (Body & Activity):</b>\n\n"
                    "<i>\"I open my <b>mouth</b> to speak English with confidence!\"</i>\n"
                    "<i>(Saya membuka mulut untuk berbicara bahasa Inggris dengan percaya diri!)</i>\n\n"
                    "• mouth = mulut\n"
                    "• speak = berbicara\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat penyemangat ini: <code>I speak English!</code>"
                ),
            },
        ],
    },

    # =========================================================================
    # 3. ✏️ GRAMMAR (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # Sesuai revisi: verbs, to be, adjective, part of speech
    # =========================================================================
    config.MODE_GRAMMAR: {
        config.LEVEL_BEGINNER: [
            {
                "id": "grm_beg_01",
                "badge": "✏️ To Be: Belajar 'am'",
                "prompt": (
                    "🔍 <b>Aturan 'To Be':</b>\n\n"
                    "Kata <b>I</b> (Saya) pasangannya SELALU <b>am</b>!\n\n"
                    "Contoh:\n"
                    "• <i>I am a student.</i> (Saya seorang murid)\n"
                    "• <i>I am happy.</i> (Saya bahagia)\n\n"
                    "❓ <b>Lengkapi kalimat ini:</b>\n"
                    "<code>I ___ a good boy/girl.</code> (am / is / are)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang tepat!"
                ),
            },
            {
                "id": "grm_beg_02",
                "badge": "✏️ To Be: Belajar 'is'",
                "prompt": (
                    "🔍 <b>Aturan 'To Be':</b>\n\n"
                    "Untuk orang tunggal (dia/itu):\n"
                    "• <b>He</b> (dia laki-laki) ➡️ <b>is</b>\n"
                    "• <b>She</b> (dia perempuan) ➡️ <b>is</b>\n"
                    "• <b>It</b> (hewan/benda) ➡️ <b>is</b>\n\n"
                    "Contoh: <i>She is my sister.</i> (Dia adalah adik/kakak perempuanku)\n\n"
                    "❓ <b>Lengkapi kalimat ini:</b>\n"
                    "<code>He ___ my teacher.</code> (am / is / are)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang tepat!"
                ),
            },
            {
                "id": "grm_beg_03",
                "badge": "✏️ To Be: Belajar 'are'",
                "prompt": (
                    "🔍 <b>Aturan 'To Be':</b>\n\n"
                    "Untuk orang jamak (banyak) dan 'kamu':\n"
                    "• <b>You</b> (kamu) ➡️ <b>are</b>\n"
                    "• <b>They</b> (mereka) ➡️ <b>are</b>\n"
                    "• <b>We</b> (kita / kami) ➡️ <b>are</b>\n\n"
                    "Contoh: <i>We are friends.</i> (Kita berteman)\n\n"
                    "❓ <b>Lengkapi kalimat ini:</b>\n"
                    "<code>They ___ happy today.</code> (am / is / are)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang tepat!"
                ),
            },
            {
                "id": "grm_beg_04",
                "badge": "✏️ Kuis To Be: I am a girl",
                "prompt": (
                    "🔍 <b>Latihan Soal To Be:</b>\n\n"
                    "Perhatikan kalimat ini:\n"
                    "<code>I ___ a girl.</code>\n\n"
                    "Pilihannya:\n"
                    "A. am\n"
                    "B. is\n"
                    "C. are\n\n"
                    "👉 <b>Giliranmu:</b> Ketik jawaban yang benar (am / is / are)!"
                ),
            },
            {
                "id": "grm_beg_05",
                "badge": "✏️ Kuis To Be: The Cat",
                "prompt": (
                    "🔍 <b>Latihan Soal To Be:</b>\n\n"
                    "Perhatikan kalimat ini:\n"
                    "<code>The cat ___ very cute.</code>\n"
                    "<i>(Kucing itu sangat lucu)</i>\n\n"
                    "💡 <i>Petunjuk: Karena kucingnya cuma 1 (it), kita gunakan 'is'.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Tulis to be yang benar: <b>am</b>, <b>is</b>, atau <b>are</b>?"
                ),
            },
            {
                "id": "grm_beg_06",
                "badge": "✏️ Kuis To Be: We are happy",
                "prompt": (
                    "🔍 <b>Latihan Soal To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>We ___ studying English.</code>\n"
                    "<i>(Kami sedang belajar bahasa Inggris)</i>\n\n"
                    "💡 <i>Petunjuk: 'We' (kami) pasangannya adalah 'are'.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik jawaban yang benar!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "grm_int_01",
                "badge": "✏️ Verbs: Mengenal Kata Kerja",
                "prompt": (
                    "🏃 <b>Apa itu Verb (Kata Kerja)?</b>\n"
                    "Verb adalah kata yang menunjukkan aksi atau kegiatan.\n\n"
                    "Contoh Verb sehari-hari:\n"
                    "• <b>eat</b> = makan\n"
                    "• <b>drink</b> = minum\n"
                    "• <b>sleep</b> = tidur\n"
                    "• <b>play</b> = bermain\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata kerja bahasa Inggris untuk <b>'makan'</b>!"
                ),
            },
            {
                "id": "grm_int_02",
                "badge": "✏️ Verbs: Membuat Kalimat Aksi",
                "prompt": (
                    "🏃 <b>Kalimat Sederhana dengan Verb:</b>\n\n"
                    "Susunannya mudah: <b>Subjek + Kata Kerja + Benda</b>\n"
                    "• <i>I eat rice.</i> (Saya makan nasi)\n"
                    "• <i>I drink milk.</i> (Saya minum susu)\n\n"
                    "❓ <b>Lengkapi kalimat:</b>\n"
                    "<code>I ___ football with my friends.</code>\n"
                    "<i>(Pilihan kata kerja: drink / play / sleep)</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata kerja yang tepat!"
                ),
            },
            {
                "id": "grm_int_03",
                "badge": "✏️ Adjectives: Mengenal Kata Sifat",
                "prompt": (
                    "🌸 <b>Apa itu Adjective (Kata Sifat)?</b>\n"
                    "Adjective adalah kata yang menggambarkan keadaan atau perasaan.\n\n"
                    "Contoh Adjective:\n"
                    "• <b>happy</b> = senang / gembira\n"
                    "• <b>sad</b> = sedih\n"
                    "• <b>big</b> = besar\n"
                    "• <b>small</b> = kecil\n\n"
                    "👉 <b>Giliranmu:</b> Ketik bahasa Inggris untuk kata sifat <b>'senang'</b>!"
                ),
            },
            {
                "id": "grm_int_04",
                "badge": "✏️ Adjectives: Besar dan Kecil",
                "prompt": (
                    "🐘 <b>Contoh Penggunaan Kata Sifat:</b>\n\n"
                    "• <i>The elephant is <b>big</b>.</i> (Gajah itu besar)\n"
                    "• <i>The ant is <b>small</b>.</i> (Semut itu kecil)\n\n"
                    "❓ <b>Pilih kata sifat yang cocok:</b>\n"
                    "Rumah itu luas dan besar ➡️ <code>The house is ___ (big / small)</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata sifat yang tepat!"
                ),
            },
            {
                "id": "grm_int_05",
                "badge": "✏️ Adjectives: Bersih dan Baik",
                "prompt": (
                    "✨ <b>Kata Sifat Kebaikan & Kebersihan:</b>\n\n"
                    "• <b>clean</b> = bersih\n"
                    "• <b>kind</b> = baik hati\n"
                    "• <b>smart</b> = pintar\n\n"
                    "Contoh: <i>My teacher is kind.</i> (Guruku baik hati)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata bahasa Inggris untuk <b>'pintar'</b>!"
                ),
            },
            {
                "id": "grm_int_06",
                "badge": "✏️ Verbs: Membaca dan Menulis",
                "prompt": (
                    "📖 <b>Kata Kerja Belajar:</b>\n\n"
                    "• <b>read</b> = membaca\n"
                    "• <b>write</b> = menulis\n\n"
                    "Contoh: <i>I read an English story.</i> (Saya membaca cerita bahasa Inggris)\n\n"
                    "👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk <b>'menulis'</b>!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "grm_adv_01",
                "badge": "✏️ Part of Speech: Noun (Kata Benda)",
                "prompt": (
                    "📦 <b>Part of Speech: Mengenal NOUN (Kata Benda)</b>\n\n"
                    "Noun adalah nama benda, orang, hewan, atau tempat.\n"
                    "Contoh:\n"
                    "• <b>book</b> (buku)\n"
                    "• <b>cat</b> (kucing)\n"
                    "• <b>school</b> (sekolah)\n\n"
                    "❓ Manakah yang merupakan NOUN (kata benda)?\n"
                    "A. run (berlari)\n"
                    "B. apple (apel)\n"
                    "C. happy (senang)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik huruf jawaban yang benar!"
                ),
            },
            {
                "id": "grm_adv_02",
                "badge": "✏️ Part of Speech: Verb (Kata Kerja)",
                "prompt": (
                    "🏃 <b>Part of Speech: Mengenal VERB (Kata Kerja)</b>\n\n"
                    "Verb adalah kata yang menunjukkan kegiatan atau tindakan.\n\n"
                    "❓ Pada kalimat ini, manakah yang merupakan VERB (kata kerja)?\n"
                    "<code>\"The children play in the garden.\"</code>\n"
                    "<i>(Anak-anak bermain di taman)</i>\n\n"
                    "💡 Pilihan: children / play / garden\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata kerjanya!"
                ),
            },
            {
                "id": "grm_adv_03",
                "badge": "✏️ Part of Speech: Adjective (Kata Sifat)",
                "prompt": (
                    "🌸 <b>Part of Speech: Mengenal ADJECTIVE (Kata Sifat)</b>\n\n"
                    "Adjective menjelaskan sifat atau keadaan suatu benda.\n\n"
                    "❓ Pada kalimat ini, manakah yang merupakan ADJECTIVE (kata sifat)?\n"
                    "<code>\"My sister has a beautiful doll.\"</code>\n"
                    "<i>(Adikku memiliki boneka yang cantik)</i>\n\n"
                    "💡 Pilihan: sister / beautiful / doll\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kata sifatnya!"
                ),
            },
            {
                "id": "grm_adv_04",
                "badge": "✏️ Part of Speech: Tebak Kategori",
                "prompt": (
                    "🎯 <b>Tebak Kategori Kata:</b>\n\n"
                    "Kata: <b>\"SLEEP\"</b> (tidur)\n\n"
                    "Apakah kata 'sleep' termasuk:\n"
                    "A. Noun (kata benda)\n"
                    "B. Verb (kata kerja)\n"
                    "C. Adjective (kata sifat)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik A, B, atau C!"
                ),
            },
            {
                "id": "grm_adv_05",
                "badge": "✏️ Part of Speech: Tebak Kategori",
                "prompt": (
                    "🎯 <b>Tebak Kategori Kata:</b>\n\n"
                    "Kata: <b>\"HAPPY\"</b> (bahagia / senang)\n\n"
                    "Apakah kata 'happy' termasuk:\n"
                    "A. Noun (kata benda)\n"
                    "B. Verb (kata kerja)\n"
                    "C. Adjective (kata sifat)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik A, B, atau C!"
                ),
            },
            {
                "id": "grm_adv_06",
                "badge": "✏️ Kalimat Lengkap (Noun + Verb + Adj)",
                "prompt": (
                    "🌟 <b>Menyusun Kalimat Lengkap:</b>\n\n"
                    "Perhatikan kalimat ini:\n"
                    "<code>\"The cute cat sleeps.\"</code>\n"
                    "• <b>cute</b> = Adjective (lucu)\n"
                    "• <b>cat</b> = Noun (kucing)\n"
                    "• <b>sleeps</b> = Verb (tidur)\n\n"
                    "👉 <b>Giliranmu:</b> Terjemahkan ke bahasa Indonesia dengan mengetik:\n"
                    "<i>Kucing lucu itu tidur.</i>"
                ),
            },
        ],
    },

    # =========================================================================
    # 4. 📖 READING (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # Sesuai revisi: descriptive, narrative, recount text
    # =========================================================================
    config.MODE_READING: {
        # Beginner: Descriptive Text (Mendeskripsikan hewan peliharaan, sekolah, dsb)
        config.LEVEL_BEGINNER: [
            {
                "id": "rdg_beg_01",
                "badge": "📖 Descriptive: My Cat Milo",
                "prompt": (
                    "📄 <b>Bacalah teks pendek ini:</b>\n\n"
                    "<i>\"I have a pet cat. His name is Milo. He is yellow and white. He has big green eyes. Milo likes to eat fish and sleep on the sofa.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• pet cat = kucing peliharaan\n"
                    "• big green eyes = mata hijau besar\n"
                    "• fish = ikan\n\n"
                    "❓ <b>Pertanyaan:</b> Apa warna mata Milo? (What color are Milo's eyes?)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik warnanya (green / yellow / white)!"
                ),
            },
            {
                "id": "rdg_beg_02",
                "badge": "📖 Descriptive: My School (Sekolahku)",
                "prompt": (
                    "📄 <b>Bacalah teks pendek ini:</b>\n\n"
                    "<i>\"My school is clean and beautiful. There are six classrooms. There is a big yard in front of the school. We play football in the yard.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• clean = bersih\n"
                    "• yard = halaman\n"
                    "• play football = bermain bola\n\n"
                    "❓ <b>Pertanyaan:</b> Apa yang dilakukan anak-anak di halaman sekolah?\n\n"
                    "👉 <b>Giliranmu:</b> Jawab: <code>Play football</code>"
                ),
            },
            {
                "id": "rdg_beg_03",
                "badge": "📖 Descriptive: My Bicycle (Sepedaku)",
                "prompt": (
                    "📄 <b>Bacalah teks pendek ini:</b>\n\n"
                    "<i>\"I have a new bicycle. It is bright red. It has two black wheels and a small bell. I ride my bicycle to school every day.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• bicycle = sepeda\n"
                    "• red = merah\n"
                    "• bell = bel\n\n"
                    "❓ <b>Pertanyaan:</b> Apa warna sepeda itu? (What color is the bicycle?)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik warna sepedanya dalam bahasa Inggris!"
                ),
            },
            {
                "id": "rdg_beg_04",
                "badge": "📖 Descriptive: A Sweet Banana",
                "prompt": (
                    "📄 <b>Bacalah teks pendek ini:</b>\n\n"
                    "<i>\"Banana is my favorite fruit. It is yellow when ripe. It is very sweet and healthy. Monkeys also love to eat bananas.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• fruit = buah\n"
                    "• sweet = manis\n"
                    "• healthy = sehat\n\n"
                    "❓ <b>Pertanyaan:</b> Hewan apa yang suka makan pisang pada teks di atas?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Monkeys</code>"
                ),
            },
            {
                "id": "rdg_beg_05",
                "badge": "📖 Descriptive: My Mother",
                "prompt": (
                    "📄 <b>Bacalah teks pendek ini:</b>\n\n"
                    "<i>\"My mother is very kind and pretty. She wakes up early every morning. She cooks delicious fried rice for breakfast. I love my mother very much.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• kind = baik hati\n"
                    "• cooks = memasak\n"
                    "• delicious = lezat / enak\n\n"
                    "❓ <b>Pertanyaan:</b> Apa yang dimasak Ibu untuk sarapan?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Fried rice</code>"
                ),
            },
            {
                "id": "rdg_beg_06",
                "badge": "📖 Descriptive: My Best Friend Budi",
                "prompt": (
                    "📄 <b>Bacalah teks pendek ini:</b>\n\n"
                    "<i>\"Budi is my best friend. He is tall and smart. He sits next to me in class. We always share our crayons and help each other.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• best friend = sahabat\n"
                    "• tall = tinggi\n"
                    "• smart = pintar\n\n"
                    "❓ <b>Pertanyaan:</b> Siapa nama sahabat dalam cerita di atas?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik nama sahabat tersebut!"
                ),
            },
        ],
        # Intermediate: Narrative Text (Fabel / Cerita Fiksi Pendek)
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "rdg_int_01",
                "badge": "📖 Narrative: The Rabbit and the Turtle",
                "prompt": (
                    "📄 <b>Cerita Fabel Pendek: Kelinci dan Kura-Kura</b>\n\n"
                    "<i>\"One day, a rabbit ran very fast. The turtle walked very slow. The rabbit took a nap under a tree because he was arrogant. The turtle kept walking and won the race!\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• rabbit = kelinci | turtle = kura-kura\n"
                    "• took a nap = tidur siang\n"
                    "• won the race = memenangkan lomba\n\n"
                    "❓ <b>Pertanyaan:</b> Siapa yang memenangkan lomba lari? (Who won the race?)\n\n"
                    "👉 <b>Giliranmu:</b> Jawab: <code>The turtle</code>"
                ),
            },
            {
                "id": "rdg_int_02",
                "badge": "📖 Narrative: The Thirsty Bird",
                "prompt": (
                    "📄 <b>Cerita Fabel Pendek: Burung yang Haus</b>\n\n"
                    "<i>\"A little bird was very thirsty. He saw a pitcher with a little water at the bottom. He dropped small stones into the pitcher one by one. The water rose up, and the bird drank happily.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• thirsty = haus\n"
                    "• stones = batu-batu kecil\n"
                    "• drank = minum\n\n"
                    "❓ <b>Pertanyaan:</b> Apa yang dimasukkan burung ke dalam wadah air?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Stones</code> (Batu)"
                ),
            },
            {
                "id": "rdg_int_03",
                "badge": "📖 Narrative: Sang Kancil and the River",
                "prompt": (
                    "📄 <b>Cerita Fabel Pendek: Sang Kancil yang Cerdik</b>\n\n"
                    "<i>\"Sang Kancil wanted to cross a wide river. He saw many crocodiles. He said, 'Line up! The King wants to count you.' The crocodiles lined up. Kancil jumped on their backs and safely crossed the river!\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• river = sungai\n"
                    "• crocodiles = buaya-buaya\n"
                    "• jumped = melompat\n\n"
                    "❓ <b>Pertanyaan:</b> Hewan apa yang ada di sungai? (What animals were in the river?)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Crocodiles</code>"
                ),
            },
            {
                "id": "rdg_int_04",
                "badge": "📖 Narrative: The Ant and the Dove",
                "prompt": (
                    "📄 <b>Cerita Fabel Pendek: Semut dan Merpati</b>\n\n"
                    "<i>\"A little ant fell into the water. A kind dove dropped a dry leaf into the water to save the ant. The ant climbed on the leaf. Later, the ant bit a hunter to save the dove.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• ant = semut\n"
                    "• dove = burung merpati\n"
                    "• leaf = daun\n\n"
                    "❓ <b>Pertanyaan:</b> Benda apa yang dijatuhkan burung merpati untuk menolong semut?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>A leaf</code> (Daun)"
                ),
            },
            {
                "id": "rdg_int_05",
                "badge": "📖 Narrative: The Honest Woodcutter",
                "prompt": (
                    "📄 <b>Cerita Dongeng: Penebang Kayu yang Jujur</b>\n\n"
                    "<i>\"A poor woodcutter lost his iron axe in the lake. A magical fairy showed him a golden axe, but he said, 'No, that is not mine.' Because he was honest, the fairy gave him both the iron and golden axes!\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• woodcutter = penebang kayu\n"
                    "• axe = kapak\n"
                    "• honest = jujur\n\n"
                    "❓ <b>Pertanyaan:</b> Mengapa peri memberi hadiah kedua kapak tersebut?\n\n"
                    "👉 <b>Giliranmu:</b> Karena dia... <code>Honest</code> (Jujur)"
                ),
            },
            {
                "id": "rdg_int_06",
                "badge": "📖 Narrative: The Lion and the Mouse",
                "prompt": (
                    "📄 <b>Cerita Fabel Pendek: Singa dan Tikus</b>\n\n"
                    "<i>\"A big lion spared a tiny mouse's life. Later, the lion was caught in a hunter's net. The tiny mouse came and chewed the net with his sharp teeth. The lion was free!\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• lion = singa | mouse = tikus\n"
                    "• net = jaring pemburu\n"
                    "• chewed = menggigit / mengunyah\n\n"
                    "❓ <b>Pertanyaan:</b> Siapa yang menolong singa lepas dari jaring?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>The mouse</code>"
                ),
            },
        ],
        # Advanced: Recount Text (Menceritakan Pengalaman Masa Lalu Sederhana)
        config.LEVEL_ADVANCED: [
            {
                "id": "rdg_adv_01",
                "badge": "📖 Recount: Yesterday at the Beach",
                "prompt": (
                    "📄 <b>Recount Text (Pengalaman Kemarin):</b>\n\n"
                    "<i>\"Yesterday was Sunday. My family and I went to the beach. The weather was sunny. My brother and I built a sandcastle. We ate fresh coconut water. It was a wonderful day!\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• went = pergi (bentuk lampau)\n"
                    "• built = membangun\n"
                    "• sandcastle = istana pasir\n\n"
                    "❓ <b>Pertanyaan:</b> Kemanakah penulis dan keluarganya pergi kemarin?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>To the beach</code>"
                ),
            },
            {
                "id": "rdg_adv_02",
                "badge": "📖 Recount: Helping Father in the Garden",
                "prompt": (
                    "📄 <b>Recount Text (Pengalaman Kemarin):</b>\n\n"
                    "<i>\"Last Saturday, I helped my father in the vegetable garden. We watered the chili plants and pulled out the grass. In the afternoon, father bought me sweet ice cream as a treat.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• helped = membantu\n"
                    "• garden = kebun\n"
                    "• watered = menyiram air\n\n"
                    "❓ <b>Pertanyaan:</b> Makanan manis apa yang dibelikan ayah di sore hari?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Ice cream</code>"
                ),
            },
            {
                "id": "rdg_adv_03",
                "badge": "📖 Recount: Holiday at Grandfather's Village",
                "prompt": (
                    "📄 <b>Recount Text (Pengalaman Liburan):</b>\n\n"
                    "<i>\"During the school holiday, I visited my grandparents in the village. The air was fresh and cool. I fed the chickens every morning and swam in the clean river with my cousins.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• visited = berkunjung\n"
                    "• village = desa\n"
                    "• fed the chickens = memberi makan ayam\n\n"
                    "❓ <b>Pertanyaan:</b> Hewan apa yang diberi makan setiap pagi di desa?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Chickens</code> (Ayam)"
                ),
            },
            {
                "id": "rdg_adv_04",
                "badge": "📖 Recount: Playing Football in the Rain",
                "prompt": (
                    "📄 <b>Recount Text (Pengalaman Kemarin):</b>\n\n"
                    "<i>\"Yesterday afternoon, it rained heavily. My friends and I played football in the rain. We were so happy and laughed a lot. After that, I took a warm shower at home.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• rained = hujan\n"
                    "• laughed = tertawa\n"
                    "• warm shower = mandi air hangat\n\n"
                    "❓ <b>Pertanyaan:</b> Olahraga apa yang dimainkan saat hujan?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Football</code> (Sepak bola)"
                ),
            },
            {
                "id": "rdg_adv_05",
                "badge": "📖 Recount: Cooking Fried Rice with Mother",
                "prompt": (
                    "📄 <b>Recount Text (Pengalaman Memasak):</b>\n\n"
                    "<i>\"Last night, I cooked fried rice with my mother. I helped slice the onions and crack two eggs. When it was ready, the whole family ate together happily.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• cooked = memasak\n"
                    "• onions = bawang\n"
                    "• eggs = telur\n\n"
                    "❓ <b>Pertanyaan:</b> Berapa butir telur yang digunakan? (How many eggs?)\n\n"
                    "👉 <b>Giliranmu:</b> Ketik jumlahnya: <code>Two</code>"
                ),
            },
            {
                "id": "rdg_adv_06",
                "badge": "📖 Recount: My First Day at School",
                "prompt": (
                    "📄 <b>Recount Text (Hari Pertama Masuk Sekolah):</b>\n\n"
                    "<i>\"I remember my first day in elementary school. I wore a new uniform. I felt a little nervous at first, but my teacher smiled warmly and gave me a colorful badge.\"</i>\n\n"
                    "💡 <b>Kamus Bantuan:</b>\n"
                    "• uniform = seragam\n"
                    "• nervous = gugup\n"
                    "• smiled = tersenyum\n\n"
                    "❓ <b>Pertanyaan:</b> Siapa yang tersenyum ramah kepada murid?\n\n"
                    "👉 <b>Giliranmu:</b> Ketik: <code>Teacher</code>"
                ),
            },
        ],
    },

    # =========================================================================
    # 5. 🗣️ SPEAKING (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # Latihan pengucapan kata dasar & sapaan anak dengan panduan cara baca
    # =========================================================================
    config.MODE_SPEAKING: {
        config.LEVEL_BEGINNER: [
            {
                "id": "spk_beg_01",
                "badge": "🗣️ Pengucapan: Sapaan Guru",
                "prompt": (
                    "🎙️ <b>Latihan Mengucapkan Kalimat Sapaan:</b>\n\n"
                    "<i>\"Good morning, Teacher!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Gud morniing, tii-cer!]</code>\n\n"
                    "Artinya: <i>Selamat pagi, Guru!</i>\n\n"
                    "👉 <b>Giliranmu:</b> Kirim rekaman suara (voice note) mengucapkan kalimat di atas, atau ketik ulang kalimatnya!"
                ),
            },
            {
                "id": "spk_beg_02",
                "badge": "🗣️ Pengucapan: Anggota Tubuh",
                "prompt": (
                    "🎙️ <b>Latihan Mengucapkan Kata Anggota Tubuh:</b>\n\n"
                    "<i>\"Head, Eyes, Nose, Mouth\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Hed, Ais, Nous, Maut]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan 4 kata anggota tubuh di atas melalui voice note atau ketik kembali!"
                ),
            },
            {
                "id": "spk_beg_03",
                "badge": "🗣️ Pengucapan: Menyebutkan Nama",
                "prompt": (
                    "🎙️ <b>Latihan Memperkenalkan Diri:</b>\n\n"
                    "<i>\"Hello! My name is Budi.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[He-low! Mai neim is Budi.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan kalimat di atas dengan menyebutkan namamu sendiri!"
                ),
            },
            {
                "id": "spk_beg_04",
                "badge": "🗣️ Pengucapan: Terima Kasih",
                "prompt": (
                    "🎙️ <b>Latihan Mengucapkan Terima Kasih:</b>\n\n"
                    "<i>\"Thank you very much!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Teng-kyu ve-ri mac!]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Latihlah lidahmu mengucapkan kata terima kasih di atas!"
                ),
            },
            {
                "id": "spk_beg_05",
                "badge": "🗣️ Pengucapan: Perasaan Senang",
                "prompt": (
                    "🎙️ <b>Latihan Mengucapkan Kalimat:</b>\n\n"
                    "<i>\"I am very happy today!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai em ve-ri he-pi tu-dei!]</code>\n\n"
                    "Artinya: <i>Saya sangat senang hari ini!</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan kalimat bahagia ini dengan senyuman!"
                ),
            },
            {
                "id": "spk_beg_06",
                "badge": "🗣️ Pengucapan: Sampai Jumpa",
                "prompt": (
                    "🎙️ <b>Latihan Mengucapkan Perpisahan:</b>\n\n"
                    "<i>\"See you tomorrow, friend!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Sii yu tu-mo-rou, frend!]</code>\n\n"
                    "Artinya: <i>Sampai jumpa besok, teman!</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan kalimat perpisahan di atas!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "spk_int_01",
                "badge": "🗣️ Kalimat Harian: Bangun Pagi",
                "prompt": (
                    "🎙️ <b>Latihan Melafalkan Kalimat:</b>\n\n"
                    "<i>\"I wake up early in the morning.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai weik ap er-li in de morniing.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Rekam suaramu atau ketik kalimat di atas!"
                ),
            },
            {
                "id": "spk_int_02",
                "badge": "🗣️ Kalimat Harian: Cuci Tangan",
                "prompt": (
                    "🎙️ <b>Latihan Melafalkan Kalimat:</b>\n\n"
                    "<i>\"I wash my hands with soap.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai wos mai hends wit soup.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Latihlah membaca kalimat ini dengan jelas!"
                ),
            },
            {
                "id": "spk_int_03",
                "badge": "🗣️ Kalimat Harian: Pergi Sekolah",
                "prompt": (
                    "🎙️ <b>Latihan Melafalkan Kalimat:</b>\n\n"
                    "<i>\"We go to school together.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Wii gou tu skuul tu-ge-der.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan kalimat di atas dengan lantang!"
                ),
            },
            {
                "id": "spk_int_04",
                "badge": "🗣️ Kalimat Harian: Cinta Keluarga",
                "prompt": (
                    "🎙️ <b>Latihan Melafalkan Kalimat:</b>\n\n"
                    "<i>\"I love my father and mother.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai lav mai faa-der en ma-der.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Kirimkan ucapan kasih sayang untuk orang tua ini!"
                ),
            },
            {
                "id": "spk_int_05",
                "badge": "🗣️ Kalimat Harian: Belajar Seru",
                "prompt": (
                    "🎙️ <b>Latihan Melafalkan Kalimat:</b>\n\n"
                    "<i>\"English is very fun and easy!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ing-glisy is ve-ri fan en ii-zi!]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan dengan semangat tinggi!"
                ),
            },
            {
                "id": "spk_int_06",
                "badge": "🗣️ Kalimat Harian: Membaca Buku",
                "prompt": (
                    "🎙️ <b>Latihan Melafalkan Kalimat:</b>\n\n"
                    "<i>\"I like to read storybooks.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai laik tu riid stou-ri-buks.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Latihlah membaca kalimat ini dengan lancar!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "spk_adv_01",
                "badge": "🗣️ Sajak Berima: One, Two, Three",
                "prompt": (
                    "🎙️ <b>Latihan Irama Kata (Nursery Rhyme):</b>\n\n"
                    "<i>\"One, two, three, look at me!\n"
                    "Four, five, six, pick up sticks!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Wan, tu, trii, luk et mii!\n"
                    "For, faif, siks, pik ap stiks!]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan sajak angka yang menyenangkan ini!"
                ),
            },
            {
                "id": "spk_adv_02",
                "badge": "🗣️ Sajak Warna: Red and Yellow",
                "prompt": (
                    "🎙️ <b>Latihan Irama Warna:</b>\n\n"
                    "<i>\"Red apple, yellow sun, blue sea,\n"
                    "English is so good for me!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Red e-pel, ye-low san, bluu sii,\n"
                    "Ing-glisy is sou gud for mii!]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Latihlah intonasi dan pengucapan sajak ini!"
                ),
            },
            {
                "id": "spk_adv_03",
                "badge": "🗣️ Cita-cita: Menjadi Pintar",
                "prompt": (
                    "🎙️ <b>Latihan Berbicara Percaya Diri:</b>\n\n"
                    "<i>\"I want to study hard and be smart.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai wont tu sta-di hard en bi smart.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Rekam suaramu dengan penuh keyakinan!"
                ),
            },
            {
                "id": "spk_adv_04",
                "badge": "🗣️ Membantu Orang Tua",
                "prompt": (
                    "🎙️ <b>Latihan Berbicara Percaya Diri:</b>\n\n"
                    "<i>\"I help my parents at home every day.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Ai help mai pe-rents et houm ev-ri dei.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan kalimat perbuatan baik ini!"
                ),
            },
            {
                "id": "spk_adv_05",
                "badge": "🗣️ Bersyukur Hari Ini",
                "prompt": (
                    "🎙️ <b>Latihan Berbicara Percaya Diri:</b>\n\n"
                    "<i>\"Today is a bright and beautiful day.\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Tu-dei is e brait en byuu-ti-ful dei.]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan kalimat syukur di atas!"
                ),
            },
            {
                "id": "spk_adv_06",
                "badge": "🗣️ Yel-yel Bahasa Inggris",
                "prompt": (
                    "🎙️ <b>Yel-yel Semangat Bahasa Inggris:</b>\n\n"
                    "<i>\"Yes! I can speak English!\"</i>\n\n"
                    "📖 <b>Panduan Cara Baca:</b>\n"
                    "<code>[Yes! Ai ken spiik Ing-glisy!]</code>\n\n"
                    "👉 <b>Giliranmu:</b> Ucapkan yel-yel penyemangat ini dengan gembira!"
                ),
            },
        ],
    },

    # =========================================================================
    # 6. 🎮 ENGLISH CHALLENGE (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # Sesuai revisi: DIMUDAHKAN!
    # Beginner: Unscramble super mudah (seperti "i am a girl")
    # Intermediate: Kuis to be (am / is / are)
    # Advanced: Unscramble kata kerja aksi sehari-hari
    # =========================================================================
    config.MODE_CHALLENGE: {
        # Beginner: Unscramble kata sangat mudah
        config.LEVEL_BEGINNER: [
            {
                "id": "chg_beg_01",
                "badge": "🎮 Susun Kata: I am a girl",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ girl / a / am / I ]</code>\n\n"
                    "💡 <i>Petunjuk: Mulailah dengan kata 'I' (Saya)...</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat yang benar!\n"
                    "<i>(Jawaban: I am a girl)</i>"
                ),
            },
            {
                "id": "chg_beg_02",
                "badge": "🎮 Susun Kata: He is a boy",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ boy / a / is / He ]</code>\n\n"
                    "💡 <i>Petunjuk: Mulai dengan 'He' (Dia laki-laki)...</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat yang benar!"
                ),
            },
            {
                "id": "chg_beg_03",
                "badge": "🎮 Susun Kata: This is a book",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ book / a / is / This ]</code>\n\n"
                    "💡 <i>Petunjuk: Mulai dengan 'This' (Ini)...</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat yang benar!"
                ),
            },
            {
                "id": "chg_beg_04",
                "badge": "🎮 Susun Kata: It is a cat",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ cat / a / is / It ]</code>\n\n"
                    "💡 <i>Petunjuk: Mulai dengan 'It' (Itu)...</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat yang benar!"
                ),
            },
            {
                "id": "chg_beg_05",
                "badge": "🎮 Susun Kata: I am happy",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ happy / am / I ]</code>\n\n"
                    "💡 <i>Petunjuk: Mulai dengan 'I' (Saya)...</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
            {
                "id": "chg_beg_06",
                "badge": "🎮 Susun Kata: She is a student",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ student / a / is / She ]</code>\n\n"
                    "💡 <i>Petunjuk: Mulai dengan 'She' (Dia perempuan)...</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik kalimat yang benar!"
                ),
            },
        ],
        # Intermediate: Kuis To Be (am, is, are)
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "chg_int_01",
                "badge": "🎮 Kuis To Be: I am",
                "prompt": (
                    "⭐ <b>Tantangan To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>I ___ a student.</code>\n\n"
                    "Pilihan:\n"
                    "A. am\n"
                    "B. is\n"
                    "C. are\n\n"
                    "👉 <b>Giliranmu:</b> Ketik pilihan to be yang tepat!"
                ),
            },
            {
                "id": "chg_int_02",
                "badge": "🎮 Kuis To Be: She is",
                "prompt": (
                    "⭐ <b>Tantangan To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>She ___ my kind teacher.</code>\n"
                    "<i>(Dia adalah guruku yang baik)</i>\n\n"
                    "Pilih salah satu: <b>am</b> / <b>is</b> / <b>are</b>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang benar!"
                ),
            },
            {
                "id": "chg_int_03",
                "badge": "🎮 Kuis To Be: They are",
                "prompt": (
                    "⭐ <b>Tantangan To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>They ___ my best friends.</code>\n"
                    "<i>(Mereka adalah sahabat-sahabatku)</i>\n\n"
                    "Pilih salah satu: <b>am</b> / <b>is</b> / <b>are</b>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang benar!"
                ),
            },
            {
                "id": "chg_int_04",
                "badge": "🎮 Kuis To Be: The dog",
                "prompt": (
                    "⭐ <b>Tantangan To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>The little dog ___ very cute.</code>\n"
                    "<i>(Anjing kecil itu sangat lucu)</i>\n\n"
                    "Pilih salah satu: <b>am</b> / <b>is</b> / <b>are</b>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang benar!"
                ),
            },
            {
                "id": "chg_int_05",
                "badge": "🎮 Kuis To Be: We are",
                "prompt": (
                    "⭐ <b>Tantangan To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>We ___ studying in the classroom.</code>\n"
                    "<i>(Kami sedang belajar di ruang kelas)</i>\n\n"
                    "Pilih salah satu: <b>am</b> / <b>is</b> / <b>are</b>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang benar!"
                ),
            },
            {
                "id": "chg_int_06",
                "badge": "🎮 Kuis To Be: You are",
                "prompt": (
                    "⭐ <b>Tantangan To Be:</b>\n\n"
                    "Lengkapi kalimat ini:\n"
                    "<code>You ___ very smart!</code>\n"
                    "<i>(Kamu sangat pintar!)</i>\n\n"
                    "Pilih salah satu: <b>am</b> / <b>is</b> / <b>are</b>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik to be yang benar!"
                ),
            },
        ],
        # Advanced: Unscramble Kata Kerja Sehari-hari yang Mudah
        config.LEVEL_ADVANCED: [
            {
                "id": "chg_adv_01",
                "badge": "🎮 Susun Kata: I like milk",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ milk / like / I ]</code>\n\n"
                    "💡 <i>Artinya: Saya suka susu.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
            {
                "id": "chg_adv_02",
                "badge": "🎮 Susun Kata: He plays football",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ football / plays / He ]</code>\n\n"
                    "💡 <i>Artinya: Dia bermain sepak bola.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
            {
                "id": "chg_adv_03",
                "badge": "🎮 Susun Kata: We go to school",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ to / We / school / go ]</code>\n\n"
                    "💡 <i>Artinya: Kami pergi ke sekolah.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
            {
                "id": "chg_adv_04",
                "badge": "🎮 Susun Kata: They read books",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ books / read / They ]</code>\n\n"
                    "💡 <i>Artinya: Mereka membaca buku.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
            {
                "id": "chg_adv_05",
                "badge": "🎮 Susun Kata: She eats an apple",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ an / apple / eats / She ]</code>\n\n"
                    "💡 <i>Artinya: Dia memakan sebuah apel.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
            {
                "id": "chg_adv_06",
                "badge": "🎮 Susun Kata: The baby sleeps",
                "prompt": (
                    "🧩 <b>Susun kata acak menjadi kalimat yang benar:</b>\n\n"
                    "<code>[ sleeps / baby / The ]</code>\n\n"
                    "💡 <i>Artinya: Bayi itu tidur.</i>\n\n"
                    "👉 <b>Giliranmu:</b> Ketik susunan kalimat yang benar!"
                ),
            },
        ],
    },
}


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
        }

    candidates = [ex for ex in level_dict if ex.get("id") != exclude_id]
    chosen = random.choice(candidates if candidates else level_dict)

    mode_info = config.LEARNING_MODES.get(mode, {})
    return {
        "id": chosen.get("id"),
        "title": mode_info.get("title", "Latihan Bahasa Inggris"),
        "badge": chosen.get("badge", "Latihan"),
        "prompt": chosen.get("prompt", ""),
    }


def get_offline_feedback(mode: str, level: str, safe_user_text: str) -> str:
    """
    Returns encouraging, child-friendly feedback in Indonesian when AI service is unavailable.
    """
    level_info = config.LEVEL_INFO.get(level, config.LEVEL_INFO[config.DEFAULT_LEVEL])
    badge = level_info["badge"]

    templates = [
        (
            f"✨ <b>English Buddy Note ({badge}):</b>\n\n"
            f"Jawabanmu: <i>\"{safe_user_text}\"</i>\n\n"
            f"🌟 <b>Hebat sekali!</b> Usahamu sangat luar biasa! Teruslah rajin berlatih ya. "
            f"Tekan tombol <b>🔄 Next Exercise</b> untuk latihan seru berikutnya!"
        ),
        (
            f"✨ <b>Catatan Teman Belajar ({badge}):</b>\n\n"
            f"Kamu menulis: <i>\"{safe_user_text}\"</i>\n\n"
            f"👍 <b>Pintar!</b> Belajar bahasa Inggris itu mudah dan menyenangkan kan? "
            f"Setiap kali mencoba, kamu jadi makin jago lho! Semangat terus ya!"
        ),
        (
            f"✨ <b>Pujian dari English Buddy ({badge}):</b>\n\n"
            f"Pesanmu: <i>\"{safe_user_text}\"</i>\n\n"
            f"🎉 <b>Keren banget!</b> Jangan pernah takut salah ya, karena dari mencoba kita jadi bisa. "
            f"Yuk lanjutkan ke tantangan berikutnya!"
        ),
    ]

    return random.choice(templates)
