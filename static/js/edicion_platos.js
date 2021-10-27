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

function añadir_plato(){

    input_plato= document.getElementById('nombrePlato')
    input_descri=document.getElementById('descripcionPlato')
    input_precio=document.getElementById('Precio')

    if (input_plato.value == ""){
        alert ("Por favor ingresar nombre del plato")
        input_plato.focus()
        return false
    }else{ 
        if(validar_texto(input_plato.value)== false ){
        alert("El nombre del plato solo debe llevar letras")
        input_plato.focus()
        return false
        }
    }
    
    if (input_descri.value  == ""){
        alert("Por favor ingrese la descripcion del plato")
        input_descri.focus()
        return false
    }else{ 
        if(validar_texto(input_descri.value)== false ){
        alert("En la descripcion no se permiten valores numericos")
        input_descri.focus()
        return false
        }
    }
    
    if (input_precio.value  == ""){
        alert("Por favor ingrese el precio del plato")
        input_precio.focus()
        return false
    }else{
        if(validar_numero(input_precio.value)== false){
            alert("Para el precio solo se permiten valores numericos")
            input_precio.focus()
            return false
        }
    }

    formulario.submit()

}

