import random
import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



#option 2
import random
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbol = int(input(f'How many symbols would you like?\n'))
nr_number = int(input(f'How many numbers would you like?\n'))

password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbol):
    password += random.choice(symbols)
for char in range(0, nr_number):
    password += random.choice(numbers)

finall_ans = list(password)
random.shuffle(finall_ans)
final_password = ''.join(finall_ans)
print(f'Your password is: {final_password}')