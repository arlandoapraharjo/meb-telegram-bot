"""
Curated Conversation exercises for English Buddy Bot.
Total: 200 exercises (67 Beginner, 67 Intermediate, 66 Advanced).
"""
from typing import Any, Dict, List
import config

CONVERSATION_EXERCISES: Dict[str, List[Dict[str, Any]]] = {
    config.LEVEL_BEGINNER: [
    {
        "id": "conv_beg_01",
        "badge": "💬 Sapaan Pagi (Morning Greeting)",
        "prompt": "<b>☀️ Situasi:</b> Kamu bertemu teman di depan gerbang sekolah pada pagi hari.\n\n<b>Teman:</b> <i>\"Good morning! How are you today?\"</i>\n<i>(Selamat pagi! Apa kabarmu hari ini?)</i>\n\n👉 <b>Giliranmu:</b> Balas dengan mengetik:\n<code>Good morning! I am fine, thank you.</code>\n<i>(Artinya: Selamat pagi! Saya baik-baik saja, terima kasih.)</i>",
        "expected": [
            "good morning i am fine thank you",
            "good morning! i am fine, thank you.",
            "good morning i'm fine thank you",
            "good morning, i am fine",
            "good morning i am fine",
            "i am fine thank you",
            "good morning"
        ],
        "primary_answer": "Good morning! I am fine, thank you."
    },
    {
        "id": "conv_beg_02",
        "badge": "💬 Berkenalan Nama (Introducing Yourself)",
        "prompt": "<b>👋 Situasi:</b> Ada murid baru di kelasmu yang ingin berkenalan.\n\n<b>Murid Baru:</b> <i>\"Hello! My name is Budi. What is your name?\"</i>\n<i>(Halo! Nama saya Budi. Siapa namamu?)</i>\n\n👉 <b>Giliranmu:</b> Jawab dengan nama panggilanmu (contoh jika namamu Siti):\n<code>My name is Siti.</code>\n<i>(Boleh ganti Siti dengan namamu sendiri ya!)</i>",
        "expected": [
            "my name is",
            "i am",
            "my name's"
        ],
        "primary_answer": "My name is [namamu]."
    },
    {
        "id": "conv_beg_03",
        "badge": "💬 Berterima Kasih (Saying Thank You)",
        "prompt": "<b>🎁 Situasi:</b> Teman sebangkumu meminjamkan penghapus kepadamu.\n\n<b>Teman:</b> <i>\"Here is the eraser for you.\"</i>\n<i>(Ini penghapus untukmu.)</i>\n\n👉 <b>Giliranmu:</b> Ucapkan terima kasih dengan sopan:\n<code>Thank you very much!</code>\n<i>(Artinya: Terima kasih banyak!)</i>",
        "expected": [
            "thank you very much",
            "thank you very much!",
            "thank you so much",
            "thank you",
            "thanks"
        ],
        "primary_answer": "Thank you very much!"
    },
    {
        "id": "conv_beg_04",
        "badge": "💬 Menanyakan Kabar (Asking How Are You)",
        "prompt": "<b>🤝 Situasi:</b> Kamu bertemu sahabatmu saat jam istirahat sekolah.\n\nKamu ingin bertanya apa kabarnya hari ini dalam bahasa Inggris.\n\n👉 <b>Giliranmu:</b> Ketik pertanyaan sapaan ini:\n<code>How are you, my friend?</code>\n<i>(Artinya: Apa kabarmu, temanku?)</i>",
        "expected": [
            "how are you my friend",
            "how are you, my friend?",
            "how are you my friend?",
            "how are you",
            "how are you?"
        ],
        "primary_answer": "How are you, my friend?"
    },
    {
        "id": "conv_beg_05",
        "badge": "💬 Berpamitan Pulang (Saying Goodbye)",
        "prompt": "<b>🏫 Situasi:</b> Bel pulang sekolah berbunyi, kamu berpamitan pada teman.\n\n<b>Teman:</b> <i>\"See you tomorrow!\"</i>\n<i>(Sampai jumpa besok!)</i>\n\n👉 <b>Giliranmu:</b> Balas ucapan perpisahan ramah ini:\n<code>Goodbye! See you!</code>\n<i>(Artinya: Selamat tinggal! Sampai jumpa!)</i>",
        "expected": [
            "goodbye see you",
            "goodbye! see you!",
            "goodbye",
            "bye see you",
            "see you",
            "bye"
        ],
        "primary_answer": "Goodbye! See you!"
    },
    {
        "id": "conv_beg_06",
        "badge": "💬 Perasaan Senang (Feeling Happy)",
        "prompt": "<b>🌟 Situasi:</b> Gurumu memberikan pujian karena kamu rajin belajar.\n\nKamu merasa sangat gembira hari ini.\n\n👉 <b>Giliranmu:</b> Ungkapkan perasaan bahagiamu:\n<code>I am very happy today.</code>\n<i>(Artinya: Saya sangat senang hari ini.)</i>",
        "expected": [
            "i am very happy today",
            "i am very happy today.",
            "i'm very happy today",
            "i am happy today",
            "i am happy"
        ],
        "primary_answer": "I am very happy today."
    },
    {
        "id": "conv_beg_07",
        "badge": "💬 Sapaan Siang (Good Afternoon)",
        "prompt": "<b>☀️ Situasi:</b> Pukul 13.00 siang, kamu berpapasan dengan teman di perpustakaan.\n\n👉 <b>Giliranmu:</b> Sapa temanmu dengan ucapan selamat siang:\n<code>Good afternoon!</code>\n<i>(Artinya: Selamat siang!)</i>",
        "expected": [
            "good afternoon",
            "good afternoon!",
            "good afternoon, friend"
        ],
        "primary_answer": "Good afternoon!"
    },
    {
        "id": "conv_beg_08",
        "badge": "💬 Menyebutkan Umur (Stating Age)",
        "prompt": "<b>🎂 Situasi:</b> Teman barumu bertanya: <i>\"How old are you?\"</i> (Berapa umurmu?).\n\n👉 <b>Giliranmu:</b> Jawab umurmu (contoh: 10 tahun):\n<code>I am ten years old.</code>\n<i>(Atau gunakan angka umurmu: nine / eleven / twelve)</i>",
        "expected": [
            "i am ten years old",
            "i am 10 years old",
            "i'm ten years old",
            "i'm 10 years old",
            "years old",
            "i am"
        ],
        "primary_answer": "I am ten years old."
    },
    {
        "id": "conv_beg_09",
        "badge": "💬 Meminta Tolong (Saying Please)",
        "prompt": "<b>🙏 Situasi:</b> Kamu kesulitan membuka tutup botol minum dan minta bantuan teman.\n\n👉 <b>Giliranmu:</b> Minta tolong dengan kata santun 'Please':\n<code>Please help me.</code>\n<i>(Artinya: Tolong bantu saya.)</i>",
        "expected": [
            "please help me",
            "please help me.",
            "help me please",
            "please help"
        ],
        "primary_answer": "Please help me."
    },
    {
        "id": "conv_beg_10",
        "badge": "💬 Meminta Maaf (Saying Sorry)",
        "prompt": "<b>🕊️ Situasi:</b> Kamu tidak sengaja menjatuhkan penggaris teman.\n\n👉 <b>Giliranmu:</b> Minta maaf secara tulus dalam bahasa Inggris:\n<code>I am sorry.</code>\n<i>(Artinya: Saya minta maaf.)</i>",
        "expected": [
            "i am sorry",
            "i am sorry.",
            "i'm sorry",
            "sorry"
        ],
        "primary_answer": "I am sorry."
    },
    {
        "id": "conv_beg_11",
        "badge": "💬 Sama-sama (You Are Welcome)",
        "prompt": "<b>🌸 Situasi:</b> Teman mengucapkan: <i>\"Thank you for the candy!\"</i>\n\n👉 <b>Giliranmu:</b> Balas ucapan terima kasih dengan ungkapan 'sama-sama':\n<code>You are welcome.</code>\n<i>(Artinya: Sama-sama / terima kasih kembali.)</i>",
        "expected": [
            "you are welcome",
            "you are welcome.",
            "you're welcome",
            "youre welcome"
        ],
        "primary_answer": "You are welcome."
    },
    {
        "id": "conv_beg_12",
        "badge": "💬 Menanyakan Nama Teman (Asking Name)",
        "prompt": "<b>❓ Situasi:</b> Ada teman sebaya yang duduk di sebelahmu di taman baca.\n\n👉 <b>Giliranmu:</b> Tanyakan siapa namanya dengan sopan:\n<code>What is your name?</code>\n<i>(Artinya: Siapa namamu?)</i>",
        "expected": [
            "what is your name",
            "what is your name?",
            "what's your name",
            "what's your name?"
        ],
        "primary_answer": "What is your name?"
    },
    {
        "id": "conv_beg_13",
        "badge": "💬 Senang Berkenalan (Nice to Meet You)",
        "prompt": "<b>🤝 Situasi:</b> Kamu baru saja saling menyebutkan nama dengan murid baru.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu senang berkenalan dengannya:\n<code>Nice to meet you!</code>\n<i>(Artinya: Senang berkenalan denganmu!)</i>",
        "expected": [
            "nice to meet you",
            "nice to meet you!",
            "glad to meet you"
        ],
        "primary_answer": "Nice to meet you!"
    },
    {
        "id": "conv_beg_14",
        "badge": "💬 Asal Negara (Where Are You From)",
        "prompt": "<b>🇮🇩 Situasi:</b> Teman bertanya dari mana asal negaramu.\n\n👉 <b>Giliranmu:</b> Jawab bahwa kamu berasal dari Indonesia:\n<code>I am from Indonesia.</code>\n<i>(Artinya: Saya berasal dari Indonesia.)</i>",
        "expected": [
            "i am from indonesia",
            "i am from indonesia.",
            "i'm from indonesia",
            "from indonesia"
        ],
        "primary_answer": "I am from Indonesia."
    },
    {
        "id": "conv_beg_15",
        "badge": "💬 Menyapa Bapak/Ibu Guru (Greeting Teacher)",
        "prompt": "<b>👩‍🏫 Situasi:</b> Ibu Guru masuk ke dalam kelas di pagi hari.\n\n👉 <b>Giliranmu:</b> Beri salam hormat kepada gurumu:\n<code>Good morning, Teacher!</code>\n<i>(Artinya: Selamat pagi, Guru!)</i>",
        "expected": [
            "good morning, teacher",
            "good morning teacher",
            "good morning, teacher!",
            "good morning teacher!"
        ],
        "primary_answer": "Good morning, Teacher!"
    },
    {
        "id": "conv_beg_16",
        "badge": "💬 Permisi / Maaf Menyela (Excuse Me)",
        "prompt": "<b>🚶 Situasi:</b> Kamu ingin lewat di antara dua orang yang sedang berdiri.\n\n👉 <b>Giliranmu:</b> Ucapkan kata permisi yang santun:\n<code>Excuse me.</code>\n<i>(Artinya: Permisi.)</i>",
        "expected": [
            "excuse me",
            "excuse me."
        ],
        "primary_answer": "Excuse me."
    },
    {
        "id": "conv_beg_17",
        "badge": "💬 Izin Cuci Tangan (May I)",
        "prompt": "<b>💧 Situasi:</b> Tanganmu kotor setelah menggambar dan ingin minta izin cuci tangan.\n\n👉 <b>Giliranmu:</b> Minta izin kepada guru dengan sopan:\n<code>May I wash my hands?</code>\n<i>(Artinya: Bolehkah saya mencuci tangan?)</i>",
        "expected": [
            "may i wash my hands",
            "may i wash my hands?",
            "may i wash hands"
        ],
        "primary_answer": "May I wash my hands?"
    },
    {
        "id": "conv_beg_18",
        "badge": "💬 Memberi Selamat (Congratulations)",
        "prompt": "<b>🏆 Situasi:</b> Temanmu baru saja memenangkan lomba membaca puisi.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat kepadanya:\n<code>Congratulations, my friend!</code>\n<i>(Artinya: Selamat ya, sahabatku!)</i>",
        "expected": [
            "congratulations, my friend",
            "congratulations my friend",
            "congratulations, my friend!",
            "congratulations",
            "congrats"
        ],
        "primary_answer": "Congratulations, my friend!"
    },
    {
        "id": "conv_beg_19",
        "badge": "💬 Menjawab Kabar Baik (I am Fine)",
        "prompt": "<b>😊 Situasi:</b> Guru bertanya kabarmu: <i>\"How are you?\"</i>\n\n👉 <b>Giliranmu:</b> Jawab bahwa kamu dalam keadaan baik:\n<code>I am fine, thank you.</code>\n<i>(Artinya: Saya baik-baik saja, terima kasih.)</i>",
        "expected": [
            "i am fine, thank you",
            "i am fine thank you",
            "i'm fine thank you",
            "i am fine",
            "fine thank you"
        ],
        "primary_answer": "I am fine, thank you."
    },
    {
        "id": "conv_beg_20",
        "badge": "💬 Sapaan Sore Hari (Good Evening)",
        "prompt": "<b>🌇 Situasi:</b> Pukul 18.00 saat matahari terbenam, kamu bertemu tetangga.\n\n👉 <b>Giliranmu:</b> Ucapkan salam sore/petang:\n<code>Good evening!</code>\n<i>(Artinya: Selamat sore / petang!)</i>",
        "expected": [
            "good evening",
            "good evening!"
        ],
        "primary_answer": "Good evening!"
    },
    {
        "id": "conv_beg_21",
        "badge": "💬 Ucapan Selamat Malam (Good Night)",
        "prompt": "<b>🌙 Situasi:</b> Kamu hendak tidur malam dan berpamitan pada Ibu.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat tidur kepada Ibu:\n<code>Good night, Mom!</code>\n<i>(Artinya: Selamat malam / selamat tidur, Ibu!)</i>",
        "expected": [
            "good night, mom",
            "good night mom",
            "good night, mom!",
            "good night",
            "good night, mother"
        ],
        "primary_answer": "Good night, Mom!"
    },
    {
        "id": "conv_beg_22",
        "badge": "💬 Menyambut Teman Baru (Welcome)",
        "prompt": "<b>🎉 Situasi:</b> Ada teman baru yang baru saja masuk ke kelasmu.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat datang dengan ramah:\n<code>Welcome to our class!</code>\n<i>(Artinya: Selamat datang di kelas kami!)</i>",
        "expected": [
            "welcome to our class",
            "welcome to our class!",
            "welcome to class"
        ],
        "primary_answer": "Welcome to our class!"
    },
    {
        "id": "conv_beg_23",
        "badge": "💬 Mengajak Bermain (Let's Play)",
        "prompt": "<b>⚽ Situasi:</b> Waktu istirahat tiba, kamu ingin mengajak teman bermain bersama.\n\n👉 <b>Giliranmu:</b> Ajak temanmu bermain:\n<code>Let's play together!</code>\n<i>(Artinya: Ayo kita bermain bersama!)</i>",
        "expected": [
            "let's play together",
            "let's play together!",
            "lets play together",
            "let us play together"
        ],
        "primary_answer": "Let's play together!"
    },
    {
        "id": "conv_beg_24",
        "badge": "💬 Menjawab Sampai Jumpa (See You Later)",
        "prompt": "<b>👋 Situasi:</b> Temanmu melambaikan tangan saat hendak pulang sekolah.\n\n👉 <b>Giliranmu:</b> Balas dengan ucapan sampai jumpa lagi:\n<code>See you later!</code>\n<i>(Artinya: Sampai jumpa lagi!)</i>",
        "expected": [
            "see you later",
            "see you later!",
            "see you"
        ],
        "primary_answer": "See you later!"
    },
    {
        "id": "conv_beg_25",
        "badge": "💬 Menanyakan Kabar Guru (Greeting Teacher)",
        "prompt": "<b>👩‍🏫 Situasi:</b> Kamu berpapasan dengan Pak Guru di koridor sekolah pagi ini.\n\n👉 <b>Giliranmu:</b> Sapa beliau dan tanyakan kabarnya:\n<code>Good morning, Sir. How are you?</code>\n<i>(Artinya: Selamat pagi, Pak. Bagaimana kabar Bapak?)</i>",
        "expected": [
            "good morning, sir. how are you",
            "good morning sir how are you",
            "good morning sir, how are you?",
            "good morning sir how are you?"
        ],
        "primary_answer": "Good morning, Sir. How are you?"
    },
    {
        "id": "conv_beg_26",
        "badge": "💬 Izin ke Belakang (Toilet Permission)",
        "prompt": "<b>🚽 Situasi:</b> Saat jam pelajaran berlangsung, kamu ingin izin pergi ke toilet.\n\n👉 <b>Giliranmu:</b> Minta izin kepada guru dengan sangat sopan:\n<code>May I go to the toilet, please?</code>\n<i>(Artinya: Bolehkah saya pergi ke toilet?)</i>",
        "expected": [
            "may i go to the toilet, please",
            "may i go to the toilet please",
            "may i go to the toilet",
            "can i go to the toilet"
        ],
        "primary_answer": "May I go to the toilet, please?"
    },
    {
        "id": "conv_beg_27",
        "badge": "💬 Menyapa Kawan (Greeting Friend)",
        "prompt": "<b>👋 Situasi:</b> Kamu melihat Siti berjalan santai di halaman sekolah.\n\n👉 <b>Giliranmu:</b> Sapa Siti di pagi hari:\n<code>Good morning, Siti!</code>\n<i>(Artinya: Selamat pagi, Siti!)</i>",
        "expected": [
            "good morning, siti",
            "good morning siti",
            "good morning, siti!"
        ],
        "primary_answer": "Good morning, Siti!"
    },
    {
        "id": "conv_beg_28",
        "badge": "💬 Makanan Favorit (Favorite Food)",
        "prompt": "<b>🍜 Situasi:</b> Temanmu bertanya apa makanan favoritmu saat istirahat.\n\n👉 <b>Giliranmu:</b> Katakan bahwa makanan kesukaanmu adalah mie goreng:\n<code>My favorite food is fried noodles.</code>\n<i>(Artinya: Makanan favorit saya adalah mie goreng.)</i>",
        "expected": [
            "my favorite food is fried noodles",
            "my favourite food is fried noodles",
            "favorite food is fried noodles",
            "fried noodles"
        ],
        "primary_answer": "My favorite food is fried noodles."
    },
    {
        "id": "conv_beg_29",
        "badge": "💬 Merasa Lapar (Feeling Hungry)",
        "prompt": "<b>🍽️ Situasi:</b> Perutmu berbunyi setelah olahraga, kamu ingin mengajak teman makan.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu lapar:\n<code>I am hungry, let's eat!</code>\n<i>(Artinya: Saya lapar, ayo kita makan!)</i>",
        "expected": [
            "i am hungry, let's eat",
            "i am hungry let's eat",
            "i'm hungry, let's eat",
            "i'm hungry lets eat",
            "i am hungry"
        ],
        "primary_answer": "I am hungry, let's eat!"
    },
    {
        "id": "conv_beg_30",
        "badge": "💬 Merasa Haus (Feeling Thirsty)",
        "prompt": "<b>💧 Situasi:</b> Setelah berlari di lapangan, tenggorokanmu kering.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu haus dan butuh air:\n<code>I am thirsty, I want water.</code>\n<i>(Artinya: Saya haus, saya ingin air.)</i>",
        "expected": [
            "i am thirsty, i want water",
            "i am thirsty i want water",
            "i'm thirsty, i want water",
            "i am thirsty",
            "thirsty i want water"
        ],
        "primary_answer": "I am thirsty, I want water."
    },
    {
        "id": "conv_beg_31",
        "badge": "💬 Meminjam Penghapus (Borrowing Eraser)",
        "prompt": "<b>✏️ Situasi:</b> Tulisanmu ada yang salah dan kamu tidak membawa penghapus.\n\n👉 <b>Giliranmu:</b> Pinjam penghapus ke teman dengan santun:\n<code>Can I borrow your eraser, please?</code>\n<i>(Artinya: Bolehkah saya meminjam penghapusmu?)</i>",
        "expected": [
            "can i borrow your eraser, please",
            "can i borrow your eraser please",
            "can i borrow your eraser",
            "may i borrow your eraser"
        ],
        "primary_answer": "Can I borrow your eraser, please?"
    },
    {
        "id": "conv_beg_32",
        "badge": "💬 Selamat Ulang Tahun (Happy Birthday)",
        "prompt": "<b>🎂 Situasi:</b> Hari ini teman sebangkumu merayakan hari kelahirannya.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat ulang tahun kepadanya:\n<code>Happy birthday to you!</code>\n<i>(Artinya: Selamat ulang tahun untukmu!)</i>",
        "expected": [
            "happy birthday to you",
            "happy birthday to you!",
            "happy birthday"
        ],
        "primary_answer": "Happy birthday to you!"
    },
    {
        "id": "conv_beg_33",
        "badge": "💬 Menyapa Sahabat Karib (Greeting Best Friend)",
        "prompt": "<b>🤝 Situasi:</b> Kamu berpapasan dengan sahabat terbaikmu di gerbang sekolah.\n\n👉 <b>Giliranmu:</b> Sapa sahabatmu dengan ramah:\n<code>Hello, my best friend!</code>\n<i>(Artinya: Halo, sahabat terbaikku!)</i>",
        "expected": [
            "hello, my best friend",
            "hello my best friend",
            "hello, my best friend!",
            "hello best friend"
        ],
        "primary_answer": "Hello, my best friend!"
    },
    {
        "id": "conv_beg_34",
        "badge": "💬 Menyambut Tamu di Rumah (Welcome to My House)",
        "prompt": "<b>🏡 Situasi:</b> Teman sekelasmu berkunjung ke rumahmu untuk bermain.\n\n👉 <b>Giliranmu:</b> Sambut kedatangannya dengan hangat:\n<code>Welcome to my house!</code>\n<i>(Artinya: Selamat datang di rumahku!)</i>",
        "expected": [
            "welcome to my house",
            "welcome to my house!",
            "welcome to my home"
        ],
        "primary_answer": "Welcome to my house!"
    },
    {
        "id": "conv_beg_35",
        "badge": "💬 Warna Kesukaan Hijau (Favorite Color Green)",
        "prompt": "<b>🌿 Situasi:</b> Saat mewarnai gambar pohon, teman bertanya warna kesukaanmu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa warna favoritmu adalah hijau:\n<code>My favorite color is green.</code>\n<i>(Artinya: Warna kesukaan saya adalah hijau.)</i>",
        "expected": [
            "my favorite color is green",
            "my favourite color is green",
            "favorite color is green",
            "color is green",
            "green"
        ],
        "primary_answer": "My favorite color is green."
    },
    {
        "id": "conv_beg_36",
        "badge": "💬 Kota Tempat Tinggal (Where I Live)",
        "prompt": "<b>🏙️ Situasi:</b> Guru bertanya di kota atau daerah mana kamu tinggal.\n\n👉 <b>Giliranmu:</b> Jawab bahwa kamu tinggal di Jakarta (atau kotamu):\n<code>I live in Jakarta.</code>\n<i>(Artinya: Saya tinggal di Jakarta.)</i>",
        "expected": [
            "i live in jakarta",
            "i live in jakarta.",
            "i live in",
            "live in jakarta"
        ],
        "primary_answer": "I live in Jakarta."
    },
    {
        "id": "conv_beg_37",
        "badge": "💬 Menanyakan Harga (Asking the Price)",
        "prompt": "<b>💰 Situasi:</b> Di koperasi sekolah, kamu ingin membeli sebuah pensil.\n\n👉 <b>Giliranmu:</b> Tanyakan berapa harga pensil tersebut:\n<code>How much is this pencil?</code>\n<i>(Artinya: Berapa harga pensil ini?)</i>",
        "expected": [
            "how much is this pencil",
            "how much is this pencil?",
            "how much is the pencil",
            "how much is this"
        ],
        "primary_answer": "How much is this pencil?"
    },
    {
        "id": "conv_beg_38",
        "badge": "💬 Suka Membaca Buku (I Like to Read)",
        "prompt": "<b>📚 Situasi:</b> Di perpustakaan, teman bertanya apa kegemaranmu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu suka membaca buku:\n<code>I like to read books.</code>\n<i>(Artinya: Saya suka membaca buku.)</i>",
        "expected": [
            "i like to read books",
            "i like reading books",
            "like to read books",
            "i like read books"
        ],
        "primary_answer": "I like to read books."
    },
    {
        "id": "conv_beg_39",
        "badge": "💬 Siap Belajar (Ready to Learn)",
        "prompt": "<b>🎒 Situasi:</b> Pelajaran bahasa Inggris segera dimulai, kelas bersiap-siap.\n\n👉 <b>Giliranmu:</b> Katakan dengan semangat bahwa kamu siap belajar:\n<code>I am ready to learn!</code>\n<i>(Artinya: Saya siap belajar!)</i>",
        "expected": [
            "i am ready to learn",
            "i am ready to learn!",
            "i'm ready to learn",
            "ready to learn"
        ],
        "primary_answer": "I am ready to learn!"
    },
    {
        "id": "conv_beg_40",
        "badge": "💬 Mengajak Jalan Bersama (Let's Walk Together)",
        "prompt": "<b>🚶 Situasi:</b> Saat pulang sekolah, arah rumah temanmu searah denganmu.\n\n👉 <b>Giliranmu:</b> Ajak temanmu jalan kaki bersama:\n<code>Let's walk together!</code>\n<i>(Artinya: Ayo kita jalan bersama!)</i>",
        "expected": [
            "let's walk together",
            "let's walk together!",
            "lets walk together",
            "let us walk together"
        ],
        "primary_answer": "Let's walk together!"
    },
    {
        "id": "conv_beg_41",
        "badge": "💬 Cuaca Sangat Panas (Very Hot Weather)",
        "prompt": "<b>☀️ Situasi:</b> Matahari siang ini bersinar sangat terik di lapangan.\n\n👉 <b>Giliranmu:</b> Katakan pada teman bahwa cuaca sangat panas:\n<code>It is very hot today.</code>\n<i>(Artinya: Hari ini sangat panas.)</i>",
        "expected": [
            "it is very hot today",
            "it is hot today",
            "it's very hot today",
            "very hot today"
        ],
        "primary_answer": "It is very hot today."
    },
    {
        "id": "conv_beg_42",
        "badge": "💬 Cuaca Terasa Dingin (Cold Weather)",
        "prompt": "<b>❄️ Situasi:</b> Pagi ini udara di pegunungan/desa terasa sangat sejuk dan dingin.\n\n👉 <b>Giliranmu:</b> Katakan bahwa cuaca di luar dingin:\n<code>It is cold outside.</code>\n<i>(Artinya: Di luar dingin.)</i>",
        "expected": [
            "it is cold outside",
            "it's cold outside",
            "cold outside"
        ],
        "primary_answer": "It is cold outside."
    },
    {
        "id": "conv_beg_43",
        "badge": "💬 Terima Kasih Ibu (Thank You Mom)",
        "prompt": "<b>💖 Situasi:</b> Ibu membawakan kotak bekal nasi goreng lezat ke sekolah.\n\n👉 <b>Giliranmu:</b> Ucapkan terima kasih banyak kepada Ibu:\n<code>Thank you very much, Mom!</code>\n<i>(Artinya: Terima kasih banyak, Ibu!)</i>",
        "expected": [
            "thank you very much, mom",
            "thank you very much mom",
            "thank you very much, mom!",
            "thank you mom",
            "thanks mom"
        ],
        "primary_answer": "Thank you very much, Mom!"
    },
    {
        "id": "conv_beg_44",
        "badge": "💬 Terima Kasih Ayah (Thank You Dad)",
        "prompt": "<b>🚗 Situasi:</b> Ayah mengantarmu sampai tepat di depan gerbang sekolah.\n\n👉 <b>Giliranmu:</b> Ucapkan terima kasih kepada Ayah tercinta:\n<code>Thank you very much, Dad!</code>\n<i>(Artinya: Terima kasih banyak, Ayah!)</i>",
        "expected": [
            "thank you very much, dad",
            "thank you very much dad",
            "thank you very much, dad!",
            "thank you dad",
            "thanks dad"
        ],
        "primary_answer": "Thank you very much, Dad!"
    },
    {
        "id": "conv_beg_45",
        "badge": "💬 Waktu Istirahat (Break Time)",
        "prompt": "<b>🔔 Situasi:</b> Kamu mendengar bel berbunyi dan ingin memastikan apakah sudah istirahat.\n\n👉 <b>Giliranmu:</b> Tanyakan apakah sudah jam istirahat:\n<code>Is it break time now?</code>\n<i>(Artinya: Apakah sekarang waktu istirahat?)</i>",
        "expected": [
            "is it break time now",
            "is it break time now?",
            "is it break time",
            "is it break time?"
        ],
        "primary_answer": "Is it break time now?"
    },
    {
        "id": "conv_beg_46",
        "badge": "💬 Permisi Masuk Kelas (May I Come In)",
        "prompt": "<b>🚪 Situasi:</b> Kamu tiba di kelas saat guru sudah berdiri di depan papan tulis.\n\n👉 <b>Giliranmu:</b> Ketuk pintu dan minta izin masuk:\n<code>Excuse me, may I come in?</code>\n<i>(Artinya: Permisi, bolehkah saya masuk?)</i>",
        "expected": [
            "excuse me, may i come in",
            "excuse me may i come in",
            "excuse me, may i come in?",
            "may i come in"
        ],
        "primary_answer": "Excuse me, may I come in?"
    },
    {
        "id": "conv_beg_47",
        "badge": "💬 Memberitahu Ada PR (We Have Homework)",
        "prompt": "<b>📝 Situasi:</b> Teman sebangkumu lupa apakah ada pekerjaan rumah hari ini.\n\n👉 <b>Giliranmu:</b> Beritahu dia bahwa kita ada PR bahasa Inggris:\n<code>We have English homework today.</code>\n<i>(Artinya: Kita ada PR bahasa Inggris hari ini.)</i>",
        "expected": [
            "we have english homework today",
            "we have homework today",
            "we have english homework"
        ],
        "primary_answer": "We have English homework today."
    },
    {
        "id": "conv_beg_48",
        "badge": "💬 Selamat Berlibur (Have a Nice Holiday)",
        "prompt": "<b>🏖️ Situasi:</b> Hari terakhir sekolah sebelum liburan semester tiba.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat berlibur kepada teman-teman:\n<code>Have a nice holiday!</code>\n<i>(Artinya: Semoga liburanmu menyenangkan!)</i>",
        "expected": [
            "have a nice holiday",
            "have a nice holiday!",
            "have a good holiday"
        ],
        "primary_answer": "Have a nice holiday!"
    },
    {
        "id": "conv_beg_49",
        "badge": "💬 Hewan Kesukaan Kucing (Favorite Animal Cat)",
        "prompt": "<b>🐱 Situasi:</b> Guru biologi bertanya tentang hewan yang disukai murid-murid.\n\n👉 <b>Giliranmu:</b> Katakan bahwa hewan favoritmu adalah kucing:\n<code>My favorite animal is a cat.</code>\n<i>(Artinya: Hewan favorit saya adalah kucing.)</i>",
        "expected": [
            "my favorite animal is a cat",
            "my favorite animal is cat",
            "my favourite animal is a cat",
            "favorite animal is a cat"
        ],
        "primary_answer": "My favorite animal is a cat."
    },
    {
        "id": "conv_beg_50",
        "badge": "💬 Senang Bertemu Kembali (Nice to See You Again)",
        "prompt": "<b>🌟 Situasi:</b> Masuk sekolah setelah libur panjang, kamu bertemu teman lama.\n\n👉 <b>Giliranmu:</b> Katakan senang bertemu kembali dengannya:\n<code>Nice to see you again!</code>\n<i>(Artinya: Senang bertemu denganmu lagi!)</i>",
        "expected": [
            "nice to see you again",
            "nice to see you again!",
            "glad to see you again"
        ],
        "primary_answer": "Nice to see you again!"
    },
    {
        "id": "conv_beg_51",
        "badge": "💬 Menanyakan Apa Ini (What Is This)",
        "prompt": "<b>❓ Situasi:</b> Kamu melihat buah atau benda asing di meja guru.\n\n👉 <b>Giliranmu:</b> Tanyakan apa nama benda ini dalam bahasa Inggris:\n<code>What is this in English?</code>\n<i>(Artinya: Apa nama benda ini dalam bahasa Inggris?)</i>",
        "expected": [
            "what is this in english",
            "what is this in english?",
            "what is this"
        ],
        "primary_answer": "What is this in English?"
    },
    {
        "id": "conv_beg_52",
        "badge": "💬 Menanyakan Letak Buku (Where Is My Book)",
        "prompt": "<b>🔍 Situasi:</b> Bukumu tidak ada di meja, mungkin terselip di tas teman.\n\n👉 <b>Giliranmu:</b> Tanyakan di mana letak bukumu:\n<code>Where is my English book?</code>\n<i>(Artinya: Di mana buku bahasa Inggris saya?)</i>",
        "expected": [
            "where is my english book",
            "where is my english book?",
            "where is my book"
        ],
        "primary_answer": "Where is my English book?"
    },
    {
        "id": "conv_beg_53",
        "badge": "💬 Mengaku Tidak Tahu (I Do Not Know)",
        "prompt": "<b>🤷 Situasi:</b> Teman bertanya alamat rumah seseorang yang belum kamu kenal.\n\n👉 <b>Giliranmu:</b> Jawab dengan jujur dan sopan bahwa kamu tidak tahu:\n<code>I do not know, sorry.</code>\n<i>(Artinya: Saya tidak tahu, maaf ya.)</i>",
        "expected": [
            "i do not know, sorry",
            "i do not know sorry",
            "i don't know, sorry",
            "i dont know sorry",
            "i do not know",
            "i don't know"
        ],
        "primary_answer": "I do not know, sorry."
    },
    {
        "id": "conv_beg_54",
        "badge": "💬 Sudah Paham (I Understand)",
        "prompt": "<b>💡 Situasi:</b> Guru selesai menerangkan rumus dan bertanya: \"Do you understand?\"\n\n👉 <b>Giliranmu:</b> Jawab bahwa kamu sekarang sudah paham:\n<code>I understand the lesson now.</code>\n<i>(Artinya: Saya paham pelajarannya sekarang.)</i>",
        "expected": [
            "i understand the lesson now",
            "i understand the lesson",
            "i understand now",
            "i understand"
        ],
        "primary_answer": "I understand the lesson now."
    },
    {
        "id": "conv_beg_55",
        "badge": "💬 Senang Membantu (Glad to Help)",
        "prompt": "<b>😊 Situasi:</b> Teman mengucapkan terima kasih setelah kamu meminjamkannya pensil warna.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu sangat senang bisa membantunya:\n<code>I am very happy to help you.</code>\n<i>(Artinya: Saya sangat senang membantumu.)</i>",
        "expected": [
            "i am very happy to help you",
            "i'm happy to help you",
            "happy to help you",
            "happy to help"
        ],
        "primary_answer": "I am very happy to help you."
    },
    {
        "id": "conv_beg_56",
        "badge": "💬 Meminta Tolong Geser Meja (Help Move Table)",
        "prompt": "<b>📦 Situasi:</b> Meja belajarmu terlalu berat untuk diangkat sendirian.\n\n👉 <b>Giliranmu:</b> Minta tolong teman membantumu:\n<code>Can you help me move this table?</code>\n<i>(Artinya: Bisakah kamu membantuku memindahkan meja ini?)</i>",
        "expected": [
            "can you help me move this table",
            "can you help me move this table?",
            "help me move this table"
        ],
        "primary_answer": "Can you help me move this table?"
    },
    {
        "id": "conv_beg_57",
        "badge": "💬 Mengajak Masuk dan Duduk (Come In and Sit Down)",
        "prompt": "<b>🪑 Situasi:</b> Tamumu berdiri di pintu rumahmu dengan sungkan.\n\n👉 <b>Giliranmu:</b> Persilakan dia masuk dan duduk dengan ramah:\n<code>Please come in and sit down.</code>\n<i>(Artinya: Silakan masuk dan duduk.)</i>",
        "expected": [
            "please come in and sit down",
            "come in and sit down",
            "please come in"
        ],
        "primary_answer": "Please come in and sit down."
    },
    {
        "id": "conv_beg_58",
        "badge": "💬 Selamat Hari Minggu (Have a Great Sunday)",
        "prompt": "<b>☀️ Situasi:</b> Hari Sabtu siang saat pulang, kamu berpamitan pada kawan.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat berakhir pekan / hari Minggu:\n<code>Have a great Sunday!</code>\n<i>(Artinya: Semoga hari Minggumu menyenangkan!)</i>",
        "expected": [
            "have a great sunday",
            "have a great sunday!",
            "have a nice sunday"
        ],
        "primary_answer": "Have a great Sunday!"
    },
    {
        "id": "conv_beg_59",
        "badge": "💬 Memuji Kerapian Teman (Your Shirt Looks Neat)",
        "prompt": "<b>👔 Situasi:</b> Temanmu memakai seragam baru yang disetrika sangat rapi.\n\n👉 <b>Giliranmu:</b> Berikan pujian hangat kepadanya:\n<code>Your shirt looks very neat!</code>\n<i>(Artinya: Bajumu terlihat sangat rapi!)</i>",
        "expected": [
            "your shirt looks very neat",
            "your shirt looks very neat!",
            "your shirt looks neat"
        ],
        "primary_answer": "Your shirt looks very neat!"
    },
    {
        "id": "conv_beg_60",
        "badge": "💬 Punya Sepeda Baru (I Have a New Bicycle)",
        "prompt": "<b>🚲 Situasi:</b> Temanmu melihatmu berangkat ke sekolah dengan sepeda anyar.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu memiliki sepeda baru warna merah:\n<code>I have a new red bicycle.</code>\n<i>(Artinya: Saya punya sepeda baru berwarna merah.)</i>",
        "expected": [
            "i have a new red bicycle",
            "i have a new bicycle",
            "have a new red bicycle"
        ],
        "primary_answer": "I have a new red bicycle."
    },
    {
        "id": "conv_beg_61",
        "badge": "💬 Menanyakan Waktu Sekarang (What Time Is It)",
        "prompt": "<b>⏰ Situasi:</b> Kamu tidak membawa jam tangan saat belajar mandiri.\n\n👉 <b>Giliranmu:</b> Tanyakan jam berapa sekarang kepada teman sebelahmu:\n<code>What time is it right now?</code>\n<i>(Artinya: Jam berapa sekarang?)</i>",
        "expected": [
            "what time is it right now",
            "what time is it right now?",
            "what time is it now",
            "what time is it"
        ],
        "primary_answer": "What time is it right now?"
    },
    {
        "id": "conv_beg_62",
        "badge": "💬 Ingin Minum Teh Hangat (Warm Cup of Tea)",
        "prompt": "<b>🍵 Situasi:</b> Sore hari saat hujan rintik-rintik, kamu ditanya ingin minum apa.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu ingin secangkir teh hangat:\n<code>I want a warm cup of tea.</code>\n<i>(Artinya: Saya mau secangkir teh hangat.)</i>",
        "expected": [
            "i want a warm cup of tea",
            "i want a cup of tea",
            "warm cup of tea",
            "a warm cup of tea"
        ],
        "primary_answer": "I want a warm cup of tea."
    },
    {
        "id": "conv_beg_63",
        "badge": "💬 Pamit Pulang ke Guru (Goodbye Teacher)",
        "prompt": "<b>🏫 Situasi:</b> Bel sekolah berbunyi tanda berakhirnya seluruh pelajaran hari ini.\n\n👉 <b>Giliranmu:</b> Berpamitan santun kepada guru sebelum melangkah keluar:\n<code>Goodbye, Teacher! See you tomorrow.</code>\n<i>(Artinya: Selamat tinggal, Guru! Sampai jumpa besok.)</i>",
        "expected": [
            "goodbye, teacher! see you tomorrow",
            "goodbye teacher see you tomorrow",
            "goodbye teacher, see you tomorrow",
            "see you tomorrow"
        ],
        "primary_answer": "Goodbye, Teacher! See you tomorrow."
    },
    {
        "id": "conv_beg_64",
        "badge": "💬 Siap Menghadapi Ujian (Ready for the Test)",
        "prompt": "<b>📖 Situasi:</b> Pagi ini ada ulangan harian, temanmu bertanya apakah kamu sudah belajar.\n\n👉 <b>Giliranmu:</b> Jawab dengan percaya diri bahwa kamu siap ujian:\n<code>I am ready for the test.</code>\n<i>(Artinya: Saya siap untuk ujian.)</i>",
        "expected": [
            "i am ready for the test",
            "i'm ready for the test",
            "ready for the test"
        ],
        "primary_answer": "I am ready for the test."
    },
    {
        "id": "conv_beg_65",
        "badge": "💬 Minta Maaf Terlambat (Sorry for Being Late)",
        "prompt": "<b>⏰ Situasi:</b> Rantai sepedamu putus di jalan sehingga kamu terlambat lima menit.\n\n👉 <b>Giliranmu:</b> Minta maaf pada guru karena terlambat:\n<code>I am sorry for being late, Teacher.</code>\n<i>(Artinya: Maafkan saya karena terlambat, Guru.)</i>",
        "expected": [
            "i am sorry for being late, teacher",
            "i am sorry for being late teacher",
            "i'm sorry for being late",
            "sorry for being late"
        ],
        "primary_answer": "I am sorry for being late, Teacher."
    },
    {
        "id": "conv_beg_66",
        "badge": "💬 Mendoakan Keberuntungan Ujian (Good Luck on Exam)",
        "prompt": "<b>🍀 Situasi:</b> Sahabatmu hendak maju mengikuti lomba cerdas cermat.\n\n👉 <b>Giliranmu:</b> Doakan agar dia beruntung dan sukses:\n<code>Good luck on your exam!</code>\n<i>(Artinya: Semoga sukses dalam ujianmu!)</i>",
        "expected": [
            "good luck on your exam",
            "good luck on your exam!",
            "good luck"
        ],
        "primary_answer": "Good luck on your exam!"
    },
    {
        "id": "conv_beg_67",
        "badge": "💬 Membuka Jendela Kelas (Open the Window)",
        "prompt": "<b>🪟 Situasi:</b> Ruang kelas terasa pengap dan kamu ingin membuka jendela.\n\n👉 <b>Giliranmu:</b> Minta izin membuka jendela kelas:\n<code>May I open the window, please?</code>\n<i>(Artinya: Bolehkah saya membuka jendelanya?)</i>",
        "expected": [
            "may i open the window, please",
            "may i open the window please",
            "may i open the window",
            "can i open the window"
        ],
        "primary_answer": "May I open the window, please?"
    }
],
    config.LEVEL_INTERMEDIATE: [
    {
        "id": "conv_int_01",
        "badge": "💬 Hobi Membaca Buku (Reading Hobby)",
        "prompt": "<b>📚 Situasi:</b> Temanmu bertanya tentang kegiatan favoritmu: <i>\"What do you like to do in your free time?\"</i>\n\n👉 <b>Giliranmu:</b> Jawab bahwa kamu suka membaca buku cerita:\n<code>I like reading storybooks in my free time.</code>\n<i>(Artinya: Saya suka membaca buku cerita di waktu luang.)</i>",
        "expected": [
            "i like reading storybooks in my free time",
            "i like reading storybooks",
            "i like reading books",
            "i like reading",
            "reading storybooks"
        ],
        "primary_answer": "I like reading storybooks in my free time."
    },
    {
        "id": "conv_int_02",
        "badge": "💬 Memesan Sarapan (Ordering Breakfast)",
        "prompt": "<b>🍳 Situasi:</b> Ibu bertanya kamu mau sarapan apa pagi ini.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu ingin makan nasi goreng dan minum susu:\n<code>I want fried rice and milk for breakfast.</code>\n<i>(Artinya: Saya mau nasi goreng dan susu untuk sarapan.)</i>",
        "expected": [
            "i want fried rice and milk for breakfast",
            "i want fried rice and milk",
            "fried rice and milk",
            "i want fried rice"
        ],
        "primary_answer": "I want fried rice and milk for breakfast."
    },
    {
        "id": "conv_int_03",
        "badge": "💬 Menanyakan Lokasi Perpustakaan (Asking Directions)",
        "prompt": "<b>📖 Situasi:</b> Kamu sedang mencari ruang perpustakaan di sekolah baru.\n\n👉 <b>Giliranmu:</b> Tanyakan kepada kakak kelas di mana letak perpustakaan:\n<code>Where is the school library?</code>\n<i>(Artinya: Di mana perpustakaan sekolah?)</i>",
        "expected": [
            "where is the school library",
            "where is the school library?",
            "where is the library",
            "where is the library?"
        ],
        "primary_answer": "Where is the school library?"
    },
    {
        "id": "conv_int_04",
        "badge": "💬 Menceritakan Kucing Peliharaan (Talking About Pets)",
        "prompt": "<b>🐱 Situasi:</b> Temanmu bertanya apakah kamu memelihara hewan di rumah.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu memiliki seekor kucing lucu bernama Milo:\n<code>I have a cute cat named Milo.</code>\n<i>(Artinya: Saya punya seekor kucing lucu bernama Milo.)</i>",
        "expected": [
            "i have a cute cat named milo",
            "i have a cute cat",
            "i have a cat named milo",
            "i have a cat"
        ],
        "primary_answer": "I have a cute cat named Milo."
    },
    {
        "id": "conv_int_05",
        "badge": "💬 Cuaca Hari Ini (Talking About Weather)",
        "prompt": "<b>☀️ Situasi:</b> Kamu melihat ke luar jendela kelas dan cuaca sangat cerah.\n\n👉 <b>Giliranmu:</b> Katakan pada teman bahwa cuaca hari ini cerah:\n<code>The weather is sunny and bright today.</code>\n<i>(Artinya: Cuaca hari ini cerah dan terang.)</i>",
        "expected": [
            "the weather is sunny and bright today",
            "the weather is sunny today",
            "it is sunny today",
            "sunny and bright"
        ],
        "primary_answer": "The weather is sunny and bright today."
    },
    {
        "id": "conv_int_06",
        "badge": "💬 Menanyakan Jam (Asking What Time It Is)",
        "prompt": "<b>⏰ Situasi:</b> Kamu ingin tahu apakah jam istirahat sudah tiba.\n\n👉 <b>Giliranmu:</b> Tanyakan jam berapa sekarang kepada teman sebangkumu:\n<code>What time is it now?</code>\n<i>(Artinya: Jam berapa sekarang?)</i>",
        "expected": [
            "what time is it now",
            "what time is it now?",
            "what time is it",
            "what time is it?"
        ],
        "primary_answer": "What time is it now?"
    },
    {
        "id": "conv_int_07",
        "badge": "💬 Rencana Akhir Pekan (Weekend Plans)",
        "prompt": "<b>🏡 Situasi:</b> Temanmu bertanya apa rencanamu di hari Minggu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu akan mengunjungi kakek dan nenek:\n<code>I will visit my grandparents this weekend.</code>\n<i>(Artinya: Saya akan mengunjungi kakek-nenek akhir pekan ini.)</i>",
        "expected": [
            "i will visit my grandparents this weekend",
            "i will visit my grandparents",
            "visit my grandparents",
            "i visit my grandparents"
        ],
        "primary_answer": "I will visit my grandparents this weekend."
    },
    {
        "id": "conv_int_08",
        "badge": "💬 Meminjam Pensil (Borrowing a Pencil)",
        "prompt": "<b>✏️ Situasi:</b> Pensilmu patah dan kamu ingin meminjam pensil teman.\n\n👉 <b>Giliranmu:</b> Minta izin meminjam pensil dengan sopan:\n<code>Can I borrow your pencil, please?</code>\n<i>(Artinya: Bolehkah saya meminjam pensilmu?)</i>",
        "expected": [
            "can i borrow your pencil, please",
            "can i borrow your pencil please",
            "can i borrow your pencil",
            "may i borrow your pencil"
        ],
        "primary_answer": "Can I borrow your pencil, please?"
    },
    {
        "id": "conv_int_09",
        "badge": "💬 Warna Favorit (Favorite Color)",
        "prompt": "<b>🎨 Situasi:</b> Saat pelajaran menggambar, teman bertanya warna kesukaanmu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa warna favoritmu adalah biru (atau warna lain):\n<code>My favorite color is blue.</code>\n<i>(Artinya: Warna favorit saya adalah biru.)</i>",
        "expected": [
            "my favorite color is blue",
            "my favourite color is blue",
            "favorite color is blue",
            "color is blue",
            "blue"
        ],
        "primary_answer": "My favorite color is blue."
    },
    {
        "id": "conv_int_10",
        "badge": "💬 Pelajaran Favorit (Favorite Subject)",
        "prompt": "<b>📐 Situasi:</b> Temanmu bertanya pelajaran apa yang paling kamu sukai di sekolah.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu menyukai pelajaran bahasa Inggris dan Matematika:\n<code>I like English and Mathematics.</code>\n<i>(Artinya: Saya menyukai bahasa Inggris dan Matematika.)</i>",
        "expected": [
            "i like english and mathematics",
            "i like english and math",
            "english and mathematics",
            "english and math"
        ],
        "primary_answer": "I like English and Mathematics."
    },
    {
        "id": "conv_int_11",
        "badge": "💬 Mengajak Makan Siang (Lunch at Canteen)",
        "prompt": "<b>🍱 Situasi:</b> Waktu istirahat kedua tiba, perutmu terasa lapar.\n\n👉 <b>Giliranmu:</b> Ajak temanmu makan siang bersama di kantin sekolah:\n<code>Let's eat lunch together at the canteen!</code>\n<i>(Artinya: Ayo kita makan siang bersama di kantin!)</i>",
        "expected": [
            "let's eat lunch together at the canteen",
            "let's eat lunch together",
            "lets eat lunch together",
            "eat lunch together"
        ],
        "primary_answer": "Let's eat lunch together at the canteen!"
    },
    {
        "id": "conv_int_12",
        "badge": "💬 Menawarkan Bantuan (Offering Help)",
        "prompt": "<b>📦 Situasi:</b> Temanmu tampak kerepotan membawa banyak buku paket.\n\n👉 <b>Giliranmu:</b> Tawarkan bantuan dengan ramah:\n<code>Can I help you carry the books?</code>\n<i>(Artinya: Bolehkah saya membantumu membawa buku-buku itu?)</i>",
        "expected": [
            "can i help you carry the books",
            "can i help you carry the books?",
            "can i help you",
            "may i help you"
        ],
        "primary_answer": "Can I help you carry the books?"
    },
    {
        "id": "conv_int_13",
        "badge": "💬 Jumlah Saudara (Talking About Siblings)",
        "prompt": "<b>👨‍👩‍👧‍👦 Situasi:</b> Temanmu bertanya: <i>\"How many brothers or sisters do you have?\"</i>\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu punya satu saudara laki-laki dan satu perempuan:\n<code>I have one brother and one sister.</code>\n<i>(Artinya: Saya punya satu saudara laki-laki dan satu saudara perempuan.)</i>",
        "expected": [
            "i have one brother and one sister",
            "one brother and one sister",
            "i have a brother and a sister",
            "brother and sister"
        ],
        "primary_answer": "I have one brother and one sister."
    },
    {
        "id": "conv_int_14",
        "badge": "💬 Mengingatkan Payung (Rainy Weather)",
        "prompt": "<b>🌧️ Situasi:</b> Hujan mulai turun rintik-rintik menjelang jam pulang sekolah.\n\n👉 <b>Giliranmu:</b> Ingatkan temanmu untuk membawa payung:\n<code>It is raining outside, don't forget your umbrella!</code>\n<i>(Artinya: Di luar sedang hujan, jangan lupa payungmu!)</i>",
        "expected": [
            "it is raining outside, don't forget your umbrella",
            "it is raining outside",
            "don't forget your umbrella",
            "dont forget your umbrella"
        ],
        "primary_answer": "It is raining outside, don't forget your umbrella!"
    },
    {
        "id": "conv_int_15",
        "badge": "💬 Hobi Berolahraga (Playing Football)",
        "prompt": "<b>⚽ Situasi:</b> Kamu senang berolahraga di lapangan bersama kawan-kawan.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa kamu bermain sepak bola setiap sore:\n<code>I play football with my friends every afternoon.</code>\n<i>(Artinya: Saya bermain sepak bola bersama teman-teman setiap sore.)</i>",
        "expected": [
            "i play football with my friends every afternoon",
            "i play football with my friends",
            "i play football every afternoon",
            "play football"
        ],
        "primary_answer": "I play football with my friends every afternoon."
    },
    {
        "id": "conv_int_16",
        "badge": "💬 Ucapan Ulang Tahun (Birthday Wishes)",
        "prompt": "<b>🎂 Situasi:</b> Sahabatmu hari ini merayakan hari ulang tahunnya.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat ulang tahun dengan doa kebaikan:\n<code>Happy birthday! I wish you all the best.</code>\n<i>(Artinya: Selamat ulang tahun! Semoga yang terbaik untukmu.)</i>",
        "expected": [
            "happy birthday! i wish you all the best",
            "happy birthday i wish you all the best",
            "happy birthday",
            "all the best"
        ],
        "primary_answer": "Happy birthday! I wish you all the best."
    },
    {
        "id": "conv_int_17",
        "badge": "💬 Memuji Gambar Teman (Giving a Compliment)",
        "prompt": "<b>🖼️ Situasi:</b> Temanmu menggambar pemandangan gunung yang sangat indah.\n\n👉 <b>Giliranmu:</b> Berikan pujian tulus atas karyanya:\n<code>Your drawing is very beautiful!</code>\n<i>(Artinya: Gambarmu sangat indah!)</i>",
        "expected": [
            "your drawing is very beautiful",
            "your drawing is very beautiful!",
            "your drawing is beautiful",
            "very beautiful"
        ],
        "primary_answer": "Your drawing is very beautiful!"
    },
    {
        "id": "conv_int_18",
        "badge": "💬 Meminta Pengulangan Ucapan (Pardon Me)",
        "prompt": "<b>👂 Situasi:</b> Guru memberikan instruksi tetapi suaranya kurang terdengar jelas olehmu.\n\n👉 <b>Giliranmu:</b> Minta guru mengulangi kalimatnya dengan sangat santun:\n<code>Could you please repeat that, Teacher?</code>\n<i>(Artinya: Bisakah Ibu/Bapak Guru mengulanginya?)</i>",
        "expected": [
            "could you please repeat that",
            "could you please repeat that, teacher",
            "could you repeat that",
            "please repeat that"
        ],
        "primary_answer": "Could you please repeat that, Teacher?"
    },
    {
        "id": "conv_int_19",
        "badge": "💬 Seragam Sekolah (School Uniform)",
        "prompt": "<b>👔 Situasi:</b> Kamu menceritakan pakaian yang kamu kenakan di hari Senin.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu memakai seragam merah putih:\n<code>I wear a red and white uniform on Monday.</code>\n<i>(Artinya: Saya memakai seragam merah putih pada hari Senin.)</i>",
        "expected": [
            "i wear a red and white uniform on monday",
            "i wear a red and white uniform",
            "red and white uniform",
            "wear uniform"
        ],
        "primary_answer": "I wear a red and white uniform on Monday."
    },
    {
        "id": "conv_int_20",
        "badge": "💬 Antusias Karya Wisata (School Trip)",
        "prompt": "<b>🚌 Situasi:</b> Besok kelasmu akan pergi karya wisata ke kebun binatang.\n\n👉 <b>Giliranmu:</b> Ungkapkan rasa semangatmu menyambut perjalanan besok:\n<code>I am very excited about our school trip tomorrow!</code>\n<i>(Artinya: Saya sangat bersemangat menyambut karya wisata sekolah kita besok!)</i>",
        "expected": [
            "i am very excited about our school trip tomorrow",
            "i am very excited about our school trip",
            "excited about our school trip",
            "excited school trip"
        ],
        "primary_answer": "I am very excited about our school trip tomorrow!"
    },
    {
        "id": "conv_int_21",
        "badge": "💬 Menanyakan Hobi Teman (Asking Hobby)",
        "prompt": "<b>🎯 Situasi:</b> Kamu ingin lebih akrab dengan teman baru saat istirahat.\n\n👉 <b>Giliranmu:</b> Tanyakan apa hobi favoritnya:\n<code>What is your favorite hobby?</code>\n<i>(Artinya: Apa hobi kesukaanmu?)</i>",
        "expected": [
            "what is your favorite hobby",
            "what is your favorite hobby?",
            "what is your favourite hobby",
            "what's your favorite hobby"
        ],
        "primary_answer": "What is your favorite hobby?"
    },
    {
        "id": "conv_int_22",
        "badge": "💬 Memilih Minuman (Expressing Preference)",
        "prompt": "<b>🍊 Situasi:</b> Di warung makan, teman bertanya kamu ingin minum jus jeruk atau teh.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu lebih suka jus jeruk:\n<code>I prefer fresh orange juice, please.</code>\n<i>(Artinya: Saya lebih memilih jus jeruk segar.)</i>",
        "expected": [
            "i prefer fresh orange juice, please",
            "i prefer orange juice",
            "orange juice please",
            "orange juice"
        ],
        "primary_answer": "I prefer fresh orange juice, please."
    },
    {
        "id": "conv_int_23",
        "badge": "💬 Mengajak Belajar Bersama (Study Together)",
        "prompt": "<b>📖 Situasi:</b> Ada tugas kelompok bahasa Inggris yang harus dikerjakan.\n\n👉 <b>Giliranmu:</b> Ajak kawanmu belajar bersama di rumahmu sore nanti:\n<code>Would you like to study English together this afternoon?</code>\n<i>(Artinya: Maukah kamu belajar bahasa Inggris bersama sore ini?)</i>",
        "expected": [
            "would you like to study english together this afternoon",
            "would you like to study english together",
            "study english together",
            "study together"
        ],
        "primary_answer": "Would you like to study English together this afternoon?"
    },
    {
        "id": "conv_int_24",
        "badge": "💬 Terima Kasih Bantuan PR (Thanking for Homework Help)",
        "prompt": "<b>🌟 Situasi:</b> Sahabatmu dengan sabar mengajarimu cara mengerjakan PR Matematika.\n\n👉 <b>Giliranmu:</b> Ucapkan terima kasih atas bantuannya yang berharga:\n<code>Thank you for helping me with my homework!</code>\n<i>(Artinya: Terima kasih sudah membantuku mengerjakan PR!)</i>",
        "expected": [
            "thank you for helping me with my homework",
            "thank you for helping me",
            "thank you helping homework",
            "thanks for helping"
        ],
        "primary_answer": "Thank you for helping me with my homework!"
    },
    {
        "id": "conv_int_25",
        "badge": "💬 Membeli Tiket Bus (Buying Bus Ticket)",
        "prompt": "<b>🚌 Situasi:</b> Kamu berada di loket terminal bus dan ingin membeli satu tiket ke kota.\n\n👉 <b>Giliranmu:</b> Katakan pada petugas bahwa kamu ingin membeli satu tiket bus:\n<code>I would like to buy one bus ticket, please.</code>\n<i>(Artinya: Saya ingin membeli satu tiket bus.)</i>",
        "expected": [
            "i would like to buy one bus ticket, please",
            "i would like to buy one bus ticket please",
            "i want to buy one bus ticket",
            "buy one bus ticket please"
        ],
        "primary_answer": "I would like to buy one bus ticket, please."
    },
    {
        "id": "conv_int_26",
        "badge": "💬 Menanyakan Halte Terdekat (Nearest Bus Stop)",
        "prompt": "<b>🚏 Situasi:</b> Kamu sedang di jalan raya dan mencari halte bus terdekat.\n\n👉 <b>Giliranmu:</b> Tanyakan lokasi halte bus terdekat dengan sopan:\n<code>Excuse me, where is the nearest bus stop?</code>\n<i>(Artinya: Permisi, di mana halte bus terdekat?)</i>",
        "expected": [
            "excuse me, where is the nearest bus stop",
            "excuse me, where is the nearest bus stop?",
            "where is the nearest bus stop",
            "where is the nearest bus stop?"
        ],
        "primary_answer": "Excuse me, where is the nearest bus stop?"
    },
    {
        "id": "conv_int_27",
        "badge": "💬 Menolak Ajakan dengan Sopan (Declining Politely)",
        "prompt": "<b>🤝 Situasi:</b> Teman mengajakmu bermain bola, tetapi kamu harus membantu Ibu di rumah.\n\n👉 <b>Giliranmu:</b> Tolak dengan sopan dan sebutkan alasannya:\n<code>I would love to, but I have to help my mother.</code>\n<i>(Artinya: Saya ingin sekali, tetapi saya harus membantu ibuku.)</i>",
        "expected": [
            "i would love to, but i have to help my mother",
            "i would love to but i have to help my mother",
            "i have to help my mother"
        ],
        "primary_answer": "I would love to, but I have to help my mother."
    },
    {
        "id": "conv_int_28",
        "badge": "💬 Mengembalikan Buku Perpustakaan (Returning Books)",
        "prompt": "<b>📖 Situasi:</b> Kamu mengembalikan dua buku cerita ke meja pustakawan.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu ingin mengembalikan dua buku cerita ini:\n<code>I want to return these two storybooks.</code>\n<i>(Artinya: Saya ingin mengembalikan dua buku cerita ini.)</i>",
        "expected": [
            "i want to return these two storybooks",
            "i would like to return these two storybooks",
            "return these two storybooks"
        ],
        "primary_answer": "I want to return these two storybooks."
    },
    {
        "id": "conv_int_29",
        "badge": "💬 Rencana Liburan ke Kebun Teh (Visiting Tea Garden)",
        "prompt": "<b>⛰️ Situasi:</b> Temanmu bertanya tujuan liburan keluargamu di akhir pekan.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa kalian berencana mengunjungi kebun teh di pegunungan:\n<code>We plan to visit the tea garden in the mountains.</code>\n<i>(Artinya: Kami berencana mengunjungi kebun teh di pegunungan.)</i>",
        "expected": [
            "we plan to visit the tea garden in the mountains",
            "we plan to visit the tea garden",
            "visit the tea garden in the mountains"
        ],
        "primary_answer": "We plan to visit the tea garden in the mountains."
    },
    {
        "id": "conv_int_30",
        "badge": "💬 Meminta Penjelasan Lebih Pelan (Explain More Slowly)",
        "prompt": "<b>👂 Situasi:</b> Penjelasan gurumu agak terlalu cepat dan kamu ingin mendengarnya lagi.\n\n👉 <b>Giliranmu:</b> Minta guru menerangkan lebih perlahan dengan santun:\n<code>Could you explain that again more slowly, please?</code>\n<i>(Artinya: Bisakah Bapak/Ibu menjelaskannya lagi lebih perlahan?)</i>",
        "expected": [
            "could you explain that again more slowly, please",
            "could you explain that again more slowly please",
            "could you explain that again more slowly",
            "explain that again more slowly"
        ],
        "primary_answer": "Could you explain that again more slowly, please?"
    },
    {
        "id": "conv_int_31",
        "badge": "💬 Memesan Minuman Rendah Gula (Less Sugar Iced Tea)",
        "prompt": "<b>🍹 Situasi:</b> Di kantin, kamu memesan es teh dengan sedikit gula saja.\n\n👉 <b>Giliranmu:</b> Katakan pada penjual pesanan es teh sedikit gulamu:\n<code>Can I have an iced tea with less sugar, please?</code>\n<i>(Artinya: Bolehkah saya pesan es teh dengan sedikit gula?)</i>",
        "expected": [
            "can i have an iced tea with less sugar, please",
            "can i have an iced tea with less sugar please",
            "iced tea with less sugar, please",
            "iced tea with less sugar"
        ],
        "primary_answer": "Can I have an iced tea with less sugar, please?"
    },
    {
        "id": "conv_int_32",
        "badge": "💬 Memuji Presentasi Teman (Praising Presentation)",
        "prompt": "<b>👏 Situasi:</b> Kelompok temanmu selesai mempresentasikan materi di depan kelas dengan sangat baik.\n\n👉 <b>Giliranmu:</b> Berikan pujian bahwa presentasinya jelas dan informatif:\n<code>The presentation was very clear and informative.</code>\n<i>(Artinya: Presentasinya sangat jelas dan informatif.)</i>",
        "expected": [
            "the presentation was very clear and informative",
            "presentation was very clear and informative",
            "very clear and informative"
        ],
        "primary_answer": "The presentation was very clear and informative."
    },
    {
        "id": "conv_int_33",
        "badge": "💬 Menentukan Waktu Kerja Kelompok (Group Meeting Time)",
        "prompt": "<b>👥 Situasi:</b> Kamu dan anggota kelompok merencanakan pertemuan menyelesaikan poster.\n\n👉 <b>Giliranmu:</b> Tanyakan kapan kelompok bisa bertemu untuk menyelesaikan proyek:\n<code>When should our group meet to finish the project?</code>\n<i>(Artinya: Kapan kelompok kita harus bertemu untuk menyelesaikan proyek?)</i>",
        "expected": [
            "when should our group meet to finish the project",
            "when should our group meet to finish the project?",
            "when should our group meet"
        ],
        "primary_answer": "When should our group meet to finish the project?"
    },
    {
        "id": "conv_int_34",
        "badge": "💬 Mengingatkan Pertemuan English Club (English Club Reminder)",
        "prompt": "<b>⏰ Situasi:</b> Sore ini ada latihan klub bahasa Inggris pukul 16.00.\n\n👉 <b>Giliranmu:</b> Ingatkan teman agar tidak lupa hadir:\n<code>Don't forget we have an English club meeting at four.</code>\n<i>(Artinya: Jangan lupa kita ada pertemuan klub bahasa Inggris jam empat.)</i>",
        "expected": [
            "don't forget we have an english club meeting at four",
            "dont forget we have an english club meeting at four",
            "we have an english club meeting at four"
        ],
        "primary_answer": "Don't forget we have an English club meeting at four."
    },
    {
        "id": "conv_int_35",
        "badge": "💬 Makanan Kesukaan Kelinci Piaraan (Pet Rabbit Food)",
        "prompt": "<b>🐰 Situasi:</b> Teman bertanya apa makanan kelinci peliharaanmu di rumah.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa kelincimu suka makan wortel dan bayam segar:\n<code>My pet rabbit likes to eat fresh carrots and spinach.</code>\n<i>(Artinya: Kelinci peliharaanku suka makan wortel dan bayam segar.)</i>",
        "expected": [
            "my pet rabbit likes to eat fresh carrots and spinach",
            "rabbit likes to eat fresh carrots and spinach",
            "my pet rabbit likes carrots and spinach"
        ],
        "primary_answer": "My pet rabbit likes to eat fresh carrots and spinach."
    },
    {
        "id": "conv_int_36",
        "badge": "💬 Menanyakan Jam Buka Toko Buku (Bookstore Opening Time)",
        "prompt": "<b>📚 Situasi:</b> Kamu ingin membeli buku tulis besok pagi di toko buku.\n\n👉 <b>Giliranmu:</b> Tanyakan jam berapa toko buku tersebut buka besok:\n<code>What time does the bookstore open tomorrow?</code>\n<i>(Artinya: Jam berapa toko buku itu buka besok?)</i>",
        "expected": [
            "what time does the bookstore open tomorrow",
            "what time does the bookstore open tomorrow?",
            "what time does the bookstore open"
        ],
        "primary_answer": "What time does the bookstore open tomorrow?"
    },
    {
        "id": "conv_int_37",
        "badge": "💬 Memuji Rasa Nasi Goreng (Tasty Fried Rice)",
        "prompt": "<b>🍳 Situasi:</b> Temanmu membagikan bekal nasi goreng buatannya yang lezat.\n\n👉 <b>Giliranmu:</b> Puji bahwa nasi gorengnya sangat enak dan gurih:\n<code>This fried rice is really tasty and flavorful!</code>\n<i>(Artinya: Nasi goreng ini sungguh enak dan kaya rasa!)</i>",
        "expected": [
            "this fried rice is really tasty and flavorful",
            "this fried rice is really tasty and flavorful!",
            "this fried rice is really tasty"
        ],
        "primary_answer": "This fried rice is really tasty and flavorful!"
    },
    {
        "id": "conv_int_38",
        "badge": "💬 Rekomendasi Buku Kosakata (Vocabulary Book Advice)",
        "prompt": "<b>📖 Situasi:</b> Di perpustakaan, kamu meminta saran teman yang pintar bahasa Inggris.\n\n👉 <b>Giliranmu:</b> Tanyakan buku mana yang ia rekomendasikan untuk belajar kosakata:\n<code>Which book do you recommend for learning vocabulary?</code>\n<i>(Artinya: Buku mana yang kamu rekomendasikan untuk belajar kosakata?)</i>",
        "expected": [
            "which book do you recommend for learning vocabulary",
            "which book do you recommend for learning vocabulary?",
            "which book do you recommend"
        ],
        "primary_answer": "Which book do you recommend for learning vocabulary?"
    },
    {
        "id": "conv_int_39",
        "badge": "💬 Mengajak Bersepeda Sore (Riding Bicycles Together)",
        "prompt": "<b>🚲 Situasi:</b> Sore hari yang sejuk, kamu ingin mengajak tetangga bermain sepeda.\n\n👉 <b>Giliranmu:</b> Ajak temanmu bersepeda mengelilingi perumahan / desa:\n<code>Do you want to ride bicycles around the neighborhood?</code>\n<i>(Artinya: Maukah kamu bersepeda keliling lingkungan sekitar?)</i>",
        "expected": [
            "do you want to ride bicycles around the neighborhood",
            "do you want to ride bicycles around the neighborhood?",
            "ride bicycles around the neighborhood"
        ],
        "primary_answer": "Do you want to ride bicycles around the neighborhood?"
    },
    {
        "id": "conv_int_40",
        "badge": "💬 Meminta Sup Hangat (Warming Up Soup)",
        "prompt": "<b>🍲 Situasi:</b> Sup ayam yang kamu pesan di warung terasa sudah dingin.\n\n👉 <b>Giliranmu:</b> Sampaikan keluhan dengan sopan dan minta dipanaskan:\n<code>Excuse me, my soup is cold, could you warm it up?</code>\n<i>(Artinya: Permisi, sup saya dingin, bisakah dihangatkan?)</i>",
        "expected": [
            "excuse me, my soup is cold, could you warm it up",
            "excuse me, my soup is cold, could you warm it up?",
            "could you warm it up",
            "soup is cold could you warm it up"
        ],
        "primary_answer": "Excuse me, my soup is cold, could you warm it up?"
    },
    {
        "id": "conv_int_41",
        "badge": "💬 Berbagi Payung saat Hujan (Sharing Umbrella)",
        "prompt": "<b>🌧️ Situasi:</b> Hujan turun lebat dan kawanmu tidak membawa payung.\n\n👉 <b>Giliranmu:</b> Tawarkan untuk berbagi payung agar dia tidak kehujanan:\n<code>You can share my umbrella so you won't get wet.</code>\n<i>(Artinya: Kamu boleh memakai payungku bersama agar tidak basah.)</i>",
        "expected": [
            "you can share my umbrella so you won't get wet",
            "you can share my umbrella so you wont get wet",
            "you can share my umbrella"
        ],
        "primary_answer": "You can share my umbrella so you won't get wet."
    },
    {
        "id": "conv_int_42",
        "badge": "💬 Cita-cita Menjadi Guru Bahasa Inggris (Becoming English Teacher)",
        "prompt": "<b>👩‍🏫 Situasi:</b> Dalam perbincangan tentang masa depan, kamu menceritakan mimpimu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu ingin menjadi guru bahasa Inggris di kampung halaman:\n<code>I want to become an English teacher in my hometown.</code>\n<i>(Artinya: Saya ingin menjadi guru bahasa Inggris di kampung halaman saya.)</i>",
        "expected": [
            "i want to become an english teacher in my hometown",
            "i want to be an english teacher in my hometown",
            "become an english teacher in my hometown"
        ],
        "primary_answer": "I want to become an English teacher in my hometown."
    },
    {
        "id": "conv_int_43",
        "badge": "💬 Asal Sekolah Dasar (Previous School)",
        "prompt": "<b>🏫 Situasi:</b> Teman barumu penasaran tentang sekolah asalmu terdahulu.\n\n👉 <b>Giliranmu:</b> Tanyakan dari Sekolah Dasar mana ia lulus:\n<code>Which elementary school did you graduate from?</code>\n<i>(Artinya: Dari sekolah dasar mana kamu lulus?)</i>",
        "expected": [
            "which elementary school did you graduate from",
            "which elementary school did you graduate from?",
            "which school did you graduate from"
        ],
        "primary_answer": "Which elementary school did you graduate from?"
    },
    {
        "id": "conv_int_44",
        "badge": "💬 Meminjam Kamus Sebentar (Borrowing Dictionary)",
        "prompt": "<b>📚 Situasi:</b> Kamu perlu mengecek arti satu kata sulit di kamus milik teman.\n\n👉 <b>Giliranmu:</b> Minta izin meminjam kamus sebentar saja:\n<code>May I borrow your English dictionary for a moment?</code>\n<i>(Artinya: Bolehkah saya meminjam kamus bahasa Inggrismu sebentar?)</i>",
        "expected": [
            "may i borrow your english dictionary for a moment",
            "may i borrow your english dictionary for a moment?",
            "can i borrow your english dictionary for a moment"
        ],
        "primary_answer": "May I borrow your English dictionary for a moment?"
    },
    {
        "id": "conv_int_45",
        "badge": "💬 Menjelaskan Aturan Permainan (Explaining Game Rules)",
        "prompt": "<b>🎲 Situasi:</b> Temanmu belum pernah bermain ular tangga dan bertanya caranya.\n\n👉 <b>Giliranmu:</b> Jelaskan langkah awal melempar dadu dan menggerakkan bidak:\n<code>First, you throw the dice and move your piece.</code>\n<i>(Artinya: Pertama, kamu lempar dadunya dan gerakkan bidakmu.)</i>",
        "expected": [
            "first, you throw the dice and move your piece",
            "first you throw the dice and move your piece",
            "throw the dice and move your piece"
        ],
        "primary_answer": "First, you throw the dice and move your piece."
    },
    {
        "id": "conv_int_46",
        "badge": "💬 Menanyakan Keadaan Teman Murung (Checking on Friend)",
        "prompt": "<b>😟 Situasi:</b> Temanmu tampak lesu dan pucat saat duduk di kelas.\n\n👉 <b>Giliranmu:</b> Tanyakan keadaannya dengan penuh rasa peduli:\n<code>You look tired today, are you feeling alright?</code>\n<i>(Artinya: Kamu tampak lelah hari ini, apakah kamu baik-baik saja?)</i>",
        "expected": [
            "you look tired today, are you feeling alright",
            "you look tired today, are you feeling alright?",
            "you look tired today are you feeling alright?",
            "are you feeling alright"
        ],
        "primary_answer": "You look tired today, are you feeling alright?"
    },
    {
        "id": "conv_int_47",
        "badge": "💬 Petunjuk Membuat Teh Manis (Making Sweet Tea)",
        "prompt": "<b>🍵 Situasi:</b> Adikmu bertanya bagaimana cara membuat teh manis yang pas.\n\n👉 <b>Giliranmu:</b> Jelaskan bahwa ia perlu menambahkan dua sendok gula:\n<code>To make sweet tea, add two spoons of sugar.</code>\n<i>(Artinya: Untuk membuat teh manis, tambahkan dua sendok gula.)</i>",
        "expected": [
            "to make sweet tea, add two spoons of sugar",
            "to make sweet tea add two spoons of sugar",
            "add two spoons of sugar"
        ],
        "primary_answer": "To make sweet tea, add two spoons of sugar."
    },
    {
        "id": "conv_int_48",
        "badge": "💬 Mengingatkan Baju Olahraga (Sports Uniform Reminder)",
        "prompt": "<b>🏃 Situasi:</b> Besok ada jadwal pelajaran senam dan lari pagi di sekolah.\n\n👉 <b>Giliranmu:</b> Ingatkan sahabatmu untuk membawa seragam olahraga besok:\n<code>Remember to bring your sports uniform tomorrow.</code>\n<i>(Artinya: Ingat untuk membawa seragam olahragamu besok.)</i>",
        "expected": [
            "remember to bring your sports uniform tomorrow",
            "remember to bring your sports uniform",
            "bring your sports uniform tomorrow"
        ],
        "primary_answer": "Remember to bring your sports uniform tomorrow."
    },
    {
        "id": "conv_int_49",
        "badge": "💬 Menikmati Musik Gitar (Acoustic Guitar Music)",
        "prompt": "<b>🎸 Situasi:</b> Kamu sedang menceritakan cara menenangkan pikiran setelah seharian belajar.\n\n👉 <b>Giliranmu:</b> Katakan bahwa mendengarkan musik gitar akustik membuat pikiran rileks:\n<code>Listening to acoustic guitar music relaxes my mind.</code>\n<i>(Artinya: Mendengarkan musik gitar akustik membuat pikiranku rileks.)</i>",
        "expected": [
            "listening to acoustic guitar music relaxes my mind",
            "listening to guitar music relaxes my mind",
            "guitar music relaxes my mind"
        ],
        "primary_answer": "Listening to acoustic guitar music relaxes my mind."
    },
    {
        "id": "conv_int_50",
        "badge": "💬 Mendoakan Cepat Sembuh (Get Well Soon)",
        "prompt": "<b>💐 Situasi:</b> Temanmu sedang terbaring sakit dan tidak bisa hadir ke sekolah.\n\n👉 <b>Giliranmu:</b> Kirimkan pesan doa agar ia lekas pulih dan sembuh:\n<code>Get well soon! We all miss you at school.</code>\n<i>(Artinya: Semoga lekas sembuh! Kami semua merindukanmu di sekolah.)</i>",
        "expected": [
            "get well soon! we all miss you at school",
            "get well soon we all miss you at school",
            "get well soon! we miss you at school",
            "get well soon"
        ],
        "primary_answer": "Get well soon! We all miss you at school."
    },
    {
        "id": "conv_int_51",
        "badge": "💬 Membersihkan Kelas Bersama (Cleaning Classroom)",
        "prompt": "<b>🧹 Situasi:</b> Jam pelajaran berakhir dan lantai kelas tampak berdebu.\n\n👉 <b>Giliranmu:</b> Ajak teman-teman membersihkan kelas sebelum pulang:\n<code>Let's clean the classroom together before going home.</code>\n<i>(Artinya: Ayo kita bersihkan ruang kelas bersama sebelum pulang.)</i>",
        "expected": [
            "let's clean the classroom together before going home",
            "lets clean the classroom together before going home",
            "clean the classroom together before going home"
        ],
        "primary_answer": "Let's clean the classroom together before going home."
    },
    {
        "id": "conv_int_52",
        "badge": "💬 Jam Keberangkatan Kereta (Train Departure Time)",
        "prompt": "<b>🚆 Situasi:</b> Di stasiun kereta api, kamu ingin tahu jadwal kereta pagi ke Surabaya.\n\n👉 <b>Giliranmu:</b> Tanyakan jam berapa kereta pagi berangkat ke Surabaya:\n<code>What time does the morning train depart for Surabaya?</code>\n<i>(Artinya: Jam berapa kereta pagi berangkat menuju Surabaya?)</i>",
        "expected": [
            "what time does the morning train depart for surabaya",
            "what time does the morning train depart for surabaya?",
            "what time does the train depart for surabaya"
        ],
        "primary_answer": "What time does the morning train depart for Surabaya?"
    },
    {
        "id": "conv_int_53",
        "badge": "💬 Alasan Keterlambatan Bus (Bus Flat Tire)",
        "prompt": "<b>🚌 Situasi:</b> Kamu tiba di sekolah sedikit terlambat karena kendala di perjalanan.\n\n👉 <b>Giliranmu:</b> Jelaskan bahwa bus sekolah mengalami ban kempes di jalan:\n<code>The school bus had a flat tire on the way.</code>\n<i>(Artinya: Bus sekolah mengalami ban kempes di perjalanan.)</i>",
        "expected": [
            "the school bus had a flat tire on the way",
            "school bus had a flat tire on the way",
            "had a flat tire on the way"
        ],
        "primary_answer": "The school bus had a flat tire on the way."
    },
    {
        "id": "conv_int_54",
        "badge": "💬 Membawakan Tas Teman (Carrying Heavy Bag)",
        "prompt": "<b>🎒 Situasi:</b> Temanmu tampak kelelahan menenteng tas ransel yang sangat berat.\n\n👉 <b>Giliranmu:</b> Tawarkan bantuan untuk membawakannya:\n<code>Your bag looks heavy, let me carry it for you.</code>\n<i>(Artinya: Tasmu terlihat berat, biar saya bawakan untukmu.)</i>",
        "expected": [
            "your bag looks heavy, let me carry it for you",
            "your bag looks heavy let me carry it for you",
            "let me carry it for you"
        ],
        "primary_answer": "Your bag looks heavy, let me carry it for you."
    },
    {
        "id": "conv_int_55",
        "badge": "💬 Menanyakan Lokasi Bank (Asking for Bank/ATM)",
        "prompt": "<b>🏦 Situasi:</b> Di sekitar area pasar tradisional, kamu mencari letak ATM atau bank.\n\n👉 <b>Giliranmu:</b> Tanyakan apakah ada bank atau ATM di dekat pasar ini:\n<code>Is there an ATM or bank near this market?</code>\n<i>(Artinya: Apakah ada ATM atau bank di dekat pasar ini?)</i>",
        "expected": [
            "is there an atm or bank near this market",
            "is there an atm or bank near this market?",
            "is there an atm near this market"
        ],
        "primary_answer": "Is there an ATM or bank near this market?"
    },
    {
        "id": "conv_int_56",
        "badge": "💬 Menonton Film Animasi (Animated Movies)",
        "prompt": "<b>🎬 Situasi:</b> Teman bertanya tontonan kesukaanmu saat akhir pekan di rumah.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu sangat menikmati menonton film kartun bersama keluarga:\n<code>I really enjoy watching animated movies with my family.</code>\n<i>(Artinya: Saya sangat menikmati menonton film animasi bersama keluarga.)</i>",
        "expected": [
            "i really enjoy watching animated movies with my family",
            "i enjoy watching animated movies with my family",
            "watching animated movies with my family"
        ],
        "primary_answer": "I really enjoy watching animated movies with my family."
    },
    {
        "id": "conv_int_57",
        "badge": "💬 Bantuan Formulir Pendaftaran (Registration Form Help)",
        "prompt": "<b>📋 Situasi:</b> Ada lembar pendaftaran lomba bahasa Inggris yang petunjuknya kurang kamu pahami.\n\n👉 <b>Giliranmu:</b> Minta bantuan teman untuk membantu mengisi formulir ini:\n<code>Could you help me fill out this registration form?</code>\n<i>(Artinya: Bisakah kamu membantuku mengisi formulir pendaftaran ini?)</i>",
        "expected": [
            "could you help me fill out this registration form",
            "could you help me fill out this registration form?",
            "help me fill out this registration form"
        ],
        "primary_answer": "Could you help me fill out this registration form?"
    },
    {
        "id": "conv_int_58",
        "badge": "💬 Mematikan Keran Hemat Air (Saving Tap Water)",
        "prompt": "<b>🚰 Situasi:</b> Kamu melihat keran wastafel sekolah masih mengalirkan air sia-sia.\n\n👉 <b>Giliranmu:</b> Ingatkan kawan bahwa kita harus mematikan keran untuk hemat air:\n<code>We should turn off the tap to save water.</code>\n<i>(Artinya: Kita harus mematikan keran untuk menghemat air.)</i>",
        "expected": [
            "we should turn off the tap to save water",
            "turn off the tap to save water",
            "we must turn off the tap to save water"
        ],
        "primary_answer": "We should turn off the tap to save water."
    },
    {
        "id": "conv_int_59",
        "badge": "💬 Opini Belajar Bahasa Inggris (Opinion on Learning English)",
        "prompt": "<b>🌟 Situasi:</b> Guru meminta murid mengemukakan pendapat tentang belajar bahasa Inggris.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa menurutmu belajar bahasa Inggris sangat menyenangkan:\n<code>In my opinion, learning English is very enjoyable.</code>\n<i>(Artinya: Menurut pendapat saya, belajar bahasa Inggris sangat menyenangkan.)</i>",
        "expected": [
            "in my opinion, learning english is very enjoyable",
            "in my opinion learning english is very enjoyable",
            "learning english is very enjoyable"
        ],
        "primary_answer": "In my opinion, learning English is very enjoyable."
    },
    {
        "id": "conv_int_60",
        "badge": "💬 Waktu Kedatangan Bus (Bus Arrival Time)",
        "prompt": "<b>⏰ Situasi:</b> Kamu dan teman sudah berdiri di halte menunggu bus selama 10 menit.\n\n👉 <b>Giliranmu:</b> Tanyakan berapa lama lagi bus akan tiba:\n<code>How long does it take for the bus to arrive?</code>\n<i>(Artinya: Berapa lama waktu yang dibutuhkan bus untuk tiba?)</i>",
        "expected": [
            "how long does it take for the bus to arrive",
            "how long does it take for the bus to arrive?",
            "how long for the bus to arrive"
        ],
        "primary_answer": "How long does it take for the bus to arrive?"
    },
    {
        "id": "conv_int_61",
        "badge": "💬 Pengalaman Berkemah (Camping Experience)",
        "prompt": "<b>⛺ Situasi:</b> Kamu menceritakan pengalaman seru saat kemah pramuka di bukit pinus.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa kalian tidur di tenda dan mendengar suara jangkrik malam hari:\n<code>We slept in tents and listened to crickets at night.</code>\n<i>(Artinya: Kami tidur di tenda dan mendengarkan suara jangkrik di malam hari.)</i>",
        "expected": [
            "we slept in tents and listened to crickets at night",
            "slept in tents and listened to crickets at night",
            "we slept in tents and listened to crickets"
        ],
        "primary_answer": "We slept in tents and listened to crickets at night."
    },
    {
        "id": "conv_int_62",
        "badge": "💬 Harapan Cuaca Cerah (Hoping for Sunny Weather)",
        "prompt": "<b>🏸 Situasi:</b> Kamu dan kawan punya rencana bertanding bulu tangkis di lapangan besok pagi.\n\n👉 <b>Giliranmu:</b> Ungkapkan harapan agar besok cuaca cerah:\n<code>I hope tomorrow is sunny so we can play badminton.</code>\n<i>(Artinya: Saya berharap besok cerah sehingga kita bisa bermain bulu tangkis.)</i>",
        "expected": [
            "i hope tomorrow is sunny so we can play badminton",
            "hope tomorrow is sunny so we can play badminton",
            "tomorrow is sunny so we can play badminton"
        ],
        "primary_answer": "I hope tomorrow is sunny so we can play badminton."
    },
    {
        "id": "conv_int_63",
        "badge": "💬 Izin Pamit Meninggalkan Rapat (Leaving Meeting Early)",
        "prompt": "<b>🚪 Situasi:</b> Di rapat OSIS/kelas, kamu ada janji dokter yang tidak bisa ditunda.\n\n👉 <b>Giliranmu:</b> Minta izin dengan sopan untuk meninggalkan rapat lebih awal:\n<code>Excuse me, I have another appointment and must leave early.</code>\n<i>(Artinya: Permisi, saya ada janji lain dan harus pamit lebih awal.)</i>",
        "expected": [
            "excuse me, i have another appointment and must leave early",
            "i have another appointment and must leave early",
            "excuse me i must leave early"
        ],
        "primary_answer": "Excuse me, I have another appointment and must leave early."
    },
    {
        "id": "conv_int_64",
        "badge": "💬 Memilih Baju Terbaik (Choosing Best Shirt)",
        "prompt": "<b>👔 Situasi:</b> Kamu mencoba dua kemeja berbeda untuk pentas seni sekolah.\n\n👉 <b>Giliranmu:</b> Tanyakan pada sahabatmu baju mana yang terlihat lebih bagus:\n<code>Which shirt do you think looks better on me?</code>\n<i>(Artinya: Baju mana yang menurutmu terlihat lebih bagus untukku?)</i>",
        "expected": [
            "which shirt do you think looks better on me",
            "which shirt do you think looks better on me?",
            "which shirt looks better on me"
        ],
        "primary_answer": "Which shirt do you think looks better on me?"
    },
    {
        "id": "conv_int_65",
        "badge": "💬 Kelas Bersih dan Nyaman (Clean and Comfortable Class)",
        "prompt": "<b>✨ Situasi:</b> Setelah regu piket bekerja keras menyapu dan mengepel kelas.\n\n👉 <b>Giliranmu:</b> Puji bahwa kelas hari ini terasa sangat bersih dan nyaman:\n<code>Our classroom is very clean and comfortable today.</code>\n<i>(Artinya: Ruang kelas kita sangat bersih dan nyaman hari ini.)</i>",
        "expected": [
            "our classroom is very clean and comfortable today",
            "classroom is very clean and comfortable today",
            "clean and comfortable today"
        ],
        "primary_answer": "Our classroom is very clean and comfortable today."
    },
    {
        "id": "conv_int_66",
        "badge": "💬 Membaca Majalah Dinding (School Wall Magazine)",
        "prompt": "<b>📰 Situasi:</b> Ada artikel dan puisi baru yang ditempel di majalah dinding sekolah.\n\n👉 <b>Giliranmu:</b> Tanyakan pada teman apakah sudah membaca cerita baru di mading:\n<code>Have you read the new story on the wall magazine?</code>\n<i>(Artinya: Apakah kamu sudah membaca cerita baru di majalah dinding?)</i>",
        "expected": [
            "have you read the new story on the wall magazine",
            "have you read the new story on the wall magazine?",
            "read the new story on the wall magazine"
        ],
        "primary_answer": "Have you read the new story on the wall magazine?"
    },
    {
        "id": "conv_int_67",
        "badge": "💬 Berpamitan Libur Semester (Semester Holiday Farewell)",
        "prompt": "<b>🏖️ Situasi:</b> Bel terakhir semester berbunyi, siswa bersiap libur dua pekan.\n\n👉 <b>Giliranmu:</b> Ucapkan selamat liburan dan sampai jumpa semester depan:\n<code>Enjoy your school holiday, see you next semester!</code>\n<i>(Artinya: Selamat menikmati libur sekolah, sampai jumpa semester depan!)</i>",
        "expected": [
            "enjoy your school holiday, see you next semester",
            "enjoy your school holiday, see you next semester!",
            "enjoy your holiday see you next semester"
        ],
        "primary_answer": "Enjoy your school holiday, see you next semester!"
    }
],
    config.LEVEL_ADVANCED: [
    {
        "id": "conv_adv_01",
        "badge": "💬 Cita-cita Mulia (Dream Career)",
        "prompt": "<b>🩺 Situasi:</b> Guru meminta murid menceritakan cita-cita di masa depan.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kamu ingin menjadi dokter untuk menolong orang sakit di desa:\n<code>I want to be a doctor to help sick people in my village.</code>\n<i>(Artinya: Saya ingin menjadi dokter untuk menolong orang sakit di desaku.)</i>",
        "expected": [
            "i want to be a doctor to help sick people in my village",
            "i want to be a doctor to help sick people",
            "i want to be a doctor",
            "doctor to help sick people"
        ],
        "primary_answer": "I want to be a doctor to help sick people in my village."
    },
    {
        "id": "conv_adv_02",
        "badge": "💬 Menjaga Lingkungan (Protecting Environment)",
        "prompt": "<b>🌱 Situasi:</b> Kamu sedang berdiskusi tentang cara menjaga kebersihan bumi.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kita harus menanam pohon dan membuang sampah pada tempatnya:\n<code>We should plant more trees and keep our surroundings clean.</code>\n<i>(Artinya: Kita harus menanam lebih banyak pohon dan menjaga lingkungan tetap bersih.)</i>",
        "expected": [
            "we should plant more trees and keep our surroundings clean",
            "we should plant more trees",
            "plant trees and keep clean",
            "plant more trees"
        ],
        "primary_answer": "We should plant more trees and keep our surroundings clean."
    },
    {
        "id": "conv_adv_03",
        "badge": "💬 Menceritakan Liburan Desa (Describing Vacation)",
        "prompt": "<b>🌾 Situasi:</b> Temanmu bertanya bagaimana liburan sekolahmu kemarin.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa kamu mengunjungi kakekmu dan memberi makan kambing di desa:\n<code>Last holiday, I visited my grandfather and fed his goats in the village.</code>\n<i>(Artinya: Liburan lalu, saya mengunjungi kakek dan memberi makan kambing-kambingnya di desa.)</i>",
        "expected": [
            "last holiday, i visited my grandfather and fed his goats in the village",
            "last holiday i visited my grandfather and fed his goats",
            "visited my grandfather and fed his goats",
            "visited my grandfather"
        ],
        "primary_answer": "Last holiday, I visited my grandfather and fed his goats in the village."
    },
    {
        "id": "conv_adv_04",
        "badge": "💬 Merekomendasikan Buku Cerita (Book Recommendation)",
        "prompt": "<b>📚 Situasi:</b> Kamu baru saja selesai membaca cerita fabel yang penuh pesan moral.\n\n👉 <b>Giliranmu:</b> Rekomendasikan buku tersebut kepada temanmu:\n<code>You should read this fable because it teaches us about honesty.</code>\n<i>(Artinya: Kamu harus membaca fabel ini karena ia mengajarkan kita tentang kejujuran.)</i>",
        "expected": [
            "you should read this fable because it teaches us about honesty",
            "you should read this fable",
            "teaches us about honesty",
            "read this fable"
        ],
        "primary_answer": "You should read this fable because it teaches us about honesty."
    },
    {
        "id": "conv_adv_05",
        "badge": "💬 Menasihati Teman yang Sakit (Giving Healthy Advice)",
        "prompt": "<b>💊 Situasi:</b> Teman sebangkumu tampak pucat dan mengeluh pusing setelah upacara.\n\n👉 <b>Giliranmu:</b> Beri saran agar ia minum air putih dan istirahat di ruang UKS:\n<code>You should drink plenty of water and rest in the clinic room.</code>\n<i>(Artinya: Kamu sebaiknya minum banyak air dan beristirahat di ruang UKS.)</i>",
        "expected": [
            "you should drink plenty of water and rest in the clinic room",
            "you should drink plenty of water and rest",
            "drink plenty of water and rest",
            "drink water and rest"
        ],
        "primary_answer": "You should drink plenty of water and rest in the clinic room."
    },
    {
        "id": "conv_adv_06",
        "badge": "💬 Berbakti Kepada Orang Tua (Gratitude to Parents)",
        "prompt": "<b>❤️ Situasi:</b> Guru meminta murid menuliskan ungkapan rasa syukur terhadap orang tua.\n\n👉 <b>Giliranmu:</b> Tuliskan bahwa kamu bersyukur atas kasih sayang tulus orang tuamu:\n<code>I am truly grateful for my parents' unconditional love and care.</code>\n<i>(Artinya: Saya sungguh bersyukur atas kasih sayang dan perhatian tulus kedua orang tua saya.)</i>",
        "expected": [
            "i am truly grateful for my parents' unconditional love and care",
            "i am truly grateful for my parents",
            "grateful for my parents' love",
            "grateful for my parents"
        ],
        "primary_answer": "I am truly grateful for my parents' unconditional love and care."
    },
    {
        "id": "conv_adv_07",
        "badge": "💬 Kuliner Khas Nusantara (Indonesian Traditional Food)",
        "prompt": "<b>🍛 Situasi:</b> Teman bertukar cerita tentang masakan daerah favorit di Indonesia.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa Rendang adalah makanan daging lezat kaya rempah dari Sumatera Barat:\n<code>Rendang is a delicious spicy beef dish from West Sumatra.</code>\n<i>(Artinya: Rendang adalah masakan daging sapi pedas yang lezat dari Sumatera Barat.)</i>",
        "expected": [
            "rendang is a delicious spicy beef dish from west sumatra",
            "rendang is a delicious spicy beef dish",
            "rendang is delicious spicy beef",
            "delicious spicy beef dish"
        ],
        "primary_answer": "Rendang is a delicious spicy beef dish from West Sumatra."
    },
    {
        "id": "conv_adv_08",
        "badge": "💬 Pentingnya Belajar Bahasa Inggris (Why Learn English)",
        "prompt": "<b>🌏 Situasi:</b> Dalam diskusi kelas, kamu ditanya mengapa kita perlu belajar bahasa Inggris.\n\n👉 <b>Giliranmu:</b> Jelaskan bahwa bahasa Inggris membuka wawasan dan jendela ke dunia luar:\n<code>Learning English opens doors to knowledge and global friendships.</code>\n<i>(Artinya: Belajar bahasa Inggris membuka pintu pengetahuan dan persahabatan global.)</i>",
        "expected": [
            "learning english opens doors to knowledge and global friendships",
            "learning english opens doors to knowledge",
            "learning english opens doors",
            "opens doors to knowledge"
        ],
        "primary_answer": "Learning English opens doors to knowledge and global friendships."
    },
    {
        "id": "conv_adv_09",
        "badge": "💬 Pola Hidup Sehat (Healthy Lifestyle Habits)",
        "prompt": "<b>🍎 Situasi:</b> Kamu diminta membagikan tips agar tubuh tetap bugar dan berenergi di sekolah.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa makan sayuran dan tidur 8 jam membuat tubuh bugar:\n<code>Eating fresh vegetables and sleeping eight hours keep our body strong.</code>\n<i>(Artinya: Makan sayuran segar dan tidur delapan jam menjaga tubuh kita tetap kuat.)</i>",
        "expected": [
            "eating fresh vegetables and sleeping eight hours keep our body strong",
            "eating vegetables and sleeping eight hours",
            "vegetables and sleeping eight hours",
            "keep our body strong"
        ],
        "primary_answer": "Eating fresh vegetables and sleeping eight hours keep our body strong."
    },
    {
        "id": "conv_adv_10",
        "badge": "💬 Jangan Takut Membuat Kesalahan (Overcoming Mistakes)",
        "prompt": "<b>💡 Situasi:</b> Temanmu merasa malu karena salah menjawab soal di papan tulis.\n\n👉 <b>Giliranmu:</b> Hibur kawanmu bahwa membuat kesalahan adalah bagian alami dari proses belajar:\n<code>Making mistakes is a normal step in learning something new.</code>\n<i>(Artinya: Membuat kesalahan adalah langkah wajar dalam mempelajari hal baru.)</i>",
        "expected": [
            "making mistakes is a normal step in learning something new",
            "making mistakes is a normal step in learning",
            "making mistakes is a normal step",
            "mistakes is a normal step"
        ],
        "primary_answer": "Making mistakes is a normal step in learning something new."
    },
    {
        "id": "conv_adv_11",
        "badge": "💬 Manfaat Komputer & Belajar (Technology in Education)",
        "prompt": "<b>💻 Situasi:</b> Kamu sedang belajar di laboratorium komputer sekolah.\n\n👉 <b>Giliranmu:</b> Katakan bahwa komputer membantu siswa mencari ilmu dengan cepat:\n<code>Computers help students explore useful knowledge very quickly.</code>\n<i>(Artinya: Komputer membantu para siswa menjelajahi ilmu bermanfaat dengan sangat cepat.)</i>",
        "expected": [
            "computers help students explore useful knowledge very quickly",
            "computers help students explore useful knowledge",
            "help students explore useful knowledge",
            "computers help students"
        ],
        "primary_answer": "Computers help students explore useful knowledge very quickly."
    },
    {
        "id": "conv_adv_12",
        "badge": "💬 Gotong Royong Warga (Community Cooperation)",
        "prompt": "<b>🤝 Situasi:</b> Warga desamu mengadakan kerja bakti membersihkan selokan di hari Minggu.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa gotong royong membuat lingkungan bersih dan rukun:\n<code>Cooperation makes our neighborhood clean, safe, and peaceful.</code>\n<i>(Artinya: Gotong royong membuat lingkungan kita bersih, aman, dan damai.)</i>",
        "expected": [
            "cooperation makes our neighborhood clean, safe, and peaceful",
            "cooperation makes our neighborhood clean",
            "clean safe and peaceful",
            "neighborhood clean"
        ],
        "primary_answer": "Cooperation makes our neighborhood clean, safe, and peaceful."
    },
    {
        "id": "conv_adv_13",
        "badge": "💬 Rencana Jenjang Sekolah (Entering Junior High)",
        "prompt": "<b>🎓 Situasi:</b> Guru bertanya apa rencanamu setelah lulus dari Sekolah Dasar (SD).\n\n👉 <b>Giliranmu:</b> Sampaikan tekadmu untuk melanjutkan ke SMP dengan giat belajar:\n<code>After graduating from primary school, I will enter junior high school.</code>\n<i>(Artinya: Setelah lulus dari sekolah dasar, saya akan masuk sekolah menengah pertama.)</i>",
        "expected": [
            "after graduating from primary school, i will enter junior high school",
            "after graduating from primary school i will enter junior high school",
            "enter junior high school",
            "junior high school"
        ],
        "primary_answer": "After graduating from primary school, I will enter junior high school."
    },
    {
        "id": "conv_adv_14",
        "badge": "💬 Hari Kemerdekaan Indonesia (Independence Day)",
        "prompt": "<b>🇮🇩 Situasi:</b> Kamu menceritakan kemeriahan lomba 17 Agustus di kampungmu.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa Indonesia merayakan kemerdekaan setiap tanggal 17 Agustus:\n<code>We celebrate Indonesian Independence Day on the seventeenth of August.</code>\n<i>(Artinya: Kita merayakan Hari Kemerdekaan Indonesia pada tanggal 17 Agustus.)</i>",
        "expected": [
            "we celebrate indonesian independence day on the seventeenth of august",
            "we celebrate indonesian independence day",
            "independence day on the seventeenth of august",
            "seventeenth of august"
        ],
        "primary_answer": "We celebrate Indonesian Independence Day on the seventeenth of August."
    },
    {
        "id": "conv_adv_15",
        "badge": "💬 Rasa Hormat Kepada Guru (Respect for Teachers)",
        "prompt": "<b>💐 Situasi:</b> Pada peringatan Hari Guru, kamu ingin menyampaikan rasa hormatmu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa bapak dan ibu guru membimbing kita dengan sabar:\n<code>Our teachers guide us with boundless patience and wisdom.</code>\n<i>(Artinya: Guru-guru kita membimbing kita dengan kesabaran dan kebijaksanaan tanpa batas.)</i>",
        "expected": [
            "our teachers guide us with boundless patience and wisdom",
            "our teachers guide us with patience and wisdom",
            "teachers guide us with patience",
            "patience and wisdom"
        ],
        "primary_answer": "Our teachers guide us with boundless patience and wisdom."
    },
    {
        "id": "conv_adv_16",
        "badge": "💬 Menghibur Teman Sedih (Showing Empathy)",
        "prompt": "<b>🤗 Situasi:</b> Temanmu tampak bersedih karena kehilangan buku catatan kesayangannya.\n\n👉 <b>Giliranmu:</b> Berikan dukungan hangat bahwa kamu siap membantunya mencari:\n<code>Don't be sad, I will help you look for your notebook.</code>\n<i>(Artinya: Jangan sedih ya, saya akan membantumu mencari buku catatanmu.)</i>",
        "expected": [
            "don't be sad, i will help you look for your notebook",
            "don't be sad i will help you look for your notebook",
            "dont be sad i will help you",
            "i will help you look for your notebook"
        ],
        "primary_answer": "Don't be sad, I will help you look for your notebook."
    },
    {
        "id": "conv_adv_17",
        "badge": "💬 Kekuatan Kerja Kelompok (Power of Teamwork)",
        "prompt": "<b>🧩 Situasi:</b> Kelompok belajarmu baru saja berhasil menyelesaikan tugas poster besar.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kerja sama membuat tugas yang sulit menjadi ringan:\n<code>Teamwork makes difficult challenges feel much easier and lighter.</code>\n<i>(Artinya: Kerja sama tim membuat tantangan sulit terasa jauh lebih mudah dan ringan.)</i>",
        "expected": [
            "teamwork makes difficult challenges feel much easier and lighter",
            "teamwork makes difficult challenges feel easier",
            "teamwork makes difficult challenges easier",
            "teamwork makes challenges easier"
        ],
        "primary_answer": "Teamwork makes difficult challenges feel much easier and lighter."
    },
    {
        "id": "conv_adv_18",
        "badge": "💬 Keindahan Alam Pedesaan (Beauty of Nature)",
        "prompt": "<b>🌄 Situasi:</b> Kamu berdiri di atas bukit desa memandangi matahari terbit di sawah.\n\n👉 <b>Giliranmu:</b> Ungkapkan kekagumanmu pada keindahan alam ciptaan Tuhan:\n<code>The golden sunrise over the green rice fields is breathtaking.</code>\n<i>(Artinya: Matahari terbit keemasan di atas persawahan hijau sungguh menakjubkan.)</i>",
        "expected": [
            "the golden sunrise over the green rice fields is breathtaking",
            "the golden sunrise over the green rice fields",
            "golden sunrise over the green rice fields",
            "sunrise over green rice fields"
        ],
        "primary_answer": "The golden sunrise over the green rice fields is breathtaking."
    },
    {
        "id": "conv_adv_19",
        "badge": "💬 Kebiasaan Menabung (Saving Pocket Money)",
        "prompt": "<b>💰 Situasi:</b> Kamu memiliki celengan ayam di kamar untuk menyisihkan uang saku.\n\n👉 <b>Giliranmu:</b> Ceritakan bahwa kamu menyisihkan uang saku setiap hari:\n<code>I save some of my pocket money in my piggy bank every day.</code>\n<i>(Artinya: Saya menyisihkan sebagian uang saku di celengan setiap hari.)</i>",
        "expected": [
            "i save some of my pocket money in my piggy bank every day",
            "i save some of my pocket money in my piggy bank",
            "save pocket money in piggy bank",
            "save some pocket money"
        ],
        "primary_answer": "I save some of my pocket money in my piggy bank every day."
    },
    {
        "id": "conv_adv_20",
        "badge": "💬 Tokoh Pendidikan Indonesia (Ki Hajar Dewantara)",
        "prompt": "<b>🏫 Situasi:</b> Di kelas sejarah, guru membahas pahlawan nasional bidang pendidikan.\n\n👉 <b>Giliranmu:</b> Sebutkan bahwa Ki Hajar Dewantara adalah bapak pendidikan kita:\n<code>Ki Hajar Dewantara is the revered father of education in Indonesia.</code>\n<i>(Artinya: Ki Hajar Dewantara adalah bapak pendidikan yang dihormati di Indonesia.)</i>",
        "expected": [
            "ki hajar dewantara is the revered father of education in indonesia",
            "ki hajar dewantara is the father of education in indonesia",
            "father of education in indonesia",
            "ki hajar dewantara"
        ],
        "primary_answer": "Ki Hajar Dewantara is the revered father of education in Indonesia."
    },
    {
        "id": "conv_adv_21",
        "badge": "💬 Disiplin Waktu Belajar (Time Management)",
        "prompt": "<b>⏰ Situasi:</b> Temanmu kagum karena kamu selalu mengumpulkan PR tepat waktu.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kamu selalu menyelesaikan PR sebelum bermain:\n<code>I always finish all my school homework before playing games.</code>\n<i>(Artinya: Saya selalu menyelesaikan semua PR sekolah sebelum bermain game.)</i>",
        "expected": [
            "i always finish all my school homework before playing games",
            "i always finish my homework before playing games",
            "finish homework before playing games",
            "finish all homework before playing"
        ],
        "primary_answer": "I always finish all my school homework before playing games."
    },
    {
        "id": "conv_adv_22",
        "badge": "💬 Kesantunan di Tempat Umum (Public Manners)",
        "prompt": "<b>🚌 Situasi:</b> Kamu antre bersama teman saat hendak menaiki bus sekolah.\n\n👉 <b>Giliranmu:</b> Ingatkan teman agar selalu tertib mengantre dengan sabar:\n<code>Always queue patiently and speak politely in public places.</code>\n<i>(Artinya: Selalulah mengantre dengan sabar dan berbicara sopan di tempat umum.)</i>",
        "expected": [
            "always queue patiently and speak politely in public places",
            "queue patiently and speak politely in public places",
            "queue patiently and speak politely",
            "speak politely in public places"
        ],
        "primary_answer": "Always queue patiently and speak politely in public places."
    },
    {
        "id": "conv_adv_23",
        "badge": "💬 Mengembangkan Bakat Seni (Expressing Creativity)",
        "prompt": "<b>🎨 Situasi:</b> Kamu gemar melukis dan menulis cerita di buku harianmu.\n\n👉 <b>Giliranmu:</b> Katakan bahwa melukis dan menulis membantumu menuangkan ide:\n<code>Painting and writing help me express my imagination freely.</code>\n<i>(Artinya: Melukis dan menulis membantuku mengekspresikan imajinasi dengan bebas.)</i>",
        "expected": [
            "painting and writing help me express my imagination freely",
            "painting and writing help me express my imagination",
            "express my imagination freely",
            "express imagination"
        ],
        "primary_answer": "Painting and writing help me express my imagination freely."
    },
    {
        "id": "conv_adv_24",
        "badge": "💬 Motivasi Terus Belajar (Lifelong Learning)",
        "prompt": "<b>🌟 Situasi:</b> Kamu membagikan kata mutiara motivasi di papan majalah dinding kelas.\n\n👉 <b>Giliranmu:</b> Tuliskan semboyan bahwa kita tidak boleh berhenti belajar:\n<code>Never stop learning because life never stops teaching us.</code>\n<i>(Artinya: Jangan pernah berhenti belajar karena hidup tidak pernah berhenti mengajar kita.)</i>",
        "expected": [
            "never stop learning because life never stops teaching us",
            "never stop learning because life never stops teaching",
            "never stop learning",
            "life never stops teaching us"
        ],
        "primary_answer": "Never stop learning because life never stops teaching us."
    },
    {
        "id": "conv_adv_25",
        "badge": "💬 Verifikasi Berita Medsos (Fact-Checking News)",
        "prompt": "<b>📱 Situasi:</b> Dalam diskusi literasi digital, kamu mengingatkan bahaya hoaks di media sosial.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kita harus memverifikasi berita sebelum membagikannya:\n<code>We should verify news before sharing it online.</code>\n<i>(Artinya: Kita harus memverifikasi berita sebelum membagikannya di internet.)</i>",
        "expected": [
            "we should verify news before sharing it online",
            "verify news before sharing it online",
            "we must verify news before sharing it online"
        ],
        "primary_answer": "We should verify news before sharing it online."
    },
    {
        "id": "conv_adv_26",
        "badge": "💬 Melestarikan Seni Tari Tradisional (Traditional Dance Heritage)",
        "prompt": "<b>💃 Situasi:</b> Kamu berbicara tentang pentingnya mempelajari tarian daerah nusantara.\n\n👉 <b>Giliranmu:</b> Katakan bahwa melestarikan tari tradisional menjaga identitas budaya kita:\n<code>Preserving traditional dances keeps our cultural identity alive.</code>\n<i>(Artinya: Melestarikan tarian tradisional menjaga identitas budaya kita tetap hidup.)</i>",
        "expected": [
            "preserving traditional dances keeps our cultural identity alive",
            "preserving traditional dances keeps cultural identity alive",
            "keeps our cultural identity alive"
        ],
        "primary_answer": "Preserving traditional dances keeps our cultural identity alive."
    },
    {
        "id": "conv_adv_27",
        "badge": "💬 Kebiasaan Membaca Harian (Daily Reading Habit)",
        "prompt": "<b>📚 Situasi:</b> Dalam seminar literasi sekolah, kamu membagikan tips meningkatkan nalar kritis.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa membaca harian memperkaya kosakata dan melatih nalar kritis:\n<code>Reading daily expands vocabulary and enhances critical thinking.</code>\n<i>(Artinya: Membaca setiap hari memperluas kosakata dan meningkatkan kemampuan berpikir kritis.)</i>",
        "expected": [
            "reading daily expands vocabulary and enhances critical thinking",
            "reading daily expands vocabulary and improves critical thinking",
            "expands vocabulary and enhances critical thinking"
        ],
        "primary_answer": "Reading daily expands vocabulary and enhances critical thinking."
    },
    {
        "id": "conv_adv_28",
        "badge": "💬 Transisi Energi Bersih (Clean Energy Transition)",
        "prompt": "<b>⚡ Situasi:</b> Dalam debat ilmiah, kamu menyoroti solusi perubahan iklim global.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa beralih ke energi bersih menekan emisi karbon dunia:\n<code>Transitioning to clean energy reduces global carbon emissions.</code>\n<i>(Artinya: Beralih ke energi bersih mengurangi emisi karbon global.)</i>",
        "expected": [
            "transitioning to clean energy reduces global carbon emissions",
            "transitioning to clean energy reduces carbon emissions",
            "clean energy reduces global carbon emissions"
        ],
        "primary_answer": "Transitioning to clean energy reduces global carbon emissions."
    },
    {
        "id": "conv_adv_29",
        "badge": "💬 Mengatasi Kecemasan Ujian (Managing Exam Anxiety)",
        "prompt": "<b>🧠 Situasi:</b> Temanmu merasa gugup berlebihan menjelang ujian kelulusan.\n\n👉 <b>Giliranmu:</b> Beri saran bahwa latihan pernapasan dan tidur cukup meredakan cemas:\n<code>Practicing deep breathing and good sleep helps reduce exam anxiety.</code>\n<i>(Artinya: Latihan pernapasan dalam dan tidur cukup membantu mengurangi kecemasan ujian.)</i>",
        "expected": [
            "practicing deep breathing and good sleep helps reduce exam anxiety",
            "deep breathing and good sleep helps reduce exam anxiety",
            "helps reduce exam anxiety"
        ],
        "primary_answer": "Practicing deep breathing and good sleep helps reduce exam anxiety."
    },
    {
        "id": "conv_adv_30",
        "badge": "💬 Kejujuran Akademik (Academic Integrity)",
        "prompt": "<b>⚖️ Situasi:</b> Kamu menekankan prinsip kejujuran saat mengerjakan ujian mandiri.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kejujuran akademik lebih berharga daripada nilai tinggi dari mencontek:\n<code>Academic integrity is more valuable than achieving high scores dishonestly.</code>\n<i>(Artinya: Integritas akademik lebih berharga daripada meraih nilai tinggi secara tidak jujur.)</i>",
        "expected": [
            "academic integrity is more valuable than achieving high scores dishonestly",
            "academic integrity is more valuable than high scores dishonestly",
            "integrity is more valuable than high scores dishonestly"
        ],
        "primary_answer": "Academic integrity is more valuable than achieving high scores dishonestly."
    },
    {
        "id": "conv_adv_31",
        "badge": "💬 Bahaya Sampah Plastik di Sungai (Plastic in Rivers)",
        "prompt": "<b>🌊 Situasi:</b> Saat aksi bersih sungai desa, kamu mengedukasi warga tentang bahaya limbah plastik.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa sampah plastik di sungai membahayakan ekosistem dan kesehatan:\n<code>Plastic waste in rivers endangers aquatic ecosystems and human health.</code>\n<i>(Artinya: Sampah plastik di sungai membahayakan ekosistem air dan kesehatan manusia.)</i>",
        "expected": [
            "plastic waste in rivers endangers aquatic ecosystems and human health",
            "plastic waste in rivers endangers aquatic ecosystems",
            "endangers aquatic ecosystems and human health"
        ],
        "primary_answer": "Plastic waste in rivers endangers aquatic ecosystems and human health."
    },
    {
        "id": "conv_adv_32",
        "badge": "💬 Kepemimpinan Pemuda Desa (Youth Leadership)",
        "prompt": "<b>🌟 Situasi:</b> Dalam forum karang taruna, kamu memotivasi generasi muda desa.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa pemimpin muda memiliki daya untuk membawa perubahan positif:\n<code>Young leaders have the power to create positive change in communities.</code>\n<i>(Artinya: Pemimpin muda memiliki kekuatan untuk menciptakan perubahan positif di masyarakat.)</i>",
        "expected": [
            "young leaders have the power to create positive change in communities",
            "young leaders have the power to create positive change",
            "power to create positive change in communities"
        ],
        "primary_answer": "Young leaders have the power to create positive change in communities."
    },
    {
        "id": "conv_adv_33",
        "badge": "💬 Menghargai Keberagaman Tradisi (Respecting Cultural Diversity)",
        "prompt": "<b>🇮🇩 Situasi:</b> Pada peringatan Hari Sumpah Pemuda, kamu berbicara tentang persatuan bangsa.\n\n👉 <b>Giliranmu:</b> Katakan bahwa menghargai keberagaman tradisi memupuk kerukunan masyarakat multikultural:\n<code>Respecting diverse traditions fosters harmony in a multicultural society.</code>\n<i>(Artinya: Menghormati tradisi yang beragam menumbuhkan keharmonisan dalam masyarakat multikultural.)</i>",
        "expected": [
            "respecting diverse traditions fosters harmony in a multicultural society",
            "respecting diverse traditions fosters harmony",
            "fosters harmony in a multicultural society"
        ],
        "primary_answer": "Respecting diverse traditions fosters harmony in a multicultural society."
    },
    {
        "id": "conv_adv_34",
        "badge": "💬 Menumbuhkan Rasa Ingin Tahu (Cultivating Curiosity)",
        "prompt": "<b>🎨 Situasi:</b> Dalam lokakarya pendidikan anak, kamu membahas cara mendorong kreativitas siswa.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa merangsang rasa ingin tahu anak mendorong inovasi artistik:\n<code>Encouraging children to express curiosity stimulates artistic innovation.</code>\n<i>(Artinya: Mendorong anak-anak mengekspresikan rasa ingin tahu merangsang inovasi artistik.)</i>",
        "expected": [
            "encouraging children to express curiosity stimulates artistic innovation",
            "encouraging children to express curiosity",
            "stimulates artistic innovation"
        ],
        "primary_answer": "Encouraging children to express curiosity stimulates artistic innovation."
    },
    {
        "id": "conv_adv_35",
        "badge": "💬 Pola Makan Seimbang dan Imunitas (Balanced Diet and Immunity)",
        "prompt": "<b>🥗 Situasi:</b> Kamu memberikan penyuluhan kesehatan tentang pentingnya gizi seimbang.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa makanan kaya serat dan vitamin memperkuat daya tahan tubuh:\n<code>A balanced diet rich in fibers and vitamins boosts our immune system.</code>\n<i>(Artinya: Pola makan seimbang yang kaya serat dan vitamin memperkuat sistem kekebalan tubuh kita.)</i>",
        "expected": [
            "a balanced diet rich in fibers and vitamins boosts our immune system",
            "balanced diet rich in fibers and vitamins boosts our immune system",
            "boosts our immune system"
        ],
        "primary_answer": "A balanced diet rich in fibers and vitamins boosts our immune system."
    },
    {
        "id": "conv_adv_36",
        "badge": "💬 Waspada Kecanduan Gadget (Avoiding Digital Addiction)",
        "prompt": "<b>📱 Situasi:</b> Teman-temanmu sering menghabiskan berjam-jam menatap layar ponsel tanpa henti.\n\n👉 <b>Giliranmu:</b> Ingatkan bahwa meski ponsel berguna, kita harus waspada kecanduan digital:\n<code>Smartphones connect us instantly but we must avoid digital addiction.</code>\n<i>(Artinya: Ponsel pintar menghubungkan kita seketika namun kita harus menghindari kecanduan digital.)</i>",
        "expected": [
            "smartphones connect us instantly but we must avoid digital addiction",
            "we must avoid digital addiction",
            "smartphones connect us instantly"
        ],
        "primary_answer": "Smartphones connect us instantly but we must avoid digital addiction."
    },
    {
        "id": "conv_adv_37",
        "badge": "💬 Menghormati Jasa Para Pahlawan (Honoring National Heroes)",
        "prompt": "<b>🎖️ Situasi:</b> Menjelang Hari Pahlawan 10 November, kamu membacakan pidato reflektif.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kita menghormati keberanian pahlawan yang memperjuangkan kemerdekaan:\n<code>We honor the courage of heroes who fought for our freedom.</code>\n<i>(Artinya: Kita menghormati keberanian para pahlawan yang berjuang demi kemerdekaan kita.)</i>",
        "expected": [
            "we honor the courage of heroes who fought for our freedom",
            "honor the courage of heroes who fought for our freedom",
            "heroes who fought for our freedom"
        ],
        "primary_answer": "We honor the courage of heroes who fought for our freedom."
    },
    {
        "id": "conv_adv_38",
        "badge": "💬 Gotong Royong Pererat Solidaritas (Community Service and Solidarity)",
        "prompt": "<b>🤝 Situasi:</b> Saat musyawarah desa, kamu mengajak warga giat kerja bakti.\n\n👉 <b>Giliranmu:</b> Katakan bahwa partisipasi aktif dalam kerja bakti mempererat kerukunan sosial:\n<code>Active participation in community service strengthens social cohesion.</code>\n<i>(Artinya: Partisipasi aktif dalam pelayanan masyarakat memperkuat keterikatan sosial.)</i>",
        "expected": [
            "active participation in community service strengthens social cohesion",
            "participation in community service strengthens social cohesion",
            "strengthens social cohesion"
        ],
        "primary_answer": "Active participation in community service strengthens social cohesion."
    },
    {
        "id": "conv_adv_39",
        "badge": "💬 Menabung untuk Kemandirian Finansial (Early Saving Habits)",
        "prompt": "<b>💰 Situasi:</b> Guru ekonomi bertanya apa kunci mengelola keuangan sejak muda.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa membiasakan menabung sejak dini menjamin stabilitas finansial:\n<code>Developing saving habits at an early age ensures financial stability.</code>\n<i>(Artinya: Membangun kebiasaan menabung sejak dini menjamin stabilitas keuangan.)</i>",
        "expected": [
            "developing saving habits at an early age ensures financial stability",
            "saving habits at an early age ensures financial stability",
            "ensures financial stability"
        ],
        "primary_answer": "Developing saving habits at an early age ensures financial stability."
    },
    {
        "id": "conv_adv_40",
        "badge": "💬 Rendah Hati dan Haus Ilmu (Humility and Lifelong Learning)",
        "prompt": "<b>🌱 Situasi:</b> Kamu membagikan nasihat bijak di catatan jurnal kepemimpinan.\n\n👉 <b>Giliranmu:</b> Tuliskan bahwa sikap rendah hati dan kemauan terus belajar adalah tanda kebijaksanaan sejati:\n<code>Humility and continuous learning are marks of true wisdom.</code>\n<i>(Artinya: Kerendahan hati dan terus belajar adalah tanda-tanda kebijaksanaan sejati.)</i>",
        "expected": [
            "humility and continuous learning are marks of true wisdom",
            "humility and learning are marks of true wisdom",
            "marks of true wisdom"
        ],
        "primary_answer": "Humility and continuous learning are marks of true wisdom."
    },
    {
        "id": "conv_adv_41",
        "badge": "💬 Mengubah Kegagalan Jadi Pembelajaran (Resilience Through Setbacks)",
        "prompt": "<b>🧗 Situasi:</b> Rekan setimmu kecewa berat karena kalah dalam lomba debat.\n\n👉 <b>Giliranmu:</b> Kuatkan hatinya bahwa ketangguhan mengubah kegagalan menjadi batu loncatan berharga:\n<code>Resilience turns difficult setbacks into valuable stepping stones.</code>\n<i>(Artinya: Ketangguhan mental mengubah kegagalan berat menjadi batu loncatan berharga.)</i>",
        "expected": [
            "resilience turns difficult setbacks into valuable stepping stones",
            "resilience turns setbacks into valuable stepping stones",
            "valuable stepping stones"
        ],
        "primary_answer": "Resilience turns difficult setbacks into valuable stepping stones."
    },
    {
        "id": "conv_adv_42",
        "badge": "💬 Hak Akses Air Bersih (Universal Access to Clean Water)",
        "prompt": "<b>💧 Situasi:</b> Kamu memaparkan esai tentang kelestarian sumber mata air pegunungan.\n\n👉 <b>Giliranmu:</b> Tegaskan bahwa akses terhadap air minum yang aman adalah hak asasi manusia:\n<code>Access to safe drinking water is a fundamental human right.</code>\n<i>(Artinya: Akses terhadap air minum yang aman adalah hak asasi manusia yang mendasar.)</i>",
        "expected": [
            "access to safe drinking water is a fundamental human right",
            "access to clean drinking water is a fundamental human right",
            "fundamental human right"
        ],
        "primary_answer": "Access to safe drinking water is a fundamental human right."
    },
    {
        "id": "conv_adv_43",
        "badge": "💬 Dampak Pemanasan Global (Global Warming Impact)",
        "prompt": "<b>🌡️ Situasi:</b> Di kelas geografi, kamu diminta merangkum dampak pemanasan bumi.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa pemanasan global memicu berbagai cuaca ekstrem di seantero dunia:\n<code>Global warming causes extreme weather phenomena around the world.</code>\n<i>(Artinya: Pemanasan global menyebabkan fenomena cuaca ekstrem di seluruh dunia.)</i>",
        "expected": [
            "global warming causes extreme weather phenomena around the world",
            "global warming causes extreme weather around the world",
            "extreme weather phenomena around the world"
        ],
        "primary_answer": "Global warming causes extreme weather phenomena around the world."
    },
    {
        "id": "conv_adv_44",
        "badge": "💬 Manfaat Menguasai Bahasa Asing (Benefits of Multilingualism)",
        "prompt": "<b>🌏 Situasi:</b> Kamu diwawancarai tentang motivasi tekun mengasah keterampilan bahasa.\n\n👉 <b>Giliranmu:</b> Katakan bahwa fasih bahasa asing membuka peluang karier secara mendunia:\n<code>Speaking foreign languages broadens career opportunities globally.</code>\n<i>(Artinya: Menguasai bahasa asing memperluas peluang karier secara global.)</i>",
        "expected": [
            "speaking foreign languages broadens career opportunities globally",
            "speaking foreign languages broadens career opportunities",
            "broadens career opportunities globally"
        ],
        "primary_answer": "Speaking foreign languages broadens career opportunities globally."
    },
    {
        "id": "conv_adv_45",
        "badge": "💬 Mendengarkan Nasihat Lansia (Listening to the Elderly)",
        "prompt": "<b>👴 Situasi:</b> Kamu berdiskusi tentang cara mempererat relasi antar-generasi di desa.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa mendengarkan para lansia dengan seksama menjembatani jarak generasi:\n<code>Listening attentively to the elderly bridges the generation gap.</code>\n<i>(Artinya: Mendengarkan para orang tua dengan seksama menjembatani perbedaan generasi.)</i>",
        "expected": [
            "listening attentively to the elderly bridges the generation gap",
            "listening to the elderly bridges the generation gap",
            "bridges the generation gap"
        ],
        "primary_answer": "Listening attentively to the elderly bridges the generation gap."
    },
    {
        "id": "conv_adv_46",
        "badge": "💬 Menjaga Keseimbangan Belajar dan Istirahat (Preventing Study Burnout)",
        "prompt": "<b>⚖️ Situasi:</b> Temanmu belajar hingga larut malam setiap hari sampai jatuh sakit.\n\n👉 <b>Giliranmu:</b> Beri saran bahwa menyeimbangkan belajar dan istirahat mencegah kelelahan mental:\n<code>Balancing study and leisure prevents mental exhaustion and burnout.</code>\n<i>(Artinya: Menyeimbangkan waktu belajar dan santai mencegah kelelahan mental dan kejenuhan.)</i>",
        "expected": [
            "balancing study and leisure prevents mental exhaustion and burnout",
            "balancing study and rest prevents mental exhaustion",
            "prevents mental exhaustion and burnout"
        ],
        "primary_answer": "Balancing study and leisure prevents mental exhaustion and burnout."
    },
    {
        "id": "conv_adv_47",
        "badge": "💬 Berdialog Konstruktif (Constructive Dialogue)",
        "prompt": "<b>🤝 Situasi:</b> Terjadi perbedaan sudut pandang sengit dalam musyawarah pemilihan ketua OSIS.\n\n👉 <b>Giliranmu:</b> Ingatkan bahwa dialog sehat menuntut kesediaan mendengar pendapat berbeda secara santun:\n<code>Constructive dialogue requires listening politely to differing views.</code>\n<i>(Artinya: Dialog konstruktif menuntut kesediaan mendengarkan pandangan yang berbeda dengan santun.)</i>",
        "expected": [
            "constructive dialogue requires listening politely to differing views",
            "dialogue requires listening politely to differing views",
            "listening politely to differing views"
        ],
        "primary_answer": "Constructive dialogue requires listening politely to differing views."
    },
    {
        "id": "conv_adv_48",
        "badge": "💬 Manfaat Ruang Terbuka Hijau (Urban Green Spaces)",
        "prompt": "<b>🌳 Situasi:</b> Kamu menulis artikel mengenai perlunya taman kota yang asri.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa taman kota menyediakan pasokan oksigen segar dan tempat rekreasi warga:\n<code>Urban parks provide fresh oxygen and recreational spaces for citizens.</code>\n<i>(Artinya: Taman kota menyediakan oksigen segar dan ruang rekreasi bagi warga.)</i>",
        "expected": [
            "urban parks provide fresh oxygen and recreational spaces for citizens",
            "parks provide fresh oxygen and recreational spaces",
            "fresh oxygen and recreational spaces for citizens"
        ],
        "primary_answer": "Urban parks provide fresh oxygen and recreational spaces for citizens."
    },
    {
        "id": "conv_adv_49",
        "badge": "💬 Peran Teladan Guru (Teacher Moral Guidance)",
        "prompt": "<b>👩‍🏫 Situasi:</b> Dalam pidato wisuda kelulusan, kamu menyampaikan apresiasi mendalam kepada guru.\n\n👉 <b>Giliranmu:</b> Katakan bahwa pendidik tidak hanya mengasah akal tetapi juga membina kompas moral siswa:\n<code>Educators shape not only intellect but also students' moral compass.</code>\n<i>(Artinya: Pendidik tidak hanya membentuk kecerdasan namun juga kompas moral para siswa.)</i>",
        "expected": [
            "educators shape not only intellect but also students' moral compass",
            "educators shape not only intellect but also moral compass",
            "shape not only intellect but also students' moral compass"
        ],
        "primary_answer": "Educators shape not only intellect but also students' moral compass."
    },
    {
        "id": "conv_adv_50",
        "badge": "💬 Mendukung Pengrajin Lokal (Supporting Local Artisans)",
        "prompt": "<b>🛍️ Situasi:</b> Di pameran UMKM desa, kamu mengajak pengunjung membeli kerajinan tangan lokal.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa membeli produk pengrajin lokal memperkuat kemandirian ekonomi desa:\n<code>Buying from local artisans strengthens our village economic independence.</code>\n<i>(Artinya: Membeli dari perajin lokal memperkuat kemandirian ekonomi desa kita.)</i>",
        "expected": [
            "buying from local artisans strengthens our village economic independence",
            "buying from local artisans strengthens village economic independence",
            "strengthens our village economic independence"
        ],
        "primary_answer": "Buying from local artisans strengthens our village economic independence."
    },
    {
        "id": "conv_adv_51",
        "badge": "💬 Olahraga Rutin Tingkatkan Fokus (Exercise and Focus)",
        "prompt": "<b>🏃 Situasi:</b> Kamu membagikan kiat konsentrasi belajar kepada rekan sekelas.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa olahraga aerobik teratur meningkatkan stamina jantung dan fokus belajar:\n<code>Regular aerobic exercise improves cardiovascular endurance and focus.</code>\n<i>(Artinya: Olahraga aerobik teratur meningkatkan daya tahan kardiovaskular dan fokus.)</i>",
        "expected": [
            "regular aerobic exercise improves cardiovascular endurance and focus",
            "regular exercise improves cardiovascular endurance and focus",
            "improves cardiovascular endurance and focus"
        ],
        "primary_answer": "Regular aerobic exercise improves cardiovascular endurance and focus."
    },
    {
        "id": "conv_adv_52",
        "badge": "💬 Menjaga Hutan Hujan Tropis (Preserving Tropical Rainforests)",
        "prompt": "<b>🌴 Situasi:</b> Kamu menyusun laporan tentang kekayaan hayati hutan nusantara.\n\n👉 <b>Giliranmu:</b> Katakan bahwa melindungi hutan hujan menyelamatkan tumbuhan berkhasiat obat yang belum terkuak:\n<code>Preserving rainforests safeguards countless undiscovered medicinal plants.</code>\n<i>(Artinya: Melestarikan hutan hujan melindungi tanaman obat berkhasiat yang tak terhitung jumlahnya.)</i>",
        "expected": [
            "preserving rainforests safeguards countless undiscovered medicinal plants",
            "preserving rainforests safeguards undiscovered medicinal plants",
            "safeguards countless undiscovered medicinal plants"
        ],
        "primary_answer": "Preserving rainforests safeguards countless undiscovered medicinal plants."
    },
    {
        "id": "conv_adv_53",
        "badge": "💬 Bertanya sebagai Awal Riset (Curious Inquiry in Science)",
        "prompt": "<b>🔬 Situasi:</b> Guru sains mengajak siswa berpikir kritis dalam praktikum laboratorium.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa mengajukan pertanyaan bermakna adalah gerbang penyelidikan ilmiah:\n<code>Asking thoughtful questions is the first step toward scientific inquiry.</code>\n<i>(Artinya: Mengajukan pertanyaan yang bermakna adalah langkah awal menuju penyelidikan ilmiah.)</i>",
        "expected": [
            "asking thoughtful questions is the first step toward scientific inquiry",
            "asking questions is the first step toward scientific inquiry",
            "first step toward scientific inquiry"
        ],
        "primary_answer": "Asking thoughtful questions is the first step toward scientific inquiry."
    },
    {
        "id": "conv_adv_54",
        "badge": "💬 Tepat Waktu Cermin Rasa Hormat (Punctuality and Respect)",
        "prompt": "<b>⏰ Situasi:</b> Kamu selalu datang lima menit lebih awal sebelum rapat dimulai.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa ketepatan waktu menunjukkan rasa saling menghargai dan dedikasi:\n<code>Punctuality demonstrates mutual respect and professional dedication.</code>\n<i>(Artinya: Ketepatan waktu menunjukkan rasa saling menghormati dan dedikasi profesional.)</i>",
        "expected": [
            "punctuality demonstrates mutual respect and professional dedication",
            "punctuality demonstrates mutual respect",
            "demonstrates mutual respect and professional dedication"
        ],
        "primary_answer": "Punctuality demonstrates mutual respect and professional dedication."
    },
    {
        "id": "conv_adv_55",
        "badge": "💬 Perlindungan Satwa Liar (Protecting Endangered Wildlife)",
        "prompt": "<b>🦏 Situasi:</b> Dalam kampanye perlindungan Badak Jawa dan Harimau Sumatera.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa hukum perlindungan satwa yang tegas mencegah perburuan liar:\n<code>Strict wildlife protection laws prevent illegal poaching and habitat loss.</code>\n<i>(Artinya: Hukum perlindungan satwa liar yang tegas mencegah perburuan liar dan hilangnya habitat.)</i>",
        "expected": [
            "strict wildlife protection laws prevent illegal poaching and habitat loss",
            "wildlife protection laws prevent illegal poaching and habitat loss",
            "prevent illegal poaching and habitat loss"
        ],
        "primary_answer": "Strict wildlife protection laws prevent illegal poaching and habitat loss."
    },
    {
        "id": "conv_adv_56",
        "badge": "💬 Kolaborasi Internasional (International Cooperation)",
        "prompt": "<b>🌐 Situasi:</b> Pada simulasi sidang PBB (Model UN), kamu mewakili delegasi pemuda.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kerja sama global mampu mengatasi tantangan besar seperti iklim:\n<code>International collaboration solves global challenges like climate change.</code>\n<i>(Artinya: Kolaborasi internasional menyelesaikan tantangan global seperti perubahan iklim.)</i>",
        "expected": [
            "international collaboration solves global challenges like climate change",
            "collaboration solves global challenges like climate change",
            "solves global challenges like climate change"
        ],
        "primary_answer": "International collaboration solves global challenges like climate change."
    },
    {
        "id": "conv_adv_57",
        "badge": "💬 Kesehatan Mental dan Raga (Mental and Physical Wellness)",
        "prompt": "<b>🧘 Situasi:</b> Dalam pekan kesadaran kesehatan siswa di sekolah.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa kesadaran kesehatan mental sama pentingnya dengan kebugaran fisik:\n<code>Mental health awareness is just as crucial as physical wellness.</code>\n<i>(Artinya: Kesadaran kesehatan mental sama pentingnya dengan kebugaran fisik.)</i>",
        "expected": [
            "mental health awareness is just as crucial as physical wellness",
            "mental health is just as crucial as physical wellness",
            "as crucial as physical wellness"
        ],
        "primary_answer": "Mental health awareness is just as crucial as physical wellness."
    },
    {
        "id": "conv_adv_58",
        "badge": "💬 Latihan Konsisten Menuju Kemahiran (Daily Practice and Mastery)",
        "prompt": "<b>🎯 Situasi:</b> Kamu menasihati adik kelas yang ingin mahir memainkan biola.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa latihan konsisten setiap hari mengubah bakat menjadi kemahiran sejati:\n<code>Consistent daily practice turns natural talent into lasting mastery.</code>\n<i>(Artinya: Latihan harian yang konsisten mengubah bakat alami menjadi kemahiran yang abadi.)</i>",
        "expected": [
            "consistent daily practice turns natural talent into lasting mastery",
            "daily practice turns natural talent into lasting mastery",
            "turns natural talent into lasting mastery"
        ],
        "primary_answer": "Consistent daily practice turns natural talent into lasting mastery."
    },
    {
        "id": "conv_adv_59",
        "badge": "💬 Mengurangi Sampah Makanan (Preventing Food Waste)",
        "prompt": "<b>🍱 Situasi:</b> Kamu mengamati banyak sisa makanan yang terbuang di kantin sekolah.\n\n👉 <b>Giliranmu:</b> Ingatkan bahwa mencegah sampah makanan membutuhkan perencanaan porsi yang bijak:\n<code>Preventing food waste requires mindful purchasing and meal planning.</code>\n<i>(Artinya: Mencegah sampah makanan membutuhkan pembelian dan perencanaan porsi makan yang bijak.)</i>",
        "expected": [
            "preventing food waste requires mindful purchasing and meal planning",
            "preventing food waste requires mindful meal planning",
            "mindful purchasing and meal planning"
        ],
        "primary_answer": "Preventing food waste requires mindful purchasing and meal planning."
    },
    {
        "id": "conv_adv_60",
        "badge": "💬 Transportasi Kereta Listrik (Electric Transit and Traffic)",
        "prompt": "<b>🚊 Situasi:</b> Kamu mengamati kemacetan kota metropolitan dan solusi transportasi massal.\n\n👉 <b>Giliranmu:</b> Katakan bahwa kereta dan bus listrik mengurai kemacetan kota secara efisien:\n<code>Electric trains and buses alleviate urban traffic congestion efficiently.</code>\n<i>(Artinya: Kereta dan bus listrik meredakan kemacetan lalu lintas perkotaan secara efisien.)</i>",
        "expected": [
            "electric trains and buses alleviate urban traffic congestion efficiently",
            "electric trains and buses reduce traffic congestion efficiently",
            "alleviate urban traffic congestion efficiently"
        ],
        "primary_answer": "Electric trains and buses alleviate urban traffic congestion efficiently."
    },
    {
        "id": "conv_adv_61",
        "badge": "💬 Kepedulian Sosial bagi Kaum Rentan (Social Caring for Vulnerable)",
        "prompt": "<b>🤲 Situasi:</b> Dalam kegiatan bakti sosial panti asuhan, kamu membagikan motivasi kepada relawan.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa menjadi warga yang baik berarti peduli pada sesama yang membutuhkan:\n<code>Citizenship means caring for vulnerable members of our society.</code>\n<i>(Artinya: Kewarganegaraan sejati berarti peduli terhadap anggota masyarakat kita yang rentan.)</i>",
        "expected": [
            "citizenship means caring for vulnerable members of our society",
            "caring for vulnerable members of our society",
            "citizenship means caring for vulnerable members"
        ],
        "primary_answer": "Citizenship means caring for vulnerable members of our society."
    },
    {
        "id": "conv_adv_62",
        "badge": "💬 Menghargai Proses Belajar (The Learning Journey)",
        "prompt": "<b>📖 Situasi:</b> Kamu merefleksikan proses belajar bahasa Inggris dari nol hingga lancar.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa proses pembelajaran seringkali lebih bermakna daripada tujuan akhir:\n<code>The learning journey is often more transformative than the destination.</code>\n<i>(Artinya: Proses perjalanan belajar seringkali lebih mengubah diri daripada sekadar tujuan akhir.)</i>",
        "expected": [
            "the learning journey is often more transformative than the destination",
            "learning journey is more transformative than the destination",
            "more transformative than the destination"
        ],
        "primary_answer": "The learning journey is often more transformative than the destination."
    },
    {
        "id": "conv_adv_63",
        "badge": "💬 Menghapus Prasangka Sosial (Dismantling Stereotypes)",
        "prompt": "<b>🕊️ Situasi:</b> Kamu berorasi dalam peringatan hari toleransi sedunia di aula sekolah.\n\n👉 <b>Giliranmu:</b> Sampaikan bahwa pendidikan meruntuhkan prasangka dan memajukan martabat manusia:\n<code>Education dismantles stereotypes and promotes universal human dignity.</code>\n<i>(Artinya: Pendidikan meruntuhkan stereotip dan memajukan martabat manusia yang universal.)</i>",
        "expected": [
            "education dismantles stereotypes and promotes universal human dignity",
            "education dismantles stereotypes and promotes human dignity",
            "dismantles stereotypes and promotes universal human dignity"
        ],
        "primary_answer": "Education dismantles stereotypes and promotes universal human dignity."
    },
    {
        "id": "conv_adv_64",
        "badge": "💬 Literasi Digital bagi Generasi Muda (Digital Literacy Safety)",
        "prompt": "<b>💻 Situasi:</b> Kamu membawakan materi pelatihan internet sehat bagi adik-adik kelas.\n\n👉 <b>Giliranmu:</b> Katakan bahwa literasi digital membekali siswa menjelajahi informasi secara aman dan bijak:\n<code>Digital literacy equips learners to navigate information safely and wisely.</code>\n<i>(Artinya: Literasi digital membekali para siswa untuk menjelajahi informasi dengan aman dan bijak.)</i>",
        "expected": [
            "digital literacy equips learners to navigate information safely and wisely",
            "digital literacy equips learners to navigate information safely",
            "navigate information safely and wisely"
        ],
        "primary_answer": "Digital literacy equips learners to navigate information safely and wisely."
    },
    {
        "id": "conv_adv_65",
        "badge": "💬 Keteguhan Menggapai Cita-cita (Perseverance in Adversity)",
        "prompt": "<b>🧗 Situasi:</b> Kamu menuliskan kalimat mutiara inspiratif di dinding ruang belajar bersama.\n\n👉 <b>Giliranmu:</b> Tuliskan bahwa ketekunan di tengah rintangan menjadi ciri orang-orang sukses:\n<code>Perseverance in the face of adversity defines great achievers.</code>\n<i>(Artinya: Ketekunan dalam menghadapi kesulitan menentukan para peraih keberhasilan besar.)</i>",
        "expected": [
            "perseverance in the face of adversity defines great achievers",
            "perseverance in the face of adversity",
            "defines great achievers"
        ],
        "primary_answer": "Perseverance in the face of adversity defines great achievers."
    },
    {
        "id": "conv_adv_66",
        "badge": "💬 Masa Depan Cerah Melalui Pendidikan (Brighter Future for Indonesia)",
        "prompt": "<b>🇮🇩 Situasi:</b> Kamu membagikan mimpi dan visimu untuk kemajuan generasi penerus bangsa.\n\n👉 <b>Giliranmu:</b> Katakan bahwa masa depan yang cerah berawal dari pendidikan berkualitas untuk semua:\n<code>A brighter future begins with accessible, high-quality education for all.</code>\n<i>(Artinya: Masa depan yang lebih cerah bermula dari pendidikan bermutu yang dapat diakses semua orang.)</i>",
        "expected": [
            "a brighter future begins with accessible, high-quality education for all",
            "a brighter future begins with accessible high-quality education for all",
            "a brighter future begins with high-quality education for all"
        ],
        "primary_answer": "A brighter future begins with accessible, high-quality education for all."
    }
],
}
