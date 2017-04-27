import random

def dice():
    return random.randint(1, 6)

def get_eight():
    counter = 0
    while True:
        dice1 = dice()
        dice2 = dice()
        counter += 1
        if dice1 + dice2 == 8:
            print(dice1, dice2, counter)
            break

for dummy_i in range(10):
    get_eight()