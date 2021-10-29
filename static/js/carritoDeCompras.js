const clickboton = document.querySelectorAll('.button')
const tboby = document.querySelector('.tboby')
let carrito = []

clickboton.forEach(btn => {
    btn.addEventListener('click', agregarAlCarritoItem)
})

function agregarAlCarritoItem(evento){
    const boton = evento.target
    const item = boton.closest('.card')
    const itemTitulo = item.querySelector('.card-title').textContent;
    const itemPrecio = item.querySelector('.Precio').textContent;
    const itemImagen = item.querySelector('.card-img-top').src;

    const nuevoItem = {
        titulo: itemTitulo,
        precio: itemPrecio,
        img: itemImagen,
        cantidad: 1
    }

    agregarItemCarrito(nuevoItem)
}


function agregarItemCarrito(nuevoItem){

    const alert = document.querySelector('.alert')

    setTimeout(function(){
        alert.classList.add('hide')
    } , 2000
    )

    alert.classList.remove('hide')

    const entradaDelElemeto = tboby.getElementsByClassName('input__element')
    
    for(let i=0; i < carrito.length ; i++){
        if(carrito[i].titulo.trim() === nuevoItem.titulo.trim()){
            carrito[i].cantidad ++;
            const valorDeEntrada = entradaDelElemeto[i]
            valorDeEntrada.value++;
            totalCarrito()
            return null;
        }
    }
    carrito.push(nuevoItem)
    renderCarrito()
}

function renderCarrito(){
    tboby.innerHTML= ''
    carrito.map(item =>{
        const tr = document.createElement('tr')
        tr.classList.add('ItemCarrito')
        const content = `
            <th scope="row">1</th>
            <td class="table__productos">
                <img src=${item.img} alt="">
                <h6 class="title">${item.titulo}</h6>
            </td>
            <td class="table__price"><p>${item.precio}</p></td>
            <td class="table__cantidad">
                <input type="number" min="1" value=${item.cantidad} class="input__element">
                <button class="delete btn btn-danger">x</button>
            </td>
        `

        tr.innerHTML = content;
        tboby.append(tr)

        tr.querySelector('.delete').addEventListener('click', eliminarItemDelCarrito)
        tr.querySelector('.input__element').addEventListener('change',sumaDeLaCantidad)
    })
    totalCarrito()
}

function totalCarrito(){
    let total = 0;
    const itemCarTotal = document.querySelector('.itemCarTotal')
    carrito.forEach((item)=> {
        const precio = Number(item.precio.replace("$", ''))
        total = total + precio*item.cantidad
    }) 
    itemCarTotal.innerHTML = `Total $${total}`
    agregarLocalStorage()
}

function eliminarItemDelCarrito(evento){
    const botonEliminar = evento.target
    const tr = botonEliminar.closest('.ItemCarrito')
    const titulo = tr.querySelector('.title').textContent;
    for(let i = 0; i<carrito.length;i++){
        if(carrito[i].titulo.trim() === titulo.trim()){
            carrito.splice(i, 1)
        }
    }

    const alert = document.querySelector('.remover')

    setTimeout(function(){
        alert.classList.add('remover')
    } , 2000
    )

    alert.classList.remove('remover')

    tr.remove()
    totalCarrito()
}

function sumaDeLaCantidad(evento){
    const sumar = evento.target
    const tr = sumar.closest('.ItemCarrito')
    const titulo = tr.querySelector('.title').textContent;

    carrito.forEach(item=>{
        if(item.titulo.trim() === titulo){
            sumar.value < 1 ? (sumar.value = 1) : sumar.value;
            item.cantidad = sumar.value;
            totalCarrito()
        }
    })
}


function agregarLocalStorage(){
    localStorage.setItem('carrito', JSON.stringify(carrito))
}

window.onload = function(){
    const storage = JSON.parse(localStorage.getItem('carrito'));
    if(storage){
        carrito = storage;
        renderCarrito()
    }
}

let pagos = document.querySelector('.comprarCarrito')
pagos.addEventListener('click',miPago)

function miPago() {
    alert('Su pago a sido realizado con exito!')
    localStorage.clear() 
  }

















    

    



    