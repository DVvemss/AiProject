import random
import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from datetime import datetime

# API key untuk OpenWeatherMap
api_key = "YOUR_API_KEY"  # Ganti dengan API key Anda

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Jakarta,id&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return weather, temperature

    return None, None

def greetings():
    responses = ['Hello', 'Hi', 'Hello, how can I help you']
    opener = random.choice(responses)
    speak(opener)
    return opener

def process_input(user_input):
    # Anda dapat menambahkan logika dan fungsi yang pemrosesan yang lebih kompleks

    # Cek jika input mengandung kata "cari"
    if 'search' in user_input.lower():
        search_query = user_input.lower().replace('search', '').strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
        return f"Search results for '{search_query}' in a browser."
    
    elif 'open' in user_input.lower():
        url = user_input.lower().replace('open', '').replace('dotcom', '.com').replace(' ', '').strip()
        if 'http://' not in url and 'https://' not in url:
            url = 'http://' + url
        webbrowser.open(url)    
        return f"Opens {url} in the browser."

    return "I am unable to process your request at this time"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'en')  # Mengatur suara menjadi bahasa Inggris
    engine.setProperty('rate', 150)  # Mengatur kecepatan ucapan (opsional)
    engine.setProperty('volume', 0.75)  # Mengatur volume ucapan (opsional)
    engine.say(text)
    engine.runAndWait()

def run_assistant():
    # Mengucapkan waktu, hari, tanggal, cuaca, dan suhu saat pertama kali dijalankan
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_day = now.strftime("%A")
    current_date = now.strftime("%B %d, %Y")
    weather, temperature = get_weather()
    
    greetings_message = greetings()
    weather_message = f"Today is {current_day}, {current_date}. The current time is {current_time}."

    if weather and temperature:
        weather_message += f" The weather is {weather} with a temperature of {temperature} degrees Celsius."
    
    print(greetings_message)
    print(weather_message)
    speak(greetings_message)
    time.sleep(1)
    speak(weather_message)
    
    # Membuat objek recognizer di luar loop
    r = sr.Recognizer()

    is_voice_input = False  # Untuk menandai apakah input suara atau input manual
    

    while True: 
        if not is_voice_input:
            user_input = input("You : ")

            if user_input.lower() == 'keluar' or user_input.lower() == 'close' or user_input.lower() == 'shutdown' or user_input.lower() == 'quit':
                print("Assistant : Bye")
                speak("Bye")
                break
            
            if user_input.lower() == 'inputan manual':
                print("You : Manual Input")
                speak("Okay, I'll switch to manual input")
                is_voice_input = False

            else:
                is_voice_input = True
                print("You : Voice")
                speak("Okey, I'll listen to you")

        else:
            with sr.Microphone() as source:
                speak("Listening to...")
                print("Start Talking...")
                audio = r.listen(source, phrase_time_limit=5)  # Menggunakan batasan waktu maksimum 5 detik (opsional)

            try:
                user_input = r.recognize_google(audio, language='id-ID')
                print("You : " + user_input)
                
                if user_input.lower() == 'keluar' or user_input.lower() == 'close' or user_input.lower() == 'shutdown' or user_input.lower() == 'quit':
                    print("Assistant : Bye")
                    speak("Bye")
                    break

                elif user_input.lower() == 'inputan manual':
                    print("You : Manual Input")
                    speak("Okay, I'll switch to manual input")
                    is_voice_input = False

                else:
                    response = process_input(user_input)
                    print("Assistant : ", response)
                    speak(response)

            except sr.UnknownValueError:
                print("Assistant: Sorry, I can't recognize your voice.")
            except sr.RequestError:
                print("Assistant : Sorry, there was a problem with the voice recognition service.")


if __name__ == '__main__':
    run_assistant()
