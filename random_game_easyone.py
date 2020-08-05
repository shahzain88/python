from random import randint
start = 1
stop = 10


def guess_pram(user_num, random_num):
    if 0 < user_num < 11:
        if user_num == random_num:
            print("great work!")
            return True
    else:
        print('i saide 1-10')
        return False


if __name__ == "__main__":
    random_num = randint(start, stop)
    while True:
        try:
            user_num = int(input("guss a num 1 to 10 >>>"))
            if (guess_pram(user_num, random_num)):
                break
        except ValueError:
            print("enter a number")
            continue
