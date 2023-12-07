import mysql.connector as mysql

class DatabaseConnector:

    connection = None
    
    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host= "localhost",
            port=3306,
            database="asteroid_db",
            user="root",
            passwd="147896325"
        )
        cls.connection = db_connection

