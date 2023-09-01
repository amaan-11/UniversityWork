choice= True
aiprorts={}
while choice!=0:
    choice=int(input("Enter 1 if you want to enter new airport data, \n2 if you want to fetch information of an existing airport and \n0 if you want to quit,"))
    if choice==1:
        ICAO_code=input("Enter the ICAO code,")
        airport_name=input("Enter the name of the airport,")
        aiprorts[ICAO_code]=airport_name
    if choice==2:
        ICAO_code=input("Enter the ICAO code of the airport you want to search for,")
        print(aiprorts[ICAO_code],"is the name of the airport")
    if choice==3:
        break