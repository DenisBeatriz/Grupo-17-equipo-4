import sqlite3
from sqlite3 import Error

def conexion_base():
    try:
        
        conexion = sqlite3.connect('base_datos_general.db')
        print("Conexion Exitosa")
        return conexion
    except Error:
        print(Error)