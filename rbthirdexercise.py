import mysql.connector
import geopy
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3307,
         database='flight_game',
         user='root',
         password='thosebatteriesaredead',
         autocommit=True
         )

cursor=connection.cursor()
ICAO_code1=input("Enter the ICAO code of the first airport")
ICAO_code2=input("Enter the ICAO code of the second airport")
query="select latitude_deg, longitude_deg from airport where ident in (%s, %s);"
cursor.execute(query, (ICAO_code1,ICAO_code2))
result=cursor.fetchall()
print(result)