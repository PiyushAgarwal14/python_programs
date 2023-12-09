# print("hello")

# name = input("Enter your name?")
# print('hello ' + name)

# num1 =  int(input('Enter a integer'))
# print(num1)

# num2 = float(input('Enter a float'))
# print(num2)

# num3 = str(input('Enter a string'))
# print (num3)

# ********************************************

# fundamental datatypes
# int
# float
# bool
# str
# list
# tuple
# dict
# set
# complex

# ************************************************
# print("Addition")
# print (2 + 4)

# print("Subtraction")
# print(2-4)

# print("Multiply")
# print(2 * 3)

# print("Dividend")
# print(2 / 4)

# square root
# print( 2 ** 2)

# mod
# print (12 % 2)

# type
# print (type(2 + 5))
# print (type(2 * 3.2))
# print(type('piyush'))

# print(10 / 3)
# print (10 // 3)

# **round of**
# print(round(3.1))

# square root
# print(pow(4, 2))

# print(round(3.8))

# absolute value of argument
# print(abs(-5))

# *** operator precedence ***
# print(12 + 6 * 3)

# print((12*12) - 4 ** 2)
# ()
# **
#  * /
#  + -
#  BODMAS bracket, exponent, multiply, divide, add, subtract

# print(bin(6))
# print(hex(17))

# print(int('0b110', 2))

# (*** 08/12/2023 ****)

# print(2**3)
# print(pow(2, 3))

# (**** variables are snake_case (no space) *****)
# (*** variables start with lower case or underscore  ***)
# (*** variables are case sensitive ***))
# (*** variables can be letter, numbers, underscores)
# (*** Dont overwrite keywords ***)

# user = 10
# print(user)

# user_1 = 11
# print(user_1)

# _user_1 = 12
# print(_user_1)

# Piyush = 55
# print(Piyush)

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# print(a,b,c)

# (**** augmented assignment operators ****)

# some_value = 5
# print(some_value)

# some_value = 5+2
# print(some_value)

# some_value = some_value + 3
# print(some_value)

# some_value += 4
# print(some_value)

# some_value -= 6
# print(some_value)

# some_value *= 2
# print(some_value)

# some_value /= 2
# print(some_value)

# some_value //=2
# print(some_value)

# some_value %= 2
# print(some_value)

# some_value **= 2
# print(some_value)

# print(type("hello world, this is a string"))

# long_string = '''
#   Amazing

#   ^ ^
#    -
#  cool

#  # #
#  ---
# '''
# print(long_string)

# first_name = 'Piyush'
# last_name = 'Agarwal'
# full_name = first_name + ' ' + last_name
# print(full_name)

# String concationation
# print('Piyush ' + 'Agarwal')

# print(str(55))
# print(type(str(55)))

# print(type(int(str(100))))

# a = str(55)
# b = int(a)
# c = type(b)
# print(c)

# a = 'hello'
# b = 'HELLO'
# b = b.lower()

## print(b)

# if a == b:
#   print('true')
# else:
#   print('false')

# esacpe sequence

# weather = "It\'s \"cold\" nignt"
# print(weather)

# weather = "It\\s \"cold\" nignt"
# print(weather)

# weather = "\t It\'s \"cold\" nignt \n hope you have a good day"
# print(weather)

# name = str('Piyush')
# age = int(22)
# print('Welcome ' + name + '. You are ' + str(age) + ' year old')

# formatted string
# print(f'Welcome {name} You are {age} years old')

# selfish = 'me me me'
# #          01234567
# print(selfish[7])

# arr = '01234567'
# # # [start:stop:stepover]
#  print(arr[0:8:2])

# print(arr[::-1])

# a = 'reviver'
# a[::-1]

# if a == a[::-1]:
#   print('palindrome')
# else:
#   print('not palindrome')

# arr = '1234567'
# print(len(arr))

# word = 'hello my name is'
# print(word.upper())
# print(word.capitalize())
# print(word.lower())

# print(word.find('is'))
# print(word.replace('my' , 'Piyush'))
# (*** strings are immutable ***)

# (****** 09/12/2023) ******)

# booleans

# name = 'piyush'
# is_cool = False
# is_cool = True
# print(bool('true'))

# birth_year = int(input('In which year you were born \n'))
# age = 2023 - birth_year
# print(f'Your age is {age}')

# user_name = str(input('Enter your username \n'))
# password = str(input('Enter your password \n'))

# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'Your password {hidden_password} is {password_length} letters long')

# list
# list slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart)
# print(amazon_cart[0::2])

# amazon_cart[0] = 'laptop'
# print(amazon_cart)

#  *** list is mutable ***

# new_cart = amazon_cart[:]
# new_cart[0] = 'tshirt'
# print(new_cart)
# print(amazon_cart)

# **** Matrix ****

# list = [
#   [1,2,5],
#   [2,4,6],
#   [7,8,9]
# ]

# print(list[0] [2])

# append

# basket = [1, 2, 3, 4, 5]
# print(len(basket))
# print(basket)

# new_basket = basket.append(100)
# print(new_basket)

# basket.append(100)
# new_basket = basket
# print(basket)
# print(new_basket)

# basket.insert(4,100)
# new_basket = basket
# print(basket)
# print(new_basket)

# basket.extend([100])
# print(basket)

# // pop

# basket.pop()
# basket.pop()
# basket.pop(0)

# // remove
# basket.remove(3)
# print(basket)

# new_basket = basket.pop(4)
# print(new_basket)

# basket.clear()
# print(basket)

# bucket = ['a', 'b', 'c', 'd', 'e', 'c']
# print(bucket.index('e'))
# print(bucket.index('b',0,2))

# print('d' in bucket)
# print('h' in bucket)

# print('i' in 'My name is Piyush')

# print(bucket.count('c'))

# bucket = ['a', 'b', 'c', 'e', 'd', 'e', 'c']
# bucket.sort()
# print(bucket)
# print(sorted(bucket))  #create new array -  method 1
# print(bucket)

# new_bucket = bucket[:] # method
# new_bucket.sort()      # 2
# print(new_bucket)
# print(bucket)

# new_bucket = bucket.copy() # method 3
# new_bucket.sort()
# print(new_bucket)
# print(bucket)

# *** sort aand reverse  ***
# bucket = ['a', 'b', 'c', 'e', 'd', 'e', 'c']
# bucket.sort()
# bucket.reverse()
# # print(bucket)
# print(bucket[::-1])
# print(bucket)

# //range

# print(list(range(101)))

# sentence = ' '
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'piyush'])
# print(new_sentence)

# word2 = ' '.join(['hello', 'hi', 'by', 'by'])
# print(word2)

# ( *** list unpacking ***)

# a, b, c, *others, p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(b)
# print(c)
# print(others)
# print(p)

# weapons = None
# print(weapons)

# Dictionary

# dictionary = {
#   'a' : ['1', '2', '3'],
#   'b' : 'hello',
#   'c' : True
# }

# print(dictionary['a'])
# print(dictionary)

# my_list = [
#   {
#     'a' : [4,5,6],
#     'b' : 'hello',
#     'x' : False
#   },

#   {
#     'a' : [7,8,9],
#     'b' : 'hello',
#     'v' : True
#   }
# ]
# print(my_list[0] ['a'] [2])
# print(my_list[1] ['b'])

# library = {
#   'basket' : [1,2,3],
#   'greet' : 'hello',
#   'age': 22
# }
# print(library.get('age', 25))

# user2 = dict(name='piyush')
# print(user2)

task = {'a': [1, 2, 3], 'b': 'hii', 'u': 26}

# print( 'a' in task)
# print('a' in task.keys())
# print(26 in task.values())

# print(task.items())
# task.clear()
# print(task)

# task2 = task.copy()
# print(task.clear())
# print(task2)

# print(task.pop('u'))
# print(task)

# print(task.popitem())

# print(task.update({'u' : '22'}))
# print(task)

# print(task.update({'age' : 20}))
# print(task)
