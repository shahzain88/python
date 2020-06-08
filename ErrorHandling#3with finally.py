num = 1
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except (ValueError, KeyError) as err:
        print(f'pleas enter a number\n{err}')
        continue
    except ZeroDivisionError as err:
        print(f'ENter an age higher then 0\n{err}')
        break
    else:
        print('Thank you!')
        break
    finally:
        print('final thing to do like num +1')
        num = num + 1
        print(f'you can mistake {5 - num} time.')
        if num > 4:
            print("you misstaked a lot try again :\\")
            break
    print('can you hear me?')
