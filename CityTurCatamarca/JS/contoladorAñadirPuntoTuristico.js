document.addEventListener('DOMContentLoaded', function() {
 
  const inputArchivo = document.getElementById('imgPuntoTuristico');
  const spanNombreArchivo = document.getElementById('nombreArchivoSeleccionado');
  const labelDelArchivo = document.querySelector('label[for="imgPuntoTuristico"]');
  const form = document.querySelector('#formularioAgregar form'); 

  if (!inputArchivo || !spanNombreArchivo || !labelDelArchivo || !form) {
    console.error('Error JS: No se encontraron los elementos críticos.');
    return;
  }

  let fileWasSelected = false;


  labelDelArchivo.addEventListener('mousedown', function() {
     
      labelDelArchivo.classList.add('is-focused');
      labelDelArchivo.classList.remove('input-error');
      fileWasSelected = false; 
  });


  inputArchivo.addEventListener('change', function(e) {
    
      fileWasSelected = true; 
      
      labelDelArchivo.classList.remove('is-focused'); 

      if (e.target.files && e.target.files.length > 0) {
        spanNombreArchivo.textContent = e.target.files[0].name;
        labelDelArchivo.classList.add('archivo-valido');
        labelDelArchivo.classList.remove('input-error');
      } else {
        spanNombreArchivo.textContent = 'No se eligió ningún archivo';
        labelDelArchivo.classList.remove('archivo-valido');
      }
  });


  window.addEventListener('focus', function() {
      setTimeout(function() {
          if (fileWasSelected === false) {
              labelDelArchivo.classList.remove('is-focused');
          }
      }, 1); 
  });


  form.addEventListener('submit', function(event) {
      if (inputArchivo.files.length === 0) {
        event.preventDefault(); 
        labelDelArchivo.classList.add('input-error');
        spanNombreArchivo.textContent = '¡Debes seleccionar un archivo!';
      }
  });

});