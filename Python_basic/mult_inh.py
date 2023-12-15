# Multiple Inheritance

class User(object):

  def sign_in(self):
    print("logged in")

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def powers(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def check_arrows(self):
    print(f'Checking arrows: arrows left:- {self.num_arrows}')

  def run(self):
    print('ran very fast')

class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, num_arrows):
    Archer.__init__(self, name, num_arrows)
    Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 75)
hb1.sign_in()
hb1.powers()
hb1.check_arrows()