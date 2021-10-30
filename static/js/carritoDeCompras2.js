const clickboton = document.querySelectorAll('.button')


clickboton.forEach(btn => {
    btn.addEventListener('click', Ingrese)
})

function Ingrese() {
    alert('Para agregar al carrito de comprar ingrese a su cuenta!');
  }

const L = document.querySelectorAll('.listaDeDeseos')

L.forEach(btn =>{
    btn.addEventListener('click', IngreseL)
})

function IngreseL(){
    alert('Para agregar a la lista de deseos ingrese a su cuenta!');
}




