from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
  print(acc, item)
  return acc + item
  
#       acc   my_list   
#        0      1
#        1      2
#        3      3
#        6

print(reduce(accumulator, my_list, 0))