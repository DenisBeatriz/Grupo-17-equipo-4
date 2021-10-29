const clickbotonL = document.querySelectorAll('.listaDeDeseos')
const tbobyL = document.querySelector('.tbobyL')
let carritoL = []

clickbotonL.forEach(btn => {
    btn.addEventListener('click', agregarAlCarritoItemL)
})

function agregarAlCarritoItemL(evento){
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

    agregarItemCarritoL(nuevoItem)
}


function agregarItemCarritoL(nuevoItem){


    const entradaDelElemetoL = tbobyL.getElementsByClassName('input__element')
    
    for(let i=0; i < carritoL.length ; i++){
        if(carritoL[i].titulo.trim() === nuevoItem.titulo.trim()){
            carritoL[i].cantidad ++;
            const valorDeEntradaL = entradaDelElemetoL[i]
            valorDeEntradaL.value++;
            totalCarritoL()
            return null;
        }
    }
    carritoL.push(nuevoItem)
    renderCarritoL()
}

function renderCarritoL(){
    tbobyL.innerHTML= ''
    carritoL.map(item =>{
        const trL = document.createElement('tr')
        trL.classList.add('ItemCarrito')
        const contentL = `
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

        trL.innerHTML = contentL;
        tbobyL.append(trL)

        trL.querySelector('.delete').addEventListener('click', eliminarItemDelCarrito)
        trL.querySelector('.input__element').addEventListener('change',sumaDeLaCantidad)
    })
    totalCarritoL()
}

function totalCarritoL(){
    let total = 0;
    const itemCarTotal = document.querySelector('.itemCarTotal')
    carritoL.forEach((item)=> {
        const precio = Number(item.precio.replace("$", ''))
        total = total + precio*item.cantidad
    }) 
    itemCarTotal.innerHTML = `Total $${total}`
    agregarLocalStorageL()
}

function eliminarItemDelCarritoL(evento){
    const botonEliminar = evento.target
    const tr = botonEliminar.closest('.ItemCarrito')
    const titulo = tr.querySelector('.title').textContent;
    for(let i = 0; i<carritoL.length;i++){
        if(carritoL[i].titulo.trim() === titulo.trim()){
            carritoL.splice(i, 1)
        }
    }

    const alert = document.querySelector('.remover')

    setTimeout(function(){
        alert.classList.add('remover')
    } , 2000
    )

    alert.classList.remove('remover')

    tr.remove()
    totalCarritoL()
}

function sumaDeLaCantidadL(evento){
    const sumar = evento.target
    const tr = sumar.closest('.ItemCarrito')
    const titulo = tr.querySelector('.title').textContent;

    carritoL.forEach(item=>{
        if(item.titulo.trim() === titulo){
            sumar.value < 1 ? (sumar.value = 1) : sumar.value;
            item.cantidad = sumar.value;
            totalCarritoL()
        }
    })
}


function agregarLocalStorageL(){
    localStorage.setItem('carritoL', JSON.stringify(carritoL))
}

window.onload = function(){
    const storage = JSON.parse(localStorage.getItem('carritoL'));
    if(storage){
        carritoL = storage;
        renderCarritoL()
    }
}
