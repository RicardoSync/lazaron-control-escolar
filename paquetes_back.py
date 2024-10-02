import mysql.connector
from notificaciones import enviar_notificacion

mydb = mysql.connector.connect(
    host="localhost",
    database="spider",
    user="ciso",
    password="ciso"
)



def guardar_paquetes(nombre, velocidad, precio):
    mycursor = mydb.cursor()

    sql = "INSERT INTO paquetes (nombre, velocidad, precio) VALUES (%s, %s, %s)"
    val = (nombre, velocidad, precio)

    mycursor.execute(sql, val)
    mydb.commit()
    enviar_notificacion("DOBLENET", "Paquete guardado!")


def guardar_antenas(nombre, modelo):
    mycursor = mydb.cursor()

    sql = "INSERT INTO antenas (nombre, modelo) VALUES (%s, %s)"
    val = (nombre, modelo)

    mycursor.execute(sql, val)
    mydb.commit()
    enviar_notificacion("DOBLENET", "Antena almacenada!")

def guardar_router(nombre, modelo):
    mycursor = mydb.cursor()

    sql = "INSERT INTO routers (nombre, modelo) VALUES (%s, %s)"
    val = (nombre, modelo)

    mycursor.execute(sql, val)
    mydb.commit()
    enviar_notificacion("DOBLENET", "Router almacenado!")