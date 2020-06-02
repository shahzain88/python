
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5


}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}
How_my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
print(How_my_dict)
