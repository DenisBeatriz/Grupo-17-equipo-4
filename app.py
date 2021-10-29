#resolucion de conflicto
from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from templates import base_datos
import sqlite3


app= Flask(__name__)
"""rutas de las pestañas"""

#iniciar una sesion
app.secret_key='mysecretkey'

@app.route("/")
def funcion_home():
    return render_template('home1.html')

@app.route("/home2")
def funcion_home2():
    return render_template('home2.html')

@app.route("/login")
def funcion_login():
    return render_template('login.html')

@app.route("/registro")
def funcion_registro():
    return render_template('registro_usuario.html')


@app.route("/perfinlUsuario")
def funcion_perfil():
    return render_template('perfil_usuario.html')

@app.route("/menu")
def funcion_menu():
    return render_template('menu.html')


@app.route("/pedido")
def funcion_pedido():
    return render_template('pedido.html')

@app.route("/pagosAdmin")
def funcion_pagoAdmin():
    return render_template('pagosAdmin.html')

@app.route("/descripcionProducto")
def funcion_descripcionProducto():
    return render_template('descripcionProducto.html')

@app.route("/carritoDecompras")
def funcion_carritoDeCompras():
    return render_template('carritoDecompras.html')

@app.route("/edicionPlatos")
def funcion_edicionPlatos():
    return render_template('edicionPlatos.html')


@app.route("/listaDeseos")
def funcion_listaDeseos():
    return render_template('listaDeseos.html')


@app.route("/admin")
def funcion_admin():
    return render_template('admin.html')

@app.route("/revisionComentarios")
def funcion_revision_de_comentarios():
    return render_template('revisionComentarios.html')

@app.route("/pagosUsuario")
def funcion_pagos_usuario():
    return render_template('pagosUsuario.html')

@app.route("/super_admin")
def funcion_super_admin():
    return render_template('super_admin.html')



"""RUTAS DE COMPROBACION"""
@app.route("/edicion_platos", methods=["POST"])#como insertar una imagen desde el ordenador
def edicionplato():#añadir plato a la base de datos
    
    if request.method =='POST':
        nombre= request.form['nombrePlato']
        descripcion= request.form['descripcionPlato']
        precioPlato= request.form['precio']
        print(nombre, descripcion, precioPlato)
    
    conec= base_datos.conexion_sql()
    cursorObj= conec.cursor()
    sqlite1= 'INSERT INTO PRODUCTOS (PRODUCTO, DESCRIPCION, PRECIO) VALUES (?,?,?)'
    cursorObj.execute(sqlite1, [nombre,descripcion,precioPlato])
    conec.commit()
    conec.close()
    return ("exito")


@app.route("/editar_plato", methods =["GET","POST"])#para modificar el plato
def edicion_plato_admin():
    if request.method =='GET' or request.method =='POST':
        id_producto= request.form['IDproducto1']
    #tengo que poner una busqueda del producto con el ID, retornar un valor si existe, y modificarlo
        conec= base_datos.conexion_sql()
        cursorObj= conec.cursor()
        #Busqueda del producto
        sqlitea='SELECT * FROM PRODUCTOS WHERE (?)'#pendiente
        cursorObj.execute(sqlitea, [id_producto])
        conec.commit()
        conec.close()
        a=True
        if (a==True):
            flash('Revision exitosa')
            return render_template('edicionPlatos.html')
        
@app.route("/eliminar_plato")
def eliminar_platoa():
    id_producto=eliminar_plato()#pendiente
    conec= base_datos.conexion_sql()
    cursorObj= conec.cursor()
    #Busqueda del producto
    sqlitea='SELECT * FROM PRODUCTOS WHERE (?)'
    cursorObj.execute(sqlitea, [id_producto])
    conec.commit()
    conec.close()

@app.route("/resultados", methods =["POST"])#liminar y/o desbloquear usuario
def resultados():
    if(request.method == "POST"):
        cedula_user=request.form['cedula']
    print(cedula_user)
    return "INGRESO CEDULA"

"""
@app.route("/conexion_bd")
def conexion_bd():
    conec= base_datos.conexion_sql
    
    strsql='select * from PRODUCTOS'
    
    cursorObj= conec.cursor()

    cursorObj.execute(strsql)
    productos= cursorObj.fetchall()

    return str(productos)
"""
def consultas(tabla):
    conec= base_datos.conexion_sql()
    
    strsql='select * from' + tabla
    
    cursorObj= conec.cursor()

    cursorObj.execute(strsql)
    datos= cursorObj.fetchall()
    conec.close()

    return str(datos)   
    """
def adicionar_datos(id, nombre,precio):
    conec=base_datos.conexion_sql()
    strsql='insert into Producto (id, nombre, precio) value'({},{},
    {}).format(id, nombre, precio)

    cursoObj =conec.cursor()
    cursoObj.execute(strsql)
    cursoObj.commit()
    conec.close()
    return True
"""


""" envio correo eliminacion y debloqueo de una cuenta
def enviarCorreo_El(correo_Usu, correo_admin, contraseña_admin):
    mensaje = -'Le notificamos que su cuenta se elimino de la pagina Duck Donuts, para mayor información, dirigirse a un punto de atención'
    asunto= 'Cuenta Eliminada'

    mensaje='Subject: {}\n\n{}'.format(asunto, mensaje)
    server = smtplib.SMTP('smtp.uninortes.com',587)
    server.starttls()
    server.login(correo_admin,contraseña_admin)
    server.sendmail(correo_admin, correo_Usu, mensaje)
    server.quit()

def enviarCorreo_Des(correo_Usu, correo_admin, contraseña_admin):
    mensaje = -'Le notificamos que su cuenta se desbloqueara actomaticamente en 1 día, para mayor información, dirigirse a un punto de atención'
    asunto= 'Cuenta Desbloqueada'

    mensaje='Subject: {}\n\n{}'.format(asunto, mensaje)
    server = smtplib.SMTP('smtp.uninortes.com',587)
    server.starttls()
    server.login(correo_admin,contraseña_admin)
    server.sendmail(correo_admin, correo_Usu, mensaje)
    server.quit()
"""