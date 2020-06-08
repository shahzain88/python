# to make Generators you need to use range and yield
def generatore_function(num):
    for i in range(num):
        # whit yield you can stop functions and run them one by one
        yield i


g = generatore_function(100)
next(g)
next(g)
print(
    f'with next you can stop functions\n It is saveinge one data only  \n{next(g)} \n')

# it takes one data then let the yield move to next one .
for item in generatore_function(100):
    print(item)
