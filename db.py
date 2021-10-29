import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        print("holaaa")
        con = sqlite3.connect('base_datos_general.db')
        return con;
    except Error:
        print(Error)