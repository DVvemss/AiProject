import random
import time
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime



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
    print(greetings())
    time.sleep(1)

    # Mengucapkan waktu saat pertama kali dijalankan
    now = datetime.now()
    curren_time = now.strftime("%H:%M")
    speak(f"The current time is {curren_time}")
    
    # Membuat objek recognizer di luar loop
    r = sr.Recognizer()

    while True: 
         user_input = input("You : ")

         if user_input.lower() == 'keluar' or user_input.lower() == 'close' or user_input.lower() == 'shutdown' or user_input.lower() == 'quit':
             print("Assistant : Bye")
             speak("Bye")
             break
         
         # Menggunakan recognizer hanya jika input bukan dari keyboard
         if user_input.lower() != 'voice':
             response = process_input(user_input)
             print("Assisten : ", response)
             speak(response)

         else:
            # Menggunaan microphone sebagai source suara
            with sr.Microphone() as source:
            # mengatur timeout menjadi 1 detik (optional)
                r.adjust_for_ambient_noise(source, duration=1)
                speak("Listening to...")
                print("Start Talking...")
                # Menggunakan buffering agar tidak ada jeda
                audio = r.listen(source, phrase_time_limit=5) # Menggunakan batasan waktu maksimum 5 detik (opsional)

            try:
                # Menggunakan recognizer untuk mengubah suara menjadi teks
                user_input = r.recognize_google(audio, language='id-ID')
                print("You : " + user_input)
                # user_input = input("Anda : ")

                if user_input.lower() == 'keluar' or user_input.lower() == 'close' or user_input.lower() == 'shutdown' or user_input.lower() == 'quit':
                    print("Assistant : Bye")
                    speak("Bye")
                    break

                response = process_input(user_input)
                print("Asisten : " , response)
                speak((response))

            except sr.UnknownValueError:
                print("Assistant: Sorry, I can't recognize your voice.")
            except sr.RequestError:
                print("Assistant : Sorry, there was a problem with the voice recognition service.")


if __name__ == '__main__':
    run_assistant()