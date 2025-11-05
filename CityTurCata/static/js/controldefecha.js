document.addEventListener("DOMContentLoaded", () => {

    const campoFechaUsuario = document.getElementById("fechaReserva");

    const labelFechaUsuario = document.querySelector('label[for="fechaReserva"]');

    if (!campoFechaUsuario || !labelFechaUsuario) {
        return; 
    }


    campoFechaUsuario.addEventListener("change", () => {
        
        if (!campoFechaUsuario.value) return;

        const partes = campoFechaUsuario.value.split('-').map(Number);
        const fechaUsuario = new Date(partes[0], partes[1] - 1, partes[2]);

        const fechaActual = new Date();
        
        fechaActual.setHours(0, 0, 0, 0); 

        if (fechaUsuario < fechaActual) {
            // Fecha seleccionada es ANTERIOR a hoy (Inválido)
            campoFechaUsuario.style.color = "red";
            campoFechaUsuario.style.border = "5px solid red";
            labelFechaUsuario.style.top = "1px";
            labelFechaUsuario.style.fontSize = "12px"
            campoFechaUsuario.setCustomValidity("Fecha invalida: No puedes elegir una fecha pasada.");
            
        } else {
            // Fecha seleccionada es HOY o FUTURA (Válido)
            campoFechaUsuario.style.color = "gray"; 
            campoFechaUsuario.style.border = "3px solid green"; 
            campoFechaUsuario.setCustomValidity("");
        }
    });
});