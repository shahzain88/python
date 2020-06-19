import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

MASTER = "Zain"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# [0]is english woman, [1] is japanese woman ,no other voices
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

    # I dont want this for now
    # speak(f"I am {Ai_name} ! How can i help you.")


def takeComand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(speak_pleas_list_choice)
        speak(speak_pleas_list_choice)
        audio = r.listen(source)
    try:
        print("lets see...")
        speak("lets see .")
        query = r.recognize_google(audio, language='en-us')
        print(f"you said:{query}\n")
        speak(f"you said:{query}\n")
    except Exception:
        print("Say that again please .")
        speak("Say that again please .")
        query = None
    return query


def takeComand_two():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("ok")
        speak("say my name")
        audio = r.listen(source)
    try:
        print("lets see...")
        query = r.recognize_google(audio, language='en-us')
        print(f"Do you want to call me :{query}\n")
        speak(f"Do you want to call me :{query}\n")
        query = takeComand()
        if "yes" in query.lower():
            print("Thanks for this butiful name")
            speak("Thanks for this butiful name")
        else:
            print(f"ok. I will not change my name from {Ai_name}")
            speak(f"ok. I will not change my name from {Ai_name}")
    except Exception:
        print("Say that again please .")
        speak("Say that again please .")
        query = None
    return query


# lists for random

beginning_list = ['Initializing', 'Starting', 'Opening']
beginning_list_choice = random.choice(beginning_list)
speak_pleas_list = ['You can speak now .', f'I am ready to take order {MASTER}!',
                    'What can i do for you?', f'How can I help you {MASTER}?', 'Is there something that I can do for you?']
speak_pleas_list_choice = random.choice(speak_pleas_list)


Ai_name = "Buggy"
print(beginning_list_choice + " " + Ai_name + "...")
speak(beginning_list_choice + " " + Ai_name)
wishMe()
while True:

    # random lists that runs with loop
    query = takeComand()
    query

    # there was a bug witch alwas said None can't be in Lower case
    if query == None:
        speak("speak some thing")
        print("speak some thing")

    # comands witch is related to Buggy in my hardwer
    # 1:about buggy
    elif 'quit'in query.lower():
        speak("ok bye")
        print("ok bye")
        break
    elif 'change your name' in query.lower():
        speak("witch name are you going to give me?")
        middle_query = takeComand_two()
        middle_query
        if middle_query == None:
            speak("tell me my name")
            print("tell me my name")
        else:
            Ai_name = middle_query

    elif 'what is your name' in query.lower():
        speak(f"My name is {Ai_name}")
        print(f"My name is {Ai_name}")

    elif 'how are you' in query.lower():
        print(random.choice(['I am Good thank you ', 'Well I fell more batter to see you ',
                             f'{MASTER} I am computer dont wory about me', ]))
        speak(random.choice(['I am Good thank you ', 'Well I fell more batter to see you ',
                             f'{MASTER} I am computer dont wory about me', ]))
    elif 'What is going on' in query.lower():
        print(random.choice(['I am Good thank you ', 'Well I fell more batter to see you ',
                             f'{MASTER} I am computer dont wory about me', ]))
        speak(print(random.choice(['I am Good thank you ', 'Well I fell more batter to see you ',
                                   f'{MASTER} I am computer dont wory about me', ])))

    elif 'witch color do you like' in query.lower():
        Ai_like_color = random.choice(
            ['Yellow is my favorite', 'It\'s Yellow', 'I like Yellow the most'])
        print(Ai_like_color + '.')
        speak(Ai_like_color + '.')

    elif 'what\'s your favorite color' in query.lower():
        Ai_like_color = random.choice(
            ['Yellow is my favorite', 'It\'s Yellow', 'I like Yellow the most'])
        print(Ai_like_color + '.')
        speak(Ai_like_color + '.')

    elif 'what age are you' in query.lower():
        Ai_age_random = random.choice(['I am 19 years old', 'I\'m 19', '19'])
        print(Ai_age_random)
        speak(Ai_age_random)
    elif 'how old are you' in query.lower():
        Ai_age_random = random.choice(['I am 19 years old', 'I\'m 19', '19'])
        print(Ai_age_random)
        speak(Ai_age_random)

    elif 'tell me your age' in query.lower():
        Ai_age_random = random.choice(['I am 19 years old', 'I\'m 19', '19'])
        print(Ai_age_random)
        speak(Ai_age_random)

    elif 'what is your height' in query.lower():
        Ai_hight_random = random.choice(
            ['I am 164 centimetres tall', 'I become 164 centimetre'])
        print(Ai_hight_random)
        speak(Ai_hight_random)

    elif 'how tall are you' in query.lower():
        Ai_hight_random = random.choice(
            ['I am 164 centimetres tall', 'I become 164 centimetre'])
        print(Ai_hight_random)
        speak(Ai_hight_random)

    elif 'who is your favorite porson' in query.lower():
        Ai_favorite_band = random.choice(
            ['San is my favorite', 'I like San the most', 'It\'s San', 'Of course it is San'])
        print(Ai_favorite_band)
        speak(Ai_favorite_band)

    elif 'who is your favorite' in query.lower():
        Ai_favorite_band = random.choice(
            ['San is my favorite', 'I like San the most', 'It\'s San', 'Of course it is San'])
        print(Ai_favorite_band)
        speak(Ai_favorite_band)

    elif 'pubg' in query.lower():
        Ai_hate_pubg = random.choice(
            ['Oh God i hate pubg game the most', 'I hate PUBG'])
        print(Ai_hate_pubg)
        speak(Ai_hate_pubg)

    elif 'what do you hate' in query.lower():
        Ai_hate_pubg = random.choice(
            ['Oh God i hate pubg game the most', 'I hate PUBG'])
        print(Ai_hate_pubg)
        speak(Ai_hate_pubg)

    # 2:telling buggy to do some thing in side this compeuter

    elif "play music" in query.lower():
        songs_dir = "C:\\Users\\ShahZain\\Downloads\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "what"and "time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}.")

    elif "open vs code" in query.lower():
        code_path = "C:\\Users\\ShahZain\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif "open download" in query.lower():
        code_path = "C:\\Users\\ShahZain\\Downloads"
        os.startfile(code_path)

    elif "open desktop" in query.lower():
        code_path = "C:\\Users\\ShahZain\\Desktop"
        os.startfile(code_path)

    elif "read this " in query.lower():
        speak("What do you want me to read? paste be low.")
        print("What do you want me to read? paste be low.\n")
        read = input(">>>")
        speak(read)
        speak("i hope that helps you. But you have to try once, ok!")

    # 3:telling bugy to do things out side of dhis pc.

    elif 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif "open youtube" in query.lower():
        url = 'http://youtube.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "search" and "in youtube" in query.lower():
        new = 4
        speak("searching in youtube")
        print("searching in youtube")
        query = query.replace('in youtube', "").replace('search', "")
        url = 'https://www.youtube.com/results?search_query='
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        print("Searched   " + query)
        webbrowser.get(chrome_path).open(url + query, new=new)

    elif "open google" in query.lower():
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

    else:

        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

        speak(" i am searching in google ")
        print(" i am searching in google ")
        new = 2
        url = 'https://www.google.com/search?q='
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        print("Searched   " + query)
        webbrowser.get(chrome_path).open(url + query, new=new)

        # speak('was this the answer you wanted?')
        # print('was this the answer you wanted?')
        # middle_query = takeComand_two()
        # middle_query
        # if middle_query == None:
        #     speak("speak some thing")
        #     print("speak some thing")
        # elif "yes" in middle_query.lower():
        #     speak("i hope it helps you .")
        # else:
        #     print(query)
