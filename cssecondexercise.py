while True:
    c_class=input("Enter your class(In capital letters),")
    classes=["LUX","A","B","C"]
    if c_class not in classes:
        print("Invalid cabin class")
        continue
    if c_class == "LUX":
        print("You have chosen an upper-deck cabin with a balcony")
    if c_class == "A":
        print("You have chosen an above the car deck, equipped with a window")
    if c_class == "B":
        print("You have chosen a windowless cabin above the car deck")
    if c_class == "C":
        print("You have chosen a windowless cabin below the car deck")