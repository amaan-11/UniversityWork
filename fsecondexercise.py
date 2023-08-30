import random
def diceroll(sides):
    roll=random.randrange(1,sides+1)
    return roll
rolled=0
sides=int(input("Enter the number of sides of the dice,"))
while rolled!=sides:
    rolled=diceroll(sides)
    print(rolled)