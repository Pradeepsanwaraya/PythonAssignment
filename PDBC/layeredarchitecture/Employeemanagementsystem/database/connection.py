import mysql.connector
class Database:
    def connect(self):
        connection=mysql.connector.connect(host="localhost",
                user="root",
                password="Shreya@123",
                database="pdbcpractise")
        return connection