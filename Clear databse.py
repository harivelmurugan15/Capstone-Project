import mysql.connector

con = mysql.connector.connect(
    host = "hostname",
    username = "username",
    password = "password",
    database = "database")

cursor = con.cursor()

query = "truncate table bus_routes"
cursor.execute(query)


