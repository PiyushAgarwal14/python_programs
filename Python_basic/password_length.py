user_name = str(input('Enter your username \n'))
password = str(input('Enter your password \n'))

password_length = len(password)
hidden_password = '*' * password_length

print(f'Your password {hidden_password} is {password_length} letters long')
