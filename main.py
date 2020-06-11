from utility import *
from shopping.more_shopping import shopping_cart as shop

shop.buy("plam")
print(shop.buy("hours"))
print(multiply(3, 4))
print(divide(3, 4))
# This will give you error , cause of utility.max() improted
# print(max([1,2,3]))