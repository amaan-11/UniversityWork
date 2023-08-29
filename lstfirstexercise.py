import random
num_rolls=int(input("Enter the number of times you want to roll the dice,"))
print("rolls are as follows :")
for i in range(num_rolls):
    roll_result=random.randrange(1,6)
    print(roll_result)