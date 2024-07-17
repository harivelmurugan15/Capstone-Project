import pandas as pd
from web_scrapping import bus_routes_name,bus_route_link,bus_names,bus_type,departing_time,duration,reaching_time,star_rating,price,seat_availablity
import mysql.connector

df = pd.DataFrame()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df['bus_routes_name'] = bus_routes_name
df['bus_route_link'] = bus_route_link
df['bus_names'] = bus_names
df['bus_type'] = bus_type
df['departing_time'] = departing_time
df['duration'] = duration
df['reaching_time'] = reaching_time
df['star_rating'] = star_rating
df['price'] = price
df['seat_availablity'] = seat_availablity

print(df)
df.to_csv("dataframe_redbus.csv")

con = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "12345",
    database = "MDE92")

cursor = con.cursor()

query = """ create table if not exists bus_routes(id INT PRIMARY KEY AUTO_INCREMENT,bus_routes_name varchar(225),
                 bus_route_link varchar(225),bus_names varchar(225),bus_type varchar(225),
                 departing_time DATETIME,duration varchar(225),reaching_time DATETIME,
                 star_rating FLOAT,price decimal(10,2),seat_availablity int)"""
cursor.execute(query)

query1 = '''insert into bus_routes(bus_routes_name, bus_route_link, bus_names, bus_type,departing_time, duration, 
                reaching_time,star_rating, price, seat_availablity)
                 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

for index in df.index:
    row = df.loc[index].values
    value = [str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]) ,str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9])]
    cursor.execute(query1,value)
    con.commit()