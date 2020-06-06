from time import time


def performance(fn):
    def wrapper(*args, **kwargs):

        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


@performance
def longe_time():
    for i in range(100000000):
        i*5


longe_time()

print('hellooo')
