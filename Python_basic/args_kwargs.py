# *args **kwargs

# def super_func(*args):
#   return sum(args)

# print(super_func(1,2,3,4,5))

# def func(*args, **kwargs):
#   total = 0
#   for i in kwargs.values():
#     total += i
#   return sum(args) + total
# print(func(1,2,3,4,5, num1=5, num2=10))

# def function(*args, **kwargs):
#   print(kwargs, args)
# print(function(1,2,3,4,5, num1 = 10, num2 = 30))

# Rule: -->>> parameters, *args, default parameters, **kwargs


# def func(name, *args, i='hi', **kwargs):
#   print(name, i)
#   total = 0
#   for i in kwargs.values():
#     total += i
#   return sum(args) + total


# print(func('piyush', 1, 2, 3, 4, 5, num1=5, num2=10))





# method 1

# def highest_even(*args):
#   # print(args)
#   highest = 0
#   for i in args:
#     if ((i % 2) == 0) and i > highest:
#       highest = i
#   return highest

# print(highest_even(10,2,3,4,8,11))


# method 2

# def highest_even(li):
#   highest = []
#   for i in li:
#     if ((i % 2) == 0):
#       highest.append(i)
#   return max(highest)
# print(highest_even([10,2,3,4,8,11]))
