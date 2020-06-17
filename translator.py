from translate import Translator


def setup_translator(ask_lang="ja", to_translate="enter something here to translate"):
    translator = Translator(to_lang=str(ask_lang))
    translation = translator.translate(to_translate)
    return print(translation)


try:
    while True:
        lang = input('witch langweg do you want to translate in two worlds : ')
        if len(lang) > 2:
            print("only to latters!!")
        else:
            print(f"Thank you! lang = {lang}")
            break
    file_path = f"en_file_to_{lang}.txt"\

    with open("en_file_intro.txt", mode="r") as en_file_introduce:
        en_file_read = en_file_introduce.read()
        setup_translator(lang, en_file_read)
    with open(file_path, mode="w") as my_file2:
        my_file2.write(en_file_read)
except FileNotFoundError:
    print("file dose not found")
