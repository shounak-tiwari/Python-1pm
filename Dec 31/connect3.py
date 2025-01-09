import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
password = "root",
database="college",
)

if dataBase.is_connected():
    print("yes connect")

    cursor = dataBase.cursor()

    query = """
        INSERT INTO record (id, name, class, phone_number)
        VALUES (%s, %s, %s, %s);
        """
        
    demo_data = (100, "Kanika Chouhan", "B.Tech", 9303090117)

        # Executing the query
    cursor.execute(query, demo_data)

        # Committing the transaction
    dataBase.commit()

    print("Student data is inserted into the database")
