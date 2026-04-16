print('welcome to Treasure Island Your Mission is to find the tresure.')
choice_one = input('Left or right: ').strip().upper()


if choice_one == 'RIGHT':
    print('Game Over')
    exit()
choice_two = input('swim or wait: ').strip().upper()
if choice_two == 'SWIM':
    print('Game Over')
    exit()
choice_three = input('red or blue or yellow: ').strip().upper()    
if choice_three == 'YELLOW':
    print('You Win')
    exit()
elif choice_three == 'RED' or choice_three == 'BLUE':
    print('Game Over')
    exit()
else:
    print('invalid choice')
        

     