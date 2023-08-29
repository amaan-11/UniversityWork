import random
number=random.randrange(0,10)
guess=-1
while guess!=number:
    guess=int(input("Enter your guess"))
    if guess==number:
        print("You are correct!!!!!!!!!")
    if guess>number:
        print("Too high")
    if guess<number:
        print("Too low")