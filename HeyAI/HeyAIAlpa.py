import random
import pyttsx3
from datetime import datetime
import requests
import webbrowser
import os
import pywhatkit
import glob
import time
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice to an English voice (you can choose any English voice available)
engine.setProperty('voice', voices[1].id)

# Set the speed of speech (default value: 1.0)
engine.setProperty('rate', 150)  # Set the speed to 150 words per minute

# Set the volume of speech (default value: 1.0)
engine.setProperty('volume', 0.8)  # Set the volume to 0.8 (80% of maximum volume)

# Function to get the current weather information
def get_weather():
    # Replace with your OpenWeatherMap API Key
    api_key = "ef7bfb3cad53847f9b4f765e99565bb8"

    # Replace with the city name you want to display the weather for
    city = "Jakarta"

    # Create the URL to request the current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Send an HTTP GET request to the OpenWeatherMap API
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        # Get the current temperature in Celsius
        temperature = weather_data['main']['temp'] - 273.15

        # Get the weather description
        weather_description = weather_data['weather'][0]['description']

        return temperature, weather_description
    else:
        return None, None

# Function to search for music in local or offline storage
def search_music_offline(song_name):
    music_files = glob.glob('C:\\Users\\DVvemsss\\Music\\*.mp3')  # Replace with your music storage directory

    for music_file in music_files:
        filename = os.path.basename(music_file)
        if song_name.lower() in filename.lower():
            return music_file

    return None

# Function to provide responses based on user input
def respond_to_user_input(user_input):
    greetings = ['Hello!', 'Hi!', 'Hello, how can I assist you?']
    responses = ['Sure!', 'No problem.', 'Alright.', 'I will do my best.']
    goodbye = ['Goodbye!', 'Farewell!', 'Take care!']

    if user_input.lower() in ['hello', 'hi']:
        response = random.choice(greetings)

    elif user_input.lower() in ['thank you']:
        response = random.choice(["You're welcome!", 'Glad to help.', 'No problem.'])

    elif user_input.lower() in ['goodbye']:
        response = random.choice(goodbye)

    elif user_input.lower().startswith('search '):
        song_name = user_input[7:]
        music_file = search_music_offline(song_name)
        if music_file:
            response = f'Playing {song_name} from local storage.'
            os.startfile(music_file)
        else:
            response = f'Cannot find {song_name} in local storage. Searching for music online.'
            pywhatkit.playonyt(song_name)

    elif user_input.lower().startswith('open '):
        url = user_input[5:]
        if 'http://' not in url and 'https://' not in url:
            url = 'http://' + url
        webbrowser.open(url)
        response = 'Opening the URL in the browser.'

    elif user_input.lower().startswith('play music'):
        song_name = user_input[11:]
        music_file = search_music_offline(song_name)
        if music_file:
            response = f'Playing {song_name} from local storage.'
            os.startfile(music_file)
        else:
            response = f'Playing {song_name} on YouTube Music.'
            video_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
            webbrowser.open(video_url)

    else:
        response = random.choice(responses)

    print('Assistant:', response)
    engine.say(response)
    engine.runAndWait()

# Function to run the AI assistant
def run_assistant():
    print('Assistant: Hello, my name is Assistant. How can I assist you?')
    engine.say('Hello, my name is Assistant. How can I assist you?')
    engine.runAndWait()

    # Display the current day, date, month, and year
    now = datetime.now()
    print('Time:', now.strftime("%A, %d %B %Y %H:%M:%S"))
    engine.say(f"It's {now.strftime('%A')}, {now.strftime('%B')} {now.day}, {now.year}.\n")
    engine.say(f"The time is {now.strftime('%H:%M:%S')}")
    engine.runAndWait()

    # Add a 1-second delay before getting weather information
    time.sleep(1)

    # Get the current weather information
    temperature, weather_description = get_weather()

    # Display the current weather and temperature
    if temperature is not None and weather_description is not None:
        print('Current Weather:', weather_description)
        print('Current Temperature:', round(temperature, 1), '°C')
        engine.say(f"The current weather is {weather_description}. The temperature is {round(temperature, 1)} degrees Celsius.")
        engine.runAndWait()
    else:
        print('Current Weather: Unable to retrieve weather information')
        engine.say("Sorry, unable to retrieve the current weather information.")
        engine.runAndWait()

    while True:
        try:
            with sr.Microphone() as source:
                print("Assistant: Listening...")
                r = sr.Recognizer()
                audio = r.listen(source)

            print("Assistant: Processing text...")
            user_input = r.recognize_google(audio, language="en-US")
            print("You:", user_input)
            if user_input.lower() == 'exit':
                goodbye = ['Goodbye!', 'Farewell!', 'Take care!']
                print('Assistant:', random.choice(goodbye))
                engine.say(random.choice(goodbye))
                engine.runAndWait()
                break
            else:
                respond_to_user_input(user_input)
        except sr.UnknownValueError:
            print("Assistant: Sorry, I couldn't recognize your voice. Please try again.")
            engine.say("Sorry, I couldn't recognize your voice. Please try again.")
            engine.runAndWait()
        except sr.RequestError:
            print("Assistant: Sorry, there was an error with the speech recognition service. Please try again.")
            engine.say("Sorry, there was an error with the speech recognition service. Please try again.")
            engine.runAndWait()

# Run the AI assistant
run_assistant()
