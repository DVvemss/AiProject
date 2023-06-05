import random
import time
import webbrowser
import subprocess
import pyttsx3
import requests
from bs4 import BeautifulSoup
import turtle
import openai

# Inisialisasi mesin text-to-speech
engine = pyttsx3.init()

# pengaturan suara 
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

# Inisialisasi turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("AI Assistant")
screen.setup(width = 800, height = 600)
turtle_pen = turtle.Turtle()
turtle_pen.color("white")
turtle_pen.hideturtle()
turtle_pen.penup()
turtle_pen.goto(0, 0)

# Data Pengguna
user_data = {}

# Inisisal API OpenAI
openai_api_key = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetings():
    responses = ['Halo', 'Hai', 'Halo, ada yang bisa saya bantu']
    return random.choice(responses)

def process_input(user_input):
    if 'cari di Google' in user_input:
        query = user_input.replace('cari di Google', '')
        search_google(query)
        return "Membuka hasil pencarian di Google."



