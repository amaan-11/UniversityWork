import random
threedigitcode=0
fourdigitcode=0
for i in range(3):
    digit=random.randrange(0,9)
    threedigitcode=threedigitcode+digit
for i in range(4):
    digit=random.randrange(1,6)
    fourdigitcode=fourdigitcode+digit
print("The three digit code=",threedigitcode)
print("The four digit code=",fourdigitcode)