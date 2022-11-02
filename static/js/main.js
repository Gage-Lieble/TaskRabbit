
// Allows 1 button to open multiple links
function openLinks(links){
    links.forEach(link =>{
        window.open(link)
    })

    }




// Adding more links to 1 button

function getListLen(len){ // Gathers length of list for counter
    console.log(`${len} links in list`)
    let addInpBtn = document.getElementById('add_inp')
    let createForm = document.getElementById('create-form')
    let counter = len 
    addInpBtn.addEventListener('click', () =>{
        counter += 1
        console.log('add')
        let newInp = document.createElement("input");
        newInp.type = "text";
        newInp.name = "site-" + counter;
        newInp.placeholder = 'your link'
        newInp.className = 'edit-text'
        createForm.appendChild(newInp)
    
    })
    
}



