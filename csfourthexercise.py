year=int(input("Enter a year,"))
if year%4==0:
    if year%100==0:
        if year%400:
            print("The year "+str(year)+" is a leap year")
    else:
        print("The year "+str(year)+" is a leap year")