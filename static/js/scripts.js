const button = document.querySelectorAll(".openmodal")
const buttonC = document.querySelectorAll(".closemodal")
/* const modal = document.querySelector("dialog") */
const viewDelete = document.querySelectorAll(".excluir")
const modalDelete = document.querySelectorAll(".deletar")

button.forEach((buttonItem) => {
    /*  button.addEventListener('click', function(event){ */
    const id = buttonItem.id
    const modal = document.querySelector(`dialog#${id}`)
    const closeButton = modal.querySelector(".closemodal")
    /*  button.addEventListener('click', function(event){ */
    closeButton.addEventListener('click', (event) => {
        console.log("teste")
        /* const m = this
        console.log({m}) */
        modal.close()
    })

    buttonItem.addEventListener('click', (event) => {
        console.log("teste")
        /* const m = this
        console.log({m}) */
       /*  let id = buttonItem.id
        const modal = document.querySelector(`dialog#${id}`) */
        modal.showModal()
    })
}
);


/* buttonC.forEach((buttonItem) => {
    const id = buttonItem.id
    const modal = document.querySelector(`dialog#${id}`)
    const closeButton = modal.querySelector(".closemodal")
    ///button.addEventListener('click', function(event){ 
    closeButton.addEventListener('click', (event) => {
        console.log("teste")
        ///const m = this
        ///console.log({m})
        modal.close()
    })
}
);
 */

modalDelete.forEach((button) =>
    button.addEventListener('click', (event)=>{
        viewDelete.showModal()
      
    })
);
