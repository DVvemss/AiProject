import random
import time


def greetings():
    responses = ['Halo!', 'Hai!', 'Halo, ada yang bisa saya bantu?']
    return random.choice(responses)

def process_input(user_input):
    # Anda dapat menambahkan logika dan fungsi pemrosesan yang lebih kompleks di sini
    return "Saya tidak dapat memproses permintaan Anda saat ini."

def run_assistant():
    print(greetings())
    time.sleep(1)

    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'keluar':
            print("Asisten: Sampai jumpa!")
            break

        response = process_input(user_input)
        print("Asisten:", response)

if __name__ == '__main__':
    run_assistant()
