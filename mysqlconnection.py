import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="Nithya",
  password="root"
)
print(mydb)