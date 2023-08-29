num=int(input("Enter a number"))
if num==1:
    print("It is 1 which is neither prime nor composite.")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            check=True
            break
        else:
            check=False
    if check == True:
        print("Its a composite number")
    else:
        print("Its a prime number")
else:
    print("Negative numbers cant be prime numbers")