import random
def diceroll():
    roll=random.randrange(1,7)
    return roll
rolled=0
while rolled!=6:
    rolled=diceroll()
    print(rolled)