import random

# Lists of characters to choose from
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()_+-='

# Taking user input
char_in_password = int(input('How many alphabets do you want in your password? '))
number_in_password = int(input('How many numbers do you want in your password? '))
special_char = int(input('How many special characters do you want in your password? '))

# Creating the password list
password_list = []

# Adding random alphabets
for _ in range(char_in_password):
    password_list.append(random.choice(alphabets))

# Adding random numbers
for _ in range(number_in_password):
    password_list.append(random.choice(numbers))

# Adding random special characters
for _ in range(special_char):
    password_list.append(random.choice(special_characters))

# Shuffling the list to ensure randomness
random.shuffle(password_list)

# Joining the list to form the final password
password = ''.join(password_list)

print(f'Your password is: {password}')
