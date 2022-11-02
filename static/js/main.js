
// Allows 1 button to open multiple links
function openLinks(links){
    links.forEach(link =>{
        window.open(link)
    })

    }




// Adding more links to 1 button
let addInpBtn = document.getElementById('add_inp')
let createForm = document.getElementById('create-form')
let counter = 1
addInpBtn.addEventListener('click', () =>{
    console.log('add')
    counter += 1
    let newInp = document.createElement("input");
    newInp.type = "text";
    newInp.name = "site-" + counter;
    newInp.placeholder = 'your link'
    newInp.className = 'edit-text'
    createForm.appendChild(newInp)

})




