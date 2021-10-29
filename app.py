from flask import Flask, render_template, request
import db


app= Flask(__name__)

@app.route("/")
def funcion_home():
    return render_template('home1.html')


@app.route("/comentario", method=["POST"])
def comentario():
    comentario = request.form['comentarios']
    fecha = "20/10/2021"

    conec= db.sql_connection()
    cursorObj= conec.cursor()
    sqlite1= 'INSERT INTO COMENTARIOS (FECHA, COMENTARIO) VALUES (?,?)'

    cursorObj.execute(sqlite1, [fecha,comentario])
    conec.commit()
    conec.close()
    print(comentario)
    print(fecha)
    return "exito"

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

@app.route("/carritoDecompras2")
def funcion_carritoDeCompras2():
    return render_template('carritoDecompras2.html')

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

######
######
######
######
######
######
######
######
######
######
######
######
##descripciones de los productos
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

######
######
######
######
######
######
######
######
######
######
######
######





    










