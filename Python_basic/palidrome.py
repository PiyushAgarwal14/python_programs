a = str(input("Enter a number: "))
a[::-1]

if a == a[::-1]:
  print('palindrome')
else:
  print('not palindrome')
