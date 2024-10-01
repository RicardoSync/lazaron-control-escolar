import mysql.connector
from mysql.connector import Error
from datetime import datetime

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

# Insertar un nuevo cliente en la tabla
def insertar_cliente(id, nombre, direccion, telefono, antena, router, ip, velocidad, fecha_instalacion, dia_corte, proximo_pago, mensualidad, estado, api):
    connection = connect_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO clientes (
                id, nombre, direccion, telefono, antena, router, ip, velocidad,
                fechaInstalacion, diaCorte, proximoPago, mensualidad, estado, api
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (id, nombre, direccion, telefono, antena, router, ip, velocidad, fecha_instalacion, dia_corte, proximo_pago, mensualidad, estado, api)
        
        cursor.execute(query, data)
        connection.commit()
        print(f"Cliente {nombre} insertado correctamente")
    except Error as e:
        print(f"Error al insertar cliente: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

