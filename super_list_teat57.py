

# to have functionality of list ,need to inherate List into SuperList
class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()

print(super_list1.append(6))
print(super_list1[0])
