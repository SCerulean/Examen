const cards = document.getElementById('cards')
const items = document.getElementById('items')
const footer = document.getElementById('footer')
const templateCard = document.getElementById('template-card').content
const templateFooter = document.getElementById('template-footer').content
const templateCarrito = document.getElementById('template-carrito').content
const fragment = document.createDocumentFragment()
let carrito={}

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
    if(localStorage.getItem('carrito')) {
        carrito = JSON.parse(localStorage.getItem('carrito'))
        pintarCarrito()
    }
})

cards.addEventListener('click', e => {
    MostrarProducto(e)
})

items.addEventListener('click', e => {
    btnAccion(e)
})

const fetchData = async () => {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/lista_Productos')
        const data = await res.json()
        //console.log(data)
        Cartitas(data)
    } catch (error) {
        console.log(error)
        
    }
}

const Cartitas = data => {

    data.forEach(producto => {

        console.log(producto)
        templateCard.querySelector('h5').textContent = producto.nombre
        templateCard.querySelectorAll('p')[0].textContent = producto.precio
        templateCard.querySelectorAll('p')[1].textContent = producto.stock
        templateCard.querySelector('.btn-dark').dataset.id = producto.SKU 

        const clone = templateCard.cloneNode (true)
        fragment.appendChild(clone)

    })

    cards.appendChild(fragment)
}

const MostrarProducto = e => {
    //console.log(e.target)
    //console.log(e.target.classList.contains('btn-dark'))
    if(e.target.classList.contains('btn-dark')){
        setcarrito(e.target.parentElement)
    }
    e.stopPropagation()
}

const setcarrito = objeto => {
    //console.log(objeto)
    const producto = {
        SKU : objeto.querySelector('.btn-dark').dataset.id,
        nombre : objeto.querySelector('h5').textContent,
        precio : objeto.querySelectorAll('p')[0].textContent,
        stock : objeto.querySelectorAll('p')[1].textContent,
        cantidad: 1

    }

    if (carrito.hasOwnProperty(producto.id)) {
        producto.cantidad = carrito[producto.id].cantidad + 1
    }

    carrito[producto.id] = {...producto}
    pintarCarrito()

}

const pintarCarrito = () => {
    //console.log(carrito)
    items.innerHTML= ''
    Object.values(carrito).forEach(producto => {
        templateCarrito.querySelector('th').textContent = producto.SKU
        templateCarrito.querySelectorAll('td')[0].textContent = producto.Nombre
        templateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad
        templateCarrito.querySelector('.btn-info').dataset.id = producto.id
        templateCarrito.querySelector('.btn-danger').dataset.id = producto.id
        templateCarrito.querySelector('span').textContent = producto.cantidad * producto.precio

        const clone = templateCarrito.cloneNode(true)
        fragment.appendChild(clone)
    })

    items.appendChild(fragment)

    pintarFooter()

    localStorage.setItem('carrito',JSON.stringify(carrito))
}

const pintarFooter = () => {
    footer.innerHTML = ''
    if(Object.keys(carrito),length == 0){
        footer.innerHTML = '<th scope="row" colspan="5"> Carrito vacío - comience a comprar!</th>'

        return
    }

    const nCantidad = Object.values(carrito).reduce((acc,{cantidad}) => acc + cantidad,0)
    const nPrecio = Object.values(carrito).reduce((acc,{cantidad,precio}) => acc + precio + cantidad,0)

    templateFooter.querySelectorAll('td')[0].textContent = nCantidad
    templateFooter.querySelector('span').textContent = nPrecio

    const clone = templateFooter.cloneNode(true)
    fragment.appendChild(templateFooter)
    footer.appendChild(fragment)

    const btnVaciar = document.getElementById('vaciar-carrito')
    btnVaciar.addEventListener('click', () => {
        carrito = {}
        pintarCarrito()
    })
}

const btnAccion = e => {
    //console.log(e.target)
    //aumentar
    if(e.target.classList.contains('btn-info')){
        carrito[e.target.dataset.id]
        const producto = carrito[e.target.dataset.id]
        producto.cantidad++
        carrito[e.target.dataset.id] = {...producto}
        pintarCarrito()
    }

    //disminuir
    if(e.target.classList.contains('btn-danger')){
        const producto = carrito[e.target.dataset.id]
        producto.cantidad--
        if(producto.cantidad === 0){
            delete carrito[e.target.dataset.id]
        }
        pintarCarrito()
    }
    e.stopPropagation()
}