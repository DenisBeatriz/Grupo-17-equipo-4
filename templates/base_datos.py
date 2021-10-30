import sqlite3
from sqlite3 import Error

def conexion_sql():
    try: 
        con= sqlite3.connect('base_datos_general.db')
        
        return con;
    except Error:
        
        print(Error)

def cerrar_conexion(con):
    con.close()
