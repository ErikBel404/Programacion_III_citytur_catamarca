
 //Computadora
document.addEventListener ("DOMContentLoaded", ()=> {

    const campoFechaUsuario = document.getElementById ("fecha-reservaPc");

    campoFechaUsuario.addEventListener ("change", ()=>{
        const fechaUsuario = new Date (campoFechaUsuario.value);
        const fechaActual = new Date ();
        
        if (fechaUsuario < fechaActual){
            campoFechaUsuario.style.color = "red";
            campoFechaUsuario.style.border = "5px solid red";
            campoFechaUsuario.setCustomValidity("Fecha invalida");
            
            
        }else {
            campoFechaUsuario.style.color = "gray";
            campoFechaUsuario.style.border = "3px solid violet";
            campoFechaUsuario.setCustomValidity("");
            
        }
    });
});





