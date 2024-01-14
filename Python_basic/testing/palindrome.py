n = str(input("Enter a palindrome number: \n"))
j = n[::-1]

if (n == j):
    print("palindrome")
else:
    print("not palindrome")
