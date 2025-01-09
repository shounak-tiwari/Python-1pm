import mysql.connector
from mysql.connector import *

try:
    connection = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="root",
        # database = "college"    
        dataBase="college"
    )
    print('no error ')



except:
    print('error found')