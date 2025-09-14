function validarModificacion(agregarSelect, removerSelect) {
    const seleccionadosAgregar = agregarSelect ? [...agregarSelect.selectedOptions].map(opt => opt.value) : [];
    const seleccionadosRemover = removerSelect ? [...removerSelect.selectedOptions].map(opt => opt.value) : [];

    const conflicto = seleccionadosAgregar.some(v => seleccionadosRemover.includes(v));

    if (conflicto) {
        alert("No se puede agregar y remover el mismo punto de interés al mismo tiempo.");
        return false;
    }
    return true;
}

function actualizarOpcionesParaPar(agregarSelect, removerSelect) {
    if (!agregarSelect || !removerSelect) return;

    const seleccionadosAgregar = [...agregarSelect.selectedOptions].map(opt => opt.value);
    const seleccionadosRemover = [...removerSelect.selectedOptions].map(opt => opt.value);

    // Deshabilitar en remover lo que está seleccionado en agregar
    Array.from(removerSelect.options).forEach(opt => {
        opt.disabled = seleccionadosAgregar.includes(opt.value);
    });

    // Deshabilitar en agregar lo que está seleccionado en remover
    Array.from(agregarSelect.options).forEach(opt => {
        opt.disabled = seleccionadosRemover.includes(opt.value);
    });
}

window.addEventListener("load", () => {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        const agregar = form.querySelector('#interes-agregar, .interes-agregar');
        const remover = form.querySelector('#interes-remover, .interes-remover');

        if (!agregar || !remover) return; 

        form.addEventListener("submit", e => {
            if (!validarModificacion(agregar, remover)) {
                e.preventDefault();
            }
        });

        const handler = () => actualizarOpcionesParaPar(agregar, remover);
        agregar.addEventListener("change", handler);
        remover.addEventListener("change", handler);

        handler();
    });
});
