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

function modificar_plato(){

    input_plato= document.getElementById('nombrePlato2')
    input_descri=document.getElementById('descripcionPlato2')
    input_id=document.getElementById('Id_Producto')
    input_precio=document.getElementById('precio_mod2')

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
    if (input_id.value  == ""){
        alert("Por favor el numero de identificacion correspondiente al producto")
        input_descri.focus()
        return false
    }else{ 
        if(validar_numero(input_id.value)== false ){
        alert("En el numero de identificacion no se permiten letras")
        input_descri.focus()
        return false
        }
    }
    
    if (input_precio.value  == ""){
        alert("Por favor ingrese el precio del plato")
        input_precio.focus()
        return false
    }if (validar_numero(input_precio.value)== false) {
        alert("Para el precio solo se permiten valores numericos")
            input_precio.focus()
            return false
    } else {
        alert ("Validacion Exitosa")
        return true        
    }
    
    
}

