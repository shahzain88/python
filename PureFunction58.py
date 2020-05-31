# TO make pure function ...
# Rule is function should return same amswer
# and Producess no side effects like give the error

# point one put the vareable in side the function and make it un acces able from out side.

# Bad ex
#
# new_list = [] like thes every one can change IT.


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
# point two don't print some thing from function
# Bad ex
#   return print(new_list)


print(multiply_by2([1, 2, 3]))
