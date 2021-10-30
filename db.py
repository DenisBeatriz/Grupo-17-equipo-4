import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def obtener_conexion():
    try:
        conexion = sqlite3.connect('base_datos_general.db')
        return conexion
    except Error:
        print(Error)

def obtener_registro(condicion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if condicion == None:
        strsql = 'SELECT * FROM USUARIO'
    else: 
        strsql = 'SELECT * FROM USUARIO WHERE {}'.format(condicion)

    cursor.execute(strsql)

    datos = cursor.fetchall()
    conexion.close()

    return datos

def insertar_usuario(nombres, apellidos, cedula, email, celular, direccion, complemento, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "INSERT INTO USUARIO (CEDULA_USER, EMAIL, NOMBRE_USER, APELLIDO_USER, DIRECCION, CELULAR, COMPLEMENTO, CONTRASENA) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(cedula, email, nombres, apellidos, direccion, celular, complemento, contrasena)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def insertar_contacto2(nombre, email, mensaje):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "INSERT INTO contacto (nombre, email, mensaje) VALUES('{}','{}','{}')".format(nombre, email, mensaje)

    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def conexion_base():
    try:
        
        conexion = sqlite3.connect('base_datos_general.db')
        print("Conexion Exitosa")
        return conexion
    except Error:
        print(Error)
