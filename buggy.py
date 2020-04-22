import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email.mime import audio

print("Initializing Buggy.")
MASTER = "ShahZain88"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    speak("I am Buggy ! How can i help you.")


def takeComand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready!")
        speak("I am ready!")
        audio = r.listen(source)
    try:
        print("lets see...")
        speak("lets see .")
        query = r.recognize_google(audio, language='en-us')
        print(f"{MASTER} said:{query}\n")
        speak(f"{MASTER} said:{query}\n")
    except Exception as er:
        print("Say that again please .", er)
        speak("Say that again please .")
        query = None
    return query


def main():
    speak("Initializing Buggy.....")
    wishMe()
    query = takeComand()

    if 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif "open youtube" in query.lower():
        url = 'http://youtube.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open google" in query.lower():
        url = 'http://google.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "play music" in query.lower():
        songs_dir = "C:\\Users\\ShahZain\\Downloads\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "the time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}.")

    elif "open vs code" in query.lower:
        code_path = "C:\\Users\\ShahZain\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe"
        os.startfile(code_path)


main()
