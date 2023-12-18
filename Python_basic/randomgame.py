import random

ran_num = (random.randint(1, 10))

while True:
  try:
    num = int(input('Enter a number between 1 to 10: \n'))
  except ValueError:
    print('please enter a number')
    continue
  if num == ran_num:
    print("You guess the right number and You are a Genius !!")
    break
  else:
    num = int(input('Enter a number between 1 to 10: \n'))