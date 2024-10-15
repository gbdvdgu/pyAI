import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import randfacts
import random
import subprocess
import requests
import time
import os
import psutil  
import pyjokes  
from datetime import timedelta
from time import sleep

red = '\033[91m'
green = '\033[92m'
reset = '\033[0m'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    print(rf'''{red}
                      /$$$$$$  /$$$$$$      
                     /$$__  $$|_  $$_/      
  /$$$$$$  /$$   /$$| $$  \ $$  | $$        
 /$$__  $$| $$  | $$| $$$$$$$$  | $$        
| $$  \ $$| $$  | $$| $$__  $$  | $$        
| $$  | $$| $$  | $$| $$  | $$  | $$        
| $$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$      
| $$____/  \____  $$|__/  |__/|______/      
| $$       /$$  | $$                        
| $$      |  $$$$$$/                        
|__/       \______/                                  
                                       {green}GitHub: gbdvdgu
                                       MadeBy: Harsh Pratap Singh
{reset}''')
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        talk('Good Morning')
    elif hour < 18:
        talk('Good Afternoon')
    else:
        talk('Good Evening')

    talk('Myself Zira, How can I help you sir!')


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            listener = sr.Recognizer()
            listener.energy_threshold = 8000
            listener.adjust_for_ambient_noise(source, 1)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'zira' in command:
                command = command.replace('zira', '')
                print(f"Command: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results from the speech recognition service.")
    return command.strip()


def say_hello(text):
    greet = ["hi", "hello", "hey there"]
    responses = ["hi", "hello", "what's up", "hey there", "greetings!"]
    if text in greet:
        response = random.choice(responses)
        print(response)
        talk(response)


def calculate():
    talk("Please select any of the following operations: +, -, *, /, **")
    operation = input("Enter operation (+, -, *, /, **): ")
    talk("Enter first number")
    num1 = float(input('Enter first number: '))
    talk("Enter second number")
    num2 = float(input('Enter second number: '))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '**':
        result = num1 ** num2
    else:
        talk("Sorry, operation not available")
        return

    print(f'Result: {result}')
    talk(f'The result is {result}')


def note(text):
    date = datetime.datetime.now()
    filename = str(date).replace(":", "-") + "-note.txt"
    with open(filename, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", filename])


def temp():
    key = 'your_api_key'
    api_address = f'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid={key}'
    json_data = requests.get(api_address).json()

    if 'main' in json_data:
        temperature = round(json_data["main"]["temp"] - 273.15, 1)
        return temperature
    else:
        return "N/A"


def des():
    key = 'your_api_key'
    api_address = f'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid={key}'
    json_data = requests.get(api_address).json()

    if 'weather' in json_data:
        description = json_data["weather"][0]["description"]
        return description
    else:
        return "N/A"


def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    talk(joke)


def get_news():
    news_api_key = 'your_news_api_key'
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}'
    news = requests.get(url).json()
    articles = news['articles'][:5]
    for article in articles:
        print(article['title'])
        talk(article['title'])


def set_alarm(time_str):
    talk(f'Setting an alarm for {time_str}')
    alarm_time = datetime.datetime.strptime(time_str, "%H:%M")
    while True:
        if datetime.datetime.now().hour == alarm_time.hour and datetime.datetime.now().minute == alarm_time.minute:
            talk("It's time for your alarm!")
            break
        time.sleep(10)  


def set_timer(seconds):
    talk(f"Setting timer for {seconds} seconds")
    sleep(seconds)
    talk("Time's up!")


def play_playlist():
    playlist = ['song1', 'song2', 'song3']  # replace with your playlist
    talk("Playing your favorite playlist")
    for song in playlist:
        pywhatkit.playonyt(song)
        sleep(2)  


def system_info():
    battery = psutil.sensors_battery()
    battery_percent = battery.percent
    cpu_usage = psutil.cpu_percent(1)
    talk(f"Your system has {battery_percent}% battery remaining and the CPU usage is {cpu_usage} percent")


def guessing_game():
    number = random.randint(1, 10)
    attempts = 0
    while attempts < 3:
        talk("Guess a number between 1 and 10")
        guess = int(take_command())
        attempts += 1
        if guess == number:
            talk(f"Congratulations! You guessed it in {attempts} attempts")
            break
        elif guess > number:
            talk("Try a lower number")
        else:
            talk("Try a higher number")
    if attempts == 3:
        talk(f"Sorry, the number was {number}")


def run_zira():
    wish_me()
    while True:
        command = take_command()

        if 'hello' in command:
            say_hello(command)

        elif 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'The current time is {time}')
            print(time)

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%D / %M / %Y')
            talk(f'Today\'s date is: {date}')
            print("Today's date is: ", date)

        elif 'temperature' in command or 'weather' in command:
            current_temp = temp()
            weather_desc = des()
            talk(f'Temperature in New Delhi is {current_temp} degrees Celsius with {weather_desc}.')
            print(f'{current_temp} °C')
            print(weather_desc)

        elif 'calculate' in command:
            calculate()

        elif 'what is' in command:
            search_wiki = command.replace('what is', '').strip()
            info = wikipedia.summary(search_wiki, 1)
            talk('According to Wikipedia')
            print(info)
            talk(info)

        elif 'fact' in command:
            x = randfacts.get_fact()
            talk(f"Did you know that, {x}")

        elif 'note' in command:
            talk("Sure sir, what would you like me to write down?")
            note_text = take_command()
            note(note_text)
            talk("I have made the note successfully.")

        elif 'thank you' in command:
            thank_u_list = ['Always welcome', 'You are welcome sir', 'Any time']
            thanking = random.choice(thank_u_list)
            talk(thanking)

        elif 'open youtube' in command:
            talk("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            talk("Opening Google")
            webbrowser.open("google.com")

        elif 'joke' in command:
            tell_joke()

        elif 'news' in command:
            get_news()

        elif 'alarm' in command:
            talk("Tell me the time to set the alarm in HH:MM format")
            alarm_time = take_command()
            set_alarm(alarm_time)

        elif 'reminder' in command:
            talk("What should I remind you about?")
            reminder_text = take_command()
            talk("When should I remind you?")
            reminder_time = take_command()
            set_alarm(reminder_time)
            talk(f"Reminder set for {reminder_time}: {reminder_text}")

        elif 'playlist' in command:
            play_playlist()

        elif 'system info' in command:
            system_info()

        elif 'game' in command:
            guessing_game()

        elif 'timer' in command:
            talk("How many seconds?")
            seconds = int(take_command())
            set_timer(seconds)

        elif 'exit' in command:
            talk("Are you sure you want to exit?")
            confirmation = take_command()
            if 'yes' in confirmation or 'sure' in confirmation:
                talk("Goodbye!")
                break
            else:
                talk("Resuming assistant")

run_zira()
