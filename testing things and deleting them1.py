import datetime

today_year = datetime.date.today().year
while True:
    try:
        user_bearth_year = int(input('what year were you born? '))
        user_age = int(today_year - user_bearth_year)
    except:
        print('oopss,some thing whent worng')
    else:
        print(user_age)
