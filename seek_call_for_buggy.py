from app_jp_buggy import main, Ai_name, speak, sr


def hearing_for_name():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ja-ja')
    except Exception:
        query = None
    return query


def basecamp():
    speak("いつでも読んでください。")
    while True:
        query = hearing_for_name()

        if query == None:
            continue
        elif "バギー" in query.lower():
            speak("はーい。")
            main(Ai_name)
            continue
        elif "終わり" in query.lower():
            speak("バギーをシャットダウンしています。")
            break
        else:
            continue


if __name__ == "__main__":
    basecamp()
