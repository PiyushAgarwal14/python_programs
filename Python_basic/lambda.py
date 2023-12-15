# lambda with map
my_list = [2,4,6]
print(list(map(lambda item: item*2, my_list)))


# lambda with filter
odd = [2,4,6,7]
print(list(filter(lambda item: item%2 != 0, odd)))


# lambda with reduce
from functools import reduce
red = [1,2,3]
print(reduce(lambda acc, item: acc+item, red))