from functools import reduce
my_list = [1, 2, 3]
# even if this is tupple it will give you answer
your_list = [10, 20, 30]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    # Becouse of '!='  python comepares right side and left side  if item % 2 id not = to 0 python will return Ture.
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# map,filter,zip DOSE NOT modify the original data (list) ,BUT it makes NEW DATA (list) ,
# list will turn the result of that location to a list shape .
print(list(map(multiply_by2, my_list)))
# Filter workes with boolian (True and False) , if (onlly_odd,my_list ) True put it in the same location  as a result, if not then pop it out from thr location .
print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list)))
# we dont need to chang the data to list .
print(reduce(accumulator, my_list, 0))
