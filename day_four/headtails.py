import random
headtails = [0,1]
#random.randint returns float between 0.0 and 1.0(inclusive)
probability =random.randint(0,1)
if probability == 0:
    print('Tails')
else:
    print('Heads')