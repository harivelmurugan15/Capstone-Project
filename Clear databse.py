import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "12345",
    database = "MDE92")

cursor = con.cursor()

query = "truncate table bus_routes"
cursor.execute(query)


