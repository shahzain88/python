# When you wannt to use thr reduce function noly onse

from functools import reduce
my_list = [1, 2, 3]

# reduce workes withe two argumants acc(0),and item(from my_list)
# defolt acc is  0
# lambda prameters : action up on pramiter
print(reduce(lambda acc, item: acc + item, my_list, 0))
