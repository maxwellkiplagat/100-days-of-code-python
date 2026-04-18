print('welcome to python pizza deliveries!')
size = input('what size pizza do you want? S, M or L: ')
pepperoni = input('Do you want pepperoni on  your pizza? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

if (size == 'S' or size == 's'):
    bill = 15
elif (size == 'M' or size == 'm'):
    bill = 20
elif (size == 'L' or size == 'l'):
    bill = 25
else:
    print('Invalid size! Please choose S, M or L. ')
    exit()
if (pepperoni == 'Y' or pepperoni == 'y'):
    if (size == 'S' or size == 's'):
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 1    
print(f'your total bill is ${bill}')   
    