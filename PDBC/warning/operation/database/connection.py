import mysql.connector
def conn():
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='pradeep@1670',
        database='summerschool'
    )
    return db