import random
import pyttsx3
from datetime import datetime
import requests

# Inisialisasi mesin text-to-speech
engine = pyttsx3.init()

# Mendapatkan daftar suara yang tersedia
voices = engine.getProperty('voices')

# Mencari suara wanita dalam daftar suara yang tersedia
female_voice = voices[2]
for voice in voices:
    if 'female' in voice.name.lower():
        female_voice = voice
        break

# Mengatur suara menjadi suara wanita jika ditemukan
if female_voice is not None:
    engine.setProperty('voice', female_voice.id)
else:
    print('HeyAI: Maaf, suara wanita tidak tersedia. Suara default akan digunakan.')

# Mengatur kecepatan suara (nilai default: 1.0)
engine.setProperty('rate', 150)  # Mengatur kecepatan suara menjadi 150 kata per menit

# Mengatur volume suara (nilai default: 1.0)
engine.setProperty('volume', 0.8)  # Mengatur volume suara menjadi 0.8 (80% dari volume maksimal)

# Fungsi untuk mendapatkan informasi cuaca saat ini
def get_weather():
    # Ganti dengan API Key dari OpenWeatherMap
    api_key = "ef7bfb3cad53847f9b4f765e99565bb8"

    # Ganti dengan nama kota yang ingin Anda tampilkan cuacanya
    city = "Jakarta"

    # Membuat URL untuk meminta data cuaca saat ini
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Mengirim permintaan HTTP GET ke API OpenWeatherMap
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        # Mendapatkan informasi suhu saat ini dalam format Celsius
        temperature = weather_data['main']['temp'] - 273.15

        # Mendapatkan deskripsi cuaca saat ini
        weather_description = weather_data['weather'][0]['description']

        return temperature, weather_description
    else:
        return None, None

# Fungsi untuk memberikan respons berdasarkan input pengguna
def respond_to_user_input():
    user_input = input('Anda: ')
    greetings = ['Halo!', 'Hai!', 'Halo, apa yang bisa saya bantu?']
    responses = ['Tentu!', 'Tidak masalah.', 'Baiklah.', 'Saya akan melakukan yang terbaik.']
    goodbye = ['Sampai jumpa!', 'Selamat tinggal!', 'Hati-hati!']

    if user_input.lower() in ['halo', 'hai', 'hi']:
        response = random.choice(greetings)
    elif user_input.lower() in ['terima kasih', 'makasih']:
        response = random.choice(['Sama-sama!', 'Senang bisa membantu.', 'Tidak masalah.'])
    elif user_input.lower() in ['selamat tinggal', 'goodbye']:
        response = random.choice(goodbye)
    else:
        response = random.choice(responses)

    print('HeyAI:', response)
    engine.say(response)
    engine.runAndWait()

# Fungsi untuk menjalankan asisten AI
def run_assistant():
    print('HeyAI: Halo, nama saya HeyAI. Ada yang bisa saya bantu?')
    engine.say('Halo, nama saya HeyAI. Ada yang bisa saya bantu?')
    engine.runAndWait()

    # Menampilkan hari, tanggal, bulan, tahun saat ini
    now = datetime.now()
    print('Waktu:', now.strftime("%A, %d %B %Y %H:%M:%S"))
    engine.say(f'Sekarang adalah hari {now.strftime("%A")}, tanggal {now.day} bulan {now.strftime("%B")} tahun {now.year}.')
    engine.runAndWait()

    # Mendapatkan informasi cuaca saat ini
    temperature, weather_description = get_weather()

    # Menampilkan informasi cuaca dan suhu saat ini
    if temperature is not None and weather_description is not None:
        print('Cuaca saat ini:', weather_description)
        print('Suhu saat ini:', round(temperature, 1), '°C')
        engine.say(f'Cuaca saat ini adalah {weather_description}. Suhu saat ini adalah {round(temperature, 1)} derajat Celsius.')
        engine.runAndWait()
    else:
        print('Cuaca saat ini: Tidak dapat memperoleh informasi cuaca')
        engine.say('Maaf, tidak dapat memperoleh informasi cuaca saat ini.')
        engine.runAndWait()

    while True:
        user_input = input('Anda: ')

        if user_input.lower() in ['keluar', 'bye']:
            goodbye_message = random.choice(['Sampai jumpa!', 'Selamat tinggal!', 'Hati-hati!'])
            print('HeyAI:', goodbye_message)
            engine.say(goodbye_message)
            engine.runAndWait()
            break

        respond_to_user_input()

# Jalankan asisten AI
run_assistant()
