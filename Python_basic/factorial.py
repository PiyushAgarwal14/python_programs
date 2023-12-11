def factorial(num):
  res = 1
  for i in range(2, num + 1):
    res *= i
  return res


num = int(input('Enter an integer number for factorial: \n'))
print(f'factorial of {num} is {factorial(num)}')
