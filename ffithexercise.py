def removuneven(woowoo):
    for i in woowoo:
        if i % 2 != 0:
            woowoo.remove(i)
    return woowoo
lst = []
while True:
    num=input("Enter a number from your list, if no more left enter 'no'")
    if num == 'no':
        fin_lst=removuneven(lst)
        print("The list of numbers after removal of all uneven numbers are \n", fin_lst)
        print(lst)
    else:
        lst.append(int(num))
