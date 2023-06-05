import random
import time
import speech_recognition as sr


def greetings():
    responses = ['Halo', 'Hai', 'Halo, ada yang bisa saya bantu']
    return random.choice(responses)

def process_input(user_input):
    # Anda dapat menambahkan logika dan fungsi yang pemrosesan yang lebih kompleks
    return  "saya tidak dapat memproses permintaan Anda saat ini"

def run_assistant():
    print(greetings())
    time.sleep(1)

    # Membuat objek recognizer di luar loop
    r = sr.Recognizer()

    # Menggunaan microphone sebagai source suara
    with sr.Microphone() as source:
        # mengatur timeout menjadi 1 detik (optional)
        r.adjust_for_ambient_noise(source, duration=1)
    

    while True: 
        # Menggunaan microphone sebagai source suara
         with sr.Microphone() as source:
        # mengatur timeout menjadi 1 detik (optional)
            r.adjust_for_ambient_noise(source, duration=1)
            print("Mulai Bicara...")
            # Menggunakan buffering agar tidak ada jeda
            audio = r.listen(source, phrase_time_limit=5) # Menggunakan batasan waktu maksimum 5 detik (opsional)

            try:
                # Menggunakan recognizer untuk mengubah suara menjadi teks
                user_input = r.recognize_google(audio, language='id-ID')
                print("Anda : " + user_input)
                # user_input = input("Anda : ")

                if user_input.lower() == 'keluar':
                    print("Asisten : Sampai jumpa")
                    break

                response = process_input(user_input)
                print("Asisten : ", response)

            except sr.UnknownValueError:
                print("Asisten : Maaf, saya tidak bisa mengenali suara anda.")
            except sr.RequestError:
                print("Asisten : Maaf, terjadi masalah pada layanan pengenalan suara.")


if __name__ == '__main__':
    run_assistant()