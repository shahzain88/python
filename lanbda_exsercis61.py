# make a lambda expression which square's a list

my_list = [5, 4, 3]

# print(list(map(lambda item: item**2, my_list)))

# sort the list

a = [(0, 2, 3), (4, 3, 9), (9, 9, -1), (10, -1, 2)]
#sort will modifiy the original data
#sort has the key and value ,in this list ther is only key
#The x[2] will be the key
a.sort(key=lambda x: x[2])

print(a)
