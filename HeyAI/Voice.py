import pyttsx3

# Inisialisasi mesin text-to-speech
engine = pyttsx3.init()

# Mendapatkan daftar suara yang tersedia
voices = engine.getProperty('voices')

# Menampilkan informasi tentang setiap suara yang tersedia
for voice in voices:
    print("ID Suara:", voice.id)
    print("Nama Suara:", voice.name)
    print("Bahasa Suara:", voice.languages)
    print("Gender Suara:", voice.gender)
    print("")

# Menampilkan jumlah total suara yang tersedia
print("Total Suara Tersedia:", len(voices))
