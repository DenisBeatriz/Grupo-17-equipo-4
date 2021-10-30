from flask import Flask, render_template, request, session, redirect, url_for, flash
from types import MethodDescriptorType
import werkzeug.security as ws, db
import smtplib
import random
import string

app= Flask(__name__)
app.secret_key = 'mi_llave_secreta'

# rutas de las pestañas

@app.before_request
def antes_peticion():
    if 'email' not in session and request.endpoint in ['home2']:
        return redirect('/login')

@app.route("/", methods=['GET', 'POST'])
def home1():
    if request.method == 'GET':
        return render_template('home1.html')
    else:
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        db.insertar_contacto2(nombre, email, mensaje)

        return render_template('home1.html')

@app.route("/home2", methods=['GET', 'POST'])
def home2():
    if request.method == 'GET':
        return render_template('home2.html')
    else:
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        db.insertar_contacto2(nombre, email, mensaje)

        return render_template('home2.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        contrasena = request.form['contrasena']

        registro_usuario = db.obtener_registro("EMAIL = '{}'".format(email))

        if registro_usuario:
            contrasena_db = registro_usuario[0][8]
            inicio_exitoso = ws.check_password_hash(contrasena_db, contrasena)

            if inicio_exitoso:
                session['email'] = email
                return redirect('/home2')
            else:
                return redirect('/login')

        else:
            return redirect('/login')

@app.route("/registroUsuario", methods=['GET', 'POST'])
def registroUsuario():
    if request.method == 'GET':
        return render_template('registro_usuario.html')
    else:
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        cedula = request.form['cedula']
        email = request.form['email']
        celular = request.form['celular']
        direccion = request.form['direccion']
        complemento = request.form['complemento']
        contrasena = request.form['contrasena']
        conf_contrasena = request.form['conf_contrasena']
        db.insertar_usuario(nombres, apellidos, cedula, email, celular, direccion, complemento, ws.generate_password_hash(contrasena))

        return render_template('home2.html')

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


@app.route("/perfilUsuario")
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
    conec= db.conexion_base()
    cursorObj= conec.cursor()
    cursorObj.execute('SELECT * FROM PAGOS')
    data= cursorObj.fetchall()
    print (data)
    conec.commit()
    conec.close()
    return render_template('pagosAdmin.html', pagos=data)

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

@app.route("/desbloquear_usuario")
def desbloquear_usuario():
    return render_template('desbloqueo_user.html')

@app.route("/revisionComentarios")
def funcion_revision_de_comentarios():
    conec= db.conexion_base()
    cursorObj= conec.cursor()
    cursorObj.execute('SELECT * FROM COMENTARIOS')
    data= cursorObj.fetchall()
    print (data)
    conec.commit()
    conec.close()
    return render_template('revisionComentarios.html', comentarios=data)

@app.route("/pagosUsuario")
def funcion_pagos_usuario():
    return render_template('pagosUsuario.html')


@app.route("/super_admin")
def funcion_super_admin():
    return render_template('super_admin.html')


@app.route("/cerrar_sesion")
def cerrar_sesion():
    if 'email' in session:
        session.pop('email')

    return redirect('/')

"""RUTAS DE COMPROBACION"""
@app.route("/edicion_platos", methods=["POST"])#como insertar una imagen desde el ordenador
def edicionplato():#añadir plato a la base de datos
    
    if request.method =='POST':
        nombre= request.form['nombrePlato']
        descripcion= request.form['descripcionPlato']
        precioPlato= request.form['precio']
        print(nombre, descripcion, precioPlato)
    
    conec= db.conexion_base()
    cursorObj= conec.cursor()
    sqlite1= 'INSERT INTO PRODUCTOS (PRODUCTO, DESCRIPCION, PRECIO) VALUES (?,?,?)'
    cursorObj.execute(sqlite1, [nombre,descripcion,precioPlato])
    conec.commit()
    conec.close()
    return render_template('/edicion_platos')


@app.route("/editar_plato", methods =["GET","POST"])#para modificar el plato
def edicion_plato_admin():
    if request.method =='GET' or request.method =='POST':
        id_producto= request.form['IDproducto1']
    #tengo que poner una busqueda del producto con el ID, retornar un valor si existe, y modificarlo
        conec= db.conexion_base()
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
        
@app.route("/eliminar_plato", methods =["GET","POST"])#para modificar el plato
def eliminar_plato():
    if request.method =='GET' or request.method =='POST':
        id_producto= request.form['IDproducto1']
    #tengo que poner una busqueda del producto con el ID, retornar un valor si existe, y modificarlo
        conec= db.conexion_base()
        cursorObj= conec.cursor()
        #Busqueda del producto
        sqlitea='DELETE FROM PRODUCTOS WHERE (?)'#pendiente
        cursorObj.execute(sqlitea, [id_producto])
        conec.commit()
        conec.close()
        a=True
        if (a==True):
            flash('El plato se elimino de forma satisfactoria')
        
        return render_template('admin.html')
 

@app.route("/modificar_plato", methods=["POST"])
def modificar_plato():
    id_producto= request.form['Id_Producto']
    nombre= request.form['nombrePlato2']
    descripcion= request.form['descripcionPlato2']
    precio= request.form['precio_mod2']
    conec= db.conexion_base()
    curs= conec.cursor()
    sqlit= 'UPDATE PRODUCTOS SET PRODUCTO=? WHERE ID_PRODUCTO=?'
    curs.execute(sqlit, [nombre,id_producto])
    sqlit= 'UPDATE PRODUCTOS SET DESCRIPCION=? WHERE ID_PRODUCTO=?'
    curs.execute(sqlit, [descripcion,id_producto])
    sqlit= 'UPDATE PRODUCTOS SET PRECIO=? WHERE ID_PRODUCTO=?'
    curs.execute(sqlit, [precio,id_producto])
    conec.commit()
    conec.close()
    flash("El plato fue modificado")
    return render_template("edicionPlatos.html")


# envio correo eliminacion y debloqueo de una cuenta
@app.route("/eliminar_usuario", methods =["POST"])#FUNCIONA BIEN
def eliminar_usuario():
    id_usuario= request.form["cedula"]
    conec= db.conexion_base()
    cursorObj= conec.cursor()
        #Busqueda del producto
    sqlitea='DELETE FROM USUARIO WHERE (?)'#pendiente
    cursorObj.execute(sqlitea, [id_usuario])
    conec.commit()
    conec.close()
    flash("Usuario Eliminado con exito")
    return render_template('admin.html')

#DESBLOQUEO
@app.route("/cambios_desbloq", methods =["POST"])
def cambios_desbloq():
    cedula=request.form['Cedula12']
    contraseña=request.form['contraseña1']
    confirm_contraseña= request.form['confirm_contraseña1']
    if (contraseña == confirm_contraseña):
        #encriptar
        contraseña1= ws.generate_password_hash(contraseña)
        conec= db.conexion_base()
        curs= conec.cursor()
        sqlit= 'UPDATE USUARIO SET CONTRASEÑA=? WHERE CEDULA_USER=?'
        curs.execute(sqlit, [contraseña1,cedula])
        conec.commit()
        conec.close()
        flash ("Los cambios han sido guardados de manera exitosa")
        return render_template("desbloqueo_user.html")
    else:
        flash("Las contraseñas no son iguales")
        return render_template("desbloqueo_user.html")

@app.route("/cambios_super", methods =["POST"])
def cambios_super():
    nombre=request.form['Nombre']
    cedula=request.form['Cedula']
    email=request.form['Email']
    direc=request.form['direccion']
    apellido=request.form['Apellido']
    nickname=request.form['nickname']
    cel=request.form['celular']
    espe=request.form['Especificaciones']
    contraseña=request.form['contraseña']
    confirm_contraseña= request.form['confirm_contraseña']
    if (contraseña == confirm_contraseña):
        #encriptar
        contraseña1= ws.generate_password_hash(contraseña)
        conec= db.conexion_base()
        curs= conec.cursor()
        sqlit= 'INSERT INTO USUARIO (CEDULA_USER, NICKNAME, EMAIL, CONTRASEÑA, NOMBRE_USER, APELLIDO_USER, DIRECCION, CELULAR, COMPLEMENTO) VALUES (?,?,?,?,?,?,?,?,?)'
        curs.execute(sqlit, [cedula,nickname,email,contraseña1, nombre, apellido, direc, cel, espe])
        conec.commit()
        conec.close()
        flash ("Los cambios han sido guardados de manera exitosa")
        return render_template("super_admin.html")
    else:
        flash("Las contraseñas no son iguales")
        return render_template("super_admin.html")

@app.route("/eliminar_admin", methods=["POST"])
def eliminar_admin():
    id_admin=request.form['cedula_admin']
    conec= db.conexion_base()
    cursorObj= conec.cursor()
        #Busqueda del producto
    sqlitea='DELETE FROM USUARIO WHERE (?)'#pendiente
    cursorObj.execute(sqlitea, [id_admin])
    conec.commit()
    conec.close()
    flash("Usuario Eliminado con exito")
    return render_template('super_admin.html')

if __name__ == '__main__':
    app.run(debug=True)
