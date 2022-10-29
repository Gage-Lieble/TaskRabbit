console.log('it works')

// Allows 1 button to open multiple links
function openLinks(links){
    links.forEach(link =>{
        window.open(link)
    })

    }

let addInpBtn = document.getElementById('add_inp')

let createForm = document.getElementById('create-form')
let counter = 5
addInpBtn.addEventListener('click', () =>{
    console.log('add')
    counter += 1
    // let newInp = `<input type="text" name="site-${counter}" placeholder="website">`
    let newInp = document.createElement("input");
    newInp.type = "text";
    newInp.name = "site-" + counter;
    newInp.placeholder = 'website'
    createForm.appendChild(newInp)

})

