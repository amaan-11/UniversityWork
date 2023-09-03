import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3307,
         database='flight_game',
         user='root',
         password='thosebatteriesaredead',
         autocommit=True
         )
cursor=connection.cursor()
area_code=input("Enter the area code to get the list of airports in that region,")
query="select name from airport where iso_country = '"+area_code+"' order by type ;"
cursor.execute(query)
result=cursor.fetchall()
for i in result:
    print(i)