# class PlayerCharacter:

#   membership = True

#   def __init__(self, name, age):
#     if (self.membership):
#       self.name = name
#       self.age = age

#   def shout(self):
#     print(f'my name is {self.name}')
  
#   def run(self, hello):
#     print('run')
#     return 'final'


# player1 = PlayerCharacter('Piyush', 22)
# player2 = PlayerCharacter('Bot', 20)

# print(player1.shout())
# print(player1.name)

# print(f'Player 1 : {player1.name}, age: {player1.age} \n')
# print(f'Player 2 : {player2.name}, age: {player2.age}  \n')


class PlayerCharacter:
  membership = True
  def __init__(self, name, age):
    if (self.membership):
      self.name = name
      self.age = age

  def shout(self):
    print(f'my name is {self.name}')

  @classmethod
  def adding_numbers(cls, num1, num2):
    return cls('teddy',num1 + num2)

  # player1 = PlayerCharacter('Piyush', 22)
  
  @staticmethod
  def adding_numbers2(num1, num2):
    return num1 + num2
  

player3 = PlayerCharacter.adding_numbers(2,3)
print(player3.name, player3.age)

player4 = PlayerCharacter.adding_numbers(5,3)
print(player4.age)  