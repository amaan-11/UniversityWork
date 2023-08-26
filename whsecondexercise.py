choice=0
while choice>=0:
    choice=int(input("Enter a number to convert to centimeters,"))
    if choice<0:
        print("Error number entered is negative")
        break
    centi=choice*2.54
    print("The number after conversion is "+str(centi)+"cms")