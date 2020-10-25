import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
MASTER = "Zain"
Ai_name = "バギー"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# [0]is english woman, [3] is japanese woman ,no other voices
engine.setProperty('voice', voices[3].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("おはようございます！" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("こんにちは！" + MASTER)
    else:
        speak("こんばんは！" + MASTER)

    # I dont want this for now
    # speak(f"I am {Ai_name} ! How can i help you.")


def takeComand(speak_pleas_list_choice):

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(speak_pleas_list_choice)
        speak(speak_pleas_list_choice)
        audio = r.listen(source)
    try:
        print("処理中です…")
        speak("処理中です…")
        query = r.recognize_google(audio, language='ja-ja')
    except Exception:
        print("もう一度お願いします。")
        speak("もう一度お願いします。")
        query = None
    return query


def change_Ai_name(speak_pleas_list_choice, Ai_name):
    while True:
        try:
            speak("私にどのような名前をくださるのですか?私の名前を言ってください。")
            print("私にどのような名前をくださるのですか？私の名前を言ってください。")
            query = takeComand(speak_pleas_list_choice)
            query
            if query == None:
                continue
            else:
                speak(f"私の名前を{query}に変えますか？")
                print(f"私の名前を{query}に変えますか？")
                query = takeComand(speak_pleas_list_choice)
                if "はい" in query.lower():
                    speak(f"有り難うございます。今より{query}と呼んで下さい。")
                    print(f"有り難うございます。今より{query}と呼んで下さい。")
                    Ai_name = query
                    break
                else:
                    print(f"分かりました、私の名前を変えないで{Ai_name}のままにしておきます。")
                    speak(f"分かりました、私の名前を変えないで{Ai_name}のままにしておきます。")
                    break

        except Exception:
            print("うまくいきませんでした。最初からやり直して下さい。")
            speak("うまくいきませんでした。最初からやり直して下さい。")
            continue
    return 0


def wikipedia_search(query):
    wikipedia.set_lang("ja")
    print(query)
    query = query.replace("はどこにあるのか教えてください", "").replace("は誰ですか教えてください", "").replace("は何ですか教えてください", "").replace("は何か教えてください", "").replace("は何ですか教えて", "").replace("は何か教えて", "").replace("はどこにあるのですか", "").replace(
        "は誰ですか", "").replace("教えてください", "").replace("は何", "").replace("は誰", "").replace("教えて", "")

    result_ja = wikipedia.summary(query, sentences=3)

    print(result_ja)

    speak(result_ja)
    new = 2
    url = 'https://www.google.com/search?q='
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url + query, new=new)
    print(query + "を検索しました。")
    return 0


beginning_list = ['初期化しています', '起動しています', '開始しています']
beginning_list_choice = random.choice(beginning_list)
speak_pleas_list = ['話しても良いですよ！.', f'{MASTER}様、命令をお願いします！', ]


def main(Ai_name):

    print(Ai_name + "を" + beginning_list_choice + "...")
    speak(Ai_name + "を" + beginning_list_choice + "...")
    wishMe()
    while True:
        speak_pleas_list_choice = random.choice(speak_pleas_list)

        # random lists that runs with loop
        query = takeComand(speak_pleas_list_choice)
        query

        # there was a bug witch alwas said None can't be in Lower case
        if query == None:
            pass
        # comands witch is related to Buggy in my hardwer
        # 1:about buggy
        elif '終わり' in query.lower():
            print("わかりました.また使ってくださいね")
            speak("わかりました.また使ってくださいね")
            break
        elif 'あなたの名前を変え' in query.lower():
            change_Ai_name(speak_pleas_list_choice, Ai_name)
        elif 'あなたの名前は' in query.lower():

            print(f"私の名前は{Ai_name}です")
            speak(f"私の名前は{Ai_name}です")
        elif '元気ですか' in query.lower():
            i_am_fine = random.choice(['はい、元気です。', 'おかげさまで元気です',
                                       f'{MASTER}様、私わｐｃですので心配しないで', ])
            print(i_am_fine)
            speak(i_am_fine)

        elif '好きな色は' in query.lower():
            Ai_like_color = random.choice(
                ['黄色が一番好きです', '黄色です', '黄色が好きです'])
            print(Ai_like_color + '。')
            speak(Ai_like_color + '。')

        elif '歳はいくつ' in query.lower():
            Ai_age_random = random.choice(['私は19才です。', '私は今19です', ])
            print(Ai_age_random)
            speak(Ai_age_random)
        elif '何歳ですか' in query.lower():
            Ai_age_random = random.choice(['私は19才です。', '私は今19です', ])
            print(Ai_age_random)
            speak(Ai_age_random)

        elif '歳を教え' in query.lower():
            Ai_age_random = random.choice(['私は19才です。', '私は今19です', ])
            print(Ai_age_random)
            speak(Ai_age_random)

        elif '身長は何ですか' in query.lower():
            Ai_hight_random = random.choice(
                ['164センチメートルです', '私の身長は164センチメートルです'])
            print(Ai_hight_random)
            speak(Ai_hight_random)

        elif '身長は' in query.lower():
            Ai_hight_random = random.choice(
                ['164センチメートルです', '私の身長は164センチメートルです'])
            print(Ai_hight_random)
            speak(Ai_hight_random)

        # 2:telling buggy to do some thing in side this compeuter

        elif "音楽をつけ" in query.lower():
            songs_dir = "C:\\Users\\ShahZain\\Downloads\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "何"and "時" in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER}さん時間は{strTime}です.")

        elif "vscode 開いて" in query.lower():
            code_path = "C:\\Users\\ShahZain\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "ダウンロード ファイルを開いて" in query.lower():
            code_path = "C:\\Users\\ShahZain\\Downloads"
            os.startfile(code_path)

        elif "デスクトップを開いて" in query.lower():
            code_path = "C:\\Users\\ShahZain\\Desktop"
            os.startfile(code_path)

        elif "を読んで" in query.lower():
            speak("何を読んだらよいですか？下にペイストしてください。")
            print("何を読んだらよいですか？下にペイストしてください。\n")
            read = input(">>> ")
            speak(read)
            speak("役に立ててうれしいですが、次からは自分で読めるようにしておいてね!")

        # 3:telling bugy to do things out side of dhis pc.

        elif 'wikipedia で' in query.lower():
            try:
                wikipedia.set_lang("ja")
                query = query.replace("を Wikipedia で調べて", "").replace("を　Wikipedia で検索して", "").replace("を　Wikipedia で検索", "").replace("Wikipedia で調べて", "").replace("Wikipedia で検索して", "").replace("Wikipedia で検索", "").replace(
                    "を調べて", "").replace("を検索", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                print("そのページは見つかりませんでした。言葉を変えてもう一度お願いします。")
                speak("そのページは見つかりませんでした。言葉を変えてもう一度お願いします。")
            except (wikipedia.exceptions.DisambiguationError) as err:
                print("この問いに値する解答がいくつも有ります。次の問い例に合わせてもう一度やり直してください。\n", err)
                speak(f"この問いに値する解答がいくつも有ります。次の問い例に合わせてもう一度やり直してください。\n{err}")
            except wikipedia.exceptions.WikipediaException:
                print("検索して欲しいものを申してください。")
                speak("検索して欲しいものを申してください。")

        elif "youtube を開いて" in query.lower():
            url = 'http://youtube.com/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif "検索" and "youtube で" in query.lower():
            new = 4
            query = query.replace("を YouTube で検索して", "").replace('を YouTube で調べて', "").replace("を YouTube で検索", "").replace(
                "を調べて", "").replace("調べて", "").replace("を検索して", "").replace('を検索', "")
            url = 'https://www.youtube.com/results?search_query='
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url + query, new=new)

        elif "google を開いて" in query.lower():
            url = 'http://google.com/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif "検索" in query.lower():
            query = query.replace("をGoogle で検索して", "").replace("をGoogle で調べて", "").replace("Google で検索して", "").replace("Google で調べて", "").replace(
                "をGoogle で", "").replace("でGoogle を", "").replace(
                "Google で", "").replace("を検索して", "").replace("を調べて", "").replace("検索して", "").replace("調べて", "").replace("を検索", "")
            new = 2
            url = 'https://www.google.com/search?q='
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url + query, new=new)
            print(query + "を検索しました。")

        else:
            # try:
            #     wikipedia.set_lang("ja")
            #     result_ja = wikipedia.summary(query, sentences=3)

            #     print(result_ja)
            #     speak(result_ja)
            #     new = 2
            #     url = 'https://www.google.com/search?q='
            #     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            #     webbrowser.get(chrome_path).open(url + query, new=new)
            #     print(query + "を検索しました。")
            # except wikipedia.exceptions.PageError:
            #     print("そのページは見つかりませんでした。言葉を変えてもう一度お願いします。")
            #     speak("そのページは見つかりませんでした。言葉を変えてもう一度お願いします。")
            # except (wikipedia.exceptions.DisambiguationError) as err:
            #     print("この問いに値する解答がいくつも有ります。次の問い例に合わせてもう一度やり直してください。\n", err)
            #     speak(f"この問いに値する解答がいくつも有ります。次の問い例に合わせてもう一度やり直してください。\n{err}")
            try:
                wikipedia_search(query)
            except wikipedia.exceptions.PageError:
                print("そのページは見つかりませんでした。言葉を変えてもう一度お願いします。")
                speak("そのページは見つかりませんでした。言葉を変えてもう一度お願いします。")
            except (wikipedia.exceptions.DisambiguationError) as err:
                print("この問いに値する解答がいくつも有ります。次の問い例に合わせてもう一度やり直してください。\n", err)
                speak(f"この問いに値する解答がいくつも有ります。次の問い例に合わせてもう一度やり直してください。\n{err}")


if __name__ == "__main__":
    main(Ai_name)
