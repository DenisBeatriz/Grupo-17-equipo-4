from types import MethodDescriptorType
from flask import Flask, render_template, request
import smtplib
from templates import base_datos

app= Flask(__name__)

@app.route("/")
def funcion_home():
    return render_template('home1.html')

@app.route("/home2")
def funcion_home2():
    return render_template('home2.html')

@app.route("/login")
def funcion_login():
    return render_template('login.html')

@app.route("/menu")
def funcion_menu():
    return render_template('menu.html')

@app.route("/perfinlUsuario")
def funcion_perfil():
    return render_template('perfil_usuario.html')


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


@app.route("/revisionComentarios")
def funcion_revision_de_comentarios():
    return render_template('revisionComentarios.html')

@app.route("/pagosUsuario")
def funcion_pagos_usuario():
    return render_template('pagosUsuario.html')

@app.route("/admin")
def funcion_admin():
    return render_template('admin.html')


@app.route("/listaDeseos")
def funcion_listaDeseos():
    return render_template('listaDeseos.html')

@app.route("/edicion_platos", methods=["GET","POST"])#como insertar una imagen desde el ordenador
def prueba():
    if request.method == 'GET':
        return render_template('edicion_Platos.htm')
    else:

        print(request.form)
    return 'edicion plato exitoso'

@app.route("/resultados", methods =["POST"])
def resultados():
    print(request.form['cedula'])
    return "INGRESO CEDULA"

@app.route("/conexion_bd")
def conexion_bd():
    conec= base_datos.conexion_sql
    
    strsql='select * from PRODUCTOS'
    
    cursorObj= conec.cursor()

    cursorObj.execute(strsql)
    productos= cursorObj.fetchall()

    return str(productos)






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