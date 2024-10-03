import mysql.connector
from clientes_ui import clientes_ui_chidos

#Variable para las fuentes
titulo = ("Monospace", 14, "bold")
tamanio_entradas = 350

#Variable global
routers_guardados = []
antenas_guardadas = []
paquetes_guardados = []
antenas_guardadas_modelo = []
modelo_routers = []

#Conexion a la base de datos()
mydb = mysql.connector.connect(
    host="localhost",
    database="spider",
    user="ciso",
    password="ciso"
)

#Funciones que consultan los datos necesarios
def obtener_routers():
    global routers_guardados

    cursosr = mydb.cursor()
    cursosr.execute("SELECT * FROM routers")
    resultado_routers = cursosr.fetchall()

    routers_guardados = [fila[1] for fila in resultado_routers]


def obtener_antenas():
    global antenas_guardadas

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM antenas")
    resultado_antenas = cursor.fetchall()

    antenas_guardadas = [fila[1] for fila in resultado_antenas]

def obtener_antenas_modelo():
    global antenas_guardadas_modelo

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM antenas")
    resultado_antenas = cursor.fetchall()

    antenas_guardadas_modelo = [fila[2] for fila in resultado_antenas]

def obtener_paquetes():
    global paquetes_guardados

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM paquetes")
    resultado_paquetes = cursor.fetchall()

    paquetes_guardados = [fila[1] for fila in resultado_paquetes]


def obtener_modelos_routers():
    global modelo_routers

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM routers")
    resultado = cursor.fetchall()

    modelo_routers = [fila[2] for fila in resultado]



def llamado_avengers():
    obtener_antenas()
    obtener_antenas_modelo()
    obtener_paquetes()
    obtener_routers()
    obtener_modelos_routers()

    clientes_ui_chidos(routers_guardados, antenas_guardadas, paquetes_guardados, antenas_guardadas_modelo, modelo_routers)

llamado_avengers()