function validar_formulario_registro() {
    input_cedula = document.getElementById('cedula')
    input_email = document.getElementById('email')
    input_celular = document.getElementById('celular')
    input_contrasena = document.getElementById('contrasena')
    input_conf_contrasena = document.getElementById('conf_contrasena')

    if (!validar_cedula(input_cedula.value)) {
        alert('El campo "Cédula" sólo debe tener números.')
        return false
    }

    if (!validar_email(input_email.value)) {
        alert('Correo inváilido.')
        return false
    }

    if (!validar_celular(input_celular.value)) {
        alert('El campo "Celular" sólo debe tener números.')
        return false
    }

    if (!validar_contrasena(input_contrasena.value)) {
        alert('La contraseña debe tener al menos una mayúscula, una minúscula, un número y por lo menos 8 caracteres.')
        return false
    }

    if (input_contrasena.value != input_conf_contrasena.value) {
        alert('Las contraseñas no coinciden.')
        return false
    }

    return true
}

function validar_cedula(cedula) {
    if (/^\d+$/i.test(cedula)) {
        return true
    } else {
        return false
    }
}

function validar_email(email) {
    if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/i.test(email)) {
        return true
    } else {
        return false
    }
}

function validar_celular(celular) {
    if (/^\d+$/i.test(celular)) {
        return true
    } else {
        return false
    }
}

function validar_contrasena(contrasena) {
    if (/^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/i.test(contrasena)) {
        return true
    } else {
        return false
    }
}

