import mysql.connector
from mysql.connector import Error

try:
    
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='college'
    )
    
    if connection.is_connected():
        print("Successfully connected to the database")

        cursor = connection.cursor()

        query = """
        INSERT INTO record (id, name, class, phone_number)
        VALUES (%s, %s, %s, %s);
        """
        
        demo_data = (100, "Kanika Chouhan", "B.Tech", 9303090117)

        # Executing the query
        cursor.execute(query, demo_data)

        # Committing the transaction
        connection.commit()

        print("Student data is inserted into the database")
    else:
        print("data base not connect success")

except Error as e:
    print(f"Error occurred: {e}")

# finally:
   
#     if cursor:
#         cursor.close()
#     if connection and connection.is_connected():
#         connection.close()
#         print("Database connection closed.")
