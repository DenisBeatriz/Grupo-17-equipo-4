from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)







