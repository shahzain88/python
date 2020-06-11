from random import randint
from sys import argv


# if argv[1] != None or argv[2] != None:
try:
    start = int(argv[1])
    stop = int(argv[2])
    random_num = randint(start, stop)

    while True:
        try:
            user_num = int(
                input("which number do you think will be the same? =>"))
            if user_num == random_num:
                print(f" great work! {random_num} is right answer ")
                break
            elif user_num > stop:
                print("The number is bigger from the number which was given")

            elif user_num < start:
                print("The number is smaller from the number which was given")
            elif user_num != random_num:
                print("Try again :(")
        except ValueError:
            print("enter a number!")
        except ZeroDivisionError:
            print("The number is higher or lower from the number which was given")
# else:
#     raise ValueError("entre two numbers in terminal")
except IndexError:
    print("entre two numbers in terminal")
