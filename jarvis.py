from hashlib import new
import pyttsx3  # convert text data into speech using python
import datetime  # to fetch current date and time
import speech_recognition as sr  # convert speech from mic to text
import smtplib
from wikipedia.wikipedia import languages  # used to send emails
from secreats import senderemail, epwd, to
import webbrowser as wb  # opens brower
import pyautogui  # send whats app mesage
from time import sleep  # let programe not do anything for specific time
import wikipedia  # search through wikipedia
import pywhatkit  # for opening yt video
import requests  # for requesting weather data from api
from newsapi import NewsApiClient  # for receiving data from news api
import clipboard  # to read the selected text on the screen
import os
import pyjokes  # to get jokes
import time as tt  # to import time
import string
import random
from nltk.tokenize import word_tokenize

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello this is jarvis")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is devil")
    if voice == 3:
        engine.setProperty('voice', voices[2].id)
        speak("Hello this is friday")


def time():
    # hour = I & minutes = M & seconds = S
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is : ")
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is : ")
    speak(day)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening")
    else:
        speak("Good night")


def wishme():
    speak("Welcome back sir!")
    greeting()
    speak("Please tell me how can i help you!")


def takeCommandCMD():
    query = input("Please tell me how may i help you ?\n")
    return query


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizning......")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Please say that again....")
        return "None"
    return query


def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    server.sendmail(senderemail, to, content)
    server.close()


def sendWhatsmsg(phone_no, message):
    Message = message
    wb.open('https://www.web.whatsapp.com/send?phone='+phone_no+'&text'+Message)
    sleep(10)
    pyautogui.press('enter')


def searchgoogle():
    speak("What should i search ?")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


# http://api.openweathermap.org/data/2.5/weather?q=chandigarh&units=imperial&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd


def news():
    newsapi = NewsApiClient(api_key='7ab8e2691fa943dda08184a136631c2f')
    speak("What topic you need the news about ?")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic, language='en', page_size=2)

    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("that's it for now i'll update you in some time")


def text2speech():
    text = clipboard.paste()
    speak(text)


def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered {data["recovered"]}'
    print(covid_data)
    speak(covid_data)


def weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=chandigarh&units=imperial&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd'
    res = requests.get(url)
    data = res.json()
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    desp = data['weather'][0]['description']
    temp = round((temp - 32) * 5/9)
    print(weather)
    print(temp)
    print(desp)
    speak(f'Temerature : {temp} degree celcius')
    speak(f'Weather is {desp}')


def youtube():
    speak('What should i search ?')
    topic = takeCommandMic()
    pywhatkit.playonyt(topic)


def email():
    try:
        speak("What should i say ?")
        content = takeCommandMic()
        sendEmail(content)
        speak("Email sent sucessfully")
    except Exception as e:
        print(e)
        speak("Unable to send the email")


def message():
    user_name = {
        'Rajat': '+91 99922 41662'
        # write your all contacts here
    }
    try:
        speak("To whom you want to send this message ?")
        name = takeCommandMic()
        phone_no = user_name[name]
        speak("What is the message ?")
        message = takeCommandMic()
        sendWhatsmsg(phone_no, message)
        speak("Message has been sent")
    except Exception as e:
        print(e)
        speak("Message can not be sent")


def offline():
    speak("Bye bye sir, have a nice day")
    exit()


def screenshot():
    name_img = tt.time()
    name_img = f'E:\\Projects\\Jarvis\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)


def flip():
    speak("ok sir flipping a coin")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (''.join(toss[0]))
    speak("i flipped the coin and you got"+toss)


def roll():
    speak("Okay sir, rolling a die for you")
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("I rolled a die and you got" + roll)


def remember_something():
    speak("What should i remember ?")
    data = takeCommandMic()
    speak("You said me to remember that" + data)
    remember = open('data.txt', 'w')
    remember.write(data)
    remember.close()


def display_note():
    remember = open('data.txt', 'r')
    speak("You told me to remember that" + remember.read())


def open_vs():
    codepath = 'C:\\Users\\rajat\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    os.startfile(codepath)


wakeword = "devil"

if __name__ == "__main__":
    getvoices(2)
    wishme()
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        if wakeword in query:
            if 'time' in query:
                time()

            elif 'date' in query:
                date()

            elif 'email' in query:
                email()

            elif 'message' in query:
                message()

            elif 'wikipedia' in query:
                speak("Searching on wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

            elif 'search' in query:
                searchgoogle()

            elif 'youtube' in query:
                youtube()

            elif 'weather' in query:
                weather()

            elif 'news' in query:
                news()

            elif 'read' in query:
                text2speech()

            elif 'covid' in query:
                covid()

            elif 'open code' in query:
                open_vs()

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'screenshot' in query:
                screenshot()

            elif 'remember that' in query:
                remember_something()

            elif 'do you remember' in query:
                display_note()

            elif 'password' in query:
                passwordgen()

            elif 'flip' in query:
                flip()

            elif 'roll' in query:
                roll()

            elif 'offline' in query:
                offline()


# takeCommandMic = "hey devil what is the date today"  tokenize = ['hey' + 'devil' + 'what' + 'is' + 'the' + 'date' + 'today']
