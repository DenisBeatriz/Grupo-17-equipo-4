function validar_texto(parametro){
    var patron= /^[a-zA-ZáéíóúÁÉÍÓÚÑñ\s]*$/;
    if (parametro.search(patron)){
        return false
    }else{
        return true
    }
}

function validar_numero(parametro){
    if(!/^([0-9])*$/.test(parametro)){
        return false
    }else{
        return true
    }
}

function validar_correo(parametro){
    var patron= /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (parametro.search(patron)){
        return false
    }else{
        return true
    }
}

function super_admin(){
    input_nombre=document.getElementById('Nombre')
    input_cedula=document.getElementById('Cedula')
    input_email=document.getElementById('Email')
    input_contraseña=document.getElementById('contraseña')
    input_confir_contra=document.getElementById('confirm_contraseña')
    input_apellido=document.getElementById('Apellido')
    input_celular=document.getElementById('celular')
    input_especificaciones=document.getElementById('especificaciones')
    input_direccion=document.getElementById('direccion')
    input_nicname=document.getElementById('nickname')
    
    if (input_nombre.value == ""){//validar nombre
        alert ("Por favor ingresar nombre del usuario")
        input_nombre.focus()
        return false
    }else{ 
        if(validar_texto(input_nombre.value)== false ){
        alert("El nombre del usuario solo debe llevar letras")
        input_nombre.focus()
        return false
        }
    }

    if (input_apellido.value == ""){//validar nombre
        alert ("Por favor ingresar apellido del usuario")
        input_apellido.focus()
        return false
    }else{ 
        if(validar_texto(input_apellido.value)== false ){
        alert("El apellido del usuario solo debe llevar letras")
        input_apellido.focus()
        return false
        }
    }

    if (input_cedula.value == ""){
        alert("Por favor ingrese el numero de cedula")
        input_cedula.focus()
        return false
    }else{
        if (validar_numero(input_cedula.value)== false){
            alert("Para numero de cedula solo se permiten valores numericos")
            input_cedula.focus()
            return false
        }
    }

    if (input_email.value == ""){
        alert ("Por favor ingrese el correo electronico correspondiente al usuario")
        input_email.focus()
        return false
    }else{
        if (validar_correo(input_email.value) == false){
            alert("Por favor verifique el correo ingresado")
            input_email.focus()
            return false
        }
    }

    if (input_direccion.value == ""){
        alert ("Por favor ingrese una direccion")
        input_direccion.focus()
        return false
    }

    if (input_nicname.value == ""){
        alert ("Por favor ingrese un nickname")
        input_nicname.focus()
        return false
    }

    if (input_contraseña.value == ""){
        alert ("Por favor ingrese una contraseña")
        input_contraseña.focus()
        return false
    }

    if (input_confir_contra.value == ""){
        alert ("Por favor compruebe su contraseña")
        input_input_confir_contra.focus()
        return false
    }

    if (input_celular.value == ""){
        alert("Por favor ingrese el numero de celular")
        input_celular.focus()
        return false
    }else{
        if (validar_numero(input_celular.value)== false){
            alert("Para numero de celular solo se permiten valores numericos")
            input_celular.focus()
            return false
        }
    }

    if (input_especificaciones.value == ""){
        alert ("Por favor ingresar las especificaciones de direccion")
        input_especificaciones.focus()
        return false
    }else{ 
        if(validar_texto(input_especificaciones.value)== false ){
        alert("Para las especificaciones solo debe llevar letras")
        input_especificaciones.focus()
        return false
        }
    }
    alert ("Validacion exitosa")
    return true
}