num_month=int(input("Enter the number of the month,"))
seasons=("spring","summer","autumn","winter")
spring=(1,2,3)
summer=(4,5,6)
autumn=(7,8,9)
winter=(10,11,12)
if num_month in spring:
    print("The season this month belongs in is",seasons[0])
if num_month in summer:
    print("The season this month belongs in is",seasons[1])
if num_month in autumn:
    print("The season this month belongs in is",seasons[2])
if num_month in winter:
    print("The season this month belongs in is",seasons[3])