my_list1 = [char for char in 'hello']
my_list2 = [char for char in range(0, 100)]
my_list3 = [char*2 for char in range(0, 100)]
my_list4 = [char**2 for char in range(0, 100) if char % 2 == 0]
#           1    2                3                4
# 1___is puting the data in the list
# 2___is the place where you can change the shape of the value
# 3___is itrable . you should put a data to worke on
# 4___is the conditional staytment with it you can give it a condition if ture put the value in the list
print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
