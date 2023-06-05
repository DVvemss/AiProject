import random
import pyttsx3
from datetime import datetime
import requests

# Inisialisasi mesin teks-ke-suara
engine = pyttsx3.init()

# Mendapatkan daftar suara yang tersedia
voices = engine.getProperty('voices')

# Mencari suara perempuan dalam daftar suara yang tersedia
female_voice = voices[2]
for voice in voices:
    if 'female' in voice.name.lower():
        female_voice = voice
        break

# Mengatur suara menjadi suara perempuan jika ditemukan
if female_voice is not None:
    engine.setProperty('voice', female_voice.id)
else:
    print('HeyAI: 申し訳ありませんが、女性の声は利用できません。デフォルトの声を使用します。')

# Mengatur kecepatan suara (nilai default: 1.0)
engine.setProperty('rate', 150)  # Kecepatan suara diatur menjadi 150 kata per menit

# Mengatur volume suara (nilai default: 1.0)
engine.setProperty('volume', 0.8)  # Volume suara diatur menjadi 0.8 (80% dari volume maksimum)

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
    user_input = input('あなた: ')
    greetings = ['こんにちは！', 'やあ！', 'こんにちは、何をお手伝いできますか？']
    responses = ['もちろんです！', '問題ありません。', 'わかりました。最善を尽くします。']
    goodbye = ['さようなら！', 'さよなら！', 'お気をつけて！']

    if user_input.lower() in ['こんにちは', 'やあ', 'おはよう', 'こんばんは']:
        response = random.choice(greetings)
    elif user_input.lower() in ['ありがとう', 'どうもありがとう']:
        response = random.choice(['どういたしまして！', 'お手伝いできて嬉しいです。', '問題ありません。'])
    elif user_input.lower() in ['さようなら', 'バイバイ']:
        response = random.choice(goodbye)
    else:
        response = random.choice(responses)

    print('HeyAI:', response)
    engine.say(response)
    engine.runAndWait()

# Fungsi untuk menjalankan asisten AI
def run_assistant():
    print('HeyAI: こんにちは、私の名前はHeyAIです。何かお手伝いできますか？')
    engine.say('こんにちは、私の名前はHeyAIです。何かお手伝いできますか？')
    engine.runAndWait()

    # Menampilkan hari, tanggal, bulan, tahun saat ini
    now = datetime.now()
    print('時間:', now.strftime("%A, %d %B %Y %H:%M:%S"))
    engine.say(f'現在は{now.strftime("%A")}曜日、{now.day}日の{now.strftime("%B")}月、{now.year}年です。')
    engine.runAndWait()

    # Mendapatkan informasi cuaca saat ini
    temperature, weather_description = get_weather()

    # Menampilkan informasi cuaca dan suhu saat ini
    if temperature is not None and weather_description is not None:
        print('現在の天気:', weather_description)
        print('現在の気温:', round(temperature, 1), '°C')
        engine.say(f'現在の天気は{weather_description}です。現在の気温は摂氏{round(temperature, 1)}度です。')
        engine.runAndWait()
    else:
        print('現在の天気: 天気情報を取得できませんでした')
        engine.say('申し訳ありませんが、現在の天気情報を取得できませんでした。')
        engine.runAndWait()

    while True:
        user_input = input('あなた: ')

        if user_input.lower() in ['終了', 'バイバイ']:
            goodbye_message = random.choice(['さようなら！', 'さよなら！', 'お気をつけて！'])
            print('HeyAI:', goodbye_message)
            engine.say(goodbye_message)
            engine.runAndWait()
            break

        respond_to_user_input()

# Menjalankan asisten AI
run_assistant()
