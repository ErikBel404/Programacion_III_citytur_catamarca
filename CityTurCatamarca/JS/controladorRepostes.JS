document.addEventListener('DOMContentLoaded', function() {
    
    const now = new Date(); 
    
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0'); 
    const day = now.getDate().toString().padStart(2, '0');
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');

    const stringFechaHoraLocal = `${year}-${month}-${day}T${hours}:${minutes}`;

    const inputFechaHora = document.getElementById('fecha-hora-input');
    if (inputFechaHora) {
        inputFechaHora.value = stringFechaHoraLocal;
    }
});