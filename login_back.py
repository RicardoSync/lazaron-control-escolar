import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',     # Cambia a la dirección de tu servidor MySQL
            database='spider', # Cambia al nombre de tu base de datos
            user='ciso',          # Cambia al nombre de usuario de tu base de datos
            password='ciso'  # Cambia a tu contraseña
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Crear un nuevo usuario
def crear_usuario(username, clave):
    connection = connect_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "INSERT INTO usuarios (username, clave) VALUES (%s, %s)"
        cursor.execute(query, (username, clave))
        connection.commit()
        print(f"Usuario {username} creado exitosamente")
    except Error as e:
        print(f"Error al crear usuario: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Iniciar sesión con un usuario
def iniciar_sesion(username, clave):
    connection = connect_db()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM usuarios WHERE username = %s AND clave = %s"
        cursor.execute(query, (username, clave))
        usuario = cursor.fetchone()
        if usuario:
            print(f"Inicio de sesión exitoso para el usuario: {username}")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos")
            return False
    except Error as e:
        print(f"Error al iniciar sesión: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
