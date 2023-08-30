gall=0
def convgalltoltrs(amg):
    ltrs=amg*3.785
    return ltrs
while gall>=0:
    gall=float(input("Enter the volume in american gallons to convert it to,"))
    if gall<0:
        break
    final_val = convgalltoltrs(gall)
    print("The number in liters =", final_val)