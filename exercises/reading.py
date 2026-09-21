"""
Curated Reading Comprehension exercises for English Buddy Bot.
Total: 200 exercises (67 Beginner, 67 Intermediate, 66 Advanced).
"""
from typing import Any, Dict, List
import config

READING_EXERCISES: Dict[str, List[Dict[str, Any]]] = {
    config.LEVEL_BEGINNER: [
    {
        "id": "rdg_beg_01",
        "badge": "📖 Kucing Snowy: Nama",
        "prompt": "🐈 <b>Baca teks pendek berikut:</b>\n\"My cat is white and fluffy. Her name is <b>Snowy</b>. She likes to drink warm milk.\"\n\n👉 <b>Pertanyaan:</b> What is the cat's name? (Siapa nama kucing itu?)",
        "expected": [
            "snowy",
            "her name is snowy",
            "the cat's name is snowy"
        ],
        "primary_answer": "Snowy"
    },
    {
        "id": "rdg_beg_02",
        "badge": "📖 Kucing Snowy: Minuman",
        "prompt": "🥛 <b>Baca teks pendek berikut:</b>\n\"Snowy is a friendly cat. She loves to sit on the sofa and drink <b>warm milk</b> every morning.\"\n\n👉 <b>Pertanyaan:</b> What does Snowy like to drink? (Apa minuman kesukaan Snowy?)",
        "expected": [
            "warm milk",
            "milk",
            "she likes warm milk",
            "she drinks warm milk"
        ],
        "primary_answer": "warm milk"
    },
    {
        "id": "rdg_beg_03",
        "badge": "🚲 Sepeda Budi: Warna",
        "prompt": "🚲 <b>Baca teks pendek berikut:</b>\n\"Budi has a new bicycle. The bicycle is <b>blue</b>. He rides it to school every day.\"\n\n👉 <b>Pertanyaan:</b> What color is Budi's bicycle? (Apa warna sepeda Budi?)",
        "expected": [
            "blue",
            "the bicycle is blue",
            "it is blue"
        ],
        "primary_answer": "blue"
    },
    {
        "id": "rdg_beg_04",
        "badge": "🚲 Sepeda Budi: Lokasi",
        "prompt": "🌳 <b>Baca teks pendek berikut:</b>\n\"On Sunday afternoons, Budi rides his blue bicycle in the <b>park</b> with his friends.\"\n\n👉 <b>Pertanyaan:</b> Where does Budi ride his bicycle on Sunday? (Di mana Budi bersepeda?)",
        "expected": [
            "in the park",
            "park",
            "the park",
            "at the park"
        ],
        "primary_answer": "in the park"
    },
    {
        "id": "rdg_beg_05",
        "badge": "🌹 Kebun Sarah: Bunga",
        "prompt": "🌸 <b>Baca teks pendek berikut:</b>\n\"Sarah has a lovely garden behind her house. There are red <b>roses</b> and yellow sunflowers.\"\n\n👉 <b>Pertanyaan:</b> What color are the roses in Sarah's garden? (Apa warna bunga mawar di kebun Sarah?)",
        "expected": [
            "red",
            "red roses",
            "they are red"
        ],
        "primary_answer": "red"
    },
    {
        "id": "rdg_beg_06",
        "badge": "🌹 Kebun Sarah: Penyiram",
        "prompt": "💧 <b>Baca teks pendek berikut:</b>\n\"Every morning before school, <b>Sarah</b> waters the flowers carefully with a green watering can.\"\n\n👉 <b>Pertanyaan:</b> Who waters the flowers every morning? (Siapa yang menyiram bunga setiap pagi?)",
        "expected": [
            "sarah",
            "sarah does",
            "sarah waters them"
        ],
        "primary_answer": "Sarah"
    },
    {
        "id": "rdg_beg_07",
        "badge": "📚 Perpustakaan Sekolah: Buku",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Our school library is very spacious. It has more than one thousand <b>books</b> on tall wooden shelves.\"\n\n👉 <b>Pertanyaan:</b> What are on the tall wooden shelves? (Apa yang ada di rak kayu yang tinggi?)",
        "expected": [
            "books",
            "thousand books",
            "more than one thousand books"
        ],
        "primary_answer": "books"
    },
    {
        "id": "rdg_beg_08",
        "badge": "📚 Perpustakaan Sekolah: Aturan",
        "prompt": "🤫 <b>Baca teks pendek berikut:</b>\n\"When students enter the school library, they must keep <b>quiet</b> so everyone can read in peace.\"\n\n👉 <b>Pertanyaan:</b> How must students behave in the library? (Bagaimana siswa harus bersikap di perpustakaan?)",
        "expected": [
            "quiet",
            "keep quiet",
            "be quiet",
            "silent"
        ],
        "primary_answer": "quiet"
    },
    {
        "id": "rdg_beg_09",
        "badge": "🥞 Sarapan Ahmad: Menu",
        "prompt": "🥞 <b>Baca teks pendek berikut:</b>\n\"Ahmad wakes up at six o'clock. For breakfast, his mother cooks delicious sweet <b>pancakes</b>.\"\n\n👉 <b>Pertanyaan:</b> What does mother cook for breakfast? (Apa yang dimasak ibu untuk sarapan?)",
        "expected": [
            "pancakes",
            "pancake",
            "sweet pancakes",
            "delicious pancakes"
        ],
        "primary_answer": "pancakes"
    },
    {
        "id": "rdg_beg_10",
        "badge": "🍊 Sarapan Ahmad: Minuman",
        "prompt": "🍹 <b>Baca teks pendek berikut:</b>\n\"Along with his pancakes, Ahmad drinks a cold glass of fresh <b>orange juice</b>.\"\n\n👉 <b>Pertanyaan:</b> What does Ahmad drink with his pancakes? (Apa yang diminum Ahmad bersama pancake?)",
        "expected": [
            "orange juice",
            "juice",
            "fresh orange juice",
            "a glass of orange juice"
        ],
        "primary_answer": "orange juice"
    },
    {
        "id": "rdg_beg_11",
        "badge": "🐕 Anjing Leo: Bola",
        "prompt": "🎾 <b>Baca teks pendek berikut:</b>\n\"Leo is a golden puppy. His favorite toy is a small <b>yellow</b> ball.\"\n\n👉 <b>Pertanyaan:</b> What color is Leo's favorite toy ball? (Apa warna bola mainan kesukaan Leo?)",
        "expected": [
            "yellow",
            "yellow ball",
            "it is yellow"
        ],
        "primary_answer": "yellow"
    },
    {
        "id": "rdg_beg_12",
        "badge": "🐕 Anjing Leo: Suara",
        "prompt": "🐶 <b>Baca teks pendek berikut:</b>\n\"Whenever the mail carrier arrives at the front gate, Leo <b>barks</b> happily to greet him.\"\n\n👉 <b>Pertanyaan:</b> What does Leo do when the mail carrier arrives? (Apa yang dilakukan Leo saat pengantar surat tiba?)",
        "expected": [
            "barks",
            "he barks",
            "bark",
            "barks happily"
        ],
        "primary_answer": "barks"
    },
    {
        "id": "rdg_beg_13",
        "badge": "🍎 Pasar Minggu: Buah",
        "prompt": "🛍️ <b>Baca teks pendek berikut:</b>\n\"Mom visits the traditional market. She buys fresh sweet <b>apples</b> and crunchy carrots.\"\n\n👉 <b>Pertanyaan:</b> Which fruit does Mom buy at the market? (Buah apa yang dibeli Ibu di pasar?)",
        "expected": [
            "apples",
            "apple",
            "fresh apples",
            "sweet apples"
        ],
        "primary_answer": "apples"
    },
    {
        "id": "rdg_beg_14",
        "badge": "🗓️ Pasar Minggu: Hari",
        "prompt": "📅 <b>Baca teks pendek berikut:</b>\n\"The family goes shopping together every <b>Sunday</b> morning.\"\n\n👉 <b>Pertanyaan:</b> On what day does the family go shopping together? (Pada hari apa keluarga berbelanja bersama?)",
        "expected": [
            "sunday",
            "on sunday",
            "sunday morning"
        ],
        "primary_answer": "Sunday"
    },
    {
        "id": "rdg_beg_15",
        "badge": "🚌 Bus Merah: Tujuan",
        "prompt": "🏙️ <b>Baca teks pendek berikut:</b>\n\"The big red bus stops at our street. It takes passengers directly to the <b>city center</b>.\"\n\n👉 <b>Pertanyaan:</b> Where does the red bus take passengers? (Ke mana bus merah membawa penumpang?)",
        "expected": [
            "city center",
            "to the city center",
            "city"
        ],
        "primary_answer": "city center"
    },
    {
        "id": "rdg_beg_16",
        "badge": "🚌 Bus Merah: Sopir",
        "prompt": "👨‍✈️ <b>Baca teks pendek berikut:</b>\n\"The driver of the red bus is <b>Mr. John</b>. He is always polite and smiles at everyone.\"\n\n👉 <b>Pertanyaan:</b> Who drives the red bus? (Siapa pengemudi bus merah?)",
        "expected": [
            "mr. john",
            "mr john",
            "john"
        ],
        "primary_answer": "Mr. John"
    },
    {
        "id": "rdg_beg_17",
        "badge": "🎨 Hobi Nina: Melukis",
        "prompt": "🎨 <b>Baca teks pendek berikut:</b>\n\"Nina is an artistic girl. Her favorite hobby is <b>painting</b> landscapes on canvas.\"\n\n👉 <b>Pertanyaan:</b> What is Nina's favorite hobby? (Apa hobi kesukaan Nina?)",
        "expected": [
            "painting",
            "painting landscapes",
            "her hobby is painting"
        ],
        "primary_answer": "painting"
    },
    {
        "id": "rdg_beg_18",
        "badge": "🎨 Hobi Nina: Warna Favorit",
        "prompt": "🌿 <b>Baca teks pendek berikut:</b>\n\"Nina loves nature, so her favorite color to paint trees and hills is <b>green</b>.\"\n\n👉 <b>Pertanyaan:</b> What is Nina's favorite color for trees? (Apa warna kesukaan Nina untuk pohon?)",
        "expected": [
            "green",
            "it is green"
        ],
        "primary_answer": "green"
    },
    {
        "id": "rdg_beg_19",
        "badge": "🦒 Kebun Binatang: Hewan Tertinggi",
        "prompt": "🦒 <b>Baca teks pendek berikut:</b>\n\"At the city zoo, visitors gaze up at the <b>giraffe</b>. It is the tallest animal in the enclosure.\"\n\n👉 <b>Pertanyaan:</b> Which animal is the tallest in the zoo? (Hewan mana yang paling tinggi di kebun binatang?)",
        "expected": [
            "giraffe",
            "the giraffe"
        ],
        "primary_answer": "giraffe"
    },
    {
        "id": "rdg_beg_20",
        "badge": "🍌 Kebun Binatang: Monyet",
        "prompt": "🐒 <b>Baca teks pendek berikut:</b>\n\"The mischievous monkeys swing from branches and eat ripe sweet <b>bananas</b>.\"\n\n👉 <b>Pertanyaan:</b> What food do the monkeys eat? (Makanan apa yang dimakan para monyet?)",
        "expected": [
            "bananas",
            "banana",
            "sweet bananas",
            "ripe bananas"
        ],
        "primary_answer": "bananas"
    },
    {
        "id": "rdg_beg_21",
        "badge": "🌧️ Hari Hujan: Jas Hujan",
        "prompt": "🧥 <b>Baca teks pendek berikut:</b>\n\"When heavy raindrops begin falling, Tommy puts on his blue <b>raincoat</b> and waterproof boots.\"\n\n👉 <b>Pertanyaan:</b> What garment does Tommy put on when it rains? (Pakaian apa yang dipakai Tommy saat hujan?)",
        "expected": [
            "raincoat",
            "blue raincoat",
            "a raincoat"
        ],
        "primary_answer": "raincoat"
    },
    {
        "id": "rdg_beg_22",
        "badge": "🌧️ Hari Hujan: Payung",
        "prompt": "☂️ <b>Baca teks pendek berikut:</b>\n\"Tommy's sister carries a bright <b>yellow</b> umbrella to stay completely dry.\"\n\n👉 <b>Pertanyaan:</b> What color is her umbrella? (Apa warna payungnya?)",
        "expected": [
            "yellow",
            "bright yellow",
            "it is yellow"
        ],
        "primary_answer": "yellow"
    },
    {
        "id": "rdg_beg_23",
        "badge": "🎂 Kue Ulang Tahun: Lilin",
        "prompt": "🕯️ <b>Baca teks pendek berikut:</b>\n\"Today is Maya's birthday party. There are <b>seven</b> candles on top of her birthday cake.\"\n\n👉 <b>Pertanyaan:</b> How many candles are on Maya's cake? (Berapa banyak lilin di atas kue Maya?)",
        "expected": [
            "seven",
            "7",
            "seven candles",
            "7 candles"
        ],
        "primary_answer": "seven"
    },
    {
        "id": "rdg_beg_24",
        "badge": "🎂 Kue Ulang Tahun: Rasa",
        "prompt": "🍫 <b>Baca teks pendek berikut:</b>\n\"Maya's birthday cake is delicious. It has a rich layer of dark <b>chocolate</b> and sweet strawberries.\"\n\n👉 <b>Pertanyaan:</b> What is the main flavor of the cake? (Apa rasa utama kue tersebut?)",
        "expected": [
            "chocolate",
            "dark chocolate"
        ],
        "primary_answer": "chocolate"
    },
    {
        "id": "rdg_beg_25",
        "badge": "📖 🐇 Kelinci Bella: Makanan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Bella is a fluffy white rabbit. She loves to eat crunchy orange <b>carrots</b>.\"\n\n👉 <b>Pertanyaan:</b> What does Bella love to eat? (Apa yang disukai Bella untuk dimakan?)",
        "expected": [
            "carrots",
            "carrot",
            "orange carrots"
        ],
        "primary_answer": "carrots"
    },
    {
        "id": "rdg_beg_26",
        "badge": "📖 🐇 Kelinci Bella: Warna Bulu",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Bella has long soft ears. Her fur is completely <b>white</b>.\"\n\n👉 <b>Pertanyaan:</b> What color is Bella's fur? (Apa warna bulu Bella?)",
        "expected": [
            "white",
            "it is white"
        ],
        "primary_answer": "white"
    },
    {
        "id": "rdg_beg_27",
        "badge": "📖 🥭 Pohon Pak Danu: Jenis",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Mr. Danu has a big <b>mango</b> tree in his front yard. It bears sweet fruit every year.\"\n\n👉 <b>Pertanyaan:</b> What kind of tree is in Mr. Danu's yard? (Pohon apa yang ada di halaman Pak Danu?)",
        "expected": [
            "mango",
            "mango tree",
            "a mango tree"
        ],
        "primary_answer": "mango"
    },
    {
        "id": "rdg_beg_28",
        "badge": "📖 🥭 Pohon Pak Danu: Jumlah Burung",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"<b>Two</b> green birds build a small nest on the highest branch of the tree.\"\n\n👉 <b>Pertanyaan:</b> How many green birds build a nest? (Berapa banyak burung hijau yang membuat sarang?)",
        "expected": [
            "two",
            "2",
            "two birds"
        ],
        "primary_answer": "two"
    },
    {
        "id": "rdg_beg_29",
        "badge": "📖 🥖 Toko Roti Desa: Produk",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Every morning at six, Uncle Tom bakes delicious fresh <b>bread</b>.\"\n\n👉 <b>Pertanyaan:</b> What does Uncle Tom bake every morning? (Apa yang dipanggang Paman Tom setiap pagi?)",
        "expected": [
            "bread",
            "fresh bread"
        ],
        "primary_answer": "bread"
    },
    {
        "id": "rdg_beg_30",
        "badge": "📖 🥖 Toko Roti Desa: Nama Pembuat",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"The friendly baker who makes warm bread is named <b>Uncle Tom</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the baker's name? (Siapa nama pembuat roti ramah tersebut?)",
        "expected": [
            "uncle tom",
            "tom"
        ],
        "primary_answer": "Uncle Tom"
    },
    {
        "id": "rdg_beg_31",
        "badge": "📖 🐟 Kolam Ikan: Jumlah Ikan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Grandfather built a small pond. Inside, there are <b>five</b> golden fish.\"\n\n👉 <b>Pertanyaan:</b> How many fish are inside the pond? (Berapa banyak ikan di dalam kolam?)",
        "expected": [
            "five",
            "5",
            "five fish",
            "5 fish"
        ],
        "primary_answer": "five"
    },
    {
        "id": "rdg_beg_32",
        "badge": "📖 🐟 Kolam Ikan: Pemberi Makan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Every afternoon after school, <b>Rama</b> sprinkles fish food on the pond.\"\n\n👉 <b>Pertanyaan:</b> Who sprinkles food on the pond? (Siapa yang menabur makanan ikan?)",
        "expected": [
            "rama"
        ],
        "primary_answer": "Rama"
    },
    {
        "id": "rdg_beg_33",
        "badge": "📖 🚌 Bus Sekolah: Warna",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"The bright <b>yellow</b> school bus stops in front of Budi's house at six.\"\n\n👉 <b>Pertanyaan:</b> What color is the school bus? (Apa warna bus sekolah?)",
        "expected": [
            "yellow",
            "it is yellow"
        ],
        "primary_answer": "yellow"
    },
    {
        "id": "rdg_beg_34",
        "badge": "📖 🚌 Bus Sekolah: Pengemudi",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"<b>Mr. Hadi</b> is the careful driver who drives students to school safely.\"\n\n👉 <b>Pertanyaan:</b> Who drives students to school? (Siapa yang mengemudikan bus sekolah?)",
        "expected": [
            "mr. hadi",
            "mr hadi",
            "hadi"
        ],
        "primary_answer": "Mr. Hadi"
    },
    {
        "id": "rdg_beg_35",
        "badge": "📖 🐯 Harimau Kebun Binatang: Tempat Istirahat",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"At the zoo, a Bengal tiger sleeps under a large shady <b>tree</b>.\"\n\n👉 <b>Pertanyaan:</b> Where does the tiger sleep? (Di mana harimau tersebut tidur?)",
        "expected": [
            "under a tree",
            "under a shady tree",
            "tree",
            "under tree"
        ],
        "primary_answer": "under a tree"
    },
    {
        "id": "rdg_beg_36",
        "badge": "📖 🐘 Gajah Jinak: Makanan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"The friendly elephant drinks clean water and eats fresh green <b>grass</b>.\"\n\n👉 <b>Pertanyaan:</b> What does the elephant eat? (Apa yang dimakan gajah?)",
        "expected": [
            "grass",
            "green grass"
        ],
        "primary_answer": "grass"
    },
    {
        "id": "rdg_beg_37",
        "badge": "📖 🏖️ Pantai Minggu: Istana Pasir",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"On Sunday, Maya and her brother built a tall <b>sandcastle</b> on the shore.\"\n\n👉 <b>Pertanyaan:</b> What did Maya and her brother build? (Apa yang dibangun Maya dan kakaknya?)",
        "expected": [
            "sandcastle",
            "a sandcastle",
            "sand castle"
        ],
        "primary_answer": "sandcastle"
    },
    {
        "id": "rdg_beg_38",
        "badge": "📖 🏖️ Pantai Minggu: Jumlah Kerang",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Maya found <b>three</b> pretty pink seashells along the seashore.\"\n\n👉 <b>Pertanyaan:</b> How many seashells did Maya find? (Berapa banyak kerang yang ditemukan Maya?)",
        "expected": [
            "three",
            "3",
            "three seashells"
        ],
        "primary_answer": "three"
    },
    {
        "id": "rdg_beg_39",
        "badge": "📖 🌈 Pelangi Siang: Warna Atas",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"After the heavy rain, a rainbow appeared. The top stripe is <b>red</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the top stripe color of the rainbow? (Apa warna garis teratas pelangi?)",
        "expected": [
            "red",
            "it is red"
        ],
        "primary_answer": "red"
    },
    {
        "id": "rdg_beg_40",
        "badge": "📖 🌈 Pelangi Siang: Waktu Muncul",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"The colorful rainbow appeared right after the <b>rain</b> stopped.\"\n\n👉 <b>Pertanyaan:</b> When did the rainbow appear? (Kapan pelangi itu muncul?)",
        "expected": [
            "after rain",
            "after the rain",
            "rain"
        ],
        "primary_answer": "after rain"
    },
    {
        "id": "rdg_beg_41",
        "badge": "📖 🌹 Menanam Bunga: Jenis Bunga",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Lina loves gardening. She plants a lovely red <b>rose</b> in a ceramic pot.\"\n\n👉 <b>Pertanyaan:</b> What flower does Lina plant? (Bunga apa yang ditanam Lina?)",
        "expected": [
            "rose",
            "a rose",
            "red rose"
        ],
        "primary_answer": "rose"
    },
    {
        "id": "rdg_beg_42",
        "badge": "📖 🌹 Menanam Bunga: Lokasi Pot",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Lina places her new ceramic flower pot on the sunny <b>veranda</b>.\"\n\n👉 <b>Pertanyaan:</b> Where does Lina place the flower pot? (Di mana Lina meletakkan pot bunganya?)",
        "expected": [
            "on the veranda",
            "veranda",
            "the veranda"
        ],
        "primary_answer": "on the veranda"
    },
    {
        "id": "rdg_beg_43",
        "badge": "📖 🍚 Sarapan Pagi: Lauk Telur",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"For breakfast, Mother cooks delicious rice served with a boiled <b>egg</b>.\"\n\n👉 <b>Pertanyaan:</b> What side dish is served with rice? (Lauk apa yang disajikan bersama nasi?)",
        "expected": [
            "egg",
            "boiled egg",
            "an egg"
        ],
        "primary_answer": "egg"
    },
    {
        "id": "rdg_beg_44",
        "badge": "📖 ☕ Sarapan Pagi: Minuman Ayah",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Father reads the morning paper while sipping a cup of black <b>coffee</b>.\"\n\n👉 <b>Pertanyaan:</b> What beverage does Father sip? (Minuman apa yang diseruput Ayah?)",
        "expected": [
            "coffee",
            "black coffee"
        ],
        "primary_answer": "coffee"
    },
    {
        "id": "rdg_beg_45",
        "badge": "📖 🦜 Burung Beo: Ucapan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Rio is a clever green parrot. Every morning, he says \"<b>Good morning!</b>\"\"\n\n👉 <b>Pertanyaan:</b> What greeting does Rio say? (Ucapan salam apa yang dikatakan Rio?)",
        "expected": [
            "good morning",
            "good morning!"
        ],
        "primary_answer": "Good morning"
    },
    {
        "id": "rdg_beg_46",
        "badge": "📖 🦜 Burung Beo: Warna Bulu",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Rio's wings are covered in bright <b>green</b> feathers.\"\n\n👉 <b>Pertanyaan:</b> What color are Rio's feathers? (Apa warna bulu Rio?)",
        "expected": [
            "green",
            "bright green"
        ],
        "primary_answer": "green"
    },
    {
        "id": "rdg_beg_47",
        "badge": "📖 ⏰ Jam Antik: Lokasi",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"There is a grandfather clock ticking steadily in the <b>living room</b>.\"\n\n👉 <b>Pertanyaan:</b> In which room is the grandfather clock? (Di ruangan mana jam dinding tersebut berada?)",
        "expected": [
            "living room",
            "in the living room"
        ],
        "primary_answer": "living room"
    },
    {
        "id": "rdg_beg_48",
        "badge": "📖 ⏰ Jam Antik: Bahan Kayu",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"The historic grandfather clock was carved from dark brown <b>wood</b>.\"\n\n👉 <b>Pertanyaan:</b> What material is the clock made from? (Terbuat dari bahan apa jam tersebut?)",
        "expected": [
            "wood",
            "brown wood"
        ],
        "primary_answer": "wood"
    },
    {
        "id": "rdg_beg_49",
        "badge": "📖 👟 Sepatu Doni: Pemberi Hadiah",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"For his birthday, Doni received running shoes from his <b>aunt</b>.\"\n\n👉 <b>Pertanyaan:</b> Who gave Doni the running shoes? (Siapa yang memberikan sepatu lari pada Doni?)",
        "expected": [
            "his aunt",
            "aunt"
        ],
        "primary_answer": "aunt"
    },
    {
        "id": "rdg_beg_50",
        "badge": "📖 👟 Sepatu Doni: Warna",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Doni is proud of his running shoes because they are bright <b>blue</b>.\"\n\n👉 <b>Pertanyaan:</b> What color are the running shoes? (Apa warna sepatu lari Doni?)",
        "expected": [
            "blue",
            "bright blue"
        ],
        "primary_answer": "blue"
    },
    {
        "id": "rdg_beg_51",
        "badge": "📖 🐱 Kucing Hitam: Nama",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Siti has a quiet black kitten named <b>Shadow</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the kitten's name? (Siapa nama anak kucing tersebut?)",
        "expected": [
            "shadow"
        ],
        "primary_answer": "Shadow"
    },
    {
        "id": "rdg_beg_52",
        "badge": "📖 🐱 Kucing Hitam: Tempat Tidur",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Shadow loves to curl up and sleep on the warm <b>rug</b>.\"\n\n👉 <b>Pertanyaan:</b> Where does Shadow like to sleep? (Di mana Shadow suka tidur?)",
        "expected": [
            "on the rug",
            "rug",
            "the rug"
        ],
        "primary_answer": "on the rug"
    },
    {
        "id": "rdg_beg_53",
        "badge": "📖 🌳 Membaca di Pohon: Bahan Bacaan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"During school break, Edo sits under an oak tree and reads an adventure <b>comic</b>.\"\n\n👉 <b>Pertanyaan:</b> What does Edo read under the tree? (Apa yang dibaca Edo di bawah pohon?)",
        "expected": [
            "comic",
            "a comic",
            "adventure comic"
        ],
        "primary_answer": "comic"
    },
    {
        "id": "rdg_beg_54",
        "badge": "📖 🌳 Membaca di Pohon: Buah Pisang",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Edo's classmate Kiki brings two sweet <b>bananas</b> to share.\"\n\n👉 <b>Pertanyaan:</b> What fruit does Kiki bring? (Buah apa yang dibawa Kiki?)",
        "expected": [
            "bananas",
            "banana",
            "sweet bananas"
        ],
        "primary_answer": "bananas"
    },
    {
        "id": "rdg_beg_55",
        "badge": "📖 ⚽ Sepak Bola Desa: Tempat Main",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Every Saturday afternoon, boys play football at the village <b>field</b>.\"\n\n👉 <b>Pertanyaan:</b> Where do the boys play football? (Di mana anak-anak bermain sepak bola?)",
        "expected": [
            "field",
            "at the field",
            "village field"
        ],
        "primary_answer": "field"
    },
    {
        "id": "rdg_beg_56",
        "badge": "📖 ⚽ Sepak Bola Desa: Warna Bola",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"They kick a classic <b>black and white</b> leather ball.\"\n\n👉 <b>Pertanyaan:</b> What colors are on the ball? (Warna apa yang ada pada bola tersebut?)",
        "expected": [
            "black and white",
            "white and black"
        ],
        "primary_answer": "black and white"
    },
    {
        "id": "rdg_beg_57",
        "badge": "📖 🍲 Membantu Ibu: Sayur Bayam",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Dewi washes fresh green <b>spinach</b> in the kitchen sink.\"\n\n👉 <b>Pertanyaan:</b> What vegetable does Dewi wash? (Sayuran apa yang dicuci Dewi?)",
        "expected": [
            "spinach",
            "green spinach"
        ],
        "primary_answer": "spinach"
    },
    {
        "id": "rdg_beg_58",
        "badge": "📖 🍲 Membantu Ibu: Menu Masakan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Mother cooks a warm pot of nutritious vegetable <b>soup</b>.\"\n\n👉 <b>Pertanyaan:</b> What dish does Mother cook? (Masakan apa yang dimasak Ibu?)",
        "expected": [
            "soup",
            "vegetable soup"
        ],
        "primary_answer": "soup"
    },
    {
        "id": "rdg_beg_59",
        "badge": "📖 🥛 Peternakan Sapi: Minuman Putih",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"At the dairy farm, visitors watch how fresh <b>milk</b> is bottled.\"\n\n👉 <b>Pertanyaan:</b> What beverage is bottled at the dairy farm? (Minuman apa yang dikemas di peternakan?)",
        "expected": [
            "milk",
            "fresh milk"
        ],
        "primary_answer": "milk"
    },
    {
        "id": "rdg_beg_60",
        "badge": "📖 🥛 Peternakan Sapi: Jumlah Sapi",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"The farmer cares for <b>twenty</b> black and white cows in the barn.\"\n\n👉 <b>Pertanyaan:</b> How many cows are in the barn? (Berapa banyak sapi di kandang?)",
        "expected": [
            "twenty",
            "20",
            "twenty cows"
        ],
        "primary_answer": "twenty"
    },
    {
        "id": "rdg_beg_61",
        "badge": "📖 🎨 Kelas Seni: Gambar Pemandangan",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"In art class, students draw a majestic <b>mountain</b> with green hills.\"\n\n👉 <b>Pertanyaan:</b> What scenery object do students draw? (Objek pemandangan apa yang digambar siswa?)",
        "expected": [
            "mountain",
            "a mountain"
        ],
        "primary_answer": "mountain"
    },
    {
        "id": "rdg_beg_62",
        "badge": "📖 🎨 Kelas Seni: Warna Krayon",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Tono colors the lush hills using a bright <b>green</b> crayon.\"\n\n👉 <b>Pertanyaan:</b> What color crayon does Tono use? (Apa warna krayon yang digunakan Tono?)",
        "expected": [
            "green"
        ],
        "primary_answer": "green"
    },
    {
        "id": "rdg_beg_63",
        "badge": "📖 🍉 Kios Buah: Semangka",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Uncle Joko cuts a large round <b>watermelon</b> for customers.\"\n\n👉 <b>Pertanyaan:</b> What fruit does Uncle Joko cut? (Buah apa yang dipotong Paman Joko?)",
        "expected": [
            "watermelon",
            "a watermelon"
        ],
        "primary_answer": "watermelon"
    },
    {
        "id": "rdg_beg_64",
        "badge": "📖 🍉 Kios Buah: Warna Daging Buah",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Inside the watermelon, the sweet juicy flesh is bright <b>red</b>.\"\n\n👉 <b>Pertanyaan:</b> What color is the inside of the watermelon? (Apa warna bagian dalam semangka?)",
        "expected": [
            "red"
        ],
        "primary_answer": "red"
    },
    {
        "id": "rdg_beg_65",
        "badge": "📖 🐸 Hujan Rintik: Katak Menyanyi",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"When gentle rain taps the window, green <b>frogs</b> croak by the pond.\"\n\n👉 <b>Pertanyaan:</b> What animals croak by the pond? (Hewan apa yang bersuara di dekat kolam?)",
        "expected": [
            "frogs",
            "frog",
            "green frogs"
        ],
        "primary_answer": "frogs"
    },
    {
        "id": "rdg_beg_66",
        "badge": "📖 🍵 Hujan Rintik: Minuman Nenek",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Inside the cozy kitchen, Grandmother sips warm <b>ginger</b> tea.\"\n\n👉 <b>Pertanyaan:</b> What kind of tea does Grandmother sip? (Jenis teh apa yang diseruput Nenek?)",
        "expected": [
            "ginger tea",
            "ginger",
            "warm ginger tea"
        ],
        "primary_answer": "ginger tea"
    },
    {
        "id": "rdg_beg_67",
        "badge": "📖 ⭐ Langit Malam: Bintang",
        "prompt": "📖 <b>Baca teks pendek berikut:</b>\n\"Looking through the window, Lani counted <b>seven</b> bright stars in the sky.\"\n\n👉 <b>Pertanyaan:</b> How many stars did Lani count? (Berapa banyak bintang yang dihitung Lani?)",
        "expected": [
            "seven",
            "7",
            "seven stars"
        ],
        "primary_answer": "seven"
    }
],
    config.LEVEL_INTERMEDIATE: [
    {
        "id": "rdg_int_01",
        "badge": "🐢 Dongeng Kura-kura: Pemenang",
        "prompt": "🏁 <b>Baca fabel klasik berikut:</b>\n\"The speedy hare boasted that no one could beat him in a footrace. The slow tortoise accepted the challenge. While the hare took a nap under an oak tree, the tortoise kept walking steadily and crossed the finish line first.\"\n\n👉 <b>Pertanyaan:</b> Who won the footrace? (Siapa pemenang lomba lari tersebut?)",
        "expected": [
            "tortoise",
            "the tortoise",
            "the slow tortoise"
        ],
        "primary_answer": "the tortoise"
    },
    {
        "id": "rdg_int_02",
        "badge": "🐇 Dongeng Kura-kura: Kesalahan Kelinci",
        "prompt": "😴 <b>Baca fabel klasik berikut:</b>\n\"Confident of an easy victory, the hare stopped halfway and decided to take a <b>nap</b> under a shady tree. Because he fell asleep, he lost the race.\"\n\n👉 <b>Pertanyaan:</b> What did the hare do that caused him to lose? (Apa yang kelinci lakukan sehingga ia kalah?)",
        "expected": [
            "slept",
            "take a nap",
            "nap",
            "he slept",
            "fell asleep",
            "he took a nap"
        ],
        "primary_answer": "took a nap"
    },
    {
        "id": "rdg_int_03",
        "badge": "☀️ Tata Surya: Planet Terdekat",
        "prompt": "🪐 <b>Baca teks sains berikut:</b>\n\"Our solar system contains eight planets orbiting the sun. <b>Mercury</b> is the planet closest to the sun, making its daytime temperatures scorching hot.\"\n\n👉 <b>Pertanyaan:</b> Which planet is closest to the sun? (Planet mana yang paling dekat dengan matahari?)",
        "expected": [
            "mercury",
            "planet mercury"
        ],
        "primary_answer": "Mercury"
    },
    {
        "id": "rdg_int_04",
        "badge": "🌙 Tata Surya: Satelit Bumi",
        "prompt": "🌕 <b>Baca teks sains berikut:</b>\n\"Earth has only one natural satellite: the <b>Moon</b>. It orbits Earth once every twenty-seven days and causes ocean tides.\"\n\n👉 <b>Pertanyaan:</b> What is Earth's only natural satellite? (Apa satu-satunya satelit alami Bumi?)",
        "expected": [
            "the moon",
            "moon"
        ],
        "primary_answer": "the Moon"
    },
    {
        "id": "rdg_int_05",
        "badge": "🐝 Lebah Madu: Hasil Produksi",
        "prompt": "🍯 <b>Baca teks biologi berikut:</b>\n\"Honeybees are essential pollinators in nature. They gather sweet nectar from blooming wildflowers and transform it into golden <b>honey</b> inside their comb.\"\n\n👉 <b>Pertanyaan:</b> What do bees produce from nectar? (Apa yang dihasilkan lebah dari nektar?)",
        "expected": [
            "honey",
            "golden honey"
        ],
        "primary_answer": "honey"
    },
    {
        "id": "rdg_int_06",
        "badge": "🐝 Lebah Madu: Tempat Tinggal",
        "prompt": "🏡 <b>Baca teks biologi berikut:</b>\n\"A colony of thousands of worker bees and one queen bee resides together in a complex structure called a <b>beehive</b>.\"\n\n👉 <b>Pertanyaan:</b> Where does a bee colony live? (Di mana koloni lebah tinggal?)",
        "expected": [
            "beehive",
            "hive",
            "in a beehive",
            "a beehive"
        ],
        "primary_answer": "beehive"
    },
    {
        "id": "rdg_int_07",
        "badge": "🏕️ Berkemah di Hutan: Tempat Tidur",
        "prompt": "⛺ <b>Baca catatan perjalanan berikut:</b>\n\"During our weekend expedition in the pine forest, we pitched a waterproof <b>tent</b> on high ground to keep dry and safe overnight.\"\n\n👉 <b>Pertanyaan:</b> Where did the campers sleep? (Di mana para peserta kemah tidur?)",
        "expected": [
            "tent",
            "in a tent",
            "waterproof tent",
            "a tent"
        ],
        "primary_answer": "in a tent"
    },
    {
        "id": "rdg_int_08",
        "badge": "🏕️ Berkemah di Hutan: Makanan Api Unggun",
        "prompt": "🔥 <b>Baca catatan perjalanan berikut:</b>\n\"Around the campfire at night, the students sang songs and roasted sweet white <b>marshmallows</b> on wooden sticks.\"\n\n👉 <b>Pertanyaan:</b> What sweet treat did they roast over the campfire? (Camilan manis apa yang mereka panggang?)",
        "expected": [
            "marshmallows",
            "marshmallow",
            "white marshmallows"
        ],
        "primary_answer": "marshmallows"
    },
    {
        "id": "rdg_int_09",
        "badge": "🔬 Pameran Sains: Model Eka",
        "prompt": "🌋 <b>Baca teks kegiatan sekolah:</b>\n\"At the annual school science exhibition, Eka constructed a working model of a miniature <b>volcano</b> using baking soda and red food coloring to simulate lava.\"\n\n👉 <b>Pertanyaan:</b> What did Eka build for the science exhibition? (Apa yang dibuat Eka untuk pameran sains?)",
        "expected": [
            "volcano",
            "a volcano",
            "miniature volcano"
        ],
        "primary_answer": "a volcano"
    },
    {
        "id": "rdg_int_10",
        "badge": "🔬 Pameran Sains: Medali Pemenang",
        "prompt": "🥇 <b>Baca teks kegiatan sekolah:</b>\n\"The science judges were thoroughly impressed by the creative presentation and awarded the team a shiny <b>gold</b> medal.\"\n\n👉 <b>Pertanyaan:</b> What type of medal did the team win? (Jenis medali apa yang dimenangkan tim?)",
        "expected": [
            "gold",
            "gold medal",
            "a gold medal"
        ],
        "primary_answer": "gold medal"
    },
    {
        "id": "rdg_int_11",
        "badge": "🐬 Lumba-lumba: Golongan Hewan",
        "prompt": "🌊 <b>Baca teks zoologi berikut:</b>\n\"Although dolphins spend their entire lives swimming in oceans, they are not fish. Dolphins are warm-blooded <b>mammals</b> that give birth to live calves.\"\n\n👉 <b>Pertanyaan:</b> What biological group do dolphins belong to? (Golongan hewan apakah lumba-lumba?)",
        "expected": [
            "mammal",
            "mammals",
            "warm-blooded mammals"
        ],
        "primary_answer": "mammal"
    },
    {
        "id": "rdg_int_12",
        "badge": "🐬 Lumba-lumba: Organ Pernapasan",
        "prompt": "💨 <b>Baca teks zoologi berikut:</b>\n\"Dolphins come up to the ocean surface to inhale air through a special hole on top of their heads called a <b>blowhole</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the breathing hole on top of a dolphin's head called? (Apa nama lubang pernapasan di kepala lumba-lumba?)",
        "expected": [
            "blowhole",
            "a blowhole"
        ],
        "primary_answer": "blowhole"
    },
    {
        "id": "rdg_int_13",
        "badge": "🎨 Kain Batik: Asal Negara",
        "prompt": "🇮🇩 <b>Baca teks warisan budaya berikut:</b>\n\"Batik is a revered traditional textile technique celebrated globally. It originated and flourished across <b>Indonesia</b>, recognized as UNESCO intangible heritage.\"\n\n👉 <b>Pertanyaan:</b> From which country does traditional batik originate? (Dari negara mana batik tradisional berasal?)",
        "expected": [
            "indonesia",
            "from indonesia"
        ],
        "primary_answer": "Indonesia"
    },
    {
        "id": "rdg_int_14",
        "badge": "🎨 Kain Batik: Alat Canting",
        "prompt": "🖋️ <b>Baca teks warisan budaya berikut:</b>\n\"Artisans use a small copper spouted instrument called a <b>canting</b> to apply hot liquid wax onto fine cotton fabric.\"\n\n👉 <b>Pertanyaan:</b> What is the copper tool used to draw wax called? (Apa nama alat tembaga untuk menorehkan malam lilin?)",
        "expected": [
            "canting",
            "a canting"
        ],
        "primary_answer": "canting"
    },
    {
        "id": "rdg_int_15",
        "badge": "🏰 Kastil Kuno: Penguasa",
        "prompt": "👑 <b>Baca teks sejarah berikut:</b>\n\"Perched high on the rocky cliff, the medieval stone fortress served as the majestic residence of the wise <b>king</b> and his court.\"\n\n👉 <b>Pertanyaan:</b> Who lived in the medieval fortress? (Siapa yang tinggal di benteng batu abad pertengahan tersebut?)",
        "expected": [
            "king",
            "the king",
            "the wise king",
            "a king"
        ],
        "primary_answer": "the king"
    },
    {
        "id": "rdg_int_16",
        "badge": "🏰 Kastil Kuno: Parit Pertahanan",
        "prompt": "🛡️ <b>Baca teks sejarah berikut:</b>\n\"To prevent invaders from reaching the main gateway, the castle was encircled by a deep wide channel filled with water called a <b>moat</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the defensive water trench around the castle called? (Apa sebutan parit berair di sekeliling benteng?)",
        "expected": [
            "moat",
            "a moat"
        ],
        "primary_answer": "moat"
    },
    {
        "id": "rdg_int_17",
        "badge": "☀️ Energi Terbarukan: Tenaga Surya",
        "prompt": "⚡ <b>Baca teks energi hijau berikut:</b>\n\"Solar panels installed on rooftops absorb radiant sunlight and transform it into clean <b>electricity</b> without emitting harmful smoke.\"\n\n👉 <b>Pertanyaan:</b> What do solar panels generate from sunlight? (Apa yang dihasilkan panel surya dari sinar matahari?)",
        "expected": [
            "electricity",
            "clean electricity",
            "power"
        ],
        "primary_answer": "electricity"
    },
    {
        "id": "rdg_int_18",
        "badge": "💨 Energi Terbarukan: Kincir Angin",
        "prompt": "🍃 <b>Baca teks energi hijau berikut:</b>\n\"Giant wind turbines built across breezy coastal hills harness kinetic energy from the <b>wind</b> to drive modern electrical generators.\"\n\n👉 <b>Pertanyaan:</b> What natural force turns wind turbines? (Kekuatan alam apa yang memutar turbin kincir angin?)",
        "expected": [
            "wind",
            "the wind",
            "kinetic energy of wind"
        ],
        "primary_answer": "wind"
    },
    {
        "id": "rdg_int_19",
        "badge": "🌋 Wisata Gunung Bromo: Waktu Bangun",
        "prompt": "⏰ <b>Baca teks pariwisata berikut:</b>\n\"To catch the breathtaking dawn over the active caldera, tourists must wake up very early at <b>three</b> in the morning.\"\n\n👉 <b>Pertanyaan:</b> At what hour in the morning do tourists wake up? (Jam berapa di pagi hari para wisatawan bangun?)",
        "expected": [
            "three",
            "3",
            "3 am",
            "3:00 am",
            "three in the morning"
        ],
        "primary_answer": "3 AM"
    },
    {
        "id": "rdg_int_20",
        "badge": "🌄 Wisata Gunung Bromo: Pemandangan",
        "prompt": "🌅 <b>Baca teks pariwisata berikut:</b>\n\"From the summit of Mount Penanjakan, travelers witness a legendary golden <b>sunrise</b> rising above the sea of sand.\"\n\n👉 <b>Pertanyaan:</b> What natural morning spectacle do travelers witness? (Pemandangan pagi hari apa yang disaksikan wisatawan?)",
        "expected": [
            "sunrise",
            "golden sunrise",
            "the sunrise"
        ],
        "primary_answer": "sunrise"
    },
    {
        "id": "rdg_int_21",
        "badge": "🦅 Burung Gagak yang Pintar: Batu Kerikil",
        "prompt": "🪨 <b>Baca fabel klasik berikut:</b>\n\"A thirsty crow saw a jar with water at the bottom. Unable to reach it, the bird dropped small <b>pebbles</b> into the jar until the water level rose to the brim.\"\n\n👉 <b>Pertanyaan:</b> What did the crow drop into the jar? (Benda apa yang dimasukkan burung gagak ke dalam bejana?)",
        "expected": [
            "pebbles",
            "pebble",
            "stones",
            "small pebbles"
        ],
        "primary_answer": "pebbles"
    },
    {
        "id": "rdg_int_22",
        "badge": "🦅 Burung Gagak yang Pintar: Wadah Air",
        "prompt": "🏺 <b>Baca fabel klasik berikut:</b>\n\"The clever crow found an earthenware <b>jar</b> in the backyard that contained a small amount of fresh water.\"\n\n👉 <b>Pertanyaan:</b> What container held the fresh water? (Wadah apa yang berisi air tawar tersebut?)",
        "expected": [
            "jar",
            "a jar",
            "pitcher"
        ],
        "primary_answer": "jar"
    },
    {
        "id": "rdg_int_23",
        "badge": "🪸 Terumbu Karang: Julukan",
        "prompt": "🌊 <b>Baca teks ekologi kelautan:</b>\n\"Due to their astonishing wealth of aquatic biodiversity, coral reefs are often affectionately nicknamed the <b>rainforests</b> of the sea.\"\n\n👉 <b>Pertanyaan:</b> Coral reefs are nicknamed the 'what' of the sea? (Terumbu karang dijuluki sebagai apa di lautan?)",
        "expected": [
            "rainforests",
            "rainforest",
            "rainforests of the sea"
        ],
        "primary_answer": "rainforests"
    },
    {
        "id": "rdg_int_24",
        "badge": "🪸 Terumbu Karang: Ancaman",
        "prompt": "🌡️ <b>Baca teks ekologi kelautan:</b>\n\"Rising sea water temperatures and chemical <b>pollution</b> represent severe threats causing extensive coral bleaching.\"\n\n👉 <b>Pertanyaan:</b> Name one major threat to coral reefs mentioned: (Sebutkan salah satu ancaman utama bagi terumbu karang:)",
        "expected": [
            "pollution",
            "temperature",
            "rising temperatures",
            "chemical pollution"
        ],
        "primary_answer": "pollution"
    },
    {
        "id": "rdg_int_25",
        "badge": "📖 🦎 Komodo Dragon: Pulau Habitat",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The Komodo dragon is the world's largest living lizard species. It is endemic to the Indonesian island of <b>Komodo</b> and neighboring Flores.\"\n\n👉 <b>Pertanyaan:</b> On which Indonesian island is this lizard found? (Di pulau Indonesia mana kadal ini ditemukan?)",
        "expected": [
            "komodo",
            "komodo island",
            "island of komodo"
        ],
        "primary_answer": "Komodo"
    },
    {
        "id": "rdg_int_26",
        "badge": "📖 🦎 Komodo Dragon: Mangsa",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Using sharp serrated teeth and venomous saliva, Komodo dragons hunt large prey like wild <b>deer</b> and water buffaloes.\"\n\n👉 <b>Pertanyaan:</b> What large animal do Komodo dragons hunt? (Hewan besar apa yang diburu komodo?)",
        "expected": [
            "deer",
            "wild deer",
            "buffaloes"
        ],
        "primary_answer": "deer"
    },
    {
        "id": "rdg_int_27",
        "badge": "📖 ☕ Kopi Luwak: Hewan Luwak",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Kopi Luwak is a unique coffee variety produced from beans collected after ingestion by the Asian palm <b>civet</b>.\"\n\n👉 <b>Pertanyaan:</b> Which animal digests the coffee cherries? (Hewan apa yang mencerna buah kopi tersebut?)",
        "expected": [
            "civet",
            "asian palm civet",
            "palm civet"
        ],
        "primary_answer": "civet"
    },
    {
        "id": "rdg_int_28",
        "badge": "📖 ☕ Kopi Luwak: Rasa Khas",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Fermentation inside the animal's digestive tract gives the brewed coffee a remarkably <b>smooth</b> and less bitter aroma.\"\n\n👉 <b>Pertanyaan:</b> How is the taste described? (Bagaimana rasa kopi tersebut digambarkan?)",
        "expected": [
            "smooth",
            "less bitter"
        ],
        "primary_answer": "smooth"
    },
    {
        "id": "rdg_int_29",
        "badge": "📖 🌋 Danau Toba: Asal Letusan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Lake Toba in North Sumatra was formed by an immense volcanic super-eruption roughly <b>seventy thousand</b> years ago.\"\n\n👉 <b>Pertanyaan:</b> How many years ago did the super-eruption occur? (Berapa tahun lalu letusan dahsyat tersebut terjadi?)",
        "expected": [
            "70000",
            "70,000",
            "seventy thousand",
            "70000 years ago"
        ],
        "primary_answer": "70,000"
    },
    {
        "id": "rdg_int_30",
        "badge": "📖 🌋 Danau Toba: Pulau di Tengah",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"In the center of the vast lake lies a magnificent volcanic island known as <b>Samosir</b> Island.\"\n\n👉 <b>Pertanyaan:</b> What is the name of the island in the center? (Apa nama pulau di tengah danau tersebut?)",
        "expected": [
            "samosir",
            "samosir island"
        ],
        "primary_answer": "Samosir"
    },
    {
        "id": "rdg_int_31",
        "badge": "📖 🏛️ Candi Borobudur: Abad Dibangun",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Borobudur is the world's largest Buddhist temple monument. It was erected during the <b>ninth</b> century by the Sailendra dynasty.\"\n\n👉 <b>Pertanyaan:</b> In which century was Borobudur constructed? (Pada abad ke berapa Borobudur didirikan?)",
        "expected": [
            "ninth",
            "9th",
            "9th century",
            "ninth century"
        ],
        "primary_answer": "ninth"
    },
    {
        "id": "rdg_int_32",
        "badge": "📖 🏛️ Candi Borobudur: Bahan Batu",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The monumental tiers were constructed using millions of carved volcanic <b>andesite</b> stones without any cement.\"\n\n👉 <b>Pertanyaan:</b> What volcanic stone was used to build Borobudur? (Batu vulkanik apa yang dipakai membangun Borobudur?)",
        "expected": [
            "andesite",
            "andesite stone",
            "volcanic andesite"
        ],
        "primary_answer": "andesite"
    },
    {
        "id": "rdg_int_33",
        "badge": "📖 🦧 Orangutan Kalimantan: Sarang",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Bornean orangutans are intelligent great apes that spend their days foraging fruit and sleeping in treetop <b>nests</b>.\"\n\n👉 <b>Pertanyaan:</b> Where do orangutans sleep at night? (Di mana orangutan tidur pada malam hari?)",
        "expected": [
            "nests",
            "treetop nests",
            "in nests",
            "in trees"
        ],
        "primary_answer": "treetop nests"
    },
    {
        "id": "rdg_int_34",
        "badge": "📖 🦧 Orangutan Kalimantan: Makanan Utama",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Over sixty percent of an orangutan's daily diet consists of sweet forest <b>fruit</b> like figs and durians.\"\n\n👉 <b>Pertanyaan:</b> What makes up over 60 percent of their diet? (Apa yang menyusun lebih dari 60 persen makanan mereka?)",
        "expected": [
            "fruit",
            "forest fruit",
            "fruits"
        ],
        "primary_answer": "fruit"
    },
    {
        "id": "rdg_int_35",
        "badge": "📖 🌺 Bunga Rafflesia: Bau Busuk",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Rafflesia arnoldii produces the world's largest single flower. It emits a strong odor resembling rotting <b>meat</b> to attract flies.\"\n\n👉 <b>Pertanyaan:</b> What does the flower's smell resemble? (Mirip bau apakah aroma bunga tersebut?)",
        "expected": [
            "rotting meat",
            "meat"
        ],
        "primary_answer": "rotting meat"
    },
    {
        "id": "rdg_int_36",
        "badge": "📖 🌺 Bunga Rafflesia: Penyerbuk",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The pungent smell attracts carrion <b>flies</b> that carry pollen from one bloom to another.\"\n\n👉 <b>Pertanyaan:</b> Which insect acts as pollinator for Rafflesia? (Serangga apa yang menjadi penyerbuk Rafflesia?)",
        "expected": [
            "flies",
            "carrion flies",
            "fly"
        ],
        "primary_answer": "flies"
    },
    {
        "id": "rdg_int_37",
        "badge": "📖 🔭 Teleskop Luar Angkasa: Hubble",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Orbiting high above Earth's atmosphere, the <b>Hubble</b> Space Telescope captures ultra-clear cosmic images without cloud distortion.\"\n\n👉 <b>Pertanyaan:</b> What is the name of this famous space telescope? (Apa nama teleskop luar angkasa terkenal ini?)",
        "expected": [
            "hubble",
            "hubble telescope",
            "hubble space telescope"
        ],
        "primary_answer": "Hubble"
    },
    {
        "id": "rdg_int_38",
        "badge": "📖 🔭 Teleskop Luar Angkasa: Penemuan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Hubble provided crucial data helping astronomers measure the expansion rate of our <b>universe</b>.\"\n\n👉 <b>Pertanyaan:</b> What cosmic entity's expansion did Hubble measure? (Ekspansi apa yang diukur oleh Hubble?)",
        "expected": [
            "universe",
            "the universe"
        ],
        "primary_answer": "universe"
    },
    {
        "id": "rdg_int_39",
        "badge": "📖 🐧 Burung Penguin Antartika: Bulu Kedap",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Emperor penguins survive freezing polar blizzards thanks to their dense waterproof <b>feathers</b> and a thick layer of fat.\"\n\n👉 <b>Pertanyaan:</b> What dense covering keeps penguins warm? (Lapisan lebat apa yang menjaga penguin tetap hangat?)",
        "expected": [
            "feathers",
            "waterproof feathers"
        ],
        "primary_answer": "feathers"
    },
    {
        "id": "rdg_int_40",
        "badge": "📖 🐧 Burung Penguin Antartika: Makanan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"To nourish themselves and their chicks, adult penguins dive into icy seas to catch krill and <b>fish</b>.\"\n\n👉 <b>Pertanyaan:</b> What sea creature do penguins catch to eat? (Hewan laut apa yang ditangkap penguin?)",
        "expected": [
            "fish",
            "krill and fish",
            "krill"
        ],
        "primary_answer": "fish"
    },
    {
        "id": "rdg_int_41",
        "badge": "📖 🚂 Kereta Cepat Jakarta-Bandung: Kecepatan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The Whoosh high-speed railway connects Jakarta and Bandung, reaching a top operational speed of <b>350</b> kilometers per hour.\"\n\n👉 <b>Pertanyaan:</b> What is the maximum operational speed in km/h? (Berapa kecepatan puncak operasionalnya dalam km/jam?)",
        "expected": [
            "350",
            "350 km/h",
            "350 kilometers per hour"
        ],
        "primary_answer": "350"
    },
    {
        "id": "rdg_int_42",
        "badge": "📖 🚂 Kereta Cepat Jakarta-Bandung: Waktu Tempuh",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Passengers can travel between the two cities in just <b>forty-five</b> minutes, drastically reducing road traffic.\"\n\n👉 <b>Pertanyaan:</b> How many minutes does the journey take? (Berapa menit waktu tempuh perjalanan tersebut?)",
        "expected": [
            "forty-five",
            "45",
            "45 minutes",
            "forty five minutes"
        ],
        "primary_answer": "forty-five"
    },
    {
        "id": "rdg_int_43",
        "badge": "📖 🌱 Hutan Bakau Mangrove: Penahan Ombak",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Mangrove forests lining coastlines protect shorelines from severe erosion caused by heavy ocean <b>waves</b>.\"\n\n👉 <b>Pertanyaan:</b> What ocean force do mangroves protect shores from? (Dari kekuatan laut apa mangrove melindungi pantai?)",
        "expected": [
            "waves",
            "ocean waves",
            "erosion"
        ],
        "primary_answer": "waves"
    },
    {
        "id": "rdg_int_44",
        "badge": "📖 🌱 Hutan Bakau Mangrove: Penyimpan Karbon",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Mangrove root systems trap sediment and store massive amounts of <b>carbon</b> beneath the muddy soil.\"\n\n👉 <b>Pertanyaan:</b> What element do mangrove roots store in large quantities? (Unsur apa yang disimpan dalam jumlah besar oleh akar bakau?)",
        "expected": [
            "carbon"
        ],
        "primary_answer": "carbon"
    },
    {
        "id": "rdg_int_45",
        "badge": "📖 🍫 Pohon Kakao Cokelat: Bagian Biji",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Chocolate is crafted from the fermented seeds, commonly called <b>beans</b>, found inside large cocoa pods.\"\n\n👉 <b>Pertanyaan:</b> What part of the cocoa pod is used to make chocolate? (Bagian apa dari buah kakao yang diolah menjadi cokelat?)",
        "expected": [
            "beans",
            "seeds",
            "cocoa beans"
        ],
        "primary_answer": "beans"
    },
    {
        "id": "rdg_int_46",
        "badge": "📖 🍫 Pohon Kakao Cokelat: Daerah Tumbuh",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Cocoa trees flourish primarily in warm tropical regions located near the <b>equator</b>.\"\n\n👉 <b>Pertanyaan:</b> Near what geographical line do cocoa trees thrive? (Di dekat garis geografis apa pohon kakao tumbuh subur?)",
        "expected": [
            "equator",
            "the equator"
        ],
        "primary_answer": "equator"
    },
    {
        "id": "rdg_int_47",
        "badge": "📖 ⚡ Petir dan Badai: Kecepatan Cahaya",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"During a thunderstorm, we see lightning before hearing thunder because light travels far <b>faster</b> than sound.\"\n\n👉 <b>Pertanyaan:</b> Why do we see lightning before thunder? (Mengapa kita melihat kilat sebelum guntur?)",
        "expected": [
            "faster",
            "light travels faster",
            "light is faster than sound"
        ],
        "primary_answer": "light is faster"
    },
    {
        "id": "rdg_int_48",
        "badge": "📖 ⚡ Petir dan Badai: Muatan Listrik",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Lightning is a sudden massive discharge of static <b>electricity</b> between clouds and the earth.\"\n\n👉 <b>Pertanyaan:</b> Lightning is a discharge of what? (Kilat adalah pelepasan dari apa?)",
        "expected": [
            "electricity",
            "static electricity"
        ],
        "primary_answer": "electricity"
    },
    {
        "id": "rdg_int_49",
        "badge": "📖 🏰 Candi Prambanan: Dewa Siwa",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Prambanan is Indonesia's largest Hindu temple compound. Its soaring central shrine is dedicated to Lord <b>Shiva</b>.\"\n\n👉 <b>Pertanyaan:</b> To which deity is the central shrine dedicated? (Untuk dewa siapa candi utama didedikasikan?)",
        "expected": [
            "shiva",
            "lord shiva"
        ],
        "primary_answer": "Shiva"
    },
    {
        "id": "rdg_int_50",
        "badge": "📖 🏰 Candi Prambanan: Relief Ramayana",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The inner balustrades of the temple are decorated with stone carvings illustrating the epic story of <b>Ramayana</b>.\"\n\n👉 <b>Pertanyaan:</b> Which epic story is carved on the balustrades? (Kisah wiracarita apa yang terukir di dinding candi?)",
        "expected": [
            "ramayana",
            "the ramayana"
        ],
        "primary_answer": "Ramayana"
    },
    {
        "id": "rdg_int_51",
        "badge": "📖 🌊 Siklus Air Bumi: Penguapan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Water from oceans evaporates into vapor under the warmth of the <b>sun</b>, rising to form clouds.\"\n\n👉 <b>Pertanyaan:</b> What celestial body warms ocean water to evaporate? (Benda langit apa yang menghangatkan air laut hingga menguap?)",
        "expected": [
            "the sun",
            "sun"
        ],
        "primary_answer": "sun"
    },
    {
        "id": "rdg_int_52",
        "badge": "📖 🌊 Siklus Air Bumi: Hujan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"When clouds cool and condense, moisture falls back to the surface as <b>rain</b>.\"\n\n👉 <b>Pertanyaan:</b> What does condensed cloud moisture fall as? (Kelembapan awan jatuh kembali sebagai apa?)",
        "expected": [
            "rain",
            "rainfall"
        ],
        "primary_answer": "rain"
    },
    {
        "id": "rdg_int_53",
        "badge": "📖 🍯 Lebah Ratu: Tugas Utama",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"In a honeybee hive, the sole function of the fertile queen bee is to lay thousands of <b>eggs</b> each day.\"\n\n👉 <b>Pertanyaan:</b> What does the queen bee lay thousands of every day? (Apa yang ditelurkan ratu lebah setiap hari?)",
        "expected": [
            "eggs",
            "bee eggs"
        ],
        "primary_answer": "eggs"
    },
    {
        "id": "rdg_int_54",
        "badge": "📖 🍯 Lebah Ratu: Makanan Spesial",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Worker bees feed royal larvae a special nutrient-rich secretion called <b>royal jelly</b>.\"\n\n👉 <b>Pertanyaan:</b> What special food develops a queen bee? (Makanan khusus apa yang menumbuhkan seekor ratu lebah?)",
        "expected": [
            "royal jelly"
        ],
        "primary_answer": "royal jelly"
    },
    {
        "id": "rdg_int_55",
        "badge": "📖 🐢 Penyu Laut: Tempat Bertelur",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Female sea turtles return to the exact sandy <b>beach</b> where they were born to lay their eggs.\"\n\n👉 <b>Pertanyaan:</b> Where do female sea turtles lay their eggs? (Di mana penyu betina bertelur?)",
        "expected": [
            "beach",
            "sandy beach",
            "on the beach"
        ],
        "primary_answer": "beach"
    },
    {
        "id": "rdg_int_56",
        "badge": "📖 🐢 Penyu Laut: Umur Panjang",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Sea turtles can live for over <b>eighty</b> years, swimming thousands of miles across oceanic currents.\"\n\n👉 <b>Pertanyaan:</b> How many years can sea turtles live? (Berapa tahun penyu laut dapat hidup?)",
        "expected": [
            "eighty",
            "80",
            "80 years",
            "eighty years"
        ],
        "primary_answer": "eighty"
    },
    {
        "id": "rdg_int_57",
        "badge": "📖 🌾 Sawah Terasering: Bali Subak",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The stunning terraced rice fields in Bali are maintained through a centuries-old community water management system called <b>Subak</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the ancient Balinese water system called? (Apa nama sistem irigasi kuno di Bali?)",
        "expected": [
            "subak"
        ],
        "primary_answer": "Subak"
    },
    {
        "id": "rdg_int_58",
        "badge": "📖 🌾 Sawah Terasering: Filosofi Harmoni",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The Subak system embodies the philosophy of Tri Hita Karana, promoting harmony between people, nature, and the <b>Creator</b>.\"\n\n👉 <b>Pertanyaan:</b> Subak promotes harmony between humans, nature, and whom? (Subak memelihara keselarasan antara manusia, alam, dan siapa?)",
        "expected": [
            "creator",
            "god",
            "the creator"
        ],
        "primary_answer": "Creator"
    },
    {
        "id": "rdg_int_59",
        "badge": "📖 🫀 Jantung Manusia: Fungsi Pompa",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The human heart beats over one hundred thousand times daily to pump oxygenated <b>blood</b> through blood vessels.\"\n\n👉 <b>Pertanyaan:</b> What liquid does the heart pump through the body? (Cairan apa yang dipompa jantung ke seluruh tubuh?)",
        "expected": [
            "blood",
            "oxygenated blood"
        ],
        "primary_answer": "blood"
    },
    {
        "id": "rdg_int_60",
        "badge": "📖 🫀 Jantung Manusia: Jumlah Ruang",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The human heart is divided into <b>four</b> chambers: two atria and two ventricles.\"\n\n👉 <b>Pertanyaan:</b> How many chambers does the heart have? (Berapa banyak ruang yang dimiliki jantung manusia?)",
        "expected": [
            "four",
            "4",
            "four chambers"
        ],
        "primary_answer": "four"
    },
    {
        "id": "rdg_int_61",
        "badge": "📖 🌋 Gunung Krakatau: Tahun Letusan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"The catastrophic eruption of Krakatoa in the Sunda Strait occurred in the year <b>1883</b>, triggering global tsunamis.\"\n\n👉 <b>Pertanyaan:</b> In what year did Krakatoa erupt cataclysmically? (Pada tahun berapa Krakatau meletus dahsyat?)",
        "expected": [
            "1883",
            "in 1883"
        ],
        "primary_answer": "1883"
    },
    {
        "id": "rdg_int_62",
        "badge": "📖 🌋 Gunung Krakatau: Anak Krakatau",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Decades after the 1883 collapse, a new volcanic cone emerged from the sea named <b>Anak Krakatau</b>.\"\n\n👉 <b>Pertanyaan:</b> What is the name of the new volcanic island that emerged? (Apa nama pulau gunung baru yang muncul?)",
        "expected": [
            "anak krakatau"
        ],
        "primary_answer": "Anak Krakatau"
    },
    {
        "id": "rdg_int_63",
        "badge": "📖 🎨 Rumah Gadang Minangkabau: Bentuk Atap",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Rumah Gadang is traditional architecture in West Sumatra famous for roof peaks shaped like buffalo <b>horns</b>.\"\n\n👉 <b>Pertanyaan:</b> What animal part do the roof peaks resemble? (Bagian hewan apa yang mirip dengan lengkungan atap Rumah Gadang?)",
        "expected": [
            "horns",
            "buffalo horns"
        ],
        "primary_answer": "horns"
    },
    {
        "id": "rdg_int_64",
        "badge": "📖 🎨 Rumah Gadang Minangkabau: Sistem Kekerabatan",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Minangkabau society is renowned for practicing a <b>matrilineal</b> heritage system where ancestral property passes through women.\"\n\n👉 <b>Pertanyaan:</b> What heritage lineage system does Minangkabau follow? (Sistem garis keturunan apa yang dianut Minangkabau?)",
        "expected": [
            "matrilineal",
            "matrilineal system"
        ],
        "primary_answer": "matrilineal"
    },
    {
        "id": "rdg_int_65",
        "badge": "📖 🪐 Cincin Planet Saturnus: Es dan Batu",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Saturn is encircled by dazzling rings composed of billions of pieces of water <b>ice</b> and rocky debris.\"\n\n👉 <b>Pertanyaan:</b> What substance primarily makes up Saturn's rings along with rocks? (Zat apa yang menyusun cincin Saturnus selain bebatuan?)",
        "expected": [
            "ice",
            "water ice"
        ],
        "primary_answer": "ice"
    },
    {
        "id": "rdg_int_66",
        "badge": "📖 🪐 Cincin Planet Saturnus: Satelit Terbesar",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Saturn's largest moon, named <b>Titan</b>, possesses a thick atmosphere and liquid methane lakes.\"\n\n👉 <b>Pertanyaan:</b> What is the name of Saturn's largest moon? (Apa nama bulan terbesar di Saturnus?)",
        "expected": [
            "titan"
        ],
        "primary_answer": "Titan"
    },
    {
        "id": "rdg_int_67",
        "badge": "📖 🌲 Fotosintesis Daun: Klorofil",
        "prompt": "📖 <b>Baca teks informatif berikut:</b>\n\"Leaves appear green because they contain a specialized pigment called <b>chlorophyll</b> that absorbs sunlight.\"\n\n👉 <b>Pertanyaan:</b> What green pigment absorbs solar energy in leaves? (Pigmen hijau apa yang menyerap energi surya pada daun?)",
        "expected": [
            "chlorophyll"
        ],
        "primary_answer": "chlorophyll"
    }
],
    config.LEVEL_ADVANCED: [
    {
        "id": "rdg_adv_01",
        "badge": "🤖 AI di Bidang Medis: Manfaat Utama",
        "prompt": "🩺 <b>Baca teks teknologi medis berikut:</b>\n\"Modern hospitals are rapidly integrating machine learning into their clinical workflows. Artificial Intelligence algorithms trained on millions of radiological scans assist physicians in achieving accurate <b>early diagnosis</b> of complex conditions. By detecting anomalies before symptoms become severe, these diagnostic systems drastically increase patient survival rates.\"\n\n👉 <b>Pertanyaan:</b> What key diagnostic benefit does AI provide according to the passage? (Manfaat diagnostik utama apa yang diberikan AI?)",
        "expected": [
            "early diagnosis",
            "accurate early diagnosis",
            "diagnosis",
            "early detection",
            "an accurate early diagnosis"
        ],
        "primary_answer": "early diagnosis"
    },
    {
        "id": "rdg_adv_02",
        "badge": "🤖 AI di Bidang Medis: Pengawasan Dokter",
        "prompt": "👩‍⚕️ <b>Baca teks teknologi medis berikut:</b>\n\"Although algorithmic diagnostic tools can process medical imaging in seconds, they are not infallible. Despite automated machine precision, medical ethicists emphasize that final clinical decisions must always remain under competent human <b>oversight</b>. Experienced doctors provide the ethical judgment and empathetic patient care that machines cannot replicate.\"\n\n👉 <b>Pertanyaan:</b> Final clinical decisions must always remain under human what? (Keputusan klinis akhir harus selalu di bawah apa dari manusia?)",
        "expected": [
            "oversight",
            "human oversight",
            "supervision",
            "competent human oversight"
        ],
        "primary_answer": "oversight"
    },
    {
        "id": "rdg_adv_03",
        "badge": "🏭 Revolusi Industri: Sumber Tenaga",
        "prompt": "⚙️ <b>Baca teks sejarah modern berikut:</b>\n\"Prior to the mid-eighteenth century, human manufacturing relied strictly on manual labor, draft animals, and watermills. The transformation from agrarian handcrafting to mechanized manufacturing was propelled by James Watt's refinement of the commercial <b>steam</b> engine. This revolutionary power source enabled factories to operate continuously regardless of weather or river flow.\"\n\n👉 <b>Pertanyaan:</b> What type of engine powered the mechanization of manufacturing? (Mesin bertenaga apakah yang mendorong mekanisasi manufaktur?)",
        "expected": [
            "steam",
            "steam engine",
            "the steam engine",
            "commercial steam engine"
        ],
        "primary_answer": "steam engine"
    },
    {
        "id": "rdg_adv_04",
        "badge": "🏭 Revolusi Industri: Abad Dimulai",
        "prompt": "📜 <b>Baca teks sejarah modern berikut:</b>\n\"Technological innovations gradually reshaped trade routes, urban demographics, and labor systems across the globe. The first wave of the Industrial Revolution unfolded initially in Great Britain during the latter half of the <b>eighteenth</b> century. Soon afterward, industrialization expanded rapidly across continental Europe and North America.\"\n\n👉 <b>Pertanyaan:</b> In which century did the first industrial revolution begin? (Pada abad ke berapa revolusi industri pertama dimulai?)",
        "expected": [
            "eighteenth",
            "18th",
            "18th century",
            "eighteenth century",
            "the 18th century",
            "the eighteenth century"
        ],
        "primary_answer": "18th century"
    },
    {
        "id": "rdg_adv_05",
        "badge": "🌳 Hutan Amazon: Persentase Oksigen",
        "prompt": "🌿 <b>Baca teks biosfer global berikut:</b>\n\"Covering over five million square kilometers across South America, the Amazon rainforest harbors unmatched biodiversity. Often referred to as the green lungs of our planet, the Amazon Basin rainforest produces roughly <b>twenty</b> percent of Earth's total terrestrial oxygen. It also stabilizes global climate patterns by storing massive amounts of carbon.\"\n\n👉 <b>Pertanyaan:</b> What percentage of terrestrial oxygen does the Amazon produce? (Berapa persen oksigen daratan yang dihasilkan Amazon?)",
        "expected": [
            "twenty",
            "20",
            "20 percent",
            "20%",
            "twenty percent",
            "roughly twenty percent",
            "about 20%"
        ],
        "primary_answer": "20%"
    },
    {
        "id": "rdg_adv_06",
        "badge": "🌳 Hutan Amazon: Ancaman Deforestasi",
        "prompt": "🚜 <b>Baca teks biosfer global berikut:</b>\n\"Despite its critical ecological role, the tropical biome faces unprecedented environmental pressures. Unchecked illegal logging and expansive cattle ranching drive rapid <b>deforestation</b>, threatening countless indigenous wildlife species with extinction. Conservationists urge international treaties to protect these fragile primary forests.\"\n\n👉 <b>Pertanyaan:</b> What ecological crisis is caused by logging and ranching? (Krisis ekologis apa yang disebabkan oleh penebangan dan peternakan?)",
        "expected": [
            "deforestation",
            "rapid deforestation",
            "forest loss",
            "the deforestation"
        ],
        "primary_answer": "deforestation"
    },
    {
        "id": "rdg_adv_07",
        "badge": "☢️ Marie Curie: Penemuan Radium",
        "prompt": "🔬 <b>Baca teks biografi saintis berikut:</b>\n\"Working tirelessly in an unventilated wooden shed in Paris, Marie Curie investigated pitchblende ore. Through relentless isolation of radioactive minerals, physicist Marie Curie discovered two new radioactive elements: polonium and <b>radium</b>. Her pioneering discoveries laid the foundation for modern nuclear physics and cancer radiation therapy.\"\n\n👉 <b>Pertanyaan:</b> In addition to polonium, what radioactive element did Marie Curie discover? (Selain polonium, unsur radioaktif apa yang ditemukan Marie Curie?)",
        "expected": [
            "radium",
            "element radium",
            "the element radium"
        ],
        "primary_answer": "radium"
    },
    {
        "id": "rdg_adv_08",
        "badge": "☢️ Marie Curie: Jumlah Nobel",
        "prompt": "🏆 <b>Baca teks biografi saintis berikut:</b>\n\"Marie Curie's scientific brilliance broke numerous gender barriers in academia. Marie Curie remains the only historic figure to have achieved <b>two</b> Nobel Prizes across two completely distinct scientific disciplines: Physics and Chemistry. Her legacy continues to inspire generations of scientists worldwide.\"\n\n👉 <b>Pertanyaan:</b> How many Nobel Prizes did Marie Curie win? (Berapa banyak Hadiah Nobel yang diraih Marie Curie?)",
        "expected": [
            "two",
            "2",
            "two nobel prizes",
            "2 nobel prizes"
        ],
        "primary_answer": "two"
    },
    {
        "id": "rdg_adv_09",
        "badge": "🌊 Laut Dalam: Kemosintesis",
        "prompt": "🔦 <b>Baca teks oseanografi berikut:</b>\n\"The ocean's deepest zones experience freezing temperatures and immense hydrostatic pressure. In the pitch-black abyssal trenches devoid of sunlight, specialized benthic bacteria sustain life via <b>chemosynthesis</b> rather than photosynthetic solar energy. These microscopic organisms convert toxic volcanic chemicals into nutritious organic compounds.\"\n\n👉 <b>Pertanyaan:</b> What process replaces photosynthesis in total deep-sea darkness? (Proses apa yang menggantikan fotosintesis dalam kegelapan laut dalam?)",
        "expected": [
            "chemosynthesis",
            "bacterial chemosynthesis"
        ],
        "primary_answer": "chemosynthesis"
    },
    {
        "id": "rdg_adv_10",
        "badge": "🌊 Laut Dalam: Ventilasi Hidrotermal",
        "prompt": "🌋 <b>Baca teks oseanografi berikut:</b>\n\"Submersibles exploring oceanic ridges discovered towering chimney formations on the seafloor. Deep hydrothermal vents spew mineral-rich water heated by subterranean volcanic <b>magma</b>, sustaining astonishing alien-like biological colonies. Giant tube worms, blind shrimp, and crabs thrive in these superheated thermal fields.\"\n\n👉 <b>Pertanyaan:</b> What subterranean substance heats hydrothermal vents? (Zat bawah tanah apa yang memanaskan ventilasi hidrotermal?)",
        "expected": [
            "magma",
            "volcanic magma",
            "subterranean volcanic magma"
        ],
        "primary_answer": "magma"
    },
    {
        "id": "rdg_adv_11",
        "badge": "🧱 Tembok Besar Cina: Tujuan Utama",
        "prompt": "🏯 <b>Baca teks sejarah arsitektur berikut:</b>\n\"The Great Wall represents one of mankind's greatest engineering feats. Stretching thousands of miles across northern ridges, the monumental fortifications were erected for border <b>defense</b> against nomadic incursions. Watchtowers and beacon signals allowed imperial garrisons to coordinate rapid military responses.\"\n\n👉 <b>Pertanyaan:</b> What was the primary military function of the Great Wall? (Apa fungsi pertahanan militer utama dari Tembok Besar?)",
        "expected": [
            "defense",
            "defence",
            "border defense",
            "protection"
        ],
        "primary_answer": "defense"
    },
    {
        "id": "rdg_adv_12",
        "badge": "🧱 Tembok Besar Cina: Bahan Bangunan",
        "prompt": "🧗 <b>Baca teks sejarah arsitektur berikut:</b>\n\"Early builders utilized rammed earth and timber to construct regional barriers. However, the enduring Ming dynasty sections of the wall were fortified utilizing quarried granite <b>stone</b> and kiln-fired bricks bonded with sticky rice mortar. This sturdy construction enabled the fortress to withstand centuries of weathering.\"\n\n👉 <b>Pertanyaan:</b> What masonry materials were primarily used besides bricks? (Material bebatuan apa yang digunakan selain batu bata?)",
        "expected": [
            "stone",
            "granite",
            "granite stone",
            "quarried granite stone"
        ],
        "primary_answer": "stone"
    },
    {
        "id": "rdg_adv_13",
        "badge": "🧊 Mencairnya Gletser: Efek Permukaan Laut",
        "prompt": "🌊 <b>Baca teks klimatologi berikut:</b>\n\"Rising global atmospheric temperatures have initiated dramatic retreats in glaciers from Greenland to Antarctica. Accelerated melting of polar ice caps and continental glaciers discharges trillions of tons of freshwater, resulting in alarming global sea level <b>rise</b>. Coastal communities and low-lying islands face growing risks of chronic flooding.\"\n\n👉 <b>Pertanyaan:</b> What happens to global sea levels when glaciers melt? (Apa yang terjadi pada permukaan laut global saat gletser mencair?)",
        "expected": [
            "rise",
            "sea level rise",
            "they rise",
            "it rises",
            "global sea level rise"
        ],
        "primary_answer": "rise"
    },
    {
        "id": "rdg_adv_14",
        "badge": "🧊 Mencairnya Gletser: Gas Rumah Kaca",
        "prompt": "🏭 <b>Baca teks klimatologi berikut:</b>\n\"Scientists observe that industrial emissions trap excessive heat inside the planetary biosphere. Anthropogenic emissions of <b>carbon dioxide</b> trap thermal infrared radiation within the atmosphere, driving unprecedented thermal acceleration. Transitioning towards renewable clean energy is essential to slow polar melting.\"\n\n👉 <b>Pertanyaan:</b> What greenhouse gas is highlighted as trapping heat? (Gas rumah kaca apa yang disorot karena memerangkap panas?)",
        "expected": [
            "carbon dioxide",
            "co2",
            "carbon dioxide (co2)"
        ],
        "primary_answer": "carbon dioxide"
    },
    {
        "id": "rdg_adv_15",
        "badge": "🎨 Era Renaisans: Tempat Lahir",
        "prompt": "🏛️ <b>Baca teks sejarah seni berikut:</b>\n\"Following the late Middle Ages, a powerful intellectual and artistic movement swept through Europe. Marking the cultural rebirth of European classical philosophy and realistic humanism, the Renaissance blossomed during the fourteenth century in <b>Italy</b>. Cities like Florence and Venice became bustling epicenters for wealthy merchant patrons and visionary artists.\"\n\n👉 <b>Pertanyaan:</b> In which European country did the Renaissance originate? (Di negara Eropa mana masa Renaisans bermula?)",
        "expected": [
            "italy",
            "in italy"
        ],
        "primary_answer": "Italy"
    },
    {
        "id": "rdg_adv_16",
        "badge": "🎨 Era Renaisans: Sang Polimatik",
        "prompt": "🖼️ <b>Baca teks sejarah seni berikut:</b>\n\"The Italian Renaissance celebrated multi-talented thinkers who unified art, engineering, and anatomy. Embodying the supreme Renaissance polymath, <b>Leonardo da Vinci</b> achieved immortal acclaim through masterpieces such as the Mona Lisa. His intricate sketchbooks also anticipated helicopters, tanks, and automated calculating machines.\"\n\n👉 <b>Pertanyaan:</b> Who painted the Mona Lisa and embodied the Renaissance genius? (Siapa pelukis Mona Lisa yang mencerminkan kejeniusan Renaisans?)",
        "expected": [
            "leonardo da vinci",
            "da vinci",
            "leonardo",
            "leonardo da vinci"
        ],
        "primary_answer": "Leonardo da Vinci"
    },
    {
        "id": "rdg_adv_17",
        "badge": "🚀 Eksplorasi Mars: Target Misi",
        "prompt": "🪐 <b>Baca teks eksplorasi antariksa berikut:</b>\n\"Planetary scientists explore the Red Planet to understand whether habitable environments ever existed beyond Earth. Equipped with advanced spectrometer instruments, robotic planetary rovers analyze ancient lakebed sediments to uncover biosignature signs of past microbial <b>life</b>. Finding organic traces would fundamentally transform our understanding of the cosmos.\"\n\n👉 <b>Pertanyaan:</b> What signs are planetary rovers seeking in Martian sediments? (Tanda-tanda apa yang dicari oleh penjelajah robotik di sedimen Mars?)",
        "expected": [
            "life",
            "microbial life",
            "signs of life",
            "past life",
            "past microbial life"
        ],
        "primary_answer": "life"
    },
    {
        "id": "rdg_adv_18",
        "badge": "🚀 Eksplorasi Mars: Nama Rover",
        "prompt": "🤖 <b>Baca teks eksplorasi antariksa berikut:</b>\n\"Interplanetary space exploration reached a technological milestone in February 2021. NASA's car-sized robotic rover named <b>Perseverance</b> successfully touched down inside Jezero Crater to collect pristine rock core samples. The mission also carried a solar-powered scout helicopter named Ingenuity to test aerial flight.\"\n\n👉 <b>Pertanyaan:</b> What is the name of NASA's rover in Jezero Crater? (Apa nama robot penjelajah NASA di Kawah Jezero?)",
        "expected": [
            "perseverance",
            "perseverance rover",
            "the perseverance rover",
            "rover perseverance"
        ],
        "primary_answer": "Perseverance"
    },
    {
        "id": "rdg_adv_19",
        "badge": "🌊 Mikroplastik Laut: Ukuran",
        "prompt": "🔬 <b>Baca teks pencemaran laut berikut:</b>\n\"Plastic pollution in marine ecosystems poses severe threats to oceanic food webs. Marine scientists classify synthetic debris measuring less than <b>5 millimeters</b> in diameter as hazardous microplastics. These minuscule particles result from both industrial manufacturing and the gradual breakdown of discarded consumer packaging.\"\n\n👉 <b>Pertanyaan:</b> Microplastics are defined as synthetic debris measuring less than what size? (Mikroplastik didefinisikan berukuran kurang dari berapa?)",
        "expected": [
            "5 millimeters",
            "5 mm",
            "5 millimeters in diameter",
            "five millimeters",
            "less than 5 millimeters"
        ],
        "primary_answer": "5 millimeters"
    },
    {
        "id": "rdg_adv_20",
        "badge": "🌊 Mikroplastik Laut: Dampak Hewan",
        "prompt": "🐟 <b>Baca teks pencemaran laut berikut:</b>\n\"Because microplastics drift near the water surface, they frequently mimic natural food sources. Small plankton and filter-feeding marine organisms suffer toxic chemical absorption through accidental <b>ingestion</b>. Over time, these synthetic pollutants accumulate up the food chain, eventually reaching human consumers.\"\n\n👉 <b>Pertanyaan:</b> How do filter-feeding organisms absorb toxins from microplastics? (Melalui apa organisme penyaring menyerap racun mikroplastik?)",
        "expected": [
            "ingestion",
            "accidental ingestion",
            "by ingestion",
            "through ingestion"
        ],
        "primary_answer": "ingestion"
    },
    {
        "id": "rdg_adv_21",
        "badge": "🎭 Drama Shakespeare: Teater Globe",
        "prompt": "🎪 <b>Baca teks sastra klasik berikut:</b>\n\"During the Elizabethan era, London's theater scene experienced a vibrant cultural explosion. Built along the south bank of the River Thames in 1599, William Shakespeare's acting troupe staged monumental plays at <b>the Globe</b> theater. Thousands of spectators from all social classes gathered inside its open-air wooden amphitheater.\"\n\n👉 <b>Pertanyaan:</b> What was the famous London theater where Shakespeare's troupe performed? (Apa nama teater terkenal tempat pementasan naskah Shakespeare?)",
        "expected": [
            "the globe",
            "globe",
            "globe theatre",
            "the globe theatre",
            "globe theater"
        ],
        "primary_answer": "the Globe"
    },
    {
        "id": "rdg_adv_22",
        "badge": "🎭 Drama Shakespeare: Tragedi Terkenal",
        "prompt": "👑 <b>Baca teks sastra klasik berikut:</b>\n\"Shakespeare penned world-renowned comedies, histories, and deeply psychological tragedies. Centered on a brooding Danish prince grappling with filial grief, moral paralysis, and vengeance, <b>Hamlet</b> is celebrated as Shakespeare's finest psychological tragedy. The play contains the iconic soliloquy 'To be, or not to be.'\"\n\n👉 <b>Pertanyaan:</b> Which tragedy features a troubled Danish prince seeking justice? (Tragedi apa yang mengisahkan pangeran Denmark mencari keadilan?)",
        "expected": [
            "hamlet",
            "the tragedy of hamlet",
            "tragedy of hamlet"
        ],
        "primary_answer": "Hamlet"
    },
    {
        "id": "rdg_adv_23",
        "badge": "💻 Komputasi Kuantum: Qubit",
        "prompt": "⚛️ <b>Baca teks ilmu komputasi masa depan berikut:</b>\n\"Classical computers rely on binary transistors that process data strictly as zeros or ones. In quantum computing, the fundamental unit of computational information is the <b>qubit</b>. Because of quantum superposition, a qubit can exist simultaneously in multiple states, enabling exponential processing capability.\"\n\n👉 <b>Pertanyaan:</b> What is the basic unit of quantum information called? (Disebut apakah unit dasar informasi dalam komputasi kuantum?)",
        "expected": [
            "qubit",
            "the qubit",
            "quantum bit"
        ],
        "primary_answer": "qubit"
    },
    {
        "id": "rdg_adv_24",
        "badge": "💻 Komputasi Kuantum: Kemampuan Kecepatan",
        "prompt": "⚡ <b>Baca teks ilmu komputasi masa depan berikut:</b>\n\"Simulating molecular structures and chemical reactions takes supercomputers months of calculation. By harnessing quantum entanglement and superposition, quantum processors solve specific mathematical challenges exponentially <b>faster</b> than standard supercomputers. This breakthrough will accelerate pharmaceutical discoveries and encryption technologies.\"\n\n👉 <b>Pertanyaan:</b> In terms of speed, how do quantum processors solve complex equations compared to classical computers? (Terkait kecepatan, bagaimana prosesor kuantum dibandingkan komputer biasa?)",
        "expected": [
            "faster",
            "exponentially faster",
            "much faster",
            "more quickly"
        ],
        "primary_answer": "faster"
    },
    {
        "id": "rdg_adv_25",
        "badge": "🧬 CRISPR Gene Editing: Penemu Nobel",
        "prompt": "🏅 <b>Baca teks bioteknologi genomika berikut:</b>\n\"In 2012, researchers unlocked a revolutionary molecular technique capable of precisely editing genetic sequences. For transforming genetic engineering through the invention of CRISPR-Cas9 genome scissors, biochemists Emmanuelle Charpentier and Jennifer Doudna were awarded the <b>Nobel Prize</b> in Chemistry in 2020. Their technique opened new frontiers for curing hereditary illnesses.\"\n\n👉 <b>Pertanyaan:</b> What prestigious global prize did Charpentier and Doudna receive for CRISPR? (Penghargaan prestisius apa yang diraih peneliti penemu gunting molekuler CRISPR?)",
        "expected": [
            "nobel prize",
            "the nobel prize",
            "nobel prize in chemistry",
            "the nobel prize in chemistry"
        ],
        "primary_answer": "Nobel Prize"
    },
    {
        "id": "rdg_adv_26",
        "badge": "🧬 CRISPR Gene Editing: Target Pemotongan",
        "prompt": "✂️ <b>Baca teks bioteknologi genomika berikut:</b>\n\"CRISPR functions like molecular word processing software inside living cells. Guided by synthetic RNA sequences, the specialized Cas9 enzyme binds to and severs double-stranded genomic <b>DNA</b> at precise target coordinates. Researchers can then deactivate harmful mutations or insert beneficial therapeutic genes.\"\n\n👉 <b>Pertanyaan:</b> What cellular macromolecule does the Cas9 enzyme cut? (Makromolekul seluler apa yang dipotong oleh enzim Cas9?)",
        "expected": [
            "dna",
            "genomic dna",
            "the dna",
            "dna strands"
        ],
        "primary_answer": "DNA"
    },
    {
        "id": "rdg_adv_27",
        "badge": "🌌 Lubang Hitam: Cakrawala Peristiwa",
        "prompt": "🔭 <b>Baca teks astrofisika kosmik berikut:</b>\n\"Black holes are gravitational abysses where matter is compressed into extraordinary density. The outer boundary beyond which nothing—not even electromagnetic light—can escape gravitational pull is termed the <b>event horizon</b>. Inside this boundary, known physics breaks down into a gravitational singularity.\"\n\n👉 <b>Pertanyaan:</b> What is the boundary of no return surrounding a black hole called? (Disebut apakah batas luar lubang hitam di mana cahaya pun tidak bisa lepas?)",
        "expected": [
            "event horizon",
            "the event horizon"
        ],
        "primary_answer": "event horizon"
    },
    {
        "id": "rdg_adv_28",
        "badge": "🌌 Lubang Hitam: Gambar Pertama",
        "prompt": "📷 <b>Baca teks astrofisika kosmik berikut:</b>\n\"Synchronizing radio telescopes across continents created an Earth-sized virtual aperture called the Event Horizon Telescope. In 2019, astronomers captured the historic first direct visual image of the supermassive black hole located at the heart of galaxy <b>M87</b>. The luminous glowing ring revealed hot gas swirling around the central shadow.\"\n\n👉 <b>Pertanyaan:</b> What galaxy housed the first directly imaged supermassive black hole? (Galaksi apa yang menjadi tempat lubang hitam pertama yang berhasil dipotret?)",
        "expected": [
            "m87",
            "messier 87",
            "galaxy m87"
        ],
        "primary_answer": "M87"
    },
    {
        "id": "rdg_adv_29",
        "badge": "📜 Perpustakaan Alexandria: Kota Kuno",
        "prompt": "🏛️ <b>Baca teks peradaban kuno berikut:</b>\n\"Founded under the Ptolemaic dynasty, the Great Library was envisioned as a universal repository of human thought. The monumental library of Alexandria was situated along the Mediterranean coast of ancient <b>Egypt</b>. Scholars from across the known world traveled there to study astronomy, geometry, and philosophy.\"\n\n👉 <b>Pertanyaan:</b> In which ancient nation was the Great Library of Alexandria built? (Di negeri kuno manakah Perpustakaan Agung Alexandria didirikan?)",
        "expected": [
            "egypt",
            "in egypt",
            "ancient egypt"
        ],
        "primary_answer": "Egypt"
    },
    {
        "id": "rdg_adv_30",
        "badge": "📜 Perpustakaan Alexandria: Bahan Gulungan",
        "prompt": "📜 <b>Baca teks peradaban kuno berikut:</b>\n\"Before the invention of parchment codices or wood pulp paper, scribes harvested river reeds. Hundreds of thousands of ancient literary works were written and stored in Alexandria on rolled scrolls made of dried <b>papyrus</b>. Ships docking in the harbor were searched so original manuscripts could be copied by royal scribes.\"\n\n👉 <b>Pertanyaan:</b> What reed-based writing material formed the scrolls of Alexandria? (Bahan berserat tanaman apa yang digunakan untuk gulungan naskah kuno?)",
        "expected": [
            "papyrus",
            "papyrus scrolls",
            "dried papyrus"
        ],
        "primary_answer": "papyrus"
    },
    {
        "id": "rdg_adv_31",
        "badge": "🧠 Plastisitas Saraf Otak: Neuroplastisitas",
        "prompt": "⚡ <b>Baca teks neurosains kognitif berikut:</b>\n\"Scientists once believed that the adult human brain was rigid and structurally unchangeable after childhood. Neuroscientists now recognize that brain circuits continuously adapt and reorganize through <b>neuroplasticity</b>. In response to intensive learning or novel experiences, synaptic connections strengthen and grow.\"\n\n👉 <b>Pertanyaan:</b> What biological term describes the brain's ability to reorganize neural pathways? (Istilah biologis apa yang menggambarkan kemampuan otak memperbarui jalurnya?)",
        "expected": [
            "neuroplasticity",
            "brain neuroplasticity",
            "neural plasticity"
        ],
        "primary_answer": "neuroplasticity"
    },
    {
        "id": "rdg_adv_32",
        "badge": "🧠 Plastisitas Saraf Otak: Pemulihan Cedera",
        "prompt": "🏥 <b>Baca teks neurosains kognitif berikut:</b>\n\"When patients suffer traumatic neurological damage from strokes, undamaged areas of the brain can compensate. Patients recover lost motor skills and speech through intensive physical and cognitive <b>rehabilitation</b>. Structured repetitive practice stimulates healthy neurons to form new functional networks.\"\n\n👉 <b>Pertanyaan:</b> What therapeutic process assists stroke patients in recovering motor skills? (Proses terapi apa yang membantu pasien stroke memulihkan kemampuan motorik?)",
        "expected": [
            "rehabilitation",
            "cognitive rehabilitation",
            "physical rehabilitation",
            "therapy"
        ],
        "primary_answer": "rehabilitation"
    },
    {
        "id": "rdg_adv_33",
        "badge": "☀️ Fusi Nuklir Tokamak: Sumber Tenaga Bintang",
        "prompt": "🌟 <b>Baca teks energi masa depan berikut:</b>\n\"Commercial nuclear reactors rely on fission, which splits heavy uranium atoms to produce electricity. In contrast, nuclear fusion mimics the natural thermonuclear furnace that fuels our <b>sun</b> and distant stars. If perfected on Earth, fusion could deliver virtually limitless, clean, carbon-free baseload power.\"\n\n👉 <b>Pertanyaan:</b> Nuclear fusion replicates the thermonuclear process powering what celestial body? (Fusi nuklir meniru proses termonuklir yang memberi daya pada benda langit apa?)",
        "expected": [
            "sun",
            "the sun",
            "our sun"
        ],
        "primary_answer": "sun"
    },
    {
        "id": "rdg_adv_34",
        "badge": "☀️ Fusi Nuklir Tokamak: Desain Magnetik",
        "prompt": "🧲 <b>Baca teks energi masa depan berikut:</b>\n\"Containing superheated plasma at temperatures exceeding one hundred million degrees Celsius requires extraordinary engineering. The most prominent experimental magnetic confinement reactor design is the donut-shaped <b>tokamak</b>. Powerful superconducting magnets confine the roaring plasma ring without letting it touch reactor walls.\"\n\n👉 <b>Pertanyaan:</b> What donut-shaped magnetic chamber is widely used in fusion research? (Kamar magnetik berbentuk cincin apa yang digunakan dalam reaktor fusi?)",
        "expected": [
            "tokamak",
            "the tokamak",
            "tokamak reactor"
        ],
        "primary_answer": "tokamak"
    },
    {
        "id": "rdg_adv_35",
        "badge": "🌊 Palung Mariana: Kedalaman Abisal",
        "prompt": "🚢 <b>Baca teks eksplorasi samudra berikut:</b>\n\"The Challenger Deep lies in the western Pacific Ocean as the deepest identified depression on our planet. Plunging almost <b>eleven</b> kilometers beneath the ocean surface, this extreme trench plunges deeper than Mount Everest is tall. Deep-sea research submersibles require reinforced titanium hulls to explore its floor.\"\n\n👉 <b>Pertanyaan:</b> How many kilometers deep is the Challenger Deep depression roughly? (Berapa perkiraan kedalaman Palung Mariana dalam kilometer?)",
        "expected": [
            "eleven",
            "11",
            "11 kilometers",
            "eleven kilometers",
            "almost eleven kilometers",
            "11 km"
        ],
        "primary_answer": "eleven"
    },
    {
        "id": "rdg_adv_36",
        "badge": "🌊 Palung Mariana: Tekanan Hidrostatis",
        "prompt": "⚓ <b>Baca teks eksplorasi samudra berikut:</b>\n\"Descending into the hadal ocean trenches exposes exploratory vehicles to severe physical extremes. Deep-sea creatures inhabiting the Mariana Trench endure immense hydrostatic <b>pressure</b> exceeding one thousand atmospheres. Their cellular membranes utilize unique piezolyte molecules to avoid physical collapse.\"\n\n👉 <b>Pertanyaan:</b> What physical force exceeds one thousand atmospheres at the ocean floor? (Gaya fisik apa yang melebihi seribu atmosfer di dasar palung laut?)",
        "expected": [
            "pressure",
            "hydrostatic pressure",
            "immense pressure",
            "immense hydrostatic pressure"
        ],
        "primary_answer": "pressure"
    },
    {
        "id": "rdg_adv_37",
        "badge": "🕊️ Deklarasi Universal HAM: Tahun Pengesahan",
        "prompt": "🌐 <b>Baca teks hukum internasional berikut:</b>\n\"In the aftermath of the devastation caused by the Second World War, delegates united to prevent future atrocities. The United Nations General Assembly adopted the Universal Declaration of Human Rights in Paris in <b>1948</b>. This milestone treaty established universal standards of freedom and justice for all peoples and nations.\"\n\n👉 <b>Pertanyaan:</b> In what year did the United Nations adopt the Universal Declaration of Human Rights? (Pada tahun berapa Deklarasi Universal HAM disahkan PBB?)",
        "expected": [
            "1948",
            "nineteen forty-eight",
            "in 1948"
        ],
        "primary_answer": "1948"
    },
    {
        "id": "rdg_adv_38",
        "badge": "🕊️ Deklarasi Universal HAM: Pasal 1 Martabat",
        "prompt": "⚖️ <b>Baca teks hukum internasional berikut:</b>\n\"The opening articles of the declaration proclaim the innate worth of every human being. Article 1 asserts that all human beings are born free and equal in dignity and fundamental <b>rights</b>. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.\"\n\n👉 <b>Pertanyaan:</b> All human beings are declared equal in dignity and what? (Semua manusia dilahirkan setara dalam martabat dan apa?)",
        "expected": [
            "rights",
            "fundamental rights",
            "equal rights"
        ],
        "primary_answer": "rights"
    },
    {
        "id": "rdg_adv_39",
        "badge": "🍄 Jaringan Jamur Bawah Tanah: Wood Wide Web",
        "prompt": "🌲 <b>Baca teks ekologi botani berikut:</b>\n\"Beneath the quiet floor of old-growth forests lies an intricate biological internet. Underground mycorrhizal fungal networks linking tree root systems are affectionately called the <b>wood wide web</b>. Through these microscopic fungal threads, neighboring trees exchange water, nitrogen, and essential sugars.\"\n\n👉 <b>Pertanyaan:</b> What popular nickname is given to underground mycorrhizal tree communication networks? (Julukan populer apa yang diberikan pada jaringan jamur bawah tanah hutan?)",
        "expected": [
            "wood wide web",
            "the wood wide web"
        ],
        "primary_answer": "wood wide web"
    },
    {
        "id": "rdg_adv_40",
        "badge": "🍄 Jaringan Jamur Bawah Tanah: Peringatan Bahaya",
        "prompt": "🐛 <b>Baca teks ekologi botani berikut:</b>\n\"Forest trees do not merely compete for sunlight; they actively collaborate for collective survival. When attacked by insect pests or pathogenic caterpillars, trees transmit chemical <b>distress signals</b> to alert neighboring trees. Upon receiving the signal, neighboring trees produce protective tannins to repel the infestation.\"\n\n👉 <b>Pertanyaan:</b> What chemical warnings do trees transmit through fungal networks during pest attacks? (Peringatan kimiawi apa yang dikirimkan pohon saat diserang hama?)",
        "expected": [
            "distress signals",
            "chemical distress signals",
            "signals",
            "warning signals"
        ],
        "primary_answer": "distress signals"
    },
    {
        "id": "rdg_adv_41",
        "badge": "🤖 Pembelajaran Mesin: Jaringan Saraf Tiruan",
        "prompt": "🧠 <b>Baca teks kecerdasan buatan berikut:</b>\n\"Deep learning algorithms draw conceptual inspiration from biological nervous systems. Deep learning architectures inspired by human cortical neurons are called artificial <b>neural networks</b>. These layered computational architectures excel at detecting nuanced patterns across images, speech, and written language.\"\n\n👉 <b>Pertanyaan:</b> What interconnected mathematical architectures model the structure of biological neurons? (Arsitektur matematis apa yang meniru susunan neuron biologis?)",
        "expected": [
            "neural networks",
            "artificial neural networks",
            "networks"
        ],
        "primary_answer": "neural networks"
    },
    {
        "id": "rdg_adv_42",
        "badge": "🤖 Pembelajaran Mesin: Bobot Parameter",
        "prompt": "🔢 <b>Baca teks kecerdasan buatan berikut:</b>\n\"During model training, algorithms iteratively process vast datasets to minimize prediction errors. As models train on training data, backpropagation fine-tunes internal parameters known as numerical <b>weights</b>. Optimizing these weight values allows the network to generalize accurately to brand-new, unseen data.\"\n\n👉 <b>Pertanyaan:</b> What internal mathematical parameters are fine-tuned during backpropagation training? (Parameter matematis apa yang disetel saat pelatihan jaringan saraf?)",
        "expected": [
            "weights",
            "numerical weights",
            "the weights",
            "parameters"
        ],
        "primary_answer": "weights"
    },
    {
        "id": "rdg_adv_43",
        "badge": "🏛️ Filsafat Socrates: Metode Dialektika",
        "prompt": "🏺 <b>Baca teks sejarah filsafat berikut:</b>\n\"In the bustling agora of ancient Athens, Socrates engaged fellow citizens in philosophical dialogue. The classical philosophical technique of cooperative inquiry through rigorous questioning is termed the <b>Socratic method</b>. Rather than lecturing, Socrates prompted students to identify contradictions in their own beliefs.\"\n\n👉 <b>Pertanyaan:</b> What teaching technique relies on disciplined questioning to stimulate critical thinking? (Metode pembelajaran apa yang bertumpu pada tanya-jawab dialektis?)",
        "expected": [
            "socratic method",
            "the socratic method"
        ],
        "primary_answer": "Socratic method"
    },
    {
        "id": "rdg_adv_44",
        "badge": "🏛️ Filsafat Socrates: Kebijaksanaan Sejati",
        "prompt": "💭 <b>Baca teks sejarah filsafat berikut:</b>\n\"The Oracle of Delphi famously claimed that no man in Athens was wiser than Socrates. Socrates concluded that his paradoxical wisdom stemmed from recognizing that he truly knew <b>nothing</b>. Unlike arrogant politicians who pretended to possess absolute knowledge, Socrates embraced intellectual humility.\"\n\n👉 <b>Pertanyaan:</b> What did Socrates acknowledge knowing, which formed the basis of his paradoxical wisdom? (Apa yang diakui Socrates ia ketahui, yang menjadi dasar kebijaksanaannya?)",
        "expected": [
            "nothing",
            "that he knows nothing",
            "he knows nothing",
            "that he knew nothing"
        ],
        "primary_answer": "nothing"
    },
    {
        "id": "rdg_adv_45",
        "badge": "🧫 Penemuan Penisilin: Alexander Fleming",
        "prompt": "🔬 <b>Baca teks sejarah kedokteran berikut:</b>\n\"In September 1928, a Scottish bacteriologist returned from vacation to inspect his messy laboratory. Scottish physician <b>Alexander Fleming</b> discovered penicillin when green Penicillium mold contaminated a Petri dish of staphylococci. He observed that the bacterial colonies surrounding the fungal growth had dissolved completely.\"\n\n👉 <b>Pertanyaan:</b> Which Scottish scientist made the serendipitous discovery of penicillin in 1928? (Siapa ilmuwan Skotlandia yang menemukan penisilin pada tahun 1928?)",
        "expected": [
            "alexander fleming",
            "fleming",
            "dr alexander fleming",
            "sir alexander fleming"
        ],
        "primary_answer": "Alexander Fleming"
    },
    {
        "id": "rdg_adv_46",
        "badge": "🧫 Penemuan Penisilin: Jenis Obat",
        "prompt": "💊 <b>Baca teks sejarah kedokteran berikut:</b>\n\"Prior to Fleming's breakthrough, even minor bacterial infections from scratches could prove fatal. Penicillin's development revolutionized pharmaceuticals as the world's first mass-produced therapeutic <b>antibiotic</b>. It saved millions of soldiers during World War II and transformed modern infection control.\"\n\n👉 <b>Pertanyaan:</b> What class of infection-fighting medicine was pioneered by penicillin? (Golongan obat pembasmi infeksi bakteri apa yang dipelopori oleh penisilin?)",
        "expected": [
            "antibiotic",
            "an antibiotic",
            "therapeutic antibiotic",
            "antibiotics"
        ],
        "primary_answer": "antibiotic"
    },
    {
        "id": "rdg_adv_47",
        "badge": "🧊 Lapisan Es Greenland: Peningkatan Suhu",
        "prompt": "🌡️ <b>Baca teks sains kutub berikut:</b>\n\"The Greenland Ice Sheet contains enough frozen water to raise worldwide ocean levels by over seven meters. Arctic temperatures are warming at a rate <b>two hundred</b> percent faster than the planetary average. This pronounced polar amplification accelerates glacial ablation and threatens global weather stability.\"\n\n👉 <b>Pertanyaan:</b> By what percentage rate is the Arctic warming faster than the global average? (Berapa persen laju pemanasan Arktik lebih cepat dibanding rata-rata bumi?)",
        "expected": [
            "two hundred",
            "200",
            "200 percent",
            "200%",
            "two hundred percent"
        ],
        "primary_answer": "two hundred"
    },
    {
        "id": "rdg_adv_48",
        "badge": "🧊 Lapisan Es Greenland: Efek Albedo",
        "prompt": "☀️ <b>Baca teks sains kutub berikut:</b>\n\"Bright white surfaces reflect solar radiation back into space, keeping the polar regions cool. When reflective ice sheets melt into dark meltwater ponds, the landscape's decreased <b>albedo</b> absorbs more sunlight. This warming creates a dangerous positive feedback loop that intensifies thermal melting.\"\n\n👉 <b>Pertanyaan:</b> What optical reflectivity property decreases as bright ice turns into dark open water? (Sifat reflektivitas permukaan apa yang menurun saat es putih mencair?)",
        "expected": [
            "albedo",
            "the albedo",
            "albedo effect"
        ],
        "primary_answer": "albedo"
    },
    {
        "id": "rdg_adv_49",
        "badge": "🇮🇩 Sumpah Pemuda 1928: Satu Bahasa",
        "prompt": "🏛️ <b>Baca teks sejarah pergerakan nasional berikut:</b>\n\"On 28 October 1928, diverse youth delegates from across the Indonesian archipelago gathered in unity. In the historic Youth Pledge, delegates declared one motherland, one nation, and upheld <b>Bahasa Indonesia</b> as the unifying national language. This shared tongue united hundreds of diverse ethnic groups in the fight for national freedom.\"\n\n👉 <b>Pertanyaan:</b> What language was upheld as the unifying tongue in the historic 1928 Youth Pledge? (Bahasa apa yang dijunjung tinggi sebagai bahasa persatuan dalam Sumpah Pemuda?)",
        "expected": [
            "bahasa indonesia",
            "indonesian",
            "indonesian language",
            "bahasa"
        ],
        "primary_answer": "Bahasa Indonesia"
    },
    {
        "id": "rdg_adv_50",
        "badge": "🇮🇩 Sumpah Pemuda 1928: Kota Pertemuan",
        "prompt": "📜 <b>Baca teks sejarah pergerakan nasional berikut:</b>\n\"Youth organizations such as Jong Java, Jong Sumatranen Bond, and Jong Ambon set aside regional differences. The momentous Second Youth Congress took place in the colonial administrative capital then called <b>Batavia</b>, which is now Jakarta. Their solemn pledge cemented the ideological foundation for the future Republic.\"\n\n👉 <b>Pertanyaan:</b> In what colonial city was the Youth Congress convened in 1928? (Di kota kolonial manakah Kongres Pemuda II diselenggarakan?)",
        "expected": [
            "batavia",
            "city of batavia",
            "in batavia"
        ],
        "primary_answer": "Batavia"
    },
    {
        "id": "rdg_adv_51",
        "badge": "🚀 Pendaratan Apollo 11 di Bulan: Astronot Pertama",
        "prompt": "🌕 <b>Baca teks sejarah antariksa berikut:</b>\n\"On July 20, 1969, the Apollo 11 mission accomplished President Kennedy's ambitious goal of reaching lunar soil. Mission commander <b>Neil Armstrong</b> became the first human being to step onto the Moon, speaking the famous words: 'That's one small step for man, one giant leap for mankind.'\"\n\n👉 <b>Pertanyaan:</b> Who was the first human astronaut to walk on the lunar surface? (Siapakah astronot pertama yang menjejakkan kaki di permukaan Bulan?)",
        "expected": [
            "neil armstrong",
            "armstrong",
            "commander neil armstrong"
        ],
        "primary_answer": "Neil Armstrong"
    },
    {
        "id": "rdg_adv_52",
        "badge": "🚀 Pendaratan Apollo 11 di Bulan: Modul Pendarat",
        "prompt": "🦅 <b>Baca teks sejarah antariksa berikut:</b>\n\"While astronaut Michael Collins maintained lunar orbit inside the Command Module Columbia, two astronauts prepared for descent. The Apollo 11 Lunar Module christened the <b>Eagle</b> safely touched down in the Sea of Tranquility. Millions around the world listened breathlessly as Armstrong radioed: 'The Eagle has landed.'\"\n\n👉 <b>Pertanyaan:</b> What was the call sign name of the Apollo 11 lunar landing module? (Apa nama panggilan sandi modul pendarat Bulan tersebut?)",
        "expected": [
            "eagle",
            "the eagle",
            "lunar module eagle"
        ],
        "primary_answer": "Eagle"
    },
    {
        "id": "rdg_adv_53",
        "badge": "🐠 Terumbu Karang Segitiga Karang: Lokasi",
        "prompt": "🌊 <b>Baca teks keanekaragaman hayati maritim berikut:</b>\n\"Spanning six nations in the Indo-Pacific, the Coral Triangle represents the global epicenter of marine biodiversity. Over 75 percent of all known reef-building <b>coral</b> species thrive across these nutrient-rich tropical waters. Millions of coastal residents depend on these reefs for artisanal fisheries and shoreline protection.\"\n\n👉 <b>Pertanyaan:</b> The Coral Triangle contains over 75 percent of the world's species of what? (Segitiga Karang memuat lebih dari 75 persen spesies apa di dunia?)",
        "expected": [
            "coral",
            "coral species",
            "reef-building coral",
            "reef building corals"
        ],
        "primary_answer": "coral"
    },
    {
        "id": "rdg_adv_54",
        "badge": "🐠 Terumbu Karang Segitiga Karang: Raja Ampat",
        "prompt": "🏝️ <b>Baca teks keanekaragaman hayati maritim berikut:</b>\n\"Within Indonesia's eastern waters lies an archipelago celebrated as the crown jewel of oceanic life. Located in Southwest Papua, the marine paradise of <b>Raja Ampat</b> boasts the highest recorded marine biodiversity density on the planet. Its crystal-clear lagoons provide sanctuary to manta rays, dugongs, and sea turtles.\"\n\n👉 <b>Pertanyaan:</b> What archipelago in Papua is celebrated for the world's richest marine biodiversity? (Gugusan kepulauan di Papua mana yang tersohor memiliki keanekaragaman laut tertinggi?)",
        "expected": [
            "raja ampat",
            "raja ampat archipelago",
            "islands of raja ampat"
        ],
        "primary_answer": "Raja Ampat"
    },
    {
        "id": "rdg_adv_55",
        "badge": "⚡ Superkonduktivitas: Hambatan Nol",
        "prompt": "🔬 <b>Baca teks fisika kuantum terapan berikut:</b>\n\"Standard copper electrical cables lose significant energy as heat due to internal friction. Certain materials cooled below a critical cryogenic temperature exhibit superconductivity with exactly zero electrical <b>resistance</b>. This allows electrical currents to flow perpetually without experiencing any loss of power.\"\n\n👉 <b>Pertanyaan:</b> Superconductors conduct electricity with zero what? (Superkonduktor menghantarkan listrik dengan nol apa?)",
        "expected": [
            "resistance",
            "electrical resistance",
            "zero resistance",
            "zero electrical resistance"
        ],
        "primary_answer": "resistance"
    },
    {
        "id": "rdg_adv_56",
        "badge": "⚡ Superkonduktivitas: Efek Levitasi",
        "prompt": "🧲 <b>Baca teks fisika kuantum terapan berikut:</b>\n\"Superconducting materials do not merely conduct electricity without loss; they interact dramatically with magnetic fields. The complete expulsion of magnetic flux fields from a superconductor is named the <b>Meissner</b> effect. This quantum phenomenon enables frictionless high-speed maglev trains to levitate above tracks.\"\n\n👉 <b>Pertanyaan:</b> What scientific name is given to the expulsion of magnetic fields in superconductors? (Apa nama ilmiah pengusiran medan magnet pada superkonduktor?)",
        "expected": [
            "meissner",
            "meissner effect",
            "the meissner effect"
        ],
        "primary_answer": "Meissner"
    },
    {
        "id": "rdg_adv_57",
        "badge": "💡 Teori Relativitas Einstein: Persamaan Energi",
        "prompt": "📐 <b>Baca teks fisika teoretis berikut:</b>\n\"In 1905, Albert Einstein published a paper that revolutionized physics by asserting that mass and energy are equivalent. In the landmark equation E=mc², the letter 'c' symbolizes the universal speed of <b>light</b> in a vacuum. Because light speed squared is a vast number, even a tiny amount of mass holds enormous energy.\"\n\n👉 <b>Pertanyaan:</b> In Einstein's equation E=mc², what does the letter 'c' represent? (Dalam rumus E=mc², huruf 'c' melambangkan kecepatan apa?)",
        "expected": [
            "light",
            "speed of light",
            "the speed of light"
        ],
        "primary_answer": "light"
    },
    {
        "id": "rdg_adv_58",
        "badge": "💡 Teori Relativitas Einstein: Ruang dan Waktu",
        "prompt": "🌌 <b>Baca teks fisika teoretis berikut:</b>\n\"Einstein's General Theory of Relativity fundamentally transformed our understanding of the universe. Rather than treating three-dimensional space and time as separate entities, Einstein unified them into a four-dimensional continuum known as <b>spacetime</b>. Heavy planetary bodies warp this fabric, producing the effect we experience as gravity.\"\n\n👉 <b>Pertanyaan:</b> What four-dimensional fabric combines spatial dimensions with time in Einstein's physics? (Rajutan empat dimensi apa yang menyatukan ruang dan waktu?)",
        "expected": [
            "spacetime",
            "space-time",
            "fabric of spacetime",
            "the spacetime continuum"
        ],
        "primary_answer": "spacetime"
    },
    {
        "id": "rdg_adv_59",
        "badge": "💉 Vaksin mRNA: Instruksi Seluler",
        "prompt": "🧬 <b>Baca teks imunologi biomedis berikut:</b>\n\"Traditional vaccines introduce weakened or inactivated viruses to train the immune system. In contrast, messenger RNA vaccines deliver genetic blueprints instructing human cells to synthesize a harmless viral spike <b>protein</b>. Our cells recognize this foreign antigen and prepare defensive mechanisms against real infections.\"\n\n👉 <b>Pertanyaan:</b> What viral component do host cells temporarily manufacture from mRNA instructions? (Komponen virus apa yang diproduksi sementara oleh sel tubuh dari instruksi mRNA?)",
        "expected": [
            "protein",
            "spike protein",
            "viral spike protein",
            "the spike protein"
        ],
        "primary_answer": "protein"
    },
    {
        "id": "rdg_adv_60",
        "badge": "💉 Vaksin mRNA: Respon Imun",
        "prompt": "🛡️ <b>Baca teks imunologi biomedis berikut:</b>\n\"Once human cells display the synthetic viral spike protein on their surfaces, defensive immune sentinels spring into action. Specialized B-cells produce protective <b>antibodies</b> that neutralize future viral infections rapidly. This training provides long-lasting immunity without exposing the patient to active pathogens.\"\n\n👉 <b>Pertanyaan:</b> What defensive proteins are generated by immune cells to neutralize pathogens? (Protein pelindung apa yang diproduksi oleh sel imun untuk menetralkan patogen?)",
        "expected": [
            "antibodies",
            "antibody",
            "protective antibodies"
        ],
        "primary_answer": "antibodies"
    },
    {
        "id": "rdg_adv_61",
        "badge": "🌋 Geologi Cincin Api Pasifik: Lempeng Tektonik",
        "prompt": "🌏 <b>Baca teks geologi gempa bumi berikut:</b>\n\"The Pacific basin accounts for the majority of the world's most severe earthquakes and volcanic eruptions. Indonesia lies directly along the Pacific Ring of Fire, an active belt shaped by the collision of major tectonic <b>plates</b>. The friction generated by these moving rock slabs causes frequent seismic rumblings.\"\n\n👉 <b>Pertanyaan:</b> What subterranean structures collide to form the Ring of Fire? (Struktur geologis apa yang bertubrukan membentuk Cincin Api?)",
        "expected": [
            "plates",
            "tectonic plates",
            "the tectonic plates",
            "major tectonic plates"
        ],
        "primary_answer": "plates"
    },
    {
        "id": "rdg_adv_62",
        "badge": "🌋 Geologi Cincin Api Pasifik: Jalur Subduksi",
        "prompt": "🌊 <b>Baca teks geologi gempa bumi berikut:</b>\n\"When dense oceanic crust meets lighter continental crust, deep oceanic trenches and volcanic mountain arcs are formed. Where an oceanic plate plunges beneath a continental plate, the grinding zone is known as a <b>subduction</b> zone. This intense downward movement melts crustal rock into rising magma.\"\n\n👉 <b>Pertanyaan:</b> What is the zone where one tectonic plate sinks beneath another called? (Disebut apakah zona tempat lempeng samudra menunjam ke bawah lempeng benua?)",
        "expected": [
            "subduction",
            "subduction zone",
            "a subduction zone",
            "the subduction zone"
        ],
        "primary_answer": "subduction"
    },
    {
        "id": "rdg_adv_63",
        "badge": "📜 Magna Carta 1215: Pembatasan Monarki",
        "prompt": "⚖️ <b>Baca teks sejarah ketatanegaraan berikut:</b>\n\"During the Middle Ages, English barons grew increasingly frustrated with arbitrary taxes and royal abuses of authority. Sealed in 1215 at Runnymede, the Magna Carta established for the first time that even the sovereign <b>king</b> is subject to the rule of law. This historic document laid foundational principles for modern constitutional democracy.\"\n\n👉 <b>Pertanyaan:</b> Who was declared subject to the rule of law under Magna Carta? (Siapa yang dinyatakan tunduk pada hukum dalam Magna Carta?)",
        "expected": [
            "king",
            "the king",
            "sovereign king",
            "the sovereign king",
            "monarch",
            "the monarch",
            "the ruler"
        ],
        "primary_answer": "king"
    },
    {
        "id": "rdg_adv_64",
        "badge": "📜 Magna Carta 1215: Pengadilan Adil",
        "prompt": "🏛️ <b>Baca teks sejarah ketatanegaraan berikut:</b>\n\"Before 1215, medieval monarchs exercised unchecked authority to seize private property and imprison rivals without trial. Clause 39 of the charter guaranteed that no free individual could be imprisoned without lawful judgment by <b>peers</b>. This historic clause established the cornerstone for the right to a fair trial.\"\n\n👉 <b>Pertanyaan:</b> Imprisonment required lawful judgment by whom? (Penahanan memerlukan putusan sah oleh siapa?)",
        "expected": [
            "peers",
            "judgment by peers",
            "lawful judgment by peers",
            "their peers",
            "by peers"
        ],
        "primary_answer": "peers"
    },
    {
        "id": "rdg_adv_65",
        "badge": "🌊 Arus Termohalin Global: Sabuk Konveyor Laut",
        "prompt": "🧭 <b>Baca teks sirkulasi kelautan berikut:</b>\n\"Global ocean currents transport massive amounts of heat and nutrients across equatorial and polar basins. Deep ocean currents are driven by variations in water temperature and <b>salinity</b>, forming the global conveyor belt. Cold, salty water sinks near the poles and flows along the deep ocean floor.\"\n\n👉 <b>Pertanyaan:</b> Besides temperature, what property drives deep thermohaline circulation? (Selain suhu, sifat apa yang menggerakkan sirkulasi laut dalam?)",
        "expected": [
            "salinity",
            "saltiness",
            "water salinity",
            "salt concentration"
        ],
        "primary_answer": "salinity"
    },
    {
        "id": "rdg_adv_66",
        "badge": "🌊 Arus Termohalin Global: Regulasi Iklim",
        "prompt": "🌍 <b>Baca teks sirkulasi kelautan berikut:</b>\n\"The oceans act as our planet's giant thermal buffer, preventing equatorial zones from overheating and high latitudes from freezing. The North Atlantic conveyor transports equatorial heat toward Europe, regulating regional continental <b>climate</b>. Disruption to this oceanic circulation could lead to severe weather shifts across Western Europe.\"\n\n👉 <b>Pertanyaan:</b> What continental phenomenon is moderated by Atlantic heat transport? (Fenomena benua apa yang diatur oleh perpindahan panas samudera ini?)",
        "expected": [
            "climate",
            "continental climate",
            "regional climate",
            "regional continental climate"
        ],
        "primary_answer": "climate"
    }
],
}
