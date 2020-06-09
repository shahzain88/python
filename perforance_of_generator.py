from time import time


def performance(fu):
    def wrepper(*aregs, **kwaregs):
        t1 = time()
        result = fu(*aregs, **kwaregs)
        t2 = time()
        print(f'It took {t2 - t1}s to run it.')
        return result
    return wrepper


@performance
def long_function_1():
    print("1")
    for i in range(1000000):
        i*5


@performance
def long_function_2():
    print('2')
    for i in list(range(1000000)):
        i*5


long_function_1()
long_function_2()
