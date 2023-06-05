import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import requests
import json
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    print('Jarvis:', text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print('Command:', command)

    except:
        command = ""

    return command

def get_weather(city):
    api_key = 'ef7bfb3cad53847f9b4f765e99565bb8'  # Ganti dengan API key Anda dari OpenWeatherMap
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)

        if data['cod'] != '404':
            weather_info = data['weather'][0]['description']
            temperature = data['main']['temp']
            temperature = round(temperature - 273.15, 2)  # Konversi dari Kelvin ke Celcius
            talk(f"The weather in {city} is {weather_info}. The temperature is {temperature} degrees Celsius.")
        else:
            talk('Sorry, I could not retrieve the weather information.')

    except:
        talk('Sorry, there was an error retrieving the weather information.')

def get_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    try:
        response = requests.get(url)
        data = json.loads(response.text)


        joke_setup = data['setup']
        joke_punchline = data['punchline']
        talk(joke_setup)
        talk(joke_punchline)

    except:
        talk('Sorry, I could not retrive a joke at the moment.')

def search_wikipedia(topic):
    try:
        result = wikipedia.summary(topic, sentences=2)
        talk(result)

    except wikipedia.exceptions.PageError:
        talk("Sorry, I couldn't find any information on that topic")

    except wikipedia.exceptions.DisambiguationError:
        talk("There are multiple pages related to that topic, Please provide more specific details")
    
    except Exception as e:
        talk("Sorry, there was an error while searching for the information")

def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'weather in' in command:
        city = command.replace('weather in', '').strip()
        get_weather(city)
    elif 'tell me a joke' in command:
        get_joke()
    elif 'search' in command:
        topic = command.replace('search', '').strip()
        search_wikipedia(topic)
    # Tambahkan tugas lainnya sesuai keinginan Anda

while True:
    run_jarvis()
