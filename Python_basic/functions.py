# DRY do not repeat yourself (make code reuseable)

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# def show_picture():
#   for row in picture:
#     for pixel in row:
#       if (pixel == 1):
#         print('*', end="")
#       else:
#         print(' ', end="")
#     print("") # need a new line after each row

# show_picture()

# print(f'{show_picture} <- this location')

# arguments are used when we call the function
# parameters are used when we define the function
# call the function == invoke the function

# (***** arguments and parameters *****)

# # parameters
# def say_hello(name, emoji):
#   print(f'hello {name} {emoji}')

# positionals arguments
# say_hello('piyush', '''> <''')

# program ------------>

# def function(a):
#   c = a ** 2

#   print(f'square of {a} is {c}')
# a = int(input('Enter a number for square: '))
# function(a)

# example find square at 5 times --->
# for i in range(0, 5):
#     a = int(input('Enter a number for square: '))
#     function(a)

# keyword arguments --->

# def new_function(name, age):
#   print(f'Your name is {name} and you\'r {age} year\'s old \n')

# new_function(name='piyush', age='22')
# new_function(age='25', name='user1')

# default parameters ----------------->
# def default(name='test', height='6'):
#   print(f'Your name is {name} and you\'r {height} feet tall \n')

# default('piyush', '5\'9\"')
# default()

