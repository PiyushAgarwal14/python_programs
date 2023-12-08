username = str('piyush')
password = str('123')
age = int('22')

name = str(input("Enter your username: \n"))
code = str(input("Enter your password: \n"))

print("\n")

if name == username and code == password:
  print(
      f"Hello {username} '\n' Welcome on our platform \n  You\'r   {str(age)} year old"
  )

else:
  print("Usernam and Password is wrong")

# username = str('piyush')
# password = str('123')
# age = int('22')

# name = str(input("Enter your username: \n"))
# code = str(input("Enter your password: \n"))

# print("\n")

# if name == username and code == password:
#   print(f"Hello {username} '\n'Welcome on our platform \n You\'r {str(age)} year old")

# elif name != username and code != password:
#   print("Username and Password are not correct")

# elif name != username:
#   print('username is incorrect !')

# elif code != password:
#   print("password is incorrect !")
