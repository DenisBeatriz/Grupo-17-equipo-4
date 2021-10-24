const producto = document.querySelectorAll('#agregarCarrito');
producto.forEach(porCadaBotton =>{
    porCadaBotton.addEventListener('click', porCadaClick);
});


const productosSelecionados = document.querySelector('.productosElegidos');

function porCadaClick(evento){
    const boton = event.target;
    const itemGeneral = boton.closest('.general');

    const itemTitulo = itemGeneral.querySelector('.titulo').textContent;
    const itemPrecio = itemGeneral.querySelector('.precioProducto').textContent;
    const itemImagen = itemGeneral.querySelector('.imagen').src;
    

    itemsCarritoDeCompras(itemTitulo, itemPrecio, itemImagen);
}

function itemsCarritoDeCompras(itemTitulo, itemPrecio, itemImagen){
const elementoTitulo = productosSelecionados.getElementsByClassName('.carritoComprasTituloDelElemento');
//const canti = productosSelecionados.getElementsByClassName('.carritoComprasCantidadDelElemento')
for(let i = 0;i < elementoTitulo.length; i++){
    if(elementoTitulo[i].innerText === itemTitulo){
        let elementoCantidad = elementoTitulo[i].parentElement.parentElement.querySelector('.carritoComprasCantidadDelElemento');
        elementoCantidad.value++;
        actualizarTotalCarritoCompras();
        return;
    }
}
//console.log('a: itemsCarritoDeCompras -> canti', canti);

    const hileraCarritoCompras = document.createElement('div');

    const contenedorDelCarrito = `
    <div class="producto1">
        <div class="tituloImagen">
            <a href="">
                <img src=${itemImagen} alt="">
                <p class="carritoComprasTituloDelElemento">${itemTitulo}</p>
            </a>                    
        </div>
        
        <div class="cantidad">
            <div class="agregar">
                <input class="carritoComprasCantidadDelElemento" type="number" value="1" >
            </div>
            <button class="delete"><strong>Eliminar</strong></button>
        </div>

        <h1 class="carritoComprasPrecioDelElemento">${itemPrecio}</h1>
    </div>`;

    hileraCarritoCompras.innerHTML = contenedorDelCarrito;
    productosSelecionados.append(hileraCarritoCompras);

    hileraCarritoCompras.querySelector('.delete').addEventListener('click', quitarItemCarritoCompras);
    actualizarTotalCarritoCompras();

    hileraCarritoCompras.querySelector('.carritoComprasCantidadDelElemento').addEventListener('change', cambioDeCantidad);
}

function actualizarTotalCarritoCompras(){
    let total = 0;
    const tiendaCarritoTotal = document.querySelector('.tiendaCarritoTotal');
    
    const itemCarritoCompras = document.querySelectorAll('.producto1');
    
    itemCarritoCompras.forEach(producto1 =>{
        const itemCarritoComprasElementoPrecio = producto1.querySelector(
            '.carritoComprasPrecioDelElemento'
        );
        const itemcarritoComprasPrecio = Number(itemCarritoComprasElementoPrecio.textContent.replace('$', '')
        );

        const itemCarritoComprasElementoCantidad = producto1.querySelector('.carritoComprasCantidadDelElemento');
        
        const itemcarritoComprasCantidad = Number(itemCarritoComprasElementoCantidad.value
        );

        total = total + itemcarritoComprasPrecio * itemcarritoComprasCantidad;
        
    });

    tiendaCarritoTotal.innerHTML = "$"+`${total.toFixed(2)}`
}

function quitarItemCarritoCompras(event){
    const clickedBoton = event.target;
    clickedBoton.closest('.producto1').remove();
    actualizarTotalCarritoCompras();
    
}

function cambioDeCantidad(event){
    const entrada = event.target;
    //console.log(' a: cambioDeCantidad -> entrada', entrada);
    if(entrada.value <= 0){
        entrada.value = 1;
        actualizarTotalCarritoCompras();
    }
}










