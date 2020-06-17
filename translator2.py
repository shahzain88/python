from translate import Translator
import pdb


def my_setup_for_translation(lang, what_to_translate):
    translator = Translator(to_lang=str(lang))
    translation = translator.translate(what_to_translate)
    return translation


try:
    lang = str(
        input("Chouse lang that you want to translate to in two latters only : "))

    if len(lang) == 2:
        with open("en_file_introdeuce.txt", mode="r") as my_file:
            pdb.set_trace()
            text = my_file.read()
            text = my_setup_for_translation(lang, text)

            print(text)
            with open("ja_file_introdeuce.txt", mode="w") as my_file2:
                my_file2.write(text)

    else:
        print("I said TWO-LATTERS !")
except FileNotFoundError as err:
    print(f"File Not found \n {err}")
