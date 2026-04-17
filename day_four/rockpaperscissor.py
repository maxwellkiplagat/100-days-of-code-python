import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.    '))
if choice == 0:
    print(rock)
if choice == 1:
    print(paper)
if choice == 2:
    print(scissors)

print('computer chose')
computer = random.randint(0,2)
if computer == 0:
    print(rock)
if computer == 1:
    print(paper)
if computer == 2:
    print(scissors)

if choice == computer:
    print('you draw')
elif choice == 0 and  computer == 1:
    print('computer wins')
elif choice == 1 and computer == 0:
    print('you win')
elif choice == 0 and  computer == 2:
    print('you win')
elif choice == 2 and computer == 0:
    print('computer wins') 
elif choice == 1 and computer == 2:
    print('computer wins')
else:
    print('you win')
