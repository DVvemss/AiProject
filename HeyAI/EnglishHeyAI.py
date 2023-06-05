import random
import pyttsx3
from datetime import datetime
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Find a male voice from the available voices
male_voice = voices[1]
for voice in voices:
    if 'male' in voice.name.lower():
        male_voice = voice
        break

# Set the voice to male if found
if male_voice is not None:
    engine.setProperty('voice', male_voice.id)
else:
    print('HeyAI: Apologies, a male voice is not available. Using the default voice.')

# Set the voice speed (default: 1.0)
engine.setProperty('rate', 150)  # Set the voice speed to 150 words per minute

# Set the voice volume (default: 1.0)
engine.setProperty('volume', 0.8)  # Set the voice volume to 0.8 (80% of maximum volume)

# Function to get current weather information
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

        # Get the current weather description
        weather_description = weather_data['weather'][0]['description']

        return temperature, weather_description
    else:
        return None, None

# Function to respond based on user input
def respond_to_user_input():
    user_input = input('You: ')
    greetings = ['Hello!', 'Hi!', 'Hello, how can I assist you?']
    responses = ['Of course!', 'No problem.', 'Understood. I will do my best.']
    goodbye = ['Goodbye!', 'Farewell!', 'Take care!']

    if user_input.lower() in ['hello', 'hi', 'good morning', 'good afternoon', 'good evening']:
        response = random.choice(greetings)
    elif user_input.lower() in ['thank you', 'thanks']:
        response = random.choice(['You\'re welcome!', 'I\'m glad I could help.', 'No problem.'])
    elif user_input.lower() in ['goodbye', 'bye']:
        response = random.choice(goodbye)
    else:
        response = random.choice(responses)

    print('HeyAI:', response)
    engine.say(response)
    engine.runAndWait()

# Function to run the AI assistant
def run_assistant():
    print('HeyAI: Hello, my name is HeyAI. How can I assist you?')
    engine.say('Hello, my name is HeyAI. How can I assist you?')
    engine.runAndWait()

    # Display the current day, date, month, and year
    now = datetime.now()
    print('Time:', now.strftime("%A, %d %B %Y %H:%M:%S"))
    engine.say(f'It is {now.strftime("%A")}, {now.strftime("%B")} {now.day}, {now.year}.')
    engine.runAndWait()

    # Get the current weather information
    temperature, weather_description = get_weather()

    # Display the current weather and temperature
    if temperature is not None and weather_description is not None:
        print('Current Weather:', weather_description)
        print('Current Temperature:', round(temperature, 1), '°C')
        engine.say(f'The current weather is {weather_description}. The current temperature is {round(temperature, 1)} degrees Celsius.')
        engine.runAndWait()
    else:
        print('Current Weather: Unable to fetch weather information')
        engine.say('Sorry, I couldn\'t fetch the current weather information.')
        engine.runAndWait()

    while True:
        user_input = input('You: ')

        if user_input.lower() in ['quit', 'exit', 'goodbye']:
            goodbye_message = random.choice(['Goodbye!', 'Farewell!', 'Take care!'])
            print('HeyAI:', goodbye_message)
            engine.say(goodbye_message)
            engine.runAndWait()
            break

        respond_to_user_input()

# Run the AI assistant
run_assistant()
