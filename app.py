from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from templates import base_datos
import sqlite3
import db
import random
import string



app= Flask(__name__)
"""rutas de las pestañas"""

#iniciar una sesion
app.secret_key='mysecretkey'

@app.route("/")
def funcion_home():
    return render_template('home1.html')


@app.route("/comentario", methods=["POST"])
def comentario():
    comentario = request.form['comentarios']
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    conexion= db.conexion_base()
    strsql= "INSERT INTO COMENTARIOS (FECHA, CEDULA_USER, COMENTARIO) VALUES ('{}',{},'{}')".format(fecha, cedula, comentario)
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(comentario)
    print(fecha)
    print(cedula)
    return render_template('home2.html')



@app.route("/compraAROMATICA", methods=["POST"])
def compra():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "AROMATICA"
    precio = 2000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraCAFE_EN_LECHE", methods=["POST"])
def compraCAFEENLECHE():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "CAFE EN LECHE"
    precio = 3500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraCHOCOLATE_CALIENTE", methods=["POST"])
def compraCHOCOLATE_CALIENTE():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "CHOCOLATE CALIENTE"
    precio = 3500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraTORTA_DE_CHOCOLATE", methods=["POST"])
def compraTORTA_DE_CHOCOLATE():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "TORTA DE CHOCOLATE"
    precio = 5000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraTORTA_DE_VAINILLA", methods=["POST"])
def compraTORTA_VAINILLA():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "TORTA DE VAINILLA"
    precio = 6500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraTORTA_ESPECIAL", methods=["POST"])
def compraTORTA_ESPECIAL():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "TORTA ESPECIAL"
    precio = 30000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraDONA_DE_CHOCOLATE", methods=["POST"])
def compraDONA_DE_CHCOLATE():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "DONA DE CHOCOLATE"
    precio = 4500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraDONAS_RELLENAS", methods=["POST"])
def compraDONAS_RELLENAS():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "DONAS RELLENAS"
    precio = 4000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraICE_COFFE", methods=["POST"])
def compra_ICE_COFFE():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "ICE COFFE"
    precio = 3000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraJUGOS_EN_AGUA", methods=["POST"])
def compra_JUGOS_EN_AGUA():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "JUGOS EN AGUA"
    precio = 3500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraLIMONDA_NATURAL", methods=["POST"])
def compra_LIMONDA_NATURAL():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "LIMONDA NATURAL"
    precio = 3500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraMACARRONS", methods=["POST"])
def compra_MACARRONS():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "MACARRONS"
    precio = 2500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraMALTEADA", methods=["POST"])
def compra_MALTEADA():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "MALTEADA"
    precio = 5500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraMOFFIN_DE_CHOCOLATE", methods=["POST"])
def compra_MOFFIN_DE_CHOCOLATE():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "MOFFIN DE CHOCOLATE"
    precio = 2500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraPAN_ARTESANAL", methods=["POST"])
def compra_PAN_ARTESANAL():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "PAN ARTESANAL"
    precio = 3000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraPAN_FRANCES", methods=["POST"])
def compra_PAN_FRANCES():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "PAN FRANCES"
    precio = 2500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraDESCRIPCION_DEL_PRODUCTO", methods=["POST"])
def compra_compraDESCRIPCION_DEL_PRODUCTO():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "Donut de chocolate"
    precio = 4000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')


@app.route("/compraPANQUEQUES", methods=["POST"])
def compra_compraPANQUEQUES():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "PANQUEQUES"
    precio = 5000
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraPIE_DE_MARACUYA", methods=["POST"])
def compra_compraPIE_DE_MARACUYA():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "PIE DE MARACUYA"
    precio = 3500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraPONQUESITOS", methods=["POST"])
def compra_compraPONQUESITOS():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "PONQUESITOS"
    precio = 2500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')

@app.route("/compraTE_DE_MANZANILLA", methods=["POST"])
def compra_compraTE_DE_MANZANILLA():
    fecha = "20/10/2021"
    cedula = random.randint(0,9999999999999999999999)
    producto = "TE DE MANZANILLA"
    precio = 2500
    number_of_strings = 5
    length_of_string = 25
    for x in range(number_of_strings):
        abc=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))



    dominio=random.choice(["email", "gmail", "hotmail","Outlook","uninorte"])
    dominio1=random.choice([".com", ".es", ".co",".or"])
    email = abc+"@"+dominio+dominio1

    conexion= db.conexion_base()
    strsql= "INSERT INTO VENTAS (FECHA, CEDULA_USER, PRODUCTO, PRECIO, EMAIL) VALUES ('{}',{},'{}',{},'{}')".format(fecha, cedula, producto, precio, email)
    
    cursorObj= conexion.cursor()
    cursorObj.execute(strsql)
    conexion.commit()
    conexion.close()
    print(email)
    return render_template('CarritoDeCompras.html')









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

@app.route("/carritoDecompras2")
def funcion_carritoDeCompras2():
    return render_template('carritoDecompras2.html')

@app.route("/carritoDecompras")
def funcion_carritoDeCompras():
    return render_template('carritoDecompras.html')

@app.route("/edicionPlatos")
def funcion_edicionPlatos():
    return render_template('edicionPlatos.html')


@app.route("/listaDeseos")
def funcion_listaDeseos():
    return render_template('listaDeseos.html')

@app.route("/descripcionProducto")
def funcion_descripcionProducto():
    return render_template('descripcionProductos/descripcionProducto.html')

@app.route("/descripcionProducto/TORTA_DE_CHOCOLATE")
def funcion_descripcionProducto_TORTA_DE_CHOCOLATE():
    return render_template('descripcionProductos/TORTA_DE_CHOCOLATE.html')

@app.route("/descripcionProducto/TORTA_DE_VAINILLA")
def funcion_descripcionProducto_TORTA_DE_VAINILLA():
    return render_template('descripcionProductos/TORTA_DE_VAINILLA.html')

@app.route("/descripcionProducto/TORTA_ESPECIAL")
def funcion_descripcionProducto_TORTA_ESPECIAL():
    return render_template('descripcionProductos/TORTA_ESPECIAL.html')

@app.route("/descripcionProducto/PIE_DE_MARACUYA")
def funcion_descripcionProducto_PIE_DE_MARACUYA():
    return render_template('descripcionProductos/PIE_DE_MARACUYA.html')

@app.route("/descripcionProducto/PAN_FRANCES")
def funcion_descripcionProducto_PAN_FRANCES():
    return render_template('descripcionProductos/PAN_FRANCES.html')

@app.route("/descripcionProducto/PAN_ARTESANAL")
def funcion_descripcionProducto_PAN_ARTESANAL():
    return render_template('descripcionProductos/PAN_ARTESANAL.html')

@app.route("/descripcionProducto/PONQUESITOS")
def funcion_descripcionProducto_PONQUESITOS():
    return render_template('descripcionProductos/PONQUESITOS.html')

@app.route("/descripcionProducto/MOFFIN_DE_CHOCOLATE")
def funcion_descripcionProducto_MOFFIN_DE_CHOCOLATE():
    return render_template('descripcionProductos/MOFFIN_DE_CHOCOLATE.html')


@app.route("/descripcionProducto/MACARRONS")
def funcion_descripcionProducto_MACARRONS():
    return render_template('descripcionProductos/MACARRONS.html')

@app.route("/descripcionProducto/PANQUEQUES")
def funcion_descripcionProducto_PANQUEQUES():
    return render_template('descripcionProductos/PANQUEQUES.html')

@app.route("/descripcionProducto/DONAS_RELLENAS")
def funcion_descripcionProducto_DONAS_RELLENAS():
    return render_template('descripcionProductos/DONAS_RELLENAS.html')

@app.route("/descripcionProducto/DONA_DE_CHOCOLATE")
def funcion_descripcionProducto_DONAS_DE_CHOCOLATE():
    return render_template('descripcionProductos/DONA_DE_CHOCOLATE.html')

@app.route("/descripcionProducto/LIMONADA_NATURAL")
def funcion_descripcionProducto_LIMONADA_NATURAL():
    return render_template('descripcionProductos/LIMONADA_NATURAL.html')

@app.route("/descripcionProducto/JUGOS_EN_AGUA")
def funcion_descripcionProducto_JUGOS_EN_AGUA():
    return render_template('descripcionProductos/JUGOS_EN_AGUA.html')

@app.route("/descripcionProducto/ICE_COFFEE")
def funcion_descripcionProducto_ICE_COFFEE():
    return render_template('descripcionProductos/ICE_COFFEE.html')

@app.route("/descripcionProducto/MALTEADA")
def funcion_descripcionProducto_MALTEADA():
    return render_template('descripcionProductos/MALTEADA.html')

@app.route("/descripcionProducto/CAFE_EN_LECHE")
def funcion_descripcionProducto_CAFE_EN_LECHE():
    return render_template('descripcionProductos/CAFE_EN_LECHE.html')

@app.route("/descripcionProducto/TE_DE_MANZANILLA")
def funcion_descripcionProducto_TE_DE_MANZANILLA():
    return render_template('descripcionProductos/TE_DE_MANZANILLA.html')

@app.route("/descripcionProducto/AROMATICA")
def funcion_descripcionProducto_AROMATICA():
    return render_template('descripcionProductos/AROMATICA.html')

@app.route("/descripcionProducto/CHOCOLATE_CALIENTE")
def funcion_descripcionProducto_CHOCOLATE_CALIENTE():
    return render_template('descripcionProductos/CHOCOLATE_CALIENTE.html')

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

