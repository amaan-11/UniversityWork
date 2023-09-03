import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3307,
         database='flight_game',
         user='root',
         password='thosebatteriesaredead',
         autocommit=True
         )
ICAO_code=input("Enter the ICAO code of the airport you're looking for,")
cursor=connection.cursor()
statement="select name, municipality from airport where ident = '"+ICAO_code+"'"
cursor.execute(statement)
result=cursor.fetchall()
for i in result:
    print("The name of the airport is "+i[0]+" and it is located in the Town, "+i[1])