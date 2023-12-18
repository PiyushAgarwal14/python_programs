# def my_decorator(func):
  
#   def wrap_func():
#     print('*******')
#     func()
#     print('*******')
#   return wrap_func

# def hii():
#   print('hiiiiii')

# def bye():
#   print('see ya letter')
  
# hello2 = my_decorator(hii)
# hello2()


# def my_decorator(func):

#   def wrap_func(x):
#     print('******')
#     func(x)
#     print('******')
  
#   return wrap_func

# @my_decorator 
# def hello(greeting):
#   print(greeting)

# hello('hiii')





# def my_function(func):

#     def wrap_func(x):
#         print('********')
#         func(x)
#         print('********')
#     return wrap_func

# @my_function
# def testing(hii):
#     print(hii)
# testing('by!!!!!!')



# def my_function(func):

#     def wrap_func(x, y):
#         print('********')
#         func(x, y)
#         print('********')
#     return wrap_func

# @my_function
# def testing(hii, emoji):
#     print(hii, emoji)
# testing('by!!!!!!', ':)')


# def my_function(func):

#     def wrap_func(*args, **kwargs):
#         print('********')
#         func(*args, **kwargs)
#         print('********')
#     return wrap_func

# @my_function
# def testing(hii, emoji=':('):
#     print(hii, emoji)
# testing('by!!!!!!')


from time import time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    
    result =  fn(*args, **kwargs):
    
    t2 =  time()
    print(f'took {t2-t1} s')
    return result
  return wrapper

@performance

def long_time():
  for i in range(100000000):
    i*5
long_time()





# def hi():
#   print('hiiiiiii')

# greet = hi
# del hi
# greet()

# def hello(func):
#   func()

# def greet():
#   print('still here.....')

# a = hello(greet)
# a

