"""
Curated Challenge exercises for English Buddy Bot.
Total: 200 exercises (67 Beginner, 67 Intermediate, 66 Advanced).
"""
from typing import Any, Dict, List
import config

CHALLENGE_EXERCISES: Dict[str, List[Dict[str, Any]]] = {
    config.LEVEL_BEGINNER: [
    {
        "id": "chg_beg_01",
        "badge": "🔤 Susun Huruf: C-A-T",
        "prompt": "🐱 <b>Word Scramble: Hewan Peliharaan</b>\n\nSusun huruf acak ini menjadi nama hewan berbulu yang mengeong:\n<b>[ T - C - A ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "cat",
            "a cat"
        ],
        "primary_answer": "cat"
    },
    {
        "id": "chg_beg_02",
        "badge": "🔤 Susun Huruf: D-O-G",
        "prompt": "🐶 <b>Word Scramble: Sahabat Setia</b>\n\nSusun huruf acak ini menjadi nama hewan yang menggonggong:\n<b>[ G - D - O ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "dog",
            "a dog"
        ],
        "primary_answer": "dog"
    },
    {
        "id": "chg_beg_03",
        "badge": "🔤 Susun Huruf: B-O-O-K",
        "prompt": "📖 <b>Word Scramble: Benda Belajar</b>\n\nSusun huruf ini menjadi benda yang kita baca:\n<b>[ O - B - K - O ]</b>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "book",
            "a book"
        ],
        "primary_answer": "book"
    },
    {
        "id": "chg_beg_04",
        "badge": "🔤 Susun Huruf: B-A-L-L",
        "prompt": "⚽ <b>Word Scramble: Mainan Olahraga</b>\n\nSusun huruf ini menjadi benda bulat yang ditendang saat bermain bola:\n<b>[ L - B - L - A ]</b>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "ball",
            "a ball"
        ],
        "primary_answer": "ball"
    },
    {
        "id": "chg_beg_05",
        "badge": "🔤 Susun Huruf: S-U-N",
        "prompt": "☀️ <b>Word Scramble: Di Langit Siang</b>\n\nSusun huruf ini menjadi benda langit penerang bumi:\n<b>[ N - U - S ]</b>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "sun",
            "the sun"
        ],
        "primary_answer": "sun"
    },
    {
        "id": "chg_beg_06",
        "badge": "🔤 Susun Huruf: T-R-E-E",
        "prompt": "🌳 <b>Word Scramble: Tumbuhan Rimbun</b>\n\nSusun huruf ini menjadi nama tumbuhan berkayu dan berdaun:\n<b>[ E - E - T - R ]</b>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "tree",
            "a tree"
        ],
        "primary_answer": "tree"
    },
    {
        "id": "chg_beg_07",
        "badge": "🔤 Susun Huruf: F-I-S-H",
        "prompt": "🐟 <b>Word Scramble: Hewan Air</b>\n\nSusun huruf ini menjadi nama hewan yang berenang di air:\n<b>[ H - S - I - F ]</b>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "fish",
            "a fish"
        ],
        "primary_answer": "fish"
    },
    {
        "id": "chg_beg_08",
        "badge": "🔤 Susun Huruf: S-T-A-R",
        "prompt": "⭐ <b>Word Scramble: Di Langit Malam</b>\n\nSusun huruf ini menjadi benda langit yang berkelap-kelip di malam hari:\n<b>[ R - T - A - S ]</b>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "star",
            "a star"
        ],
        "primary_answer": "star"
    },
    {
        "id": "chg_beg_09",
        "badge": "🧩 Susun Kalimat: She is happy",
        "prompt": "😊 <b>Sentence Unscramble (3 kata):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ is / She / happy ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "she is happy",
            "she is happy."
        ],
        "primary_answer": "She is happy"
    },
    {
        "id": "chg_beg_10",
        "badge": "🧩 Susun Kalimat: I drink milk",
        "prompt": "🥛 <b>Sentence Unscramble (3 kata):</b>\n\nSusun kata-kata ini menjadi kalimat yang benar:\n<b>[ drink / I / milk ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "i drink milk",
            "i drink milk."
        ],
        "primary_answer": "I drink milk"
    },
    {
        "id": "chg_beg_11",
        "badge": "🧩 Susun Kalimat: The sky is blue",
        "prompt": "🌤️ <b>Sentence Unscramble (4 kata):</b>\n\nSusun kata-kata ini menjadi kalimat yang tepat:\n<b>[ blue / The / is / sky ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "the sky is blue",
            "the sky is blue."
        ],
        "primary_answer": "The sky is blue"
    },
    {
        "id": "chg_beg_12",
        "badge": "🧩 Susun Kalimat: We have a cat",
        "prompt": "🐈 <b>Sentence Unscramble (4 kata):</b>\n\nSusun kata-kata ini menjadi kalimat yang benar:\n<b>[ a / We / cat / have ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "we have a cat",
            "we have a cat."
        ],
        "primary_answer": "We have a cat"
    },
    {
        "id": "chg_beg_13",
        "badge": "🧩 Susun Kalimat: He runs fast",
        "prompt": "🏃 <b>Sentence Unscramble (3 kata):</b>\n\nSusun kata-kata ini menjadi kalimat yang benar:\n<b>[ fast / He / runs ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "he runs fast",
            "he runs fast."
        ],
        "primary_answer": "He runs fast"
    },
    {
        "id": "chg_beg_14",
        "badge": "🧩 Susun Kalimat: I love my mom",
        "prompt": "❤️ <b>Sentence Unscramble (4 kata):</b>\n\nSusun kata-kata ini menjadi kalimat kasih sayang:\n<b>[ mom / love / I / my ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "i love my mom",
            "i love my mom."
        ],
        "primary_answer": "I love my mom"
    },
    {
        "id": "chg_beg_15",
        "badge": "🧩 Susun Kalimat: It is cold",
        "prompt": "❄️ <b>Sentence Unscramble (3 kata):</b>\n\nSusun kata-kata ini menjadi kalimat cuaca:\n<b>[ cold / It / is ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "it is cold",
            "it is cold."
        ],
        "primary_answer": "It is cold"
    },
    {
        "id": "chg_beg_16",
        "badge": "🧩 Susun Kalimat: They play football",
        "prompt": "⚽ <b>Sentence Unscramble (3 kata):</b>\n\nSusun kata-kata ini menjadi kalimat yang padu:\n<b>[ football / play / They ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "they play football",
            "they play football."
        ],
        "primary_answer": "They play football"
    },
    {
        "id": "chg_beg_17",
        "badge": "❓ Tebak Kata: Hewan Meow",
        "prompt": "🐱 <b>Riddle Ringan:</b>\n\n\"I have four soft paws, sharp claws, and I say 'Meow'. What animal am I?\"\n\n👉 <b>Tebak nama hewannya:</b>",
        "expected": [
            "cat",
            "a cat"
        ],
        "primary_answer": "cat"
    },
    {
        "id": "chg_beg_18",
        "badge": "❓ Tebak Kata: Buah Kuning",
        "prompt": "🍌 <b>Riddle Ringan:</b>\n\n\"I am long and yellow. Monkeys love to eat me and I peel easily. What fruit am I?\"\n\n👉 <b>Tulis nama buahnya:</b>",
        "expected": [
            "banana",
            "a banana"
        ],
        "primary_answer": "banana"
    },
    {
        "id": "chg_beg_19",
        "badge": "❓ Tebak Kata: Air Hujan",
        "prompt": "🌧️ <b>Riddle Ringan:</b>\n\n\"I fall from dark gray clouds in drops when the sky gets stormy. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "rain",
            "water"
        ],
        "primary_answer": "rain"
    },
    {
        "id": "chg_beg_20",
        "badge": "❓ Tebak Kata: Pintu Rumah",
        "prompt": "🚪 <b>Riddle Ringan:</b>\n\n\"You turn my handle and open me to enter a room. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "door",
            "a door"
        ],
        "primary_answer": "door"
    },
    {
        "id": "chg_beg_21",
        "badge": "❓ Tebak Kata: Bulan di Malam Hari",
        "prompt": "🌙 <b>Riddle Ringan:</b>\n\n\"I am round and silver in the night sky. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "moon",
            "the moon"
        ],
        "primary_answer": "moon"
    },
    {
        "id": "chg_beg_22",
        "badge": "❓ Tebak Kata: Kaus Kaki",
        "prompt": "🧦 <b>Riddle Ringan:</b>\n\n\"You put me on your feet before you wear your shoes. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "socks",
            "sock",
            "a sock"
        ],
        "primary_answer": "socks"
    },
    {
        "id": "chg_beg_23",
        "badge": "❓ Tebak Kata: Jam Penunjuk Waktu",
        "prompt": "⏰ <b>Riddle Ringan:</b>\n\n\"I have numbers from 1 to 12 and two hands that tick, showing the exact time. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "clock",
            "a clock",
            "watch"
        ],
        "primary_answer": "clock"
    },
    {
        "id": "chg_beg_24",
        "badge": "❓ Tebak Kata: Buah Apel",
        "prompt": "🍎 <b>Riddle Ringan:</b>\n\n\"There is a saying: 'An ___ a day keeps the doctor away.' What crunchy red fruit is this?\"\n\n👉 <b>Tulis nama buahnya:</b>",
        "expected": [
            "apple",
            "an apple"
        ],
        "primary_answer": "apple"
    },
    {
        "id": "chg_beg_25",
        "badge": "🔤 Susun Huruf: B-I-R-D",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Burung':\n<b>[ I - B - R - D ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "bird",
            "a bird"
        ],
        "primary_answer": "bird"
    },
    {
        "id": "chg_beg_26",
        "badge": "🔤 Susun Huruf: D-U-C-K",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Bebek':\n<b>[ K - U - C - D ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "duck",
            "a duck"
        ],
        "primary_answer": "duck"
    },
    {
        "id": "chg_beg_27",
        "badge": "🔤 Susun Huruf: M-I-L-K",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Susu':\n<b>[ K - L - I - M ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "milk"
        ],
        "primary_answer": "milk"
    },
    {
        "id": "chg_beg_28",
        "badge": "🔤 Susun Huruf: R-I-C-E",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Nasi':\n<b>[ E - C - I - R ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "rice"
        ],
        "primary_answer": "rice"
    },
    {
        "id": "chg_beg_29",
        "badge": "🔤 Susun Huruf: B-O-A-T",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Perahu':\n<b>[ T - A - O - B ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "boat",
            "a boat"
        ],
        "primary_answer": "boat"
    },
    {
        "id": "chg_beg_30",
        "badge": "🔤 Susun Huruf: C-H-A-I-R",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Kursi':\n<b>[ R - A - I - H - C ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "chair",
            "a chair"
        ],
        "primary_answer": "chair"
    },
    {
        "id": "chg_beg_31",
        "badge": "🔤 Susun Huruf: D-O-O-R",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Pintu':\n<b>[ R - O - O - D ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "door",
            "a door"
        ],
        "primary_answer": "door"
    },
    {
        "id": "chg_beg_32",
        "badge": "🔤 Susun Huruf: S-H-O-E",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Sepatu':\n<b>[ E - O - H - S ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "shoe",
            "a shoe"
        ],
        "primary_answer": "shoe"
    },
    {
        "id": "chg_beg_33",
        "badge": "🔤 Susun Huruf: F-R-O-G",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Katak':\n<b>[ G - O - R - F ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "frog",
            "a frog"
        ],
        "primary_answer": "frog"
    },
    {
        "id": "chg_beg_34",
        "badge": "🔤 Susun Huruf: S-N-O-W",
        "prompt": "🔤 <b>Word Scramble: Kosakata Bahasa Inggris</b>\n\nSusun huruf acak ini menjadi kata bahasa Inggris yang berarti 'Salju':\n<b>[ W - O - N - S ]</b>\n\n👉 <b>Tulis kata yang benar:</b>",
        "expected": [
            "snow"
        ],
        "primary_answer": "snow"
    },
    {
        "id": "chg_beg_35",
        "badge": "🧩 Susun Kalimat: I love cats",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat kasih hewan):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ cats / I / love ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "i love cats",
            "i love cats."
        ],
        "primary_answer": "I love cats"
    },
    {
        "id": "chg_beg_36",
        "badge": "🧩 Susun Kalimat: She is a teacher",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat profesi):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ a / is / teacher / She ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "she is a teacher",
            "she is a teacher."
        ],
        "primary_answer": "She is a teacher"
    },
    {
        "id": "chg_beg_37",
        "badge": "🧩 Susun Kalimat: He has a pen",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat kepemilikan):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ a / has / He / pen ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "he has a pen",
            "he has a pen."
        ],
        "primary_answer": "He has a pen"
    },
    {
        "id": "chg_beg_38",
        "badge": "🧩 Susun Kalimat: We eat bread",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat sarapan):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ bread / eat / We ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "we eat bread",
            "we eat bread."
        ],
        "primary_answer": "We eat bread"
    },
    {
        "id": "chg_beg_39",
        "badge": "🧩 Susun Kalimat: The sun is hot",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat cuaca):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ hot / sun / The / is ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "the sun is hot",
            "the sun is hot."
        ],
        "primary_answer": "The sun is hot"
    },
    {
        "id": "chg_beg_40",
        "badge": "🧩 Susun Kalimat: They are happy",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat perasaan):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ happy / are / They ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "they are happy",
            "they are happy."
        ],
        "primary_answer": "They are happy"
    },
    {
        "id": "chg_beg_41",
        "badge": "🧩 Susun Kalimat: My bag is blue",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat warna tas):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ blue / My / is / bag ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "my bag is blue",
            "my bag is blue."
        ],
        "primary_answer": "My bag is blue"
    },
    {
        "id": "chg_beg_42",
        "badge": "🧩 Susun Kalimat: Birds can fly",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat kemampuan):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ fly / Birds / can ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "birds can fly",
            "birds can fly."
        ],
        "primary_answer": "Birds can fly"
    },
    {
        "id": "chg_beg_43",
        "badge": "🧩 Susun Kalimat: Fish swim in water",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat hewan air):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ water / in / Fish / swim ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "fish swim in water",
            "fish swim in water."
        ],
        "primary_answer": "Fish swim in water"
    },
    {
        "id": "chg_beg_44",
        "badge": "🧩 Susun Kalimat: Open the door",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat perintah santun):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ door / the / Open ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "open the door",
            "open the door."
        ],
        "primary_answer": "Open the door"
    },
    {
        "id": "chg_beg_45",
        "badge": "🧩 Susun Kalimat: Close your book",
        "prompt": "🧩 <b>Sentence Unscramble (Kalimat instruksi kelas):</b>\n\nSusun kata-kata acak berikut menjadi kalimat yang benar:\n<b>[ book / your / Close ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "close your book",
            "close your book."
        ],
        "primary_answer": "Close your book"
    },
    {
        "id": "chg_beg_46",
        "badge": "❓ Tebak Benda: Salju",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am white, cold, and fall softly from winter clouds. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "snow",
            "the snow"
        ],
        "primary_answer": "snow"
    },
    {
        "id": "chg_beg_47",
        "badge": "❓ Tebak Benda: Jam Dinding",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have numbers from 1 to 12 and two hands that tick, but no mouth. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "clock",
            "a clock",
            "watch"
        ],
        "primary_answer": "clock"
    },
    {
        "id": "chg_beg_48",
        "badge": "❓ Tebak Benda: Ikan Air",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have fins, scales, and live swimming in water. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "fish",
            "a fish"
        ],
        "primary_answer": "fish"
    },
    {
        "id": "chg_beg_49",
        "badge": "❓ Tebak Benda: Ranjang Tidur",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"You lie on me at night with a pillow and blanket to sleep. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "bed",
            "a bed"
        ],
        "primary_answer": "bed"
    },
    {
        "id": "chg_beg_50",
        "badge": "❓ Tebak Benda: Buku Cerita",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have a colorful cover and many pages filled with words and pictures. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "book",
            "a book"
        ],
        "primary_answer": "book"
    },
    {
        "id": "chg_beg_51",
        "badge": "❓ Tebak Benda: Mobil",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have four wheels, doors, an engine, and carry families on roads. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "car",
            "a car"
        ],
        "primary_answer": "car"
    },
    {
        "id": "chg_beg_52",
        "badge": "❓ Tebak Hewan: Jerapah",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have an extremely long neck so I can eat leaves from the tallest trees. What animal am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "giraffe",
            "a giraffe"
        ],
        "primary_answer": "giraffe"
    },
    {
        "id": "chg_beg_53",
        "badge": "❓ Tebak Benda: Air Minum",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am clear, have no color, and you drink a glass of me when thirsty. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "water"
        ],
        "primary_answer": "water"
    },
    {
        "id": "chg_beg_54",
        "badge": "❓ Tebak Benda: Madu Manis",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am golden, sweet, and made by honeybees in a hive. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "honey"
        ],
        "primary_answer": "honey"
    },
    {
        "id": "chg_beg_55",
        "badge": "❓ Tebak Benda: Matahari",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I rise in the east, warm the earth, and shine brightly in the sky. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "sun",
            "the sun"
        ],
        "primary_answer": "sun"
    },
    {
        "id": "chg_beg_56",
        "badge": "❓ Tebak Hewan: Katak Hijau",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am a green amphibian who can jump far and say 'ribbit' near the pond. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "frog",
            "a frog"
        ],
        "primary_answer": "frog"
    },
    {
        "id": "chg_beg_57",
        "badge": "❓ Tebak Benda: Pensil Tulis",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"You hold me in your hand to write or draw on paper. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "pencil",
            "a pencil",
            "pen"
        ],
        "primary_answer": "pencil"
    },
    {
        "id": "chg_beg_58",
        "badge": "❓ Tebak Hewan: Harimau Belang",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am a big orange wild cat with black stripes that can roar loudly. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "tiger",
            "a tiger"
        ],
        "primary_answer": "tiger"
    },
    {
        "id": "chg_beg_59",
        "badge": "❓ Tebak Hewan: Sapi Perah",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am a farm animal that grazes on green grass and produces fresh milk. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "cow",
            "a cow"
        ],
        "primary_answer": "cow"
    },
    {
        "id": "chg_beg_60",
        "badge": "❓ Tebak Benda: Kursi Belajar",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"You sit on me at your school desk while studying. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "chair",
            "a chair"
        ],
        "primary_answer": "chair"
    },
    {
        "id": "chg_beg_61",
        "badge": "❓ Tebak Benda: Kaus Kaki",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"You wear me over your feet before slipping into your shoes. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "socks",
            "sock"
        ],
        "primary_answer": "socks"
    },
    {
        "id": "chg_beg_62",
        "badge": "❓ Tebak Benda: Payung Hujan",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"You open me above your head to keep dry when raindrops fall. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "umbrella",
            "an umbrella"
        ],
        "primary_answer": "umbrella"
    },
    {
        "id": "chg_beg_63",
        "badge": "❓ Tebak Hewan: Anjing Setia",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have four paws, a wagging tail, and bark happily when greeting you. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "dog",
            "a dog"
        ],
        "primary_answer": "dog"
    },
    {
        "id": "chg_beg_64",
        "badge": "❓ Tebak Hewan: Burung Bersayap",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have feathers, two wings, a beak, and lay eggs in a treetop nest. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "bird",
            "a bird"
        ],
        "primary_answer": "bird"
    },
    {
        "id": "chg_beg_65",
        "badge": "❓ Tebak Benda: Es Krim",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I am a sweet, cold dessert that melts on sunny days. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "ice cream",
            "an ice cream"
        ],
        "primary_answer": "ice cream"
    },
    {
        "id": "chg_beg_66",
        "badge": "❓ Tebak Bagian Tubuh: Gigi",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"You brush me every morning and evening with toothpaste to keep me white. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "teeth",
            "tooth"
        ],
        "primary_answer": "teeth"
    },
    {
        "id": "chg_beg_67",
        "badge": "❓ Tebak Benda: Pohon Berdaun",
        "prompt": "❓ <b>Riddle Ringan:</b>\n\n\"I have brown bark, strong roots in the soil, and green leaves dancing in the wind. What am I?\"\n\n👉 <b>Tebak jawaban bahasa Inggrisnya:</b>",
        "expected": [
            "tree",
            "a tree"
        ],
        "primary_answer": "tree"
    }
],
    config.LEVEL_INTERMEDIATE: [
    {
        "id": "chg_int_01",
        "badge": "🧩 Susun Kalimat Sedang: Sarah reads a book",
        "prompt": "📖 <b>Sentence Unscramble:</b>\n\nSusun kata-kata ini menjadi kalimat yang tepat:\n<b>[ every / Sarah / reads / book / a / morning ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "sarah reads a book every morning",
            "sarah reads a book every morning."
        ],
        "primary_answer": "Sarah reads a book every morning"
    },
    {
        "id": "chg_int_02",
        "badge": "🧩 Susun Kalimat Sedang: We went to the beach",
        "prompt": "🏖️ <b>Sentence Unscramble:</b>\n\nSusun kata-kata lampau ini menjadi kalimat yang benar:\n<b>[ yesterday / to / We / beach / the / went ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "we went to the beach yesterday",
            "we went to the beach yesterday."
        ],
        "primary_answer": "We went to the beach yesterday"
    },
    {
        "id": "chg_int_03",
        "badge": "🧩 Susun Kalimat Sedang: My brother plays the guitar",
        "prompt": "🎸 <b>Sentence Unscramble:</b>\n\nSusun kata-kata ini menjadi kalimat yang benar:\n<b>[ brother / My / guitar / the / plays / well ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "my brother plays the guitar well",
            "my brother plays the guitar well."
        ],
        "primary_answer": "My brother plays the guitar well"
    },
    {
        "id": "chg_int_04",
        "badge": "🧩 Susun Kalimat Sedang: Mom is cooking soup",
        "prompt": "🍲 <b>Sentence Unscramble:</b>\n\nSusun kata-kata present continuous ini:\n<b>[ cooking / My / mother / delicious / soup / is ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "my mother is cooking delicious soup",
            "my mother is cooking delicious soup."
        ],
        "primary_answer": "My mother is cooking delicious soup"
    },
    {
        "id": "chg_int_05",
        "badge": "🧩 Susun Kalimat Sedang: We love to study English",
        "prompt": "📚 <b>Sentence Unscramble:</b>\n\nSusun kata-kata ini menjadi kalimat yang benar:\n<b>[ love / We / together / study / English / to ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "we love to study english together",
            "we love to study english together."
        ],
        "primary_answer": "We love to study English together"
    },
    {
        "id": "chg_int_06",
        "badge": "🧩 Susun Kalimat Sedang: He bought new shoes",
        "prompt": "👟 <b>Sentence Unscramble:</b>\n\nSusun kata-kata lampau ini:\n<b>[ new / bought / yesterday / shoes / He ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "he bought new shoes yesterday",
            "he bought new shoes yesterday."
        ],
        "primary_answer": "He bought new shoes yesterday"
    },
    {
        "id": "chg_int_07",
        "badge": "🧩 Susun Kalimat Sedang: They ran around the park",
        "prompt": "🏃 <b>Sentence Unscramble:</b>\n\nSusun kata-kata ini menjadi kalimat yang rapi:\n<b>[ park / the / around / ran / They ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "they ran around the park",
            "they ran around the park."
        ],
        "primary_answer": "They ran around the park"
    },
    {
        "id": "chg_int_08",
        "badge": "🧩 Susun Kalimat Sedang: She speaks three languages",
        "prompt": "🗣️ <b>Sentence Unscramble:</b>\n\nSusun kata-kata ini menjadi kalimat yang tepat:\n<b>[ languages / fluently / speaks / three / She ]</b>\n\n👉 <b>Tulis kalimat lengkapnya:</b>",
        "expected": [
            "she speaks three languages fluently",
            "she speaks three languages fluently."
        ],
        "primary_answer": "She speaks three languages fluently"
    },
    {
        "id": "chg_int_09",
        "badge": "↔️ Antonim: Lawan kata Difficult",
        "prompt": "💡 <b>Kuis Antonim:</b>\n\nApa lawan kata dari <b>difficult</b> (sulit)?\n<i>(Petunjuk: 4 huruf, berawalan E)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "easy",
            "it is easy"
        ],
        "primary_answer": "easy"
    },
    {
        "id": "chg_int_10",
        "badge": "↔️ Antonim: Lawan kata Safe",
        "prompt": "⚠️ <b>Kuis Antonim:</b>\n\nApa lawan kata dari <b>safe</b> (aman)?\n<i>(Petunjuk: berawalan huruf D)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "dangerous"
        ],
        "primary_answer": "dangerous"
    },
    {
        "id": "chg_int_11",
        "badge": "🔄 Sinonim: Persamaan kata Intelligent",
        "prompt": "🧠 <b>Kuis Sinonim:</b>\n\nApa sinonim dari kata <b>intelligent</b> (cerdas)?\n<i>(Petunjuk: 5 huruf, berawalan S)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "smart",
            "clever"
        ],
        "primary_answer": "smart"
    },
    {
        "id": "chg_int_12",
        "badge": "↔️ Antonim: Lawan kata Noisy",
        "prompt": "🤫 <b>Kuis Antonim:</b>\n\nApa lawan kata dari <b>noisy</b> (bising/gaduh)?\n<i>(Petunjuk: 5 huruf, berawalan Q)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "quiet",
            "silent"
        ],
        "primary_answer": "quiet"
    },
    {
        "id": "chg_int_13",
        "badge": "🔄 Sinonim: Persamaan kata Begin",
        "prompt": "🏁 <b>Kuis Sinonim:</b>\n\nApa sinonim dari kata <b>begin</b> (memulai)?\n<i>(Petunjuk: 5 huruf, berawalan S)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "start"
        ],
        "primary_answer": "start"
    },
    {
        "id": "chg_int_14",
        "badge": "↔️ Antonim: Lawan kata Cheap",
        "prompt": "💎 <b>Kuis Antonim:</b>\n\nApa lawan kata dari <b>cheap</b> (murah)?\n<i>(Petunjuk: berawalan huruf E)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "expensive"
        ],
        "primary_answer": "expensive"
    },
    {
        "id": "chg_int_15",
        "badge": "🔄 Sinonim: Persamaan kata Huge",
        "prompt": "🐘 <b>Kuis Sinonim:</b>\n\nApa sinonim dari <b>huge</b> (sangat besar)?\n<i>(Petunjuk: 5 huruf, berawalan L)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "large",
            "giant",
            "enormous"
        ],
        "primary_answer": "large"
    },
    {
        "id": "chg_int_16",
        "badge": "↔️ Antonim: Lawan kata Polite",
        "prompt": "😠 <b>Kuis Antonim:</b>\n\nApa lawan kata dari <b>polite</b> (sopan)?\n<i>(Petunjuk: 4 huruf, berawalan R)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "rude",
            "impolite"
        ],
        "primary_answer": "rude"
    },
    {
        "id": "chg_int_17",
        "badge": "🕵️ Teka-Teki Logika: Kegelapan",
        "prompt": "🌑 <b>Riddle Menarik:</b>\n\n\"The more of me there is, the less you can see. What am I?\"\n<i>(Petunjuk: berawalan huruf D)</i>\n\n👉 <b>Tulis jawabannya:</b>",
        "expected": [
            "darkness",
            "dark"
        ],
        "primary_answer": "darkness"
    },
    {
        "id": "chg_int_18",
        "badge": "🕵️ Teka-Teki Logika: Sisir Rambut",
        "prompt": "💈 <b>Riddle Menarik:</b>\n\n\"I have many teeth, but I cannot eat or bite anything. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "comb",
            "a comb"
        ],
        "primary_answer": "comb"
    },
    {
        "id": "chg_int_19",
        "badge": "🕵️ Teka-Teki Logika: Botol Minum",
        "prompt": "🍾 <b>Riddle Menarik:</b>\n\n\"I have a long neck, but I have no head. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "bottle",
            "a bottle"
        ],
        "primary_answer": "bottle"
    },
    {
        "id": "chg_int_20",
        "badge": "🕵️ Teka-Teki Logika: Handuk Mandi",
        "prompt": "🚿 <b>Riddle Menarik:</b>\n\n\"What gets wetter the more it dries your body?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "towel",
            "a towel"
        ],
        "primary_answer": "towel"
    },
    {
        "id": "chg_int_21",
        "badge": "🕵️ Teka-Teki Logika: Jarum Jam",
        "prompt": "⌚ <b>Riddle Menarik:</b>\n\n\"What has two hands and a face, but cannot clap or smile?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "clock",
            "a clock",
            "watch"
        ],
        "primary_answer": "clock"
    },
    {
        "id": "chg_int_22",
        "badge": "🕵️ Teka-Teki Logika: Perangko Surat",
        "prompt": "✉️ <b>Riddle Menarik:</b>\n\n\"What can travel all around the world while remaining firmly in a corner?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "stamp",
            "a stamp",
            "postage stamp"
        ],
        "primary_answer": "stamp"
    },
    {
        "id": "chg_int_23",
        "badge": "🕵️ Teka-Teki Logika: Papan Ketik Komputer",
        "prompt": "⌨️ <b>Riddle Menarik:</b>\n\n\"I have keys with no locks, and space with no room. You can enter, but cannot go outside. What am I?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "keyboard",
            "a keyboard"
        ],
        "primary_answer": "keyboard"
    },
    {
        "id": "chg_int_24",
        "badge": "🕵️ Teka-Teki Logika: Teko Teh",
        "prompt": "🫖 <b>Riddle Menarik:</b>\n\n\"What begins with 'T', ends with 'T', and is filled with 'T' (tea)?\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "teapot",
            "a teapot"
        ],
        "primary_answer": "teapot"
    },
    {
        "id": "chg_int_25",
        "badge": "🧩 Susun Kalimat: We went to the zoo",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ yesterday / went / We / to / zoo / the ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "we went to the zoo yesterday",
            "we went to the zoo yesterday."
        ],
        "primary_answer": "We went to the zoo yesterday"
    },
    {
        "id": "chg_int_26",
        "badge": "🧩 Susun Kalimat: She wrote a long letter",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ a / letter / wrote / She / yesterday / long ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "she wrote a long letter yesterday",
            "she wrote a long letter yesterday."
        ],
        "primary_answer": "She wrote a long letter yesterday"
    },
    {
        "id": "chg_int_27",
        "badge": "🧩 Susun Kalimat: Mother cooked delicious soup",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ delicious / cooked / dinner / Mother / for / soup ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "mother cooked delicious soup for dinner",
            "mother cooked delicious soup for dinner."
        ],
        "primary_answer": "Mother cooked delicious soup for dinner"
    },
    {
        "id": "chg_int_28",
        "badge": "🧩 Susun Kalimat: My brother rides his bicycle",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ brother / My / bicycle / rides / his / school / to ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "my brother rides his bicycle to school",
            "my brother rides his bicycle to school."
        ],
        "primary_answer": "My brother rides his bicycle to school"
    },
    {
        "id": "chg_int_29",
        "badge": "🧩 Susun Kalimat: The park is near my house",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ near / house / my / The / park / is ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "the park is near my house",
            "the park is near my house."
        ],
        "primary_answer": "The park is near my house"
    },
    {
        "id": "chg_int_30",
        "badge": "🧩 Susun Kalimat: We study hard to pass",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ hard / study / We / pass / to / exam / the ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "we study hard to pass the exam",
            "we study hard to pass the exam."
        ],
        "primary_answer": "We study hard to pass the exam"
    },
    {
        "id": "chg_int_31",
        "badge": "🧩 Susun Kalimat: He painted a beautiful drawing",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ painted / drawing / beautiful / a / He / yesterday ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "he painted a beautiful drawing yesterday",
            "he painted a beautiful drawing yesterday."
        ],
        "primary_answer": "He painted a beautiful drawing yesterday"
    },
    {
        "id": "chg_int_32",
        "badge": "🧩 Susun Kalimat: I drink tea with milk",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ milk / with / tea / drink / I / breakfast / for ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "i drink tea with milk for breakfast",
            "i drink tea with milk for breakfast."
        ],
        "primary_answer": "I drink tea with milk for breakfast"
    },
    {
        "id": "chg_int_33",
        "badge": "🧩 Susun Kalimat: They were swimming in the river",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ swimming / were / They / river / the / in ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "they were swimming in the river",
            "they were swimming in the river."
        ],
        "primary_answer": "They were swimming in the river"
    },
    {
        "id": "chg_int_34",
        "badge": "🧩 Susun Kalimat: Don't forget your umbrella",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ umbrella / Don't / bring / to / forget / your ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "don't forget to bring your umbrella",
            "dont forget to bring your umbrella"
        ],
        "primary_answer": "Don't forget to bring your umbrella"
    },
    {
        "id": "chg_int_35",
        "badge": "🧩 Susun Kalimat: The library opens at eight",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ opens / library / The / eight / at / morning / every ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "the library opens every morning at eight",
            "the library opens at eight every morning"
        ],
        "primary_answer": "The library opens every morning at eight"
    },
    {
        "id": "chg_int_36",
        "badge": "🧩 Susun Kalimat: Sister plays the guitar",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\n[ guitar / plays / Sister / afternoon / the / every ]\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "sister plays the guitar every afternoon",
            "sister plays the guitar every afternoon."
        ],
        "primary_answer": "Sister plays the guitar every afternoon"
    },
    {
        "id": "chg_int_37",
        "badge": "↔️ Lawan Kata: Hot",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>hot</b> (panas)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "cold",
            "it is cold"
        ],
        "primary_answer": "cold"
    },
    {
        "id": "chg_int_38",
        "badge": "↔️ Lawan Kata: Tall",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>tall</b> (tinggi)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "short",
            "it is short"
        ],
        "primary_answer": "short"
    },
    {
        "id": "chg_int_39",
        "badge": "↔️ Lawan Kata: Rich",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>rich</b> (kaya)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "poor",
            "it is poor"
        ],
        "primary_answer": "poor"
    },
    {
        "id": "chg_int_40",
        "badge": "↔️ Lawan Kata: Strong",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>strong</b> (kuat)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "weak",
            "it is weak"
        ],
        "primary_answer": "weak"
    },
    {
        "id": "chg_int_41",
        "badge": "↔️ Lawan Kata: Dark",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>dark</b> (gelap)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "light",
            "bright"
        ],
        "primary_answer": "light"
    },
    {
        "id": "chg_int_42",
        "badge": "↔️ Lawan Kata: Clean",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>clean</b> (bersih)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "dirty",
            "it is dirty"
        ],
        "primary_answer": "dirty"
    },
    {
        "id": "chg_int_43",
        "badge": "↔️ Lawan Kata: Fast",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>fast</b> (cepat)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "slow",
            "it is slow"
        ],
        "primary_answer": "slow"
    },
    {
        "id": "chg_int_44",
        "badge": "↔️ Lawan Kata: Happy",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa lawan kata dari <b>happy</b> (gembira)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "sad",
            "unhappy"
        ],
        "primary_answer": "sad"
    },
    {
        "id": "chg_int_45",
        "badge": "🔄 Sinonim: Huge",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>huge</b> (sangat besar)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "big",
            "large",
            "gigantic"
        ],
        "primary_answer": "big"
    },
    {
        "id": "chg_int_46",
        "badge": "🔄 Sinonim: Small",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>small</b> (kecil)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "tiny",
            "little"
        ],
        "primary_answer": "tiny"
    },
    {
        "id": "chg_int_47",
        "badge": "🔄 Sinonim: Smart",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>smart</b> (pintar)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "clever",
            "intelligent"
        ],
        "primary_answer": "clever"
    },
    {
        "id": "chg_int_48",
        "badge": "🔄 Sinonim: Start",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>start</b> (memulai)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "begin",
            "to begin"
        ],
        "primary_answer": "begin"
    },
    {
        "id": "chg_int_49",
        "badge": "🔄 Sinonim: Quick",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>quick</b> (cepat)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "fast",
            "rapid"
        ],
        "primary_answer": "fast"
    },
    {
        "id": "chg_int_50",
        "badge": "🔄 Sinonim: Pretty",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>pretty</b> (cantik)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "beautiful",
            "lovely"
        ],
        "primary_answer": "beautiful"
    },
    {
        "id": "chg_int_51",
        "badge": "🔄 Sinonim: Silent",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>silent</b> (sunyi/tenang)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "quiet",
            "peaceful"
        ],
        "primary_answer": "quiet"
    },
    {
        "id": "chg_int_52",
        "badge": "🔄 Sinonim: Glad",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nApa persamaan kata dari <b>glad</b> (senang hati)?\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "happy",
            "cheerful"
        ],
        "primary_answer": "happy"
    },
    {
        "id": "chg_int_53",
        "badge": "🔍 Kategori: Bukan Buah",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> buah?\n<b>[ Apple / Banana / Carrot / Orange ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "carrot",
            "the carrot"
        ],
        "primary_answer": "carrot"
    },
    {
        "id": "chg_int_54",
        "badge": "🔍 Kategori: Benda Mati",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> makhluk hidup?\n<b>[ Dog / Cat / Fish / Car ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "car",
            "the car"
        ],
        "primary_answer": "car"
    },
    {
        "id": "chg_int_55",
        "badge": "🔍 Kategori: Bukan Warna",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> nama warna?\n<b>[ Red / Blue / Heavy / Green ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "heavy"
        ],
        "primary_answer": "heavy"
    },
    {
        "id": "chg_int_56",
        "badge": "🔍 Kategori: Bukan Profesi",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> profesi manusia?\n<b>[ Doctor / Teacher / Pencil / Pilot ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "pencil",
            "the pencil"
        ],
        "primary_answer": "pencil"
    },
    {
        "id": "chg_int_57",
        "badge": "🔍 Kategori: Nama Bulan",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang merupakan nama <b>bulan</b>?\n<b>[ Monday / Friday / April / Sunday ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "april"
        ],
        "primary_answer": "April"
    },
    {
        "id": "chg_int_58",
        "badge": "🔍 Kategori: Bukan Perabot",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> perabot rumah?\n<b>[ Table / Chair / Sofa / Shirt ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "shirt",
            "the shirt"
        ],
        "primary_answer": "shirt"
    },
    {
        "id": "chg_int_59",
        "badge": "🔍 Kategori: Makanan Padat",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang merupakan makanan padat?\n<b>[ Milk / Water / Bread / Juice ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "bread"
        ],
        "primary_answer": "bread"
    },
    {
        "id": "chg_int_60",
        "badge": "🔍 Kategori: Bukan Anggota Tubuh",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> bagian tubuh?\n<b>[ Eye / Ear / Book / Nose ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "book",
            "the book"
        ],
        "primary_answer": "book"
    },
    {
        "id": "chg_int_61",
        "badge": "🔍 Kategori: Bukan Musim",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> nama musim?\n<b>[ Summer / Winter / Morning / Spring ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "morning"
        ],
        "primary_answer": "morning"
    },
    {
        "id": "chg_int_62",
        "badge": "🔍 Kategori: Bukan Kata Kerja",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> kata kerja aktivitas?\n<b>[ Running / Swimming / Mountain / Reading ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "mountain"
        ],
        "primary_answer": "mountain"
    },
    {
        "id": "chg_int_63",
        "badge": "🔍 Kategori: Hewan Herbivora",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari hewan berikut, mana yang pemakan rumput (herbivora)?\n<b>[ Lion / Tiger / Sheep / Leopard ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "sheep"
        ],
        "primary_answer": "sheep"
    },
    {
        "id": "chg_int_64",
        "badge": "🔍 Kategori: Bukan Alat Musik",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> alat musik?\n<b>[ Violin / Piano / Television / Drum ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "television",
            "tv"
        ],
        "primary_answer": "television"
    },
    {
        "id": "chg_int_65",
        "badge": "🔍 Kategori: Bukan Bahasa",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> pelajaran bahasa?\n<b>[ English / Indonesian / Science / Arabic ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "science"
        ],
        "primary_answer": "science"
    },
    {
        "id": "chg_int_66",
        "badge": "🔍 Kategori: Kendaraan Udara",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kendaraan berikut, mana yang terbang di udara?\n<b>[ Bus / Train / Helicopter / Boat ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "helicopter"
        ],
        "primary_answer": "helicopter"
    },
    {
        "id": "chg_int_67",
        "badge": "🔍 Kategori: Bukan Cuaca",
        "prompt": "💡 <b>Tantangan Menengah:</b>\n\nDari kata berikut, mana yang <b>bukan</b> kondisi cuaca?\n<b>[ Rainy / Sunny / Salty / Cloudy ]</b>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "salty"
        ],
        "primary_answer": "salty"
    }
],
    config.LEVEL_ADVANCED: [
    {
        "id": "chg_adv_01",
        "badge": "🎭 Idiom Bahasa Inggris: Piece of cake",
        "prompt": "🍰 <b>Idiom Populer:</b>\n\nUngkapan untuk sesuatu yang sangat mudah dikerjakan:\n\"That exam was a piece of ___!\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "cake",
            "piece of cake"
        ],
        "primary_answer": "cake"
    },
    {
        "id": "chg_adv_02",
        "badge": "🎭 Idiom Bahasa Inggris: Break a leg",
        "prompt": "🎬 <b>Idiom Populer:</b>\n\nUngkapan untuk mendoakan keberhasilan pertunjukan panggung:\n\"Before entering the auditorium, the director said: 'Break a ___!'\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "leg",
            "break a leg"
        ],
        "primary_answer": "leg"
    },
    {
        "id": "chg_adv_03",
        "badge": "🎭 Idiom Bahasa Inggris: Under the weather",
        "prompt": "🤒 <b>Idiom Populer:</b>\n\nUngkapan saat sedang merasa kurang enak badan atau sakit ringan:\n\"I will stay home today because I feel under the ___.\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "weather",
            "under the weather"
        ],
        "primary_answer": "weather"
    },
    {
        "id": "chg_adv_04",
        "badge": "🎭 Idiom Bahasa Inggris: Cost an arm and a leg",
        "prompt": "💸 <b>Idiom Populer:</b>\n\nUngkapan untuk barang yang harganya selangit (sangat mahal):\n\"Buying that sports car would cost an arm and a ___.\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "leg"
        ],
        "primary_answer": "leg"
    },
    {
        "id": "chg_adv_05",
        "badge": "🎭 Idiom Bahasa Inggris: Bite the bullet",
        "prompt": "🎯 <b>Idiom Populer:</b>\n\nMenghadapi situasi yang sulit atau menyakitkan dengan penuh keberanian:\n\"You have been avoiding that dentist visit; it is time to bite the ___.\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "bullet"
        ],
        "primary_answer": "bullet"
    },
    {
        "id": "chg_adv_06",
        "badge": "🎭 Idiom Bahasa Inggris: Spill the beans",
        "prompt": "🫘 <b>Idiom Populer:</b>\n\nMembocorkan rahasia atau kejutan yang belum seharusnya diketahui:\n\"Don't tell Alex about the surprise party; he might spill the ___!\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "beans",
            "bean"
        ],
        "primary_answer": "beans"
    },
    {
        "id": "chg_adv_07",
        "badge": "🎭 Idiom Bahasa Inggris: See eye to eye",
        "prompt": "🤝 <b>Idiom Populer:</b>\n\nSepakat atau sependapat secara penuh dengan orang lain:\n\"We rarely see eye to ___ on politics, but we remain great friends.\"\n\n👉 <b>Lengkapi kata yang hilang:</b>",
        "expected": [
            "eye",
            "see eye to eye"
        ],
        "primary_answer": "eye"
    },
    {
        "id": "chg_adv_08",
        "badge": "🎭 Idiom Bahasa Inggris: Once in a blue moon",
        "prompt": "🌕 <b>Idiom Populer:</b>\n\nSesuatu peristiwa yang sangat langka terjadi:\n\"He only treats us to a restaurant once in a ___ moon.\"\n\n👉 <b>Lengkapi warna yang hilang:</b>",
        "expected": [
            "blue",
            "once in a blue moon"
        ],
        "primary_answer": "blue"
    },
    {
        "id": "chg_adv_09",
        "badge": "🏢 Profesi: Perancang Bangunan",
        "prompt": "📐 <b>Kosakata Profesi Tingkat Lanjut:</b>\n\n\"A licensed professional who designs buildings and oversees their construction is an ___.\"\n<i>(Petunjuk: berawalan huruf A)</i>\n\n👉 <b>Tulis nama profesinya:</b>",
        "expected": [
            "architect",
            "an architect"
        ],
        "primary_answer": "architect"
    },
    {
        "id": "chg_adv_10",
        "badge": "🔭 Profesi: Peneliti Antariksa",
        "prompt": "🌌 <b>Kosakata Profesi Tingkat Lanjut:</b>\n\n\"A scientist who studies celestial bodies, stars, planets, and galaxies is an ___.\"\n<i>(Petunjuk: berawalan huruf A)</i>\n\n👉 <b>Tulis nama profesinya:</b>",
        "expected": [
            "astronomer",
            "an astronomer"
        ],
        "primary_answer": "astronomer"
    },
    {
        "id": "chg_adv_11",
        "badge": "🕊️ Diplomasi: Perjanjian Damai",
        "prompt": "📜 <b>Hubungan Internasional:</b>\n\n\"A formal written agreement between sovereign nations to end conflict is a peace ___.\"\n<i>(Petunjuk: 6 huruf, berawalan T)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "treaty",
            "treaties",
            "accord"
        ],
        "primary_answer": "treaty"
    },
    {
        "id": "chg_adv_12",
        "badge": "📖 Literasi: Kamus Kata",
        "prompt": "📚 <b>Referensi Bahasa:</b>\n\n\"A comprehensive reference book containing words arranged alphabetically with meanings and pronunciations is a ___.\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "dictionary",
            "a dictionary"
        ],
        "primary_answer": "dictionary"
    },
    {
        "id": "chg_adv_13",
        "badge": "❤️ Psikologi: Kemampuan Empati",
        "prompt": "🫂 <b>Kecerdasan Emosional:</b>\n\n\"The psychological capacity to understand and intimately feel what another person is experiencing is called ___.\"\n<i>(Petunjuk: berawalan E)</i>\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "empathy"
        ],
        "primary_answer": "empathy"
    },
    {
        "id": "chg_adv_14",
        "badge": "🛂 Dokumen Perjalanan: Paspor",
        "prompt": "✈️ <b>Dokumen Internasional:</b>\n\n\"An official government travel document certifying citizenship used when crossing foreign borders is a ___.\"\n\n👉 <b>Tulis kata bahasa Inggrisnya:</b>",
        "expected": [
            "passport",
            "a passport"
        ],
        "primary_answer": "passport"
    },
    {
        "id": "chg_adv_15",
        "badge": "🗣️ Bahasa: Penerjemah Lisan",
        "prompt": "🎧 <b>Komunikasi Multibahasa:</b>\n\n\"A person who translates spoken speech in real-time between international dignitaries is an ___.\"\n<i>(Petunjuk: berawalan I)</i>\n\n👉 <b>Tulis nama profesinya:</b>",
        "expected": [
            "interpreter",
            "an interpreter"
        ],
        "primary_answer": "interpreter"
    },
    {
        "id": "chg_adv_16",
        "badge": "💊 Farmakologi: Obat Antibiotik",
        "prompt": "🧪 <b>Dunia Kedokteran:</b>\n\n\"A pharmacological substance that inhibits the growth of or destroys harmful bacteria is an ___.\"\n<i>(Petunjuk: berawalan A)</i>\n\n👉 <b>Tulis istilah medisnya:</b>",
        "expected": [
            "antibiotic",
            "an antibiotic"
        ],
        "primary_answer": "antibiotic"
    },
    {
        "id": "chg_adv_17",
        "badge": "🔄 Transformasi Pasif: Written",
        "prompt": "📜 <b>Sentence Transformation: Aktif ke Pasif</b>\n\nAktif: <i>William Shakespeare wrote Hamlet.</i>\nPasif: <i>Hamlet was ___ by William Shakespeare.</i>\n\n👉 <b>Tulis bentuk V3 dari kata 'write':</b>",
        "expected": [
            "written",
            "was written"
        ],
        "primary_answer": "written"
    },
    {
        "id": "chg_adv_18",
        "badge": "🔤 Pembentukan Kata: Happy ➔ Kebahagiaan",
        "prompt": "✨ <b>Word Formation (Nominalization):</b>\n\nUbah kata sifat <b>happy</b> menjadi kata benda (kebahagiaan):\n<i>(Petunjuk: akhiran -ness)</i>\n\n👉 <b>Tulis kata bendanya:</b>",
        "expected": [
            "happiness"
        ],
        "primary_answer": "happiness"
    },
    {
        "id": "chg_adv_19",
        "badge": "🔤 Pembentukan Kata: Decide ➔ Keputusan",
        "prompt": "🎯 <b>Word Formation (Nominalization):</b>\n\nUbah kata kerja <b>decide</b> menjadi kata benda (keputusan):\n<i>(Petunjuk: 8 huruf, berakhiran -sion)</i>\n\n👉 <b>Tulis kata bendanya:</b>",
        "expected": [
            "decision",
            "a decision"
        ],
        "primary_answer": "decision"
    },
    {
        "id": "chg_adv_20",
        "badge": "🔤 Pembentukan Kata: Quick ➔ Adverb",
        "prompt": "⚡ <b>Word Formation: Adjective to Adverb</b>\n\nUbah kata sifat <b>quick</b> (cepat) menjadi kata keterangan cara (dengan cepat):\n<i>(Petunjuk: tambahkan akhiran -ly)</i>\n\n👉 <b>Tulis kata keterangannya:</b>",
        "expected": [
            "quickly"
        ],
        "primary_answer": "quickly"
    },
    {
        "id": "chg_adv_21",
        "badge": "🔤 Prefiks Negatif: Possible ➔ Mustahil",
        "prompt": "🚫 <b>Negative Prefix:</b>\n\nTambahkan awalan pada kata <b>possible</b> (mungkin) agar bermakna 'mustahil / tidak mungkin':\n\n👉 <b>Tulis kata lengkapnya:</b>",
        "expected": [
            "impossible"
        ],
        "primary_answer": "impossible"
    },
    {
        "id": "chg_adv_22",
        "badge": "🔤 Prefiks Negatif: Agree ➔ Tidak Setuju",
        "prompt": "❌ <b>Negative Prefix:</b>\n\nTambahkan awalan pada kata <b>agree</b> (setuju) agar bermakna 'tidak setuju':\n\n👉 <b>Tulis kata lengkapnya:</b>",
        "expected": [
            "disagree"
        ],
        "primary_answer": "disagree"
    },
    {
        "id": "chg_adv_23",
        "badge": "🧩 Permainan Huruf: Ice to Rice",
        "prompt": "🍚 <b>Word Play Challenge:</b>\n\nKata untuk 'air beku' adalah <b>ICE</b>.\nTambahkan satu huruf di depannya untuk menghasilkan kata yang berarti 'butir beras/nasi':\n\n👉 <b>Tulis kata baru tersebut:</b>",
        "expected": [
            "rice"
        ],
        "primary_answer": "rice"
    },
    {
        "id": "chg_adv_24",
        "badge": "📜 Peribahasa Bijak: Louder than words",
        "prompt": "🗣️ <b>Famous Proverb:</b>\n\nLengkapi peribahasa terkenal tentang perbuatan nyata:\n\"Actions speak louder than ___.\"\n\n👉 <b>Tulis kata yang hilang:</b>",
        "expected": [
            "words",
            "word"
        ],
        "primary_answer": "words"
    },
    {
        "id": "chg_adv_25",
        "badge": "🎭 Idiom: Burn the midnight oil",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan untuk belajar atau bekerja keras hingga larut malam:\n\"He burned the midnight ___ preparing for the bar exam.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "oil",
            "burn the midnight oil"
        ],
        "primary_answer": "oil"
    },
    {
        "id": "chg_adv_26",
        "badge": "🎭 Idiom: Hit the sack",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan santai untuk pergi tidur di malam hari:\n\"I am exhausted after that marathon; it is time to hit the ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "sack",
            "hit the sack"
        ],
        "primary_answer": "sack"
    },
    {
        "id": "chg_adv_27",
        "badge": "🎭 Idiom: Let the cat out of the bag",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan membocorkan rahasia yang tadinya tertutup rapat:\n\"Don't let the cat out of the ___ about the surprise reunion!\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "bag"
        ],
        "primary_answer": "bag"
    },
    {
        "id": "chg_adv_28",
        "badge": "🎭 Idiom: Beat around the bush",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan untuk berbicara berbelit-belit tanpa langsung ke inti persoalan:\n\"Stop beating around the ___ and tell us what really happened.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "bush"
        ],
        "primary_answer": "bush"
    },
    {
        "id": "chg_adv_29",
        "badge": "🎭 Idiom: Through thick and thin",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan untuk setia menemani dalam suka maupun duka:\n\"True friends stay by your side through thick and ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "thin"
        ],
        "primary_answer": "thin"
    },
    {
        "id": "chg_adv_30",
        "badge": "🎭 Idiom: Every cloud has a silver lining",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nPeribahasa bahwa di setiap musibah selalu ada hikmah kebaikan:\n\"Don't lose hope after that loss; every cloud has a silver ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "lining"
        ],
        "primary_answer": "lining"
    },
    {
        "id": "chg_adv_31",
        "badge": "🎭 Idiom: The ball is in your court",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan bahwa giliran mengambil keputusan kini berada di tanganmu:\n\"I have made my offer; now the ball is in your ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "court"
        ],
        "primary_answer": "court"
    },
    {
        "id": "chg_adv_32",
        "badge": "🎭 Idiom: Cry over spilled milk",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan jangan membuang energi menyesali hal yang sudah terlanjur terjadi:\n\"There is no use crying over spilled ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "milk"
        ],
        "primary_answer": "milk"
    },
    {
        "id": "chg_adv_33",
        "badge": "🎭 Idiom: Better late than never",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nPeribahasa bahwa lebih baik terlambat menyelesaikan sesuatu daripada tidak sama sekali:\n\"He finally submitted his graduation thesis; better late than ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "never"
        ],
        "primary_answer": "never"
    },
    {
        "id": "chg_adv_34",
        "badge": "🎭 Idiom: A blessing in disguise",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan untuk peristiwa buruk yang ternyata membawa berkah tersembunyi:\n\"Losing that flight turned out to be a blessing in ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "disguise"
        ],
        "primary_answer": "disguise"
    },
    {
        "id": "chg_adv_35",
        "badge": "🎭 Idiom: Break the ice",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan mencairkan suasana canggung saat pertama kali berkenalan:\n\"The host told a funny joke to break the ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "ice"
        ],
        "primary_answer": "ice"
    },
    {
        "id": "chg_adv_36",
        "badge": "🎭 Idiom: Give the cold shoulder",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan mendiamkan atau bersikap dingin kepada seseorang:\n\"After the argument, he gave his rival the cold ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "shoulder"
        ],
        "primary_answer": "shoulder"
    },
    {
        "id": "chg_adv_37",
        "badge": "🎭 Idiom: Judge a book by its cover",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nNasihat bijak jangan menilai seseorang hanya dari penampilan fisiknya:\n\"Always be kind; never judge a book by its ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "cover"
        ],
        "primary_answer": "cover"
    },
    {
        "id": "chg_adv_38",
        "badge": "🎭 Idiom: Kill two birds with one stone",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nPeribahasa menyelesaikan dua hal sekaligus dalam satu tindakan:\n\"Cycling to school helps me exercise and save money, killing two birds with one ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "stone"
        ],
        "primary_answer": "stone"
    },
    {
        "id": "chg_adv_39",
        "badge": "🎭 Idiom: When pigs fly",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUngkapan untuk sesuatu yang mustahil dan tak akan pernah terjadi:\n\"He will admit his error when pigs ___!\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "fly"
        ],
        "primary_answer": "fly"
    },
    {
        "id": "chg_adv_40",
        "badge": "🔤 Pembentukan Kata: Educate ➔ Pendidikan",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata kerja <b>educate</b> menjadi kata benda (pendidikan):\n<i>(Petunjuk: berakhiran -tion)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "education"
        ],
        "primary_answer": "education"
    },
    {
        "id": "chg_adv_41",
        "badge": "🔤 Pembentukan Kata: Create ➔ Ciptaan",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata kerja <b>create</b> menjadi kata benda (ciptaan/kreasi):\n<i>(Petunjuk: berakhiran -tion)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "creation"
        ],
        "primary_answer": "creation"
    },
    {
        "id": "chg_adv_42",
        "badge": "🔤 Pembentukan Kata: Inspire ➔ Inspirasi",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata kerja <b>inspire</b> menjadi kata benda (inspirasi):\n<i>(Petunjuk: berakhiran -tion)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "inspiration"
        ],
        "primary_answer": "inspiration"
    },
    {
        "id": "chg_adv_43",
        "badge": "🔤 Pembentukan Kata: Honest ➔ Kejujuran",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>honest</b> menjadi kata benda (kejujuran):\n<i>(Petunjuk: berakhiran -y)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "honesty"
        ],
        "primary_answer": "honesty"
    },
    {
        "id": "chg_adv_44",
        "badge": "🔤 Pembentukan Kata: Brave ➔ Keberanian",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>brave</b> menjadi kata benda (keberanian):\n<i>(Petunjuk: berakhiran -ry)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "bravery"
        ],
        "primary_answer": "bravery"
    },
    {
        "id": "chg_adv_45",
        "badge": "🔤 Pembentukan Kata: Strong ➔ Kekuatan",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>strong</b> menjadi kata benda (kekuatan):\n<i>(Petunjuk: berakhiran -th)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "strength"
        ],
        "primary_answer": "strength"
    },
    {
        "id": "chg_adv_46",
        "badge": "🔤 Pembentukan Kata: Wide ➔ Lebar",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>wide</b> menjadi kata benda (lebar):\n<i>(Petunjuk: berakhiran -th)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "width"
        ],
        "primary_answer": "width"
    },
    {
        "id": "chg_adv_47",
        "badge": "🔤 Pembentukan Kata: Deep ➔ Kedalaman",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>deep</b> menjadi kata benda (kedalaman):\n<i>(Petunjuk: berakhiran -th)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "depth"
        ],
        "primary_answer": "depth"
    },
    {
        "id": "chg_adv_48",
        "badge": "🔤 Pembentukan Kata: Careful ➔ Adverb",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>careful</b> menjadi kata keterangan cara (dengan hati-hati):\n<i>(Petunjuk: tambahkan -ly)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "carefully"
        ],
        "primary_answer": "carefully"
    },
    {
        "id": "chg_adv_49",
        "badge": "🔤 Pembentukan Kata: Beautiful ➔ Adverb",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>beautiful</b> menjadi kata keterangan cara (dengan indah):\n<i>(Petunjuk: tambahkan -ly)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "beautifully"
        ],
        "primary_answer": "beautifully"
    },
    {
        "id": "chg_adv_50",
        "badge": "🔤 Pembentukan Kata: Clear ➔ Adverb",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nUbah kata sifat <b>clear</b> menjadi kata keterangan cara (dengan jelas):\n<i>(Petunjuk: tambahkan -ly)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "clearly"
        ],
        "primary_answer": "clearly"
    },
    {
        "id": "chg_adv_51",
        "badge": "🚫 Prefiks Negatif: Polite ➔ Tidak Sopan",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>polite</b> agar bermakna 'tidak sopan':\n<i>(Petunjuk: awalan im-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "impolite"
        ],
        "primary_answer": "impolite"
    },
    {
        "id": "chg_adv_52",
        "badge": "🚫 Prefiks Negatif: Patient ➔ Tidak Sabar",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>patient</b> agar bermakna 'tidak sabar / tergesa-gesa':\n<i>(Petunjuk: awalan im-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "impatient"
        ],
        "primary_answer": "impatient"
    },
    {
        "id": "chg_adv_53",
        "badge": "🚫 Prefiks Negatif: Legal ➔ Ilegal",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>legal</b> agar bermakna 'ilegal / melawan hukum':\n<i>(Petunjuk: awalan il-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "illegal"
        ],
        "primary_answer": "illegal"
    },
    {
        "id": "chg_adv_54",
        "badge": "🚫 Prefiks Negatif: Responsible ➔ Tidak Bertanggung Jawab",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>responsible</b> agar bermakna 'tidak bertanggung jawab':\n<i>(Petunjuk: awalan ir-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "irresponsible"
        ],
        "primary_answer": "irresponsible"
    },
    {
        "id": "chg_adv_55",
        "badge": "🚫 Prefiks Negatif: Accurate ➔ Tidak Akurat",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>accurate</b> agar bermakna 'tidak akurat / meleset':\n<i>(Petunjuk: awalan in-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "inaccurate"
        ],
        "primary_answer": "inaccurate"
    },
    {
        "id": "chg_adv_56",
        "badge": "🚫 Prefiks Negatif: Mature ➔ Belum Dewasa",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>mature</b> agar bermakna 'kekanak-kanakan / belum matang':\n<i>(Petunjuk: awalan im-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "immature"
        ],
        "primary_answer": "immature"
    },
    {
        "id": "chg_adv_57",
        "badge": "🚫 Prefiks Negatif: Understand ➔ Salah Paham",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>understand</b> agar bermakna 'salah paham':\n<i>(Petunjuk: awalan mis-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "misunderstand"
        ],
        "primary_answer": "misunderstand"
    },
    {
        "id": "chg_adv_58",
        "badge": "🚫 Prefiks Negatif: Honest ➔ Tidak Jujur",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>honest</b> agar bermakna 'tidak jujur / curang':\n<i>(Petunjuk: awalan dis-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "dishonest"
        ],
        "primary_answer": "dishonest"
    },
    {
        "id": "chg_adv_59",
        "badge": "🚫 Prefiks Negatif: Formal ➔ Santai",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>formal</b> agar bermakna 'informal / santai':\n<i>(Petunjuk: awalan in-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "informal"
        ],
        "primary_answer": "informal"
    },
    {
        "id": "chg_adv_60",
        "badge": "🚫 Prefiks Negatif: Correct ➔ Salah",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nTambahkan awalan pada <b>correct</b> agar bermakna 'tidak tepat / keliru':\n<i>(Petunjuk: awalan in-)</i>\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "incorrect"
        ],
        "primary_answer": "incorrect"
    },
    {
        "id": "chg_adv_61",
        "badge": "📜 Peribahasa: Practice makes perfect",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nLengkapi peribahasa terkenal tentang pentingnya latihan tekun:\n\"Practice makes ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "perfect"
        ],
        "primary_answer": "perfect"
    },
    {
        "id": "chg_adv_62",
        "badge": "📜 Peribahasa: Time is money",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nLengkapi peribahasa tentang berharganya waktu:\n\"Time is ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "money"
        ],
        "primary_answer": "money"
    },
    {
        "id": "chg_adv_63",
        "badge": "📜 Peribahasa: Knowledge is power",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nLengkapi semboyan agung tentang kekuatan ilmu pengetahuan:\n\"Knowledge is ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "power"
        ],
        "primary_answer": "power"
    },
    {
        "id": "chg_adv_64",
        "badge": "📜 Peribahasa: Where there is a will",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nLengkapi peribahasa tentang tekad yang kuat:\n\"Where there is a will, there is a ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "way"
        ],
        "primary_answer": "way"
    },
    {
        "id": "chg_adv_65",
        "badge": "📜 Peribahasa: Honesty is the best policy",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nLengkapi peribahasa moral tentang kejujuran:\n\"Honesty is the best ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "policy"
        ],
        "primary_answer": "policy"
    },
    {
        "id": "chg_adv_66",
        "badge": "📜 Peribahasa: Look before you leap",
        "prompt": "🏆 <b>Tantangan Mahir & Idiom:</b>\n\nLengkapi peribahasa tentang pertimbangan matang sebelum bertindak:\n\"Look before you ___.\"\n\n👉 <b>Tulis jawaban yang benar:</b>",
        "expected": [
            "leap"
        ],
        "primary_answer": "leap"
    }
],
}
