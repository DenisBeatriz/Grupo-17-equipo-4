from flask import Flask, render_template, request
import werkzeug.security as ws, db

app= Flask(__name__)
app.secret_key = 'mi_llave_secreta'

@app.route("/")
def funcion_home():
    return render_template('home1.html')

@app.route("/home2")
def funcion_home2():
    return render_template('home2.html')

@app.route("/login", methods=['GET', 'POST'])
def funcion_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(request.form)
        return render_template('home2.html')

@app.route("/menu")
def funcion_menu():
    return render_template('menu.html')

@app.route("/perfilUsuario")
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

@app.route("/registroUsuario", methods=['GET', 'POST'])
def funcion_registro_usuario():
    if request.method == 'GET':
        return render_template('registro_usuario.html')
    else:
        nombres = request.form('nombres')
        apellidos = request.form('apellidos')
        cedula = request.form('cedula')
        email = request.form('email')
        celular = request.form('celular')
        direccion = request.form('direccion')
        complemento = request.form('complemento')
        contrasena = request.form('contrasena')
        conf_contrasena = request.form('conf_contrasena')
        db.insertar_usuario(nombres, apellidos, cedula, email, celular, direccion, complemento, ws.generate_password_hash(contrasena))

        return render_template('home2.html')


if __name__ == '__main__':
    app.run(debug=True)







