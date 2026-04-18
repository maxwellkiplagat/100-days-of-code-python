import random
import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random_chosen_password = []

print('welcome to the pyPassword Generator!')

nr_letters = int(input('How many letters would you like in your password?\n'))
random_letters = random.sample(letters,nr_letters)
random_chosen_password.append(random_letters)

nr_symbol = int(input(f'How many symbols would you like?\n'))
random_symbol = random.sample(symbols,nr_symbol)
random_chosen_password.append(random_symbol)



nr_number = int(input(f'How many numbers would you like?\n'))
random_number = random.sample(numbers,nr_number)
random_chosen_password.append(random_number)




flat = list(itertools.chain.from_iterable(random_chosen_password))
random.shuffle(flat)

nal = ''.join(flat)

print(nal)



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
print(final_password)