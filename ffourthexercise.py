choice=True
def sumlst(woowoo):
    sum=0
    for i in woowoo:
        sum=sum+i
    return sum
lst=[]
while choice==True:
    num=input("Enter a number from your list, if no more left enter 'no'")
    if num == 'no':
        choice = False
    if choice==False:
        val=sumlst(lst)
        print("The sum of the numbers you entered is=",val)
    elif choice==True:
        lst.append(int(num))