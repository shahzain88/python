def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp_a = a
        a = b
        b = temp_a + b
    print(f"These are F0 to F{i}")


for x in fib(21):
    print(x)
