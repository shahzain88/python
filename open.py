
my_file = open("1.txt")

print(my_file.read())
# it takes the casel to the top(0)
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
print("oppopppopopopop\n.", my_file.readline())
# should Seek(0) if you wanted to print all...
print(my_file.readlines())

# finally you should close the file ,to use it somewhere else.
my_file.close()
