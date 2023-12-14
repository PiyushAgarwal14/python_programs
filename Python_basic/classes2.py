#  Encapsulation
# class PlayerCharacter:
  
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

#   def speak(self):
#     print(f'My name is {self.name} and I\'m {self.age} years old')


# player1 = PlayerCharacter('piyush', 22)
# player1.speak()



# Abstraction ---------->


# class PlayerCharacter:
#   def __init__(self, name, age):
#       self._name = name
#       self._age = age

#   def speak(self):
#     print(f'My name is {self._name} and I\'m {self._age} years old')

# player1 = PlayerCharacter('piyush', 22)
# player1.name = '!!!'
# player1.speak = 'helllo'
# print(player1.speak)


# Inheritance ------------>

# class User(object):
#   def sign_in(self):
#     print("logged in")

# class Wizard(User):
#   def __init__(self, name, power):
#     self.name = name
#     self.power = power

#   def attack(self):
#     print(f'attacking with power of {self.power}')

# class Archer(User):
#   def __init__(self, name, num_arrows):
#     self.name = name
#     self.num_arrows = num_arrows

#   def attack(self):
#     print(f'attacking with arrows: arrows left:- {self.num_arrows}')
    
# wizard1 = Wizard('witch1', 50)
# archer1 = Archer('Robin', 80)

# # wizard1.attack()
# # archer1.attack()

# print(isinstance(wizard1, object))

# Polymorphism ----------->


class User(object):
  def sign_in(self):
    print("logged in")

  def attack(self):
    print('do nothing')   # this will override in sub classes

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    User.attack(self)
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left:- {self.num_arrows}')

wizard1 = Wizard('witch1', 70)
archer1 = Archer('Robin', 50)

# def player_attack(char):
#   char.attack()
# player_attack(wizard1)
# player_attack(archer1)

for char in [wizard1, archer1]:
  char.attack()