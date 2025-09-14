
 //Computadora
document.addEventListener ("DOMContentLoaded", ()=> {

    const campoFechaUsuario = document.getElementById ("fecha-reservaPc");

    campoFechaUsuario.addEventListener ("change", ()=>{
        const fechaUsuario = new Date (campoFechaUsuario.value);
        const fechaActual = new Date ();
        
        if (fechaUsuario < fechaActual){
            campoFechaUsuario.style.color = "red";
            campoFechaUsuario.style.border = "5px solid red";
            document.getElementById ("labelFechaPc").style.borderTop= "5px solid red";
            document.getElementById ("labelFechaPc").style.borderLeft= "5px solid red";
            document.getElementById ("labelFechaPc").style.borderBottom= "5px solid red";
            campoFechaUsuario.setCustomValidity("Formato inválido");
            
        }else {
            campoFechaUsuario.style.color = "gray";
            campoFechaUsuario.style.border = "3px solid gray";
            document.getElementById ("labelFechaPc").style.borderTop= "3px solid gray";
            document.getElementById ("labelFechaPc").style.borderLeft= "3px solid gray";
            document.getElementById ("labelFechaPc").style.borderBottom= "3px solid gray";
            campoFechaUsuario.setCustomValidity("");
        }
    });
});


//Table
document.addEventListener ("DOMContentLoaded", ()=> {

    const campoFechaUsuario = document.getElementById ("fecha-reservaTablet");

    campoFechaUsuario.addEventListener ("change", ()=>{
        const fechaUsuario = new Date (campoFechaUsuario.value);
        const fechaActual = new Date ();
        
        if (fechaUsuario < fechaActual){
            campoFechaUsuario.style.color = "red";
            campoFechaUsuario.style.border = "5px solid red";
            document.getElementById ("labelFechaTablet").style.borderTop= "5px solid red";
            document.getElementById ("labelFechaTablet").style.borderLeft= "5px solid red";
            document.getElementById ("labelFechaTablet").style.borderBottom= "5px solid red";
            campoFechaUsuario.setCustomValidity("Formato inválido");
            
        }else {
            campoFechaUsuario.style.color = "gray";
            campoFechaUsuario.style.border = "3px solid gray";
            document.getElementById ("labelFechaTablet").style.borderTop= "3px solid gray";
            document.getElementById ("labelFechaTablet").style.borderLeft= "3px solid gray";
            document.getElementById ("labelFechaTablet").style.borderBottom= "3px solid gray";
            campoFechaUsuario.setCustomValidity("");
        }
    });
});



//Celular
document.addEventListener ("DOMContentLoaded", ()=> {

    const campoFechaUsuario = document.getElementById ("fecha-reservaCelular");

    campoFechaUsuario.addEventListener ("change", ()=>{
        const fechaUsuario = new Date (campoFechaUsuario.value);
        const fechaActual = new Date ();
        
        if (fechaUsuario < fechaActual){
            campoFechaUsuario.style.color = "red";
            campoFechaUsuario.style.border = "5px solid red";
            document.getElementById ("labelFechaCelular").style.borderTop= "5px solid red";
            document.getElementById ("labelFechaCelular").style.borderLeft= "5px solid red";
            document.getElementById ("labelFechaCelular").style.borderBottom= "5px solid red";
            campoFechaUsuario.setCustomValidity("Formato inválido");
            
        }else {
            campoFechaUsuario.style.color = "gray";
            campoFechaUsuario.style.border = "3px solid gray";
            document.getElementById ("labelFechaCelular").style.borderTop= "3px solid gray";
            document.getElementById ("labelFechaCelular").style.borderLeft= "3px solid gray";
            document.getElementById ("labelFechaCelular").style.borderBottom= "3px solid gray";
            campoFechaUsuario.setCustomValidity("");
        }
    });
});