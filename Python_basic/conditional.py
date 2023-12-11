# is_old = True

# is_licenced = True

# if is_old and is_licenced:
#   print('You are old enough to drive, and you have a licence')

# else:
#   print('You are not of age')

# print('ok ok ok')

is_old = bool('hello')
is_licenced = bool(5)

# print(bool('hello'))    # Truthy
# print(bool(5))          # Truthy

# print(bool(''))    # falsy
# print(bool(0))     # falsy

# if is_old and is_licenced:
#   print('You are old enough to drive, and you have a licence')
# else:
#   print('You are not of age')
#   print('ok ok ok')

# Ternary Operator

# is_friend = True
# can_message = 'message allowed' if is_friend else 'not allowed to message'
# print(can_message)

is_Friend = True
is_User = True

if is_Friend or is_User:
  print('best friends forever')
