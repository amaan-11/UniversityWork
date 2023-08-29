nums=[]
ploop=True
while ploop==True:
    number=input("Enter a number,")
    if number=="":
        break
    nums.append(int(number))
nums.sort(reverse=True)
a=0
for i in nums:
    print(i)
    a=a+1
    if a==5:
        break