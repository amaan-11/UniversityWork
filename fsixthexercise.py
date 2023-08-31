import math
def ppsqm(diameter,price):
    area=math.pi*(diameter/2)**2
    ppsqm=price/area
    return ppsqm
diam_1=float(input("Enter the diameter of the first pizza,"))
diam_2=float(input("Enter the diameter of other pizza,"))
pizz_1=float(input("Enter the price of the first pizza,"))
pizz_2=float(input("Enter the price of the other pizza,"))
ppsqm_1=ppsqm(diam_1,pizz_1)
ppsqm_2=ppsqm(diam_2,pizz_2)
if ppsqm_1<ppsqm_2:
    print("The first pizza has better unit price")
elif ppsqm_1>ppsqm_2:
    print("The other pizza has better unit price")
