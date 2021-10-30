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

function verificar_datos_deblo(){
    input_nombre=document.getElementById('Nombre')
    input_cedula=document.getElementById('Cedula12')
    input_contraseña=document.getElementById('contraseña1')//falta cifrar contraseña
    input_email=document.getElementById('Email')
    input_confir_contra=document.getElementById('confirm_contraseña1')


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
    if (input_email.value == "") {
        alert ("Por favor ingrese el correo electronico correspondiente al usuario")
        input_email.focus()
        return false
    }else{
        if (validar_correo(input_email.value) == false) {
            alert("Por favor verifique el correo ingresado")
            input_email.focus()
            return false
        }

    }

    if (input_cedula.value == ""){
        alert("Por favor ingrese el numero de cedula")
        input_cedula.focus()
        return false
    }else{
        if (validar_numero(input_cedula.value)== false) {
            alert("Para numero de cedula solo se permiten valores numericos")
            input_cedula.focus()
            return false
        }
    }

    alert("Validacion Exitosa")
    return true
}    
    