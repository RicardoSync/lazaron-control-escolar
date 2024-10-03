import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="spider",
    user="ciso",
    password="ciso"
)


def guardar_cliente():
    cursor = mydb.cursor()
    cursor.execute("INSE")