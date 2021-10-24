import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def obtener_conexion():
    try:
        conexion = sqlite3.connect('db/base_datos.db')
        return conexion
    except Error:
        print(Error)

def obtener_registro(tabla, condicion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if condicion == None:
        strsql = 'SELECT * FROM {}'.format(tabla)
    else: 
        strsql = 'SELECT * FROM {} WHERE {}'.format(tabla, condicion)

    cursor.execute(strsql)

    datos = cursor.fetchall()
    conexion.close()

    return datos

def insertar_usuario(nombres, apellidos, cedula, email, celular, direccion, complemento, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "INSERT INTO usuario (nombres, apellidos, cedula, email, celular, direccion, complemento, contrasena) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(nombres, apellidos, cedula, email, celular, direccion, complemento, contrasena)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

