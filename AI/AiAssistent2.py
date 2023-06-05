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

    while True:

        # Membuat objek recognizer
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Mulai Bicara...")
            audio = r.listen(source)

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