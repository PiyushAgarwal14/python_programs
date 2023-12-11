num = int(input('Enter a number: \n'))

num_str = str(num)
l = len(num_str)

sum = 0
for i in num_str:
  sum = sum + int(i)**l
if sum == num:
  print(f'{num} is armstrong number')

else:
  print(f'{num} is not armstrong number')
