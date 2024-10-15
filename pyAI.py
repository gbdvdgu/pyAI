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
    key = 'bd5e378503939ddaee76f12ad7a97608'  # Your OpenWeatherMap API key
    city = 'Delhi'
    api_address = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
    
    try:
        json_data = requests.get(api_address).json()
        if 'main' in json_data:
            temperature = round(json_data["main"]["temp"] - 273.15, 1)  # Convert Kelvin to Celsius
            return temperature
        else:
            print(f"Error fetching temperature data: {json_data}")
            return "N/A"
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return "N/A"

def des():
    key = 'bd5e378503939ddaee76f12ad7a97608'  # Your OpenWeatherMap API key
    city = 'Delhi'
    api_address = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
    
    try:
        json_data = requests.get(api_address).json()
        if 'weather' in json_data:
            description = json_data["weather"][0]["description"]
            return description
        else:
            print(f"Error fetching weather description: {json_data}")
            return "N/A"
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return "N/A"

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    talk(joke)

def get_news():
    news_api_key = 'pub_56303b52988c0eccb2680e15a4188c92baea2'
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        news = response.json()
        if 'articles' in news and len(news['articles']) > 0:
            articles = news['articles'][:5]
            for article in articles:
                print(article['title'])
                talk(article['title'])
        else:
            talk("No news articles found.")
            print("No articles found.")
    else:
        talk("Failed to retrieve news.")
        print(f"Error: {response.status_code}")

def set_alarm():
    talk("Please enter the alarm time in the format HH:MM")
    alarm_time_str = input("Enter the alarm time (HH:MM): ")
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
        talk(f'Setting an alarm for {alarm_time_str}')
        
        while True:
            if datetime.datetime.now().hour == alarm_time.hour and datetime.datetime.now().minute == alarm_time.minute:
                talk("It's time for your alarm!")
                break
            time.sleep(10)
    except ValueError:
        talk("Invalid time format. Please try again.")

def play_playlist():
    playlist = ['arcade', 'infected', 'Harleys In Hawaii']  # replace with your playlist
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
        
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                talk(f"Congratulations! You guessed it in {attempts} attempts")
                break
            elif guess > number:
                talk("Try a lower number")
            else:
                talk("Try a higher number")
        except ValueError:
            talk("That's not a valid number. Please enter a number between 1 and 10.")

    if attempts == 3 and guess != number:
        talk(f"Sorry, the correct number was {number}")

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
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'The current time is {current_time}')
            print(current_time)

        elif 'date' in command:
            current_date = datetime.datetime.now().strftime('%D / %M / %Y')
            talk(f'Today\'s date is: {current_date}')
            print("Today's date is: ", current_date)

        elif 'temperature' in command or 'weather' in command:
            current_temp = temp()
            weather_desc = des()
            talk(f'Temperature in New Delhi is {current_temp} degrees Celsius with {weather_desc}.')
            print(f'{current_temp} °C')
            print(weather_desc)

        elif 'calculate' in command:
            calculate()

        elif 'note' in command:
            talk('What should I note down?')
            note_text = take_command()
            note(note_text)
            talk('Noted!')

        elif 'joke' in command:
            tell_joke()

        elif 'news' in command:
            get_news()

        elif 'set alarm' in command:
            set_alarm()

        elif 'play every songs' in command:
            play_playlist()

        elif 'system info' in command:
            system_info()

        elif 'guessing game' in command:
            guessing_game()
        
        elif 'thanks zira' in command:
            thank_u_list = ['Always welcome', 'You are welcome sir', 'Any time']
            thanking = random.choice(thank_u_list)
            print(thanking)  
            talk(thanking)


        elif 'goodbye' in command or 'exit' in command:
            talk('Goodbye! Have a nice day!')
            break

        elif 'what is' in command:
            talk("What would you like to search for on Wikipedia?")
            search_wiki = input("Enter your search query for Wikipedia: ")  # Take manual input from the terminal
            try:
                info = wikipedia.summary(search_wiki, 1)
                talk('According to Wikipedia:')
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("There are multiple results for your query. Please be more specific.")
                print(e)
            except Exception as e:
                talk("I couldn't find any information on that.")
                print(e)

run_zira()
