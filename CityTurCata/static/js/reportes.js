// static/js/reportes.js
document.addEventListener('DOMContentLoaded', function() {
    
    // --- 1. Encuentra TODOS los elementos ---
    const boton = document.getElementById('boton-generar');
    const tipoSelect = document.getElementById('id_tipo_reporte');
    const formatoSelect = document.getElementById('id_formato_reporte');
    
    // Elementos opcionales
    const recorridoSelect = document.getElementById('id_recorrido');
    const fechaInicioInput = document.getElementById('id_fecha_inicio');
    const fechaFinInput = document.getElementById('id_fecha_fin');
    
    // Contenedores de los campos
    const campoRecorrido = document.getElementById('campo_recorrido');
    const campoFechas = document.getElementById('campo_fechas');
    const campoFechasFin = document.getElementById('campo_fechas_fin');

    // --- 2. Función para mostrar/ocultar campos ---
    function toggleCamposOpcionales() {
        // Verifica que los elementos existan antes de usarlos
        if (!tipoSelect || !campoRecorrido || !campoFechas || !campoFechasFin) {
            // Si faltan elementos, no hace nada para evitar errores
            return; 
        }

        const tipo = tipoSelect.value;
        
        campoRecorrido.style.display = 'none';
        campoFechas.style.display = 'none';
        campoFechasFin.style.display = 'none';

        if (tipo === 'reservaRecorrido') {
            campoRecorrido.style.display = 'block';
        } else if (tipo === 'estadisticasPasajeros') {
            campoFechas.style.display = 'block';
            campoFechasFin.style.display = 'block';
        }
    }
    
    // Ejecutar al cargar la página y cada vez que cambia el tipo de reporte
    toggleCamposOpcionales();
    if (tipoSelect) {
        tipoSelect.addEventListener('change', toggleCamposOpcionales);
    }

    // --- 3. Lógica del botón de Generar (CORREGIDA) ---
    if (boton) {
        boton.addEventListener('click', function() {
            
            if (!tipoSelect || !formatoSelect) {
                console.error("No se pueden encontrar los selectores de tipo o formato.");
                return;
            }

            // Lee los valores principales
            const tipoReporte = tipoSelect.value;
            const formato = formatoSelect.value;
            
            // --- ARREGLO CLAVE: Lee la URL desde el botón ---
            const urlBase = boton.dataset.baseUrl; // Lee el 'data-base-url'
            if (!urlBase) {
                console.error("No se encontró 'data-base-url' en el botón.");
                return;
            }
            const urlSinEndpoint = urlBase.replace('reportes/agregar/', ''); 

            let urlFinal = `${urlSinEndpoint}reportes/`;

            // Asigna la URL de la vista (basado en el 'value' del form)
            if (tipoReporte === 'recorridos_activos') { // Este 'value' es de tu form
                urlFinal += 'activos/'; // Este 'path' es de tu urls.py
            } else if (tipoReporte === 'paradas_utilizadas') {
                urlFinal += 'paradas/';
            } else if (tipoReporte === 'reservaRecorrido') {
                urlFinal += 'reservas/';
            } else if (tipoReporte === 'consultasReservas') {
                urlFinal += 'consultas/';
            } else if (tipoReporte === 'estadisticasPasajeros') {
                urlFinal += 'estadisticas/';
            }
            
            // Agrega los parámetros (formato y opcionales)
            const params = new URLSearchParams();
            params.append('formato', formato);
            
            // --- LÓGICA SEGURA (Evita el error 'null') ---
            if (tipoReporte === 'reservaRecorrido') {
                if (recorridoSelect) { // Revisa que el campo exista
                    params.append('recorrido_id', recorridoSelect.value);
                }
            }
            
            if (tipoReporte === 'estadisticasPasajeros') {
                if (fechaInicioInput && fechaFinInput) { // Revisa que los campos existan
                    params.append('fecha_inicio', fechaInicioInput.value);
                    params.append('fecha_fin', fechaFinInput.value);
                }
            }

            // Redirige al usuario
            window.location.href = `${urlFinal}?${params.toString()}`;
        });
    }
});