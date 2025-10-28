
const cantidadReservaPc = document.getElementById("NreservasPc");
const bloqueOriginalPc = document.getElementById("bloqueRepetitivoPc");

const contenedorBloqueNuevosPc = document.createElement("div");
bloqueOriginalPc.parentNode.insertBefore(contenedorBloqueNuevosPc,bloqueOriginalPc.nextSibling);

bloqueOriginalPc.style.display = "none";

cantidadReservaPc.addEventListener("change",actualizarBloqueRepetitivoPc);

function actualizarBloqueRepetitivoPc(){
    contenedorBloqueNuevosPc.innerHTML = "";

    const cantidadLugares = parseInt(cantidadReservaPc.value) || 0;

    for(let i=0;i<cantidadLugares;i++){
        const clonBloque = bloqueOriginalPc.cloneNode(true);
        


        clonBloque.style.display = "block";

        clonBloque.querySelector('input[name="nombrePersona"]').required = true;clonBloque.querySelector('input[name="dniPersona"]').required = true;

        const ptexto = document.createElement("p");
        ptexto.textContent = `Persona${i+1}`;
        ptexto.style.textAlign="center";
        ptexto.style.fontWeight="bold"
        ptexto.style.color="white";

        clonBloque.insertBefore(ptexto,clonBloque.firstChild);
        
        contenedorBloqueNuevosPc.appendChild(clonBloque);
    }
}
