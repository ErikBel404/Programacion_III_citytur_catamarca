function validarModificacion() {
    const agregarSelect = document.getElementById("interes-agregar");
    const removerSelect = document.getElementById("interes-remover");

    const seleccionadosAgregar = [...agregarSelect.selectedOptions].map(opt => opt.value);
    const seleccionadosRemover = [...removerSelect.selectedOptions].map(opt => opt.value);

    const conflicto = seleccionadosAgregar.some(v => seleccionadosRemover.includes(v));

    if (conflicto) {
        alert("No se puede agregar y remover el mismo punto de interés al mismo tiempo.");
        return false;
    }
    return true;
}

function actualizarOpciones() {
    const agregarSelect = document.getElementById("interes-agregar");
    const removerSelect = document.getElementById("interes-remover");

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
    const form = document.getElementById("formModificar");
    const agregarSelect = document.getElementById("interes-agregar");
    const removerSelect = document.getElementById("interes-remover");

    if (form) {
        form.onsubmit = () => validarModificacion();
    }

    if (agregarSelect && removerSelect) {
        agregarSelect.addEventListener("change", actualizarOpciones);
        removerSelect.addEventListener("change", actualizarOpciones);
        actualizarOpciones(); // inicializar
    }
});