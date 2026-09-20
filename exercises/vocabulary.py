"""
Curated Vocabulary exercises for English Buddy Bot.
Total: 200 exercises (67 Beginner, 67 Intermediate, 66 Advanced).
"""
from typing import Any, Dict, List
import config

VOCABULARY_EXERCISES: Dict[str, List[Dict[str, Any]]] = {
    config.LEVEL_BEGINNER: [
    {
        "id": "voc_beg_01",
        "badge": "📚 Anggota Tubuh: Head",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Head</b> = Kepala\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kepala':\n<code>Head</code>",
        "expected": [
            "head",
            "head = kepala"
        ],
        "primary_answer": "Head"
    },
    {
        "id": "voc_beg_02",
        "badge": "📚 Anggota Tubuh: Eyes",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Eyes</b> = Mata\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Mata':\n<code>Eyes</code>",
        "expected": [
            "eyes",
            "eye",
            "eyes = mata"
        ],
        "primary_answer": "Eyes"
    },
    {
        "id": "voc_beg_03",
        "badge": "📚 Anggota Tubuh: Nose",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Nose</b> = Hidung\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Hidung':\n<code>Nose</code>",
        "expected": [
            "nose",
            "nose = hidung"
        ],
        "primary_answer": "Nose"
    },
    {
        "id": "voc_beg_04",
        "badge": "📚 Anggota Tubuh: Mouth",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Mouth</b> = Mulut\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Mulut':\n<code>Mouth</code>",
        "expected": [
            "mouth",
            "mouth = mulut"
        ],
        "primary_answer": "Mouth"
    },
    {
        "id": "voc_beg_05",
        "badge": "📚 Anggota Tubuh: Ears",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Ears</b> = Telinga\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Telinga':\n<code>Ears</code>",
        "expected": [
            "ears",
            "ear",
            "ears = telinga"
        ],
        "primary_answer": "Ears"
    },
    {
        "id": "voc_beg_06",
        "badge": "📚 Anggota Tubuh: Hands",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Hands</b> = Tangan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tangan':\n<code>Hands</code>",
        "expected": [
            "hands",
            "hand",
            "hands = tangan"
        ],
        "primary_answer": "Hands"
    },
    {
        "id": "voc_beg_07",
        "badge": "📚 Anggota Tubuh: Feet",
        "prompt": "🌟 <b>Kosakata Anggota Tubuh:</b>\n\n• <b>Feet</b> = Kaki\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kaki':\n<code>Feet</code>",
        "expected": [
            "feet",
            "foot",
            "feet = kaki"
        ],
        "primary_answer": "Feet"
    },
    {
        "id": "voc_beg_08",
        "badge": "📚 Warna Dasar: Red",
        "prompt": "🎨 <b>Kosakata Warna (Colors):</b>\n\n• <b>Red</b> = Merah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk warna 'Merah':\n<code>Red</code>",
        "expected": [
            "red",
            "red = merah"
        ],
        "primary_answer": "Red"
    },
    {
        "id": "voc_beg_09",
        "badge": "📚 Warna Dasar: Blue",
        "prompt": "🎨 <b>Kosakata Warna (Colors):</b>\n\n• <b>Blue</b> = Biru\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk warna 'Biru':\n<code>Blue</code>",
        "expected": [
            "blue",
            "blue = biru"
        ],
        "primary_answer": "Blue"
    },
    {
        "id": "voc_beg_10",
        "badge": "📚 Warna Dasar: Green",
        "prompt": "🎨 <b>Kosakata Warna (Colors):</b>\n\n• <b>Green</b> = Hijau\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk warna 'Hijau':\n<code>Green</code>",
        "expected": [
            "green",
            "green = hijau"
        ],
        "primary_answer": "Green"
    },
    {
        "id": "voc_beg_11",
        "badge": "📚 Warna Dasar: Yellow",
        "prompt": "🎨 <b>Kosakata Warna (Colors):</b>\n\n• <b>Yellow</b> = Kuning\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk warna 'Kuning':\n<code>Yellow</code>",
        "expected": [
            "yellow",
            "yellow = kuning"
        ],
        "primary_answer": "Yellow"
    },
    {
        "id": "voc_beg_12",
        "badge": "📚 Angka: One",
        "prompt": "🔢 <b>Kosakata Angka (Numbers):</b>\n\n• <b>One</b> = Satu (1)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk angka '1':\n<code>One</code>",
        "expected": [
            "one",
            "1",
            "one = satu"
        ],
        "primary_answer": "One"
    },
    {
        "id": "voc_beg_13",
        "badge": "📚 Angka: Two",
        "prompt": "🔢 <b>Kosakata Angka (Numbers):</b>\n\n• <b>Two</b> = Dua (2)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk angka '2':\n<code>Two</code>",
        "expected": [
            "two",
            "2",
            "two = dua"
        ],
        "primary_answer": "Two"
    },
    {
        "id": "voc_beg_14",
        "badge": "📚 Angka: Three",
        "prompt": "🔢 <b>Kosakata Angka (Numbers):</b>\n\n• <b>Three</b> = Tiga (3)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk angka '3':\n<code>Three</code>",
        "expected": [
            "three",
            "3",
            "three = tiga"
        ],
        "primary_answer": "Three"
    },
    {
        "id": "voc_beg_15",
        "badge": "📚 Benda Kelas: Book",
        "prompt": "🎒 <b>Benda di Sekolah (Classroom Objects):</b>\n\n• <b>Book</b> = Buku\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Buku':\n<code>Book</code>",
        "expected": [
            "book",
            "a book",
            "book = buku"
        ],
        "primary_answer": "Book"
    },
    {
        "id": "voc_beg_16",
        "badge": "📚 Benda Kelas: Pencil",
        "prompt": "🎒 <b>Benda di Sekolah (Classroom Objects):</b>\n\n• <b>Pencil</b> = Pensil\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pensil':\n<code>Pencil</code>",
        "expected": [
            "pencil",
            "a pencil",
            "pencil = pensil"
        ],
        "primary_answer": "Pencil"
    },
    {
        "id": "voc_beg_17",
        "badge": "📚 Benda Kelas: Table",
        "prompt": "🎒 <b>Benda di Sekolah (Classroom Objects):</b>\n\n• <b>Table</b> = Meja\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Meja':\n<code>Table</code>",
        "expected": [
            "table",
            "a table",
            "table = meja"
        ],
        "primary_answer": "Table"
    },
    {
        "id": "voc_beg_18",
        "badge": "📚 Benda Kelas: Chair",
        "prompt": "🎒 <b>Benda di Sekolah (Classroom Objects):</b>\n\n• <b>Chair</b> = Kursi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kursi':\n<code>Chair</code>",
        "expected": [
            "chair",
            "a chair",
            "chair = kursi"
        ],
        "primary_answer": "Chair"
    },
    {
        "id": "voc_beg_19",
        "badge": "📚 Hewan Ramah: Cat",
        "prompt": "🐾 <b>Nama Hewan (Animals):</b>\n\n• <b>Cat</b> = Kucing\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kucing':\n<code>Cat</code>",
        "expected": [
            "cat",
            "a cat",
            "cat = kucing"
        ],
        "primary_answer": "Cat"
    },
    {
        "id": "voc_beg_20",
        "badge": "📚 Hewan Ramah: Dog",
        "prompt": "🐾 <b>Nama Hewan (Animals):</b>\n\n• <b>Dog</b> = Anjing\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Anjing':\n<code>Dog</code>",
        "expected": [
            "dog",
            "a dog",
            "dog = anjing"
        ],
        "primary_answer": "Dog"
    },
    {
        "id": "voc_beg_21",
        "badge": "📚 Hewan Ramah: Bird",
        "prompt": "🐾 <b>Nama Hewan (Animals):</b>\n\n• <b>Bird</b> = Burung\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Burung':\n<code>Bird</code>",
        "expected": [
            "bird",
            "a bird",
            "bird = burung"
        ],
        "primary_answer": "Bird"
    },
    {
        "id": "voc_beg_22",
        "badge": "📚 Hewan Ramah: Fish",
        "prompt": "🐾 <b>Nama Hewan (Animals):</b>\n\n• <b>Fish</b> = Ikan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ikan':\n<code>Fish</code>",
        "expected": [
            "fish",
            "a fish",
            "fish = ikan"
        ],
        "primary_answer": "Fish"
    },
    {
        "id": "voc_beg_23",
        "badge": "📚 Keluarga: Mother",
        "prompt": "👨‍👩‍👧 <b>Keluarga Saya (My Family):</b>\n\n• <b>Mother</b> = Ibu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ibu':\n<code>Mother</code>",
        "expected": [
            "mother",
            "mom",
            "mother = ibu"
        ],
        "primary_answer": "Mother"
    },
    {
        "id": "voc_beg_24",
        "badge": "📚 Keluarga: Father",
        "prompt": "👨‍👩‍👧 <b>Keluarga Saya (My Family):</b>\n\n• <b>Father</b> = Ayah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ayah':\n<code>Father</code>",
        "expected": [
            "father",
            "dad",
            "father = ayah"
        ],
        "primary_answer": "Father"
    },
    {
        "id": "voc_beg_25",
        "badge": "📚 🦁 Hewan Hutan: Lion",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Lion</b> = Singa\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Singa':\n<code>Lion</code>",
        "expected": [
            "lion",
            "a lion",
            "lion = singa"
        ],
        "primary_answer": "Lion"
    },
    {
        "id": "voc_beg_26",
        "badge": "📚 🐯 Hewan Belang: Tiger",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Tiger</b> = Harimau\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Harimau':\n<code>Tiger</code>",
        "expected": [
            "tiger",
            "a tiger",
            "tiger = harimau"
        ],
        "primary_answer": "Tiger"
    },
    {
        "id": "voc_beg_27",
        "badge": "📚 🐒 Hewan Lincah: Monkey",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Monkey</b> = Monyet\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Monyet':\n<code>Monkey</code>",
        "expected": [
            "monkey",
            "a monkey",
            "monkey = monyet"
        ],
        "primary_answer": "Monkey"
    },
    {
        "id": "voc_beg_28",
        "badge": "📚 🐄 Hewan Ternak: Cow",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Cow</b> = Sapi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sapi':\n<code>Cow</code>",
        "expected": [
            "cow",
            "a cow",
            "cow = sapi"
        ],
        "primary_answer": "Cow"
    },
    {
        "id": "voc_beg_29",
        "badge": "📚 🦆 Hewan Unggas: Duck",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Duck</b> = Bebek\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bebek':\n<code>Duck</code>",
        "expected": [
            "duck",
            "a duck",
            "duck = bebek"
        ],
        "primary_answer": "Duck"
    },
    {
        "id": "voc_beg_30",
        "badge": "📚 🐇 Hewan Lucu: Rabbit",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Rabbit</b> = Kelinci\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kelinci':\n<code>Rabbit</code>",
        "expected": [
            "rabbit",
            "a rabbit",
            "rabbit = kelinci"
        ],
        "primary_answer": "Rabbit"
    },
    {
        "id": "voc_beg_31",
        "badge": "📚 🐑 Hewan Berbulu: Sheep",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Sheep</b> = Domba\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Domba':\n<code>Sheep</code>",
        "expected": [
            "sheep",
            "a sheep",
            "sheep = domba"
        ],
        "primary_answer": "Sheep"
    },
    {
        "id": "voc_beg_32",
        "badge": "📚 🐴 Hewan Cepat: Horse",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Horse</b> = Kuda\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kuda':\n<code>Horse</code>",
        "expected": [
            "horse",
            "a horse",
            "horse = kuda"
        ],
        "primary_answer": "Horse"
    },
    {
        "id": "voc_beg_33",
        "badge": "📚 🐘 Hewan Belalai: Elephant",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Elephant</b> = Gajah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Gajah':\n<code>Elephant</code>",
        "expected": [
            "elephant",
            "an elephant",
            "elephant = gajah"
        ],
        "primary_answer": "Elephant"
    },
    {
        "id": "voc_beg_34",
        "badge": "📚 🐍 Hewan Melata: Snake",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Snake</b> = Ular\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ular':\n<code>Snake</code>",
        "expected": [
            "snake",
            "a snake",
            "snake = ular"
        ],
        "primary_answer": "Snake"
    },
    {
        "id": "voc_beg_35",
        "badge": "📚 🐭 Hewan Kecil: Mouse",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Mouse</b> = Tikus\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tikus':\n<code>Mouse</code>",
        "expected": [
            "mouse",
            "a mouse",
            "mouse = tikus"
        ],
        "primary_answer": "Mouse"
    },
    {
        "id": "voc_beg_36",
        "badge": "📚 🐸 Hewan Amfibi: Frog",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Frog</b> = Katak\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Katak':\n<code>Frog</code>",
        "expected": [
            "frog",
            "a frog",
            "frog = katak"
        ],
        "primary_answer": "Frog"
    },
    {
        "id": "voc_beg_37",
        "badge": "📚 🐜 Serangga Rajin: Ant",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Ant</b> = Semut\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Semut':\n<code>Ant</code>",
        "expected": [
            "ant",
            "an ant",
            "ant = semut"
        ],
        "primary_answer": "Ant"
    },
    {
        "id": "voc_beg_38",
        "badge": "📚 🐝 Serangga Madu: Bee",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Bee</b> = Lebah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Lebah':\n<code>Bee</code>",
        "expected": [
            "bee",
            "a bee",
            "bee = lebah"
        ],
        "primary_answer": "Bee"
    },
    {
        "id": "voc_beg_39",
        "badge": "📚 🦋 Serangga Sayap Indah: Butterfly",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Butterfly</b> = Kupu-kupu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kupu-kupu':\n<code>Butterfly</code>",
        "expected": [
            "butterfly",
            "a butterfly",
            "butterfly = kupu-kupu"
        ],
        "primary_answer": "Butterfly"
    },
    {
        "id": "voc_beg_40",
        "badge": "📚 🟣 Warna Ungu: Purple",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Purple</b> = Ungu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ungu':\n<code>Purple</code>",
        "expected": [
            "purple",
            "purple = ungu"
        ],
        "primary_answer": "Purple"
    },
    {
        "id": "voc_beg_41",
        "badge": "📚 🌸 Warna Merah Muda: Pink",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Pink</b> = Merah muda\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Merah muda':\n<code>Pink</code>",
        "expected": [
            "pink",
            "pink = merah muda",
            "pink = merah jambu"
        ],
        "primary_answer": "Pink"
    },
    {
        "id": "voc_beg_42",
        "badge": "📚 🟠 Warna Oranye: Orange",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Orange</b> = Oranye\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Oranye':\n<code>Orange</code>",
        "expected": [
            "orange",
            "orange = oranye",
            "orange = jingga"
        ],
        "primary_answer": "Orange"
    },
    {
        "id": "voc_beg_43",
        "badge": "📚 🟤 Warna Cokelat: Brown",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Brown</b> = Cokelat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Cokelat':\n<code>Brown</code>",
        "expected": [
            "brown",
            "brown = cokelat"
        ],
        "primary_answer": "Brown"
    },
    {
        "id": "voc_beg_44",
        "badge": "📚 ⚫ Warna Hitam: Black",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Black</b> = Hitam\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Hitam':\n<code>Black</code>",
        "expected": [
            "black",
            "black = hitam"
        ],
        "primary_answer": "Black"
    },
    {
        "id": "voc_beg_45",
        "badge": "📚 ⚪ Warna Putih: White",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>White</b> = Putih\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Putih':\n<code>White</code>",
        "expected": [
            "white",
            "white = putih"
        ],
        "primary_answer": "White"
    },
    {
        "id": "voc_beg_46",
        "badge": "📚 🔘 Warna Abu-abu: Gray",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Gray</b> = Abu-abu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Abu-abu':\n<code>Gray</code>",
        "expected": [
            "gray",
            "grey",
            "gray = abu-abu",
            "grey = abu-abu"
        ],
        "primary_answer": "Gray"
    },
    {
        "id": "voc_beg_47",
        "badge": "📚 🔢 Angka: Four",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Four</b> = Empat (4)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Empat (4)':\n<code>Four</code>",
        "expected": [
            "four",
            "4",
            "four = empat"
        ],
        "primary_answer": "Four"
    },
    {
        "id": "voc_beg_48",
        "badge": "📚 🔢 Angka: Five",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Five</b> = Lima (5)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Lima (5)':\n<code>Five</code>",
        "expected": [
            "five",
            "5",
            "five = lima"
        ],
        "primary_answer": "Five"
    },
    {
        "id": "voc_beg_49",
        "badge": "📚 🔢 Angka: Six",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Six</b> = Enam (6)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Enam (6)':\n<code>Six</code>",
        "expected": [
            "six",
            "6",
            "six = enam"
        ],
        "primary_answer": "Six"
    },
    {
        "id": "voc_beg_50",
        "badge": "📚 🔢 Angka: Seven",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Seven</b> = Tujuh (7)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tujuh (7)':\n<code>Seven</code>",
        "expected": [
            "seven",
            "7",
            "seven = tujuh"
        ],
        "primary_answer": "Seven"
    },
    {
        "id": "voc_beg_51",
        "badge": "📚 🔢 Angka: Eight",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Eight</b> = Delapan (8)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Delapan (8)':\n<code>Eight</code>",
        "expected": [
            "eight",
            "8",
            "eight = delapan"
        ],
        "primary_answer": "Eight"
    },
    {
        "id": "voc_beg_52",
        "badge": "📚 🔢 Angka: Nine",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Nine</b> = Sembilan (9)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sembilan (9)':\n<code>Nine</code>",
        "expected": [
            "nine",
            "9",
            "nine = sembilan"
        ],
        "primary_answer": "Nine"
    },
    {
        "id": "voc_beg_53",
        "badge": "📚 🔢 Angka: Ten",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Ten</b> = Sepuluh (10)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sepuluh (10)':\n<code>Ten</code>",
        "expected": [
            "ten",
            "10",
            "ten = sepuluh"
        ],
        "primary_answer": "Ten"
    },
    {
        "id": "voc_beg_54",
        "badge": "📚 🖊️ Alat Tulis: Pen",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Pen</b> = Pulpen\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pulpen':\n<code>Pen</code>",
        "expected": [
            "pen",
            "a pen",
            "pen = pulpen"
        ],
        "primary_answer": "Pen"
    },
    {
        "id": "voc_beg_55",
        "badge": "📚 🧼 Alat Tulis: Eraser",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Eraser</b> = Penghapus\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Penghapus':\n<code>Eraser</code>",
        "expected": [
            "eraser",
            "an eraser",
            "eraser = penghapus"
        ],
        "primary_answer": "Eraser"
    },
    {
        "id": "voc_beg_56",
        "badge": "📚 📏 Alat Tulis: Ruler",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Ruler</b> = Penggaris\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Penggaris':\n<code>Ruler</code>",
        "expected": [
            "ruler",
            "a ruler",
            "ruler = penggaris"
        ],
        "primary_answer": "Ruler"
    },
    {
        "id": "voc_beg_57",
        "badge": "📚 🚪 Bagian Kelas: Door",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Door</b> = Pintu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pintu':\n<code>Door</code>",
        "expected": [
            "door",
            "a door",
            "door = pintu"
        ],
        "primary_answer": "Door"
    },
    {
        "id": "voc_beg_58",
        "badge": "📚 🪟 Bagian Kelas: Window",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Window</b> = Jendela\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Jendela':\n<code>Window</code>",
        "expected": [
            "window",
            "a window",
            "window = jendela"
        ],
        "primary_answer": "Window"
    },
    {
        "id": "voc_beg_59",
        "badge": "📚 📋 Alat Belajar: Whiteboard",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Whiteboard</b> = Papan tulis\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Papan tulis':\n<code>Whiteboard</code>",
        "expected": [
            "whiteboard",
            "board",
            "whiteboard = papan tulis"
        ],
        "primary_answer": "Whiteboard"
    },
    {
        "id": "voc_beg_60",
        "badge": "📚 ✂️ Alat Belajar: Scissors",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Scissors</b> = Gunting\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Gunting':\n<code>Scissors</code>",
        "expected": [
            "scissors",
            "a pair of scissors",
            "scissors = gunting"
        ],
        "primary_answer": "Scissors"
    },
    {
        "id": "voc_beg_61",
        "badge": "📚 👧 Anggota Keluarga: Sister",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Sister</b> = Saudara perempuan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Saudara perempuan':\n<code>Sister</code>",
        "expected": [
            "sister",
            "my sister",
            "sister = saudara perempuan"
        ],
        "primary_answer": "Sister"
    },
    {
        "id": "voc_beg_62",
        "badge": "📚 👦 Anggota Keluarga: Brother",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Brother</b> = Saudara laki-laki\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Saudara laki-laki':\n<code>Brother</code>",
        "expected": [
            "brother",
            "my brother",
            "brother = saudara laki-laki"
        ],
        "primary_answer": "Brother"
    },
    {
        "id": "voc_beg_63",
        "badge": "📚 👶 Anggota Keluarga: Baby",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Baby</b> = Bayi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bayi':\n<code>Baby</code>",
        "expected": [
            "baby",
            "a baby",
            "baby = bayi"
        ],
        "primary_answer": "Baby"
    },
    {
        "id": "voc_beg_64",
        "badge": "📚 👵 Anggota Keluarga: Grandmother",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Grandmother</b> = Nenek\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Nenek':\n<code>Grandmother</code>",
        "expected": [
            "grandmother",
            "grandma",
            "grandmother = nenek"
        ],
        "primary_answer": "Grandmother"
    },
    {
        "id": "voc_beg_65",
        "badge": "📚 👴 Anggota Keluarga: Grandfather",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Grandfather</b> = Kakek\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kakek':\n<code>Grandfather</code>",
        "expected": [
            "grandfather",
            "grandpa",
            "grandfather = kakek"
        ],
        "primary_answer": "Grandfather"
    },
    {
        "id": "voc_beg_66",
        "badge": "📚 🍞 Makanan Sarapan: Bread",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Bread</b> = Roti\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Roti':\n<code>Bread</code>",
        "expected": [
            "bread",
            "bread = roti"
        ],
        "primary_answer": "Bread"
    },
    {
        "id": "voc_beg_67",
        "badge": "📚 🥚 Sumber Protein: Egg",
        "prompt": "🌟 <b>Kosakata Dasar:</b>\n\n• <b>Egg</b> = Telur\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Telur':\n<code>Egg</code>",
        "expected": [
            "egg",
            "an egg",
            "egg = telur"
        ],
        "primary_answer": "Egg"
    }
],
    config.LEVEL_INTERMEDIATE: [
    {
        "id": "voc_int_01",
        "badge": "📚 Rutinitas: Wake Up",
        "prompt": "⏰ <b>Rutinitas Pagi (Daily Routines):</b>\n\n• <b>Wake up</b> = Bangun tidur\n\n👉 <b>Giliranmu:</b> Tulis frasa bahasa Inggris untuk 'Bangun tidur':\n<code>Wake up</code>",
        "expected": [
            "wake up",
            "wake up = bangun tidur"
        ],
        "primary_answer": "Wake up"
    },
    {
        "id": "voc_int_02",
        "badge": "📚 Rutinitas: Take a Bath",
        "prompt": "🚿 <b>Kebersihan Diri (Hygiene):</b>\n\n• <b>Take a bath</b> = Mandi\n\n👉 <b>Giliranmu:</b> Tulis frasa bahasa Inggris untuk 'Mandi':\n<code>Take a bath</code>",
        "expected": [
            "take a bath",
            "take a shower",
            "take a bath = mandi"
        ],
        "primary_answer": "Take a bath"
    },
    {
        "id": "voc_int_03",
        "badge": "📚 Rutinitas: Brush Teeth",
        "prompt": "🪥 <b>Kebersihan Gigi:</b>\n\n• <b>Brush teeth</b> = Menggosok gigi\n\n👉 <b>Giliranmu:</b> Tulis frasa bahasa Inggris untuk 'Menggosok gigi':\n<code>Brush teeth</code>",
        "expected": [
            "brush teeth",
            "brush my teeth",
            "brush teeth = menggosok gigi"
        ],
        "primary_answer": "Brush teeth"
    },
    {
        "id": "voc_int_04",
        "badge": "📚 Makanan Pagi: Breakfast",
        "prompt": "🍳 <b>Waktu Makan (Meals):</b>\n\n• <b>Breakfast</b> = Sarapan pagi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sarapan pagi':\n<code>Breakfast</code>",
        "expected": [
            "breakfast",
            "eat breakfast",
            "breakfast = sarapan"
        ],
        "primary_answer": "Breakfast"
    },
    {
        "id": "voc_int_05",
        "badge": "📚 Rutinitas: Go to School",
        "prompt": "🎒 <b>Kegiatan Sekolah:</b>\n\n• <b>Go to school</b> = Pergi ke sekolah\n\n👉 <b>Giliranmu:</b> Tulis frasa bahasa Inggris untuk 'Pergi ke sekolah':\n<code>Go to school</code>",
        "expected": [
            "go to school",
            "go to school = pergi ke sekolah"
        ],
        "primary_answer": "Go to school"
    },
    {
        "id": "voc_int_06",
        "badge": "📚 Belajar Giat: Study Hard",
        "prompt": "📖 <b>Semangat Belajar:</b>\n\n• <b>Study hard</b> = Belajar giat / rajin belajar\n\n👉 <b>Giliranmu:</b> Tulis frasa bahasa Inggris untuk 'Belajar giat':\n<code>Study hard</code>",
        "expected": [
            "study hard",
            "study hard = belajar giat"
        ],
        "primary_answer": "Study hard"
    },
    {
        "id": "voc_int_07",
        "badge": "📚 Buah Sehat: Apple",
        "prompt": "🍎 <b>Buah-buahan (Fruits):</b>\n\n• <b>Apple</b> = Apel\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk buah 'Apel':\n<code>Apple</code>",
        "expected": [
            "apple",
            "an apple",
            "apple = apel"
        ],
        "primary_answer": "Apple"
    },
    {
        "id": "voc_int_08",
        "badge": "📚 Buah Manis: Banana",
        "prompt": "🍌 <b>Buah-buahan (Fruits):</b>\n\n• <b>Banana</b> = Pisang\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk buah 'Pisang':\n<code>Banana</code>",
        "expected": [
            "banana",
            "a banana",
            "banana = pisang"
        ],
        "primary_answer": "Banana"
    },
    {
        "id": "voc_int_09",
        "badge": "📚 Minuman Sehat: Milk",
        "prompt": "🥛 <b>Minuman (Drinks):</b>\n\n• <b>Milk</b> = Susu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Susu':\n<code>Milk</code>",
        "expected": [
            "milk",
            "glass of milk",
            "milk = susu"
        ],
        "primary_answer": "Milk"
    },
    {
        "id": "voc_int_10",
        "badge": "📚 Air Bersih: Water",
        "prompt": "💧 <b>Minuman Alami:</b>\n\n• <b>Water</b> = Air putih\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Air':\n<code>Water</code>",
        "expected": [
            "water",
            "mineral water",
            "water = air"
        ],
        "primary_answer": "Water"
    },
    {
        "id": "voc_int_11",
        "badge": "📚 Makanan Pokok: Rice",
        "prompt": "🍚 <b>Makanan (Food):</b>\n\n• <b>Rice</b> = Nasi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Nasi':\n<code>Rice</code>",
        "expected": [
            "rice",
            "white rice",
            "rice = nasi"
        ],
        "primary_answer": "Rice"
    },
    {
        "id": "voc_int_12",
        "badge": "📚 Pakaian: Shirt",
        "prompt": "👔 <b>Pakaian (Clothes):</b>\n\n• <b>Shirt</b> = Kemeja / baju berkerah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kemeja':\n<code>Shirt</code>",
        "expected": [
            "shirt",
            "a shirt",
            "shirt = kemeja"
        ],
        "primary_answer": "Shirt"
    },
    {
        "id": "voc_int_13",
        "badge": "📚 Alas Kaki: Shoes",
        "prompt": "👟 <b>Pakaian & Sepatu:</b>\n\n• <b>Shoes</b> = Sepatu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sepatu':\n<code>Shoes</code>",
        "expected": [
            "shoes",
            "shoe",
            "a pair of shoes",
            "shoes = sepatu"
        ],
        "primary_answer": "Shoes"
    },
    {
        "id": "voc_int_14",
        "badge": "📚 Perlengkapan: Bag",
        "prompt": "🎒 <b>Peralatan Sekolah:</b>\n\n• <b>Bag</b> = Tas sekolah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tas':\n<code>Bag</code>",
        "expected": [
            "bag",
            "a bag",
            "school bag",
            "bag = tas"
        ],
        "primary_answer": "Bag"
    },
    {
        "id": "voc_int_15",
        "badge": "📚 Cuaca Cerah: Sunny",
        "prompt": "☀️ <b>Kondisi Cuaca (Weather):</b>\n\n• <b>Sunny</b> = Cerah berawan matahari\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk cuaca 'Cerah':\n<code>Sunny</code>",
        "expected": [
            "sunny",
            "sunny day",
            "sunny = cerah"
        ],
        "primary_answer": "Sunny"
    },
    {
        "id": "voc_int_16",
        "badge": "📚 Cuaca Hujan: Rainy",
        "prompt": "🌧️ <b>Kondisi Cuaca (Weather):</b>\n\n• <b>Rainy</b> = Hujan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk cuaca 'Hujan':\n<code>Rainy</code>",
        "expected": [
            "rainy",
            "rain",
            "rainy day",
            "rainy = hujan"
        ],
        "primary_answer": "Rainy"
    },
    {
        "id": "voc_int_17",
        "badge": "📚 Kendaraan: Bicycle",
        "prompt": "🚲 <b>Transportasi (Transportation):</b>\n\n• <b>Bicycle</b> = Sepeda\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sepeda':\n<code>Bicycle</code>",
        "expected": [
            "bicycle",
            "bike",
            "a bicycle",
            "bicycle = sepeda"
        ],
        "primary_answer": "Bicycle"
    },
    {
        "id": "voc_int_18",
        "badge": "📚 Kendaraan Umum: Bus",
        "prompt": "🚌 <b>Transportasi Umum:</b>\n\n• <b>Bus</b> = Bus sekolah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bus':\n<code>Bus</code>",
        "expected": [
            "bus",
            "a bus",
            "school bus",
            "bus = bus"
        ],
        "primary_answer": "Bus"
    },
    {
        "id": "voc_int_19",
        "badge": "📚 Ruang Tamu: Living Room",
        "prompt": "🛋️ <b>Bagian Rumah (Parts of a House):</b>\n\n• <b>Living room</b> = Ruang tamu / ruang keluarga\n\n👉 <b>Giliranmu:</b> Tulis frasa bahasa Inggris untuk 'Ruang tamu':\n<code>Living room</code>",
        "expected": [
            "living room",
            "living room = ruang tamu"
        ],
        "primary_answer": "Living room"
    },
    {
        "id": "voc_int_20",
        "badge": "📚 Kamar Tidur: Bedroom",
        "prompt": "🛏️ <b>Bagian Rumah (Parts of a House):</b>\n\n• <b>Bedroom</b> = Kamar tidur\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kamar tidur':\n<code>Bedroom</code>",
        "expected": [
            "bedroom",
            "a bedroom",
            "bedroom = kamar tidur"
        ],
        "primary_answer": "Bedroom"
    },
    {
        "id": "voc_int_21",
        "badge": "📚 Dapur: Kitchen",
        "prompt": "🍳 <b>Tempat Memasak:</b>\n\n• <b>Kitchen</b> = Dapur\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Dapur':\n<code>Kitchen</code>",
        "expected": [
            "kitchen",
            "a kitchen",
            "kitchen = dapur"
        ],
        "primary_answer": "Kitchen"
    },
    {
        "id": "voc_int_22",
        "badge": "📚 Tempat Umum: Hospital",
        "prompt": "🏥 <b>Tempat Umum (Public Places):</b>\n\n• <b>Hospital</b> = Rumah sakit\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Rumah sakit':\n<code>Hospital</code>",
        "expected": [
            "hospital",
            "a hospital",
            "hospital = rumah sakit"
        ],
        "primary_answer": "Hospital"
    },
    {
        "id": "voc_int_23",
        "badge": "📚 Tempat Belanja: Market",
        "prompt": "🛒 <b>Tempat Umum (Public Places):</b>\n\n• <b>Market</b> = Pasar\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pasar':\n<code>Market</code>",
        "expected": [
            "market",
            "traditional market",
            "market = pasar"
        ],
        "primary_answer": "Market"
    },
    {
        "id": "voc_int_24",
        "badge": "📚 Taman Kota: Park",
        "prompt": "🌳 <b>Tempat Bermain Terbuka:</b>\n\n• <b>Park</b> = Taman bermain / taman kota\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Taman':\n<code>Park</code>",
        "expected": [
            "park",
            "a park",
            "park = taman"
        ],
        "primary_answer": "Park"
    },
    {
        "id": "voc_int_25",
        "badge": "📚 ☁️ Cuaca Berawan: Cloudy",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Cloudy</b> = Berawan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Berawan':\n<code>Cloudy</code>",
        "expected": [
            "cloudy",
            "cloudy day",
            "cloudy = berawan"
        ],
        "primary_answer": "Cloudy"
    },
    {
        "id": "voc_int_26",
        "badge": "📚 💨 Cuaca Berangin: Windy",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Windy</b> = Berangin\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Berangin':\n<code>Windy</code>",
        "expected": [
            "windy",
            "windy day",
            "windy = berangin"
        ],
        "primary_answer": "Windy"
    },
    {
        "id": "voc_int_27",
        "badge": "📚 🌊 Bentang Alam: Beach",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Beach</b> = Pantai\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pantai':\n<code>Beach</code>",
        "expected": [
            "beach",
            "a beach",
            "beach = pantai"
        ],
        "primary_answer": "Beach"
    },
    {
        "id": "voc_int_28",
        "badge": "📚 🏞️ Air Tenang: Lake",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Lake</b> = Danau\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Danau':\n<code>Lake</code>",
        "expected": [
            "lake",
            "a lake",
            "lake = danau"
        ],
        "primary_answer": "Lake"
    },
    {
        "id": "voc_int_29",
        "badge": "📚 🌈 Keindahan Langit: Rainbow",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Rainbow</b> = Pelangi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pelangi':\n<code>Rainbow</code>",
        "expected": [
            "rainbow",
            "a rainbow",
            "rainbow = pelangi"
        ],
        "primary_answer": "Rainbow"
    },
    {
        "id": "voc_int_30",
        "badge": "📚 🌸 Keindahan Alam: Flower",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Flower</b> = Bunga\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bunga':\n<code>Flower</code>",
        "expected": [
            "flower",
            "a flower",
            "flower = bunga"
        ],
        "primary_answer": "Flower"
    },
    {
        "id": "voc_int_31",
        "badge": "📚 🌱 Tumbuhan Hijau: Grass",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Grass</b> = Rumput\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Rumput':\n<code>Grass</code>",
        "expected": [
            "grass",
            "green grass",
            "grass = rumput"
        ],
        "primary_answer": "Grass"
    },
    {
        "id": "voc_int_32",
        "badge": "📚 📚 Tempat Belajar: Library",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Library</b> = Perpustakaan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Perpustakaan':\n<code>Library</code>",
        "expected": [
            "library",
            "a library",
            "school library",
            "library = perpustakaan"
        ],
        "primary_answer": "Library"
    },
    {
        "id": "voc_int_33",
        "badge": "📚 🏦 Layanan Uang: Bank",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Bank</b> = Bank\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bank':\n<code>Bank</code>",
        "expected": [
            "bank",
            "a bank",
            "bank = bank"
        ],
        "primary_answer": "Bank"
    },
    {
        "id": "voc_int_34",
        "badge": "📚 🚆 Tempat Transportasi: Station",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Station</b> = Stasiun kereta\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Stasiun kereta':\n<code>Station</code>",
        "expected": [
            "station",
            "train station",
            "station = stasiun"
        ],
        "primary_answer": "Station"
    },
    {
        "id": "voc_int_35",
        "badge": "📚 ✈️ Penerbangan: Airport",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Airport</b> = Bandara\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bandara':\n<code>Airport</code>",
        "expected": [
            "airport",
            "an airport",
            "airport = bandara"
        ],
        "primary_answer": "Airport"
    },
    {
        "id": "voc_int_36",
        "badge": "📚 🏛️ Wisata Sejarah: Museum",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Museum</b> = Museum\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Museum':\n<code>Museum</code>",
        "expected": [
            "museum",
            "a museum",
            "museum = museum"
        ],
        "primary_answer": "Museum"
    },
    {
        "id": "voc_int_37",
        "badge": "📚 🍽️ Tempat Makan: Restaurant",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Restaurant</b> = Restoran\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Restoran':\n<code>Restaurant</code>",
        "expected": [
            "restaurant",
            "a restaurant",
            "restaurant = restoran"
        ],
        "primary_answer": "Restaurant"
    },
    {
        "id": "voc_int_38",
        "badge": "📚 💊 Beli Obat: Pharmacy",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Pharmacy</b> = Apotek\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Apotek':\n<code>Pharmacy</code>",
        "expected": [
            "pharmacy",
            "a pharmacy",
            "drugstore",
            "pharmacy = apotek"
        ],
        "primary_answer": "Pharmacy"
    },
    {
        "id": "voc_int_39",
        "badge": "📚 🛁 Kebersihan Rumah: Bathroom",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Bathroom</b> = Kamar mandi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kamar mandi':\n<code>Bathroom</code>",
        "expected": [
            "bathroom",
            "a bathroom",
            "bathroom = kamar mandi"
        ],
        "primary_answer": "Bathroom"
    },
    {
        "id": "voc_int_40",
        "badge": "📚 🪞 Alat Rumah: Mirror",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Mirror</b> = Cermin\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Cermin':\n<code>Mirror</code>",
        "expected": [
            "mirror",
            "a mirror",
            "mirror = cermin"
        ],
        "primary_answer": "Mirror"
    },
    {
        "id": "voc_int_41",
        "badge": "📚 🛋️ Mebel Lembut: Sofa",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Sofa</b> = Sofa\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sofa':\n<code>Sofa</code>",
        "expected": [
            "sofa",
            "a sofa",
            "couch",
            "sofa = sofa"
        ],
        "primary_answer": "Sofa"
    },
    {
        "id": "voc_int_42",
        "badge": "📚 🛏️ Penutup Tidur: Blanket",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Blanket</b> = Selimut\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Selimut':\n<code>Blanket</code>",
        "expected": [
            "blanket",
            "a blanket",
            "blanket = selimut"
        ],
        "primary_answer": "Blanket"
    },
    {
        "id": "voc_int_43",
        "badge": "📚 ☁️ Sandaran Kepala: Pillow",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Pillow</b> = Bantal\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Bantal':\n<code>Pillow</code>",
        "expected": [
            "pillow",
            "a pillow",
            "pillow = bantal"
        ],
        "primary_answer": "Pillow"
    },
    {
        "id": "voc_int_44",
        "badge": "📚 🧥 Pakaian Hangat: Jacket",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Jacket</b> = Jaket\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Jaket':\n<code>Jacket</code>",
        "expected": [
            "jacket",
            "a jacket",
            "jacket = jaket"
        ],
        "primary_answer": "Jacket"
    },
    {
        "id": "voc_int_45",
        "badge": "📚 🧢 Pelindung Kepala: Hat",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Hat</b> = Topi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Topi':\n<code>Hat</code>",
        "expected": [
            "hat",
            "a hat",
            "cap",
            "hat = topi"
        ],
        "primary_answer": "Hat"
    },
    {
        "id": "voc_int_46",
        "badge": "📚 👖 Pakaian Kaki: Pants",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Pants</b> = Celana panjang\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Celana panjang':\n<code>Pants</code>",
        "expected": [
            "pants",
            "trousers",
            "a pair of pants",
            "pants = celana panjang"
        ],
        "primary_answer": "Pants"
    },
    {
        "id": "voc_int_47",
        "badge": "📚 🧦 Pakaian Kaki: Socks",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Socks</b> = Kaus kaki\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kaus kaki':\n<code>Socks</code>",
        "expected": [
            "socks",
            "a pair of socks",
            "socks = kaus kaki"
        ],
        "primary_answer": "Socks"
    },
    {
        "id": "voc_int_48",
        "badge": "📚 🎒 Pakaian Wajib: Uniform",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Uniform</b> = Seragam\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Seragam':\n<code>Uniform</code>",
        "expected": [
            "uniform",
            "school uniform",
            "a uniform",
            "uniform = seragam"
        ],
        "primary_answer": "Uniform"
    },
    {
        "id": "voc_int_49",
        "badge": "📚 📖 Aktivitas: Study",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Study</b> = Belajar\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Belajar':\n<code>Study</code>",
        "expected": [
            "study",
            "to study",
            "study = belajar"
        ],
        "primary_answer": "Study"
    },
    {
        "id": "voc_int_50",
        "badge": "📚 😴 Aktivitas: Sleep",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Sleep</b> = Tidur\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tidur':\n<code>Sleep</code>",
        "expected": [
            "sleep",
            "to sleep",
            "sleep = tidur"
        ],
        "primary_answer": "Sleep"
    },
    {
        "id": "voc_int_51",
        "badge": "📚 🍳 Aktivitas: Cook",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Cook</b> = Memasak\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Memasak':\n<code>Cook</code>",
        "expected": [
            "cook",
            "to cook",
            "cooking",
            "cook = memasak"
        ],
        "primary_answer": "Cook"
    },
    {
        "id": "voc_int_52",
        "badge": "📚 🧹 Aktivitas: Clean",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Clean</b> = Membersihkan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Membersihkan':\n<code>Clean</code>",
        "expected": [
            "clean",
            "to clean",
            "clean = membersihkan"
        ],
        "primary_answer": "Clean"
    },
    {
        "id": "voc_int_53",
        "badge": "📚 🚶 Aktivitas: Walk",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Walk</b> = Berjalan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Berjalan':\n<code>Walk</code>",
        "expected": [
            "walk",
            "to walk",
            "walk = berjalan"
        ],
        "primary_answer": "Walk"
    },
    {
        "id": "voc_int_54",
        "badge": "📚 🚿 Aktivitas: Wash",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Wash</b> = Mencuci\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Mencuci':\n<code>Wash</code>",
        "expected": [
            "wash",
            "to wash",
            "wash = mencuci"
        ],
        "primary_answer": "Wash"
    },
    {
        "id": "voc_int_55",
        "badge": "📚 🔬 Mata Pelajaran: Science",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Science</b> = Ilmu Pengetahuan Alam (IPA)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ilmu Pengetahuan Alam (IPA)':\n<code>Science</code>",
        "expected": [
            "science",
            "natural science",
            "science = ipa"
        ],
        "primary_answer": "Science"
    },
    {
        "id": "voc_int_56",
        "badge": "📚 📐 Mata Pelajaran: Mathematics",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Mathematics</b> = Matematika\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Matematika':\n<code>Mathematics</code>",
        "expected": [
            "mathematics",
            "math",
            "mathematics = matematika"
        ],
        "primary_answer": "Mathematics"
    },
    {
        "id": "voc_int_57",
        "badge": "📚 📜 Mata Pelajaran: History",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>History</b> = Sejarah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sejarah':\n<code>History</code>",
        "expected": [
            "history",
            "history = sejarah"
        ],
        "primary_answer": "History"
    },
    {
        "id": "voc_int_58",
        "badge": "📚 🗺️ Mata Pelajaran: Geography",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Geography</b> = Geografi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Geografi':\n<code>Geography</code>",
        "expected": [
            "geography",
            "geography = geografi"
        ],
        "primary_answer": "Geography"
    },
    {
        "id": "voc_int_59",
        "badge": "📚 🎨 Mata Pelajaran: Art",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Art</b> = Seni rupa\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Seni rupa':\n<code>Art</code>",
        "expected": [
            "art",
            "fine art",
            "art = seni"
        ],
        "primary_answer": "Art"
    },
    {
        "id": "voc_int_60",
        "badge": "📚 🎵 Mata Pelajaran: Music",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Music</b> = Seni musik\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Seni musik':\n<code>Music</code>",
        "expected": [
            "music",
            "music = musik"
        ],
        "primary_answer": "Music"
    },
    {
        "id": "voc_int_61",
        "badge": "📚 🚗 Kendaraan: Car",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Car</b> = Mobil\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Mobil':\n<code>Car</code>",
        "expected": [
            "car",
            "a car",
            "car = mobil"
        ],
        "primary_answer": "Car"
    },
    {
        "id": "voc_int_62",
        "badge": "📚 🏍️ Kendaraan: Motorcycle",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Motorcycle</b> = Sepeda motor\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sepeda motor':\n<code>Motorcycle</code>",
        "expected": [
            "motorcycle",
            "motorbike",
            "a motorcycle",
            "motorcycle = sepeda motor"
        ],
        "primary_answer": "Motorcycle"
    },
    {
        "id": "voc_int_63",
        "badge": "📚 ⛵ Kendaraan Air: Boat",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Boat</b> = Perahu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Perahu':\n<code>Boat</code>",
        "expected": [
            "boat",
            "a boat",
            "boat = perahu"
        ],
        "primary_answer": "Boat"
    },
    {
        "id": "voc_int_64",
        "badge": "📚 🚢 Kendaraan Laut Besar: Ship",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Ship</b> = Kapal laut\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kapal laut':\n<code>Ship</code>",
        "expected": [
            "ship",
            "a ship",
            "ship = kapal laut"
        ],
        "primary_answer": "Ship"
    },
    {
        "id": "voc_int_65",
        "badge": "📚 ✈️ Kendaraan Udara: Airplane",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Airplane</b> = Pesawat terbang\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pesawat terbang':\n<code>Airplane</code>",
        "expected": [
            "airplane",
            "aeroplane",
            "plane",
            "airplane = pesawat"
        ],
        "primary_answer": "Airplane"
    },
    {
        "id": "voc_int_66",
        "badge": "📚 🚁 Kendaraan Baling-baling: Helicopter",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Helicopter</b> = Helikopter\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Helikopter':\n<code>Helicopter</code>",
        "expected": [
            "helicopter",
            "a helicopter",
            "helicopter = helikopter"
        ],
        "primary_answer": "Helicopter"
    },
    {
        "id": "voc_int_67",
        "badge": "📚 🧳 Perlengkapan Perjalanan: Luggage",
        "prompt": "🌟 <b>Kosakata Menengah:</b>\n\n• <b>Luggage</b> = Koper / bagasi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Koper / bagasi':\n<code>Luggage</code>",
        "expected": [
            "luggage",
            "baggage",
            "suitcase",
            "luggage = bagasi"
        ],
        "primary_answer": "Luggage"
    }
],
    config.LEVEL_ADVANCED: [
    {
        "id": "voc_adv_01",
        "badge": "📚 Profesi: Doctor",
        "prompt": "🩺 <b>Profesi (Professions):</b>\n\n• <b>Doctor</b> = Dokter (orang yang mengobati pasien)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Dokter':\n<code>Doctor</code>",
        "expected": [
            "doctor",
            "a doctor",
            "doctor = dokter"
        ],
        "primary_answer": "Doctor"
    },
    {
        "id": "voc_adv_02",
        "badge": "📚 Profesi: Teacher",
        "prompt": "👩‍🏫 <b>Profesi (Professions):</b>\n\n• <b>Teacher</b> = Guru (orang yang mengajar di sekolah)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Guru':\n<code>Teacher</code>",
        "expected": [
            "teacher",
            "a teacher",
            "teacher = guru"
        ],
        "primary_answer": "Teacher"
    },
    {
        "id": "voc_adv_03",
        "badge": "📚 Profesi: Police Officer",
        "prompt": "👮 <b>Profesi (Professions):</b>\n\n• <b>Police officer</b> = Polisi (menjaga ketertiban)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Polisi':\n<code>Police officer</code>",
        "expected": [
            "police officer",
            "police",
            "policeman",
            "police officer = polisi"
        ],
        "primary_answer": "Police officer"
    },
    {
        "id": "voc_adv_04",
        "badge": "📚 Profesi: Farmer",
        "prompt": "🌾 <b>Profesi Mulia:</b>\n\n• <b>Farmer</b> = Petani (menanam padi dan sayuran)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Petani':\n<code>Farmer</code>",
        "expected": [
            "farmer",
            "a farmer",
            "farmer = petani"
        ],
        "primary_answer": "Farmer"
    },
    {
        "id": "voc_adv_05",
        "badge": "📚 Profesi Berani: Firefighter",
        "prompt": "🚒 <b>Penyelamat Kebakaran:</b>\n\n• <b>Firefighter</b> = Pemadam kebakaran\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pemadam kebakaran':\n<code>Firefighter</code>",
        "expected": [
            "firefighter",
            "fireman",
            "firefighter = pemadam kebakaran"
        ],
        "primary_answer": "Firefighter"
    },
    {
        "id": "voc_adv_06",
        "badge": "📚 Profesi Memasak: Chef",
        "prompt": "👨‍🍳 <b>Juru Masak Profesional:</b>\n\n• <b>Chef</b> = Koki / juru masak\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Koki':\n<code>Chef</code>",
        "expected": [
            "chef",
            "a chef",
            "cook",
            "chef = koki"
        ],
        "primary_answer": "Chef"
    },
    {
        "id": "voc_adv_07",
        "badge": "📚 Sifat Terpuji: Honest",
        "prompt": "✨ <b>Sifat Karakter (Adjectives):</b>\n\n• <b>Honest</b> = Jujur (selalu berkata benar)\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Jujur':\n<code>Honest</code>",
        "expected": [
            "honest",
            "honest = jujur"
        ],
        "primary_answer": "Honest"
    },
    {
        "id": "voc_adv_08",
        "badge": "📚 Sifat Santun: Polite",
        "prompt": "🌸 <b>Tata Krama:</b>\n\n• <b>Polite</b> = Sopan / santun bertutur kata\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Sopan':\n<code>Polite</code>",
        "expected": [
            "polite",
            "polite = sopan"
        ],
        "primary_answer": "Polite"
    },
    {
        "id": "voc_adv_09",
        "badge": "📚 Sifat Kesatria: Brave",
        "prompt": "🦁 <b>Keteguhan Hati:</b>\n\n• <b>Brave</b> = Berani (tidak takut menghadapi rintangan)\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Berani':\n<code>Brave</code>",
        "expected": [
            "brave",
            "brave = berani"
        ],
        "primary_answer": "Brave"
    },
    {
        "id": "voc_adv_10",
        "badge": "📚 Sikap Tenang: Patient",
        "prompt": "🕊️ <b>Kesabaran:</b>\n\n• <b>Patient</b> = Sabar (mampu menahan emosi dan antre tertib)\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Sabar':\n<code>Patient</code>",
        "expected": [
            "patient",
            "patient = sabar"
        ],
        "primary_answer": "Patient"
    },
    {
        "id": "voc_adv_11",
        "badge": "📚 Rajin Belajar: Diligent",
        "prompt": "🐝 <b>Kerja Keras:</b>\n\n• <b>Diligent</b> = Rajin / tekun berusaha\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Rajin':\n<code>Diligent</code>",
        "expected": [
            "diligent",
            "diligent = rajin"
        ],
        "primary_answer": "Diligent"
    },
    {
        "id": "voc_adv_12",
        "badge": "📚 Suka Berbagi: Generous",
        "prompt": "🎁 <b>Kedermawanan:</b>\n\n• <b>Generous</b> = Dermawan / suka menolong sesama\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Dermawan':\n<code>Generous</code>",
        "expected": [
            "generous",
            "generous = dermawan"
        ],
        "primary_answer": "Generous"
    },
    {
        "id": "voc_adv_13",
        "badge": "📚 Kata Kerja Aksi: Climb",
        "prompt": "🧗 <b>Kata Kerja Fisik (Action Verbs):</b>\n\n• <b>Climb</b> = Memanjat (seperti memanjat pohon)\n\n👉 <b>Giliranmu:</b> Tulis kata kerja bahasa Inggris untuk 'Memanjat':\n<code>Climb</code>",
        "expected": [
            "climb",
            "to climb",
            "climb = memanjat"
        ],
        "primary_answer": "Climb"
    },
    {
        "id": "voc_adv_14",
        "badge": "📚 Bicara Lembut: Whisper",
        "prompt": "🤫 <b>Suara Halus:</b>\n\n• <b>Whisper</b> = Berbisik dengan suara lirih\n\n👉 <b>Giliranmu:</b> Tulis kata kerja bahasa Inggris untuk 'Berbisik':\n<code>Whisper</code>",
        "expected": [
            "whisper",
            "to whisper",
            "whisper = berbisik"
        ],
        "primary_answer": "Whisper"
    },
    {
        "id": "voc_adv_15",
        "badge": "📚 Melindungi Sesama: Protect",
        "prompt": "🛡️ <b>Perlindungan:</b>\n\n• <b>Protect</b> = Melindungi / menjaga keamanan\n\n👉 <b>Giliranmu:</b> Tulis kata kerja bahasa Inggris untuk 'Melindungi':\n<code>Protect</code>",
        "expected": [
            "protect",
            "to protect",
            "protect = melindungi"
        ],
        "primary_answer": "Protect"
    },
    {
        "id": "voc_adv_16",
        "badge": "📚 Menemukan Hal Baru: Discover",
        "prompt": "🔍 <b>Eksplorasi Ilmu:</b>\n\n• <b>Discover</b> = Menemukan pengetahuan baru\n\n👉 <b>Giliranmu:</b> Tulis kata kerja bahasa Inggris untuk 'Menemukan':\n<code>Discover</code>",
        "expected": [
            "discover",
            "to discover",
            "discover = menemukan"
        ],
        "primary_answer": "Discover"
    },
    {
        "id": "voc_adv_17",
        "badge": "📚 Alam: Forest",
        "prompt": "🌲 <b>Bentang Alam (Geographical Terms):</b>\n\n• <b>Forest</b> = Hutan lebat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Hutan':\n<code>Forest</code>",
        "expected": [
            "forest",
            "a forest",
            "forest = hutan"
        ],
        "primary_answer": "Forest"
    },
    {
        "id": "voc_adv_18",
        "badge": "📚 Aliran Air: River",
        "prompt": "🌊 <b>Air Mengalir:</b>\n\n• <b>River</b> = Sungai\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sungai':\n<code>River</code>",
        "expected": [
            "river",
            "a river",
            "river = sungai"
        ],
        "primary_answer": "River"
    },
    {
        "id": "voc_adv_19",
        "badge": "📚 Puncak Tinggi: Mountain",
        "prompt": "⛰️ <b>Ketinggian Alam:</b>\n\n• <b>Mountain</b> = Gunung yang tinggi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Gunung':\n<code>Mountain</code>",
        "expected": [
            "mountain",
            "a mountain",
            "mountain = gunung"
        ],
        "primary_answer": "Mountain"
    },
    {
        "id": "voc_adv_20",
        "badge": "📚 Tanah Nusantara: Island",
        "prompt": "🏝️ <b>Wilayah Kepulauan:</b>\n\n• <b>Island</b> = Pulau yang dikelilingi laut\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pulau':\n<code>Island</code>",
        "expected": [
            "island",
            "an island",
            "island = pulau"
        ],
        "primary_answer": "Island"
    },
    {
        "id": "voc_adv_21",
        "badge": "📚 Kesehatan: Healthy",
        "prompt": "💪 <b>Kebugaran Fisik:</b>\n\n• <b>Healthy</b> = Sehat walafiat\n\n👉 <b>Giliranmu:</b> Tulis kata sifat bahasa Inggris untuk 'Sehat':\n<code>Healthy</code>",
        "expected": [
            "healthy",
            "healthy = sehat"
        ],
        "primary_answer": "Healthy"
    },
    {
        "id": "voc_adv_22",
        "badge": "📚 Obat Penyembuh: Medicine",
        "prompt": "💊 <b>Kesehatan & Farmasi:</b>\n\n• <b>Medicine</b> = Obat penyembuh penyakit\n\n👉 <b>Giliranmu:</b> Tulis kata benda bahasa Inggris untuk 'Obat':\n<code>Medicine</code>",
        "expected": [
            "medicine",
            "medicine = obat"
        ],
        "primary_answer": "Medicine"
    },
    {
        "id": "voc_adv_23",
        "badge": "📚 Wawasan Berharga: Knowledge",
        "prompt": "💡 <b>Pendidikan & Pikiran:</b>\n\n• <b>Knowledge</b> = Pengetahuan / ilmu yang bermanfaat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pengetahuan':\n<code>Knowledge</code>",
        "expected": [
            "knowledge",
            "knowledge = pengetahuan"
        ],
        "primary_answer": "Knowledge"
    },
    {
        "id": "voc_adv_24",
        "badge": "📚 Persatuan Warga: Community",
        "prompt": "🤝 <b>Kehidupan Bersama:</b>\n\n• <b>Community</b> = Komunitas / paguyuban masyarakat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Komunitas':\n<code>Community</code>",
        "expected": [
            "community",
            "community = masyarakat",
            "community = komunitas"
        ],
        "primary_answer": "Community"
    },
    {
        "id": "voc_adv_25",
        "badge": "📚 🔬 Profesi Ilmiah: Scientist",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Scientist</b> = Ilmuwan (peneliti sains)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ilmuwan (peneliti sains)':\n<code>Scientist</code>",
        "expected": [
            "scientist",
            "a scientist",
            "scientist = ilmuwan"
        ],
        "primary_answer": "Scientist"
    },
    {
        "id": "voc_adv_26",
        "badge": "📚 📰 Profesi Berita: Journalist",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Journalist</b> = Wartawan / jurnalis\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Wartawan / jurnalis':\n<code>Journalist</code>",
        "expected": [
            "journalist",
            "a journalist",
            "journalist = jurnalis"
        ],
        "primary_answer": "Journalist"
    },
    {
        "id": "voc_adv_27",
        "badge": "📚 ⚙️ Profesi Teknik: Engineer",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Engineer</b> = Insinyur / ahli teknik\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Insinyur / ahli teknik':\n<code>Engineer</code>",
        "expected": [
            "engineer",
            "an engineer",
            "engineer = insinyur"
        ],
        "primary_answer": "Engineer"
    },
    {
        "id": "voc_adv_28",
        "badge": "📚 🩺 Profesi Bedah: Surgeon",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Surgeon</b> = Dokter bedah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Dokter bedah':\n<code>Surgeon</code>",
        "expected": [
            "surgeon",
            "a surgeon",
            "surgeon = dokter bedah"
        ],
        "primary_answer": "Surgeon"
    },
    {
        "id": "voc_adv_29",
        "badge": "📚 ✈️ Profesi Terbang: Pilot",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Pilot</b> = Pilot pesawat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pilot pesawat':\n<code>Pilot</code>",
        "expected": [
            "pilot",
            "a pilot",
            "pilot = pilot"
        ],
        "primary_answer": "Pilot"
    },
    {
        "id": "voc_adv_30",
        "badge": "📚 ⚖️ Profesi Hukum: Lawyer",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Lawyer</b> = Pengacara / advokat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pengacara / advokat':\n<code>Lawyer</code>",
        "expected": [
            "lawyer",
            "a lawyer",
            "attorney",
            "lawyer = pengacara"
        ],
        "primary_answer": "Lawyer"
    },
    {
        "id": "voc_adv_31",
        "badge": "📚 💡 Profesi Kelistrikan: Electrician",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Electrician</b> = Teknisi listrik\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Teknisi listrik':\n<code>Electrician</code>",
        "expected": [
            "electrician",
            "an electrician",
            "electrician = teknisi listrik"
        ],
        "primary_answer": "Electrician"
    },
    {
        "id": "voc_adv_32",
        "badge": "📚 📖 Profesi Buku: Librarian",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Librarian</b> = Pustakawan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Pustakawan':\n<code>Librarian</code>",
        "expected": [
            "librarian",
            "a librarian",
            "librarian = pustakawan"
        ],
        "primary_answer": "Librarian"
    },
    {
        "id": "voc_adv_33",
        "badge": "📚 🔧 Profesi Mesin: Mechanic",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Mechanic</b> = Montir / mekanik\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Montir / mekanik':\n<code>Mechanic</code>",
        "expected": [
            "mechanic",
            "a mechanic",
            "mechanic = montir"
        ],
        "primary_answer": "Mechanic"
    },
    {
        "id": "voc_adv_34",
        "badge": "📚 🦷 Profesi Gigi: Dentist",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Dentist</b> = Dokter gigi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Dokter gigi':\n<code>Dentist</code>",
        "expected": [
            "dentist",
            "a dentist",
            "dentist = dokter gigi"
        ],
        "primary_answer": "Dentist"
    },
    {
        "id": "voc_adv_35",
        "badge": "📚 🌿 Ekologi Alam: Ecosystem",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Ecosystem</b> = Ekosistem (lingkungan hayati)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ekosistem (lingkungan hayati)':\n<code>Ecosystem</code>",
        "expected": [
            "ecosystem",
            "an ecosystem",
            "ecosystem = ekosistem"
        ],
        "primary_answer": "Ecosystem"
    },
    {
        "id": "voc_adv_36",
        "badge": "📚 🌱 Keanekaragaman Hayati: Biodiversity",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Biodiversity</b> = Keanekaragaman hayati\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Keanekaragaman hayati':\n<code>Biodiversity</code>",
        "expected": [
            "biodiversity",
            "biodiversity = keanekaragaman hayati"
        ],
        "primary_answer": "Biodiversity"
    },
    {
        "id": "voc_adv_37",
        "badge": "📚 ⚡ Energi Hijau: Renewable",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Renewable</b> = Terbarukan (energi ramah lingkungan)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Terbarukan (energi ramah lingkungan)':\n<code>Renewable</code>",
        "expected": [
            "renewable",
            "renewable energy",
            "renewable = terbarukan"
        ],
        "primary_answer": "Renewable"
    },
    {
        "id": "voc_adv_38",
        "badge": "📚 ☀️ Fotosintesis Tumbuhan: Photosynthesis",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Photosynthesis</b> = Fotosintesis\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Fotosintesis':\n<code>Photosynthesis</code>",
        "expected": [
            "photosynthesis",
            "photosynthesis = fotosintesis"
        ],
        "primary_answer": "Photosynthesis"
    },
    {
        "id": "voc_adv_39",
        "badge": "📚 🛡️ Konservasi Hayati: Conservation",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Conservation</b> = Konservasi / pelestarian alam\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Konservasi / pelestarian alam':\n<code>Conservation</code>",
        "expected": [
            "conservation",
            "nature conservation",
            "conservation = konservasi"
        ],
        "primary_answer": "Conservation"
    },
    {
        "id": "voc_adv_40",
        "badge": "📚 🌍 Lapisan Udara Bumi: Atmosphere",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Atmosphere</b> = Atmosfer bumi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Atmosfer bumi':\n<code>Atmosphere</code>",
        "expected": [
            "atmosphere",
            "earth atmosphere",
            "atmosphere = atmosfer"
        ],
        "primary_answer": "Atmosphere"
    },
    {
        "id": "voc_adv_41",
        "badge": "📚 🌧️ Fenomena Hujan: Precipitation",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Precipitation</b> = Presipitasi / curah hujan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Presipitasi / curah hujan':\n<code>Precipitation</code>",
        "expected": [
            "precipitation",
            "precipitation = presipitasi"
        ],
        "primary_answer": "Precipitation"
    },
    {
        "id": "voc_adv_42",
        "badge": "📚 🛰️ Benda Antariksa: Satellite",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Satellite</b> = Satelit pemancar / alami\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Satelit pemancar / alami':\n<code>Satellite</code>",
        "expected": [
            "satellite",
            "a satellite",
            "satellite = satelit"
        ],
        "primary_answer": "Satellite"
    },
    {
        "id": "voc_adv_43",
        "badge": "📚 ✨ Gugusan Bintang: Constellation",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Constellation</b> = Rasi bintang\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Rasi bintang':\n<code>Constellation</code>",
        "expected": [
            "constellation",
            "a constellation",
            "constellation = rasi bintang"
        ],
        "primary_answer": "Constellation"
    },
    {
        "id": "voc_adv_44",
        "badge": "📚 🧬 Biologi Sel: Genetics",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Genetics</b> = Genetika / pewarisan sifat\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Genetika / pewarisan sifat':\n<code>Genetics</code>",
        "expected": [
            "genetics",
            "genetics = genetika"
        ],
        "primary_answer": "Genetics"
    },
    {
        "id": "voc_adv_45",
        "badge": "📚 🤲 Sifat Rendah Hati: Humble",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Humble</b> = Rendah hati (tidak sombong)\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Rendah hati (tidak sombong)':\n<code>Humble</code>",
        "expected": [
            "humble",
            "humble = rendah hati"
        ],
        "primary_answer": "Humble"
    },
    {
        "id": "voc_adv_46",
        "badge": "📚 🎯 Semangat Maju: Ambitious",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Ambitious</b> = Berambisi positif / penuh cita-cita\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Berambisi positif / penuh cita-cita':\n<code>Ambitious</code>",
        "expected": [
            "ambitious",
            "ambitious = berambisi"
        ],
        "primary_answer": "Ambitious"
    },
    {
        "id": "voc_adv_47",
        "badge": "📚 🧗 Sikap Tangguh: Resilient",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Resilient</b> = Tangguh / pantang menyerah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tangguh / pantang menyerah':\n<code>Resilient</code>",
        "expected": [
            "resilient",
            "resilience",
            "resilient = tangguh"
        ],
        "primary_answer": "Resilient"
    },
    {
        "id": "voc_adv_48",
        "badge": "📚 ⏰ Sikap Tertib: Disciplined",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Disciplined</b> = Disiplin / patuh pada aturan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Disiplin / patuh pada aturan':\n<code>Disciplined</code>",
        "expected": [
            "disciplined",
            "disciplined = disiplin"
        ],
        "primary_answer": "Disciplined"
    },
    {
        "id": "voc_adv_49",
        "badge": "📚 🔍 Penuh Rasa Ingin Tahu: Curious",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Curious</b> = Penuh rasa ingin tahu\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Penuh rasa ingin tahu':\n<code>Curious</code>",
        "expected": [
            "curious",
            "curious = ingin tahu"
        ],
        "primary_answer": "Curious"
    },
    {
        "id": "voc_adv_50",
        "badge": "📚 🎨 Penuh Daya Cipta: Creative",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Creative</b> = Kreatif / kaya imajinasi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kreatif / kaya imajinasi':\n<code>Creative</code>",
        "expected": [
            "creative",
            "creativity",
            "creative = kreatif"
        ],
        "primary_answer": "Creative"
    },
    {
        "id": "voc_adv_51",
        "badge": "📚 🤝 Menghargai Sesama: Respectful",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Respectful</b> = Penuh rasa hormat dan santun\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Penuh rasa hormat dan santun':\n<code>Respectful</code>",
        "expected": [
            "respectful",
            "respectful = hormat"
        ],
        "primary_answer": "Respectful"
    },
    {
        "id": "voc_adv_52",
        "badge": "📚 💎 Kejujuran Moral: Integrity",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Integrity</b> = Integritas / kejujuran teguh\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Integritas / kejujuran teguh':\n<code>Integrity</code>",
        "expected": [
            "integrity",
            "integrity = integritas"
        ],
        "primary_answer": "Integrity"
    },
    {
        "id": "voc_adv_53",
        "badge": "📚 🕊️ Ketenangan Batin: Serenity",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Serenity</b> = Ketenangan / kedamaian hati\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Ketenangan / kedamaian hati':\n<code>Serenity</code>",
        "expected": [
            "serenity",
            "peacefulness",
            "serenity = ketenangan"
        ],
        "primary_answer": "Serenity"
    },
    {
        "id": "voc_adv_54",
        "badge": "📚 🔬 Dugaan Awal Ilmiah: Hypothesis",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Hypothesis</b> = Hipotesis / praduga ilmiah\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Hipotesis / praduga ilmiah':\n<code>Hypothesis</code>",
        "expected": [
            "hypothesis",
            "a hypothesis",
            "hypothesis = hipotesis"
        ],
        "primary_answer": "Hypothesis"
    },
    {
        "id": "voc_adv_55",
        "badge": "📚 🏛️ Kemajuan Bangsa: Civilization",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Civilization</b> = Peradaban umat manusia\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Peradaban umat manusia':\n<code>Civilization</code>",
        "expected": [
            "civilization",
            "a civilization",
            "civilization = peradaban"
        ],
        "primary_answer": "Civilization"
    },
    {
        "id": "voc_adv_56",
        "badge": "📚 🌐 Kerja Sama Global: Collaboration",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Collaboration</b> = Kolaborasi / kerja sama\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kolaborasi / kerja sama':\n<code>Collaboration</code>",
        "expected": [
            "collaboration",
            "cooperation",
            "collaboration = kolaborasi"
        ],
        "primary_answer": "Collaboration"
    },
    {
        "id": "voc_adv_57",
        "badge": "📚 💡 Sudut Pandang Pikiran: Perspective",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Perspective</b> = Sudut pandang / cara pandang\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Sudut pandang / cara pandang':\n<code>Perspective</code>",
        "expected": [
            "perspective",
            "a perspective",
            "perspective = sudut pandang"
        ],
        "primary_answer": "Perspective"
    },
    {
        "id": "voc_adv_58",
        "badge": "📚 📜 Pernyataan Resmi: Declaration",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Declaration</b> = Deklarasi / pernyataan resmi\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Deklarasi / pernyataan resmi':\n<code>Declaration</code>",
        "expected": [
            "declaration",
            "a declaration",
            "declaration = deklarasi"
        ],
        "primary_answer": "Declaration"
    },
    {
        "id": "voc_adv_59",
        "badge": "📚 🏆 Keunggulan Prestasi: Excellence",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Excellence</b> = Keunggulan / prestasi luar biasa\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Keunggulan / prestasi luar biasa':\n<code>Excellence</code>",
        "expected": [
            "excellence",
            "excellence = keunggulan"
        ],
        "primary_answer": "Excellence"
    },
    {
        "id": "voc_adv_60",
        "badge": "📚 ⚖️ Keadilan Hakiki: Justice",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Justice</b> = Keadilan yang jujur\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Keadilan yang jujur':\n<code>Justice</code>",
        "expected": [
            "justice",
            "justice = keadilan"
        ],
        "primary_answer": "Justice"
    },
    {
        "id": "voc_adv_61",
        "badge": "📚 📚 Kemampuan Baca Tulis: Literacy",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Literacy</b> = Literasi / kecakapan membaca\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Literasi / kecakapan membaca':\n<code>Literacy</code>",
        "expected": [
            "literacy",
            "literacy = literasi"
        ],
        "primary_answer": "Literacy"
    },
    {
        "id": "voc_adv_62",
        "badge": "📚 🤝 Tanggung Jawab Moral: Responsibility",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Responsibility</b> = Tanggung jawab tugas\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Tanggung jawab tugas':\n<code>Responsibility</code>",
        "expected": [
            "responsibility",
            "responsibility = tanggung jawab"
        ],
        "primary_answer": "Responsibility"
    },
    {
        "id": "voc_adv_63",
        "badge": "📚 💡 Kesadaran Hati: Awareness",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Awareness</b> = Kesadaran / kepekaan diri\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Kesadaran / kepekaan diri':\n<code>Awareness</code>",
        "expected": [
            "awareness",
            "awareness = kesadaran"
        ],
        "primary_answer": "Awareness"
    },
    {
        "id": "voc_adv_64",
        "badge": "📚 🌟 Daya Tahan Mental: Endurance",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Endurance</b> = Daya tahan fisik / mental\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Daya tahan fisik / mental':\n<code>Endurance</code>",
        "expected": [
            "endurance",
            "stamina",
            "endurance = daya tahan"
        ],
        "primary_answer": "Endurance"
    },
    {
        "id": "voc_adv_65",
        "badge": "📚 🚀 Kemajuan Inovasi: Innovation",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Innovation</b> = Inovasi / terobosan baru\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Inovasi / terobosan baru':\n<code>Innovation</code>",
        "expected": [
            "innovation",
            "an innovation",
            "innovation = inovasi"
        ],
        "primary_answer": "Innovation"
    },
    {
        "id": "voc_adv_66",
        "badge": "📚 🌱 Keberlanjutan Masa Depan: Sustainability",
        "prompt": "🌟 <b>Kosakata Tingkat Mahir:</b>\n\n• <b>Sustainability</b> = Keberlanjutan lingkungan\n\n👉 <b>Giliranmu:</b> Tulis kata bahasa Inggris untuk 'Keberlanjutan lingkungan':\n<code>Sustainability</code>",
        "expected": [
            "sustainability",
            "sustainability = keberlanjutan"
        ],
        "primary_answer": "Sustainability"
    }
],
}
