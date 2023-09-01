name=0
lst=set()
while name!="":
    name=input("Enter a name,")
    if name in lst:
        print("Existing name")
    elif name=="":
        break
    else:
        lst.add(name)
        print("New name")
for i in lst:
    print(i)
