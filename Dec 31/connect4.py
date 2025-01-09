import mysql.connector
from mysql.connector import Error


DataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="record2025"
)


print('database connect')