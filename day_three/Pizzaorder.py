print('welcome to python pizza deliveries!')
size = input('what size pizza do you want? S, M or L: ')
pepperoni = input('Do you want pepperoni on  your pizza? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

if (size == 'S' or size == 's'):
    bill = 15
elif (size == 'M' or size == 'm'):
    bill = 20
else:
    bill = 25
if (pepperoni == 'Y' or pepperoni == 'y'):
    bill += 2

if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1    
print(f'your total bill is ${bill}')   
    