
 //Computadora
document.addEventListener ("DOMContentLoaded", ()=> {

    const campoFechaUsuario = document.getElementById ("fecha-reservaPc");
    const labelFechaUsuario = document.getElementById ("labelFechaPc");

    campoFechaUsuario.addEventListener ("change", ()=>{
        const fechaUsuario = new Date (campoFechaUsuario.value);
        const fechaActual = new Date ();
        
        if (fechaUsuario < fechaActual){
            campoFechaUsuario.style.color = "red";
            campoFechaUsuario.style.border = "5px solid red";
            labelFechaUsuario.style.top = "1px";
            labelFechaUsuario.style.fontSize = "12px"
            campoFechaUsuario.setCustomValidity("Fecha invalida");
            
            
        }else {
            campoFechaUsuario.style.color = "gray";
            campoFechaUsuario.style.border = "3px solid violet";
            campoFechaUsuario.setCustomValidity("");
            
        }
    });
});





