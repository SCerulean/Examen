const items = document.getElementById('items')
const templateCard = document.getElementById('template-card').content
const fragment = document.createDocumentFragment()

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
})

items.addEventListener('click', e => {
    MostrarProducto(e)
})

const fetchData = async () => {
    try {
        const res = await fetch('https://jsonplaceholder.typicode.com/posts')
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
        templateCard.querySelector('h5').textContent = producto.title
        templateCard.querySelector('.btn-dark').dataset.di = producto.id 


        const clone = templateCard.cloneNode (true)
        fragment.appendChild(clone)

    })

    items.appendChild(fragment)
}

const MostrarProducto = e => {
    //console.log(e.target)
    //console.log(e.target.classList.contains('btn-dark'))
    if(e.target.classList.contains('btn-dark')){
        
    }
}