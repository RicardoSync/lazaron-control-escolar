import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Cambia según tu servidor MySQL
            database='spidernet',  # Cambia según tu base de datos
            user='root',           # Cambia al usuario de tu base de datos
            password='tu_contraseña'  # Cambia a tu contraseña
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Insertar un nuevo registro en la tabla 'antenas'
def insertar_antena(nombre, modelo):
    connection = connect_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "INSERT INTO antenas (nombre, modelo) VALUES (%s, %s)"
        cursor.execute(query, (nombre, modelo))
        connection.commit()
        print(f"Antena {nombre} con modelo {modelo} insertada correctamente")
    except Error as e:
        print(f"Error al insertar la antena: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
