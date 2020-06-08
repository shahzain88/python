while True:
    try:
        age = int(input('what is your age? '))
        10 / age
        raise KeyError('what are you doing <cut it out>')
    except ZeroDivisionError:
        print("Hello buggy dont divide by 0!")
    else:
        print("thank you!")
    finally:
        print("this is fial prossec")
