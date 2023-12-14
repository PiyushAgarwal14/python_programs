flag = 0
n = int(input('Enter a prime number: \n'))

if n > 1:
    for i in range(0,n):
        if (n % 2==0):
            flag = True
            break
if flag:
    print(f"{n} is not a prime number")
else:
    print(f'{n} is prime number')