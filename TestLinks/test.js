// THIS WORKS! - but user has to allow popups in order to open multiple links
let btn = document.getElementById('btn')
let links = ['https://www.strxngers.com/','https://www.youtube.com/','https://www.gagelieble.com/','https://www.twitter.com/'  ]


btn.addEventListener('click', () => {
    for(let i = 0; i < links.length; i++){
        window.open(links[i])
    }
})