import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
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
    except Exception:
        print("Say that again please .")
        speak("Say that again please .")
        query = None
    return query


speak("Initializing Buggy.....")
wishMe()
while True:
    query = takeComand()
    query
    if query == None:
        speak("speak some thing")
        print("speak some thing")
    elif 'quit'in query.lower():
        speak("ok bye")
        print("ok bye")
        break
    elif 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif "open" and "youtube" in query.lower():
        url = 'http://youtube.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open" and "google" in query.lower():
        url = 'http://google.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "search" in query.lower():
        speak("Searching in google..")
        print("Searching in Google..")
        query = query.replace("search" or "google", "")
        new = 2
        url = 'https://www.google.com/search?q='
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        print("Searched   " + query)
        webbrowser.get(chrome_path).open(url + query, new=new)

    elif "play music" in query.lower():
        songs_dir = "C:\\Users\\ShahZain\\Downloads\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "what"and "time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}.")

    elif "open vs code" in query.lower():
        code_path = "C:\\Users\\ShahZain\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe"
        os.startfile(code_path)

    elif "read this " in query.lower():
        speak("What do you want me to read? paste be low.")
        read = input("What do you want me to read? paste be low.\n", ">>>")
        speak(read)
        speak("i hope that helps you. But you have to try once, ok!")
    else:
        speak("wikipedia says")
        print("wikipedia says")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

        speak("could not  understand you , so i am searching in google ")
        print("could not  understand you , so i am searching in google ")
        new = 2
        url = 'https://www.google.com/search?q='
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        print("Searched   " + query)
        webbrowser.get(chrome_path).open(url + query, new=new)
