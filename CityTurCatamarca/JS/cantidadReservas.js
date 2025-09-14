//celular

const cantidadReservaCelu = document.getElementById("NreservasCelular");
const bloqueOriginalCelu = document.getElementById("bloqueRepetitivoCelular");

const contenedorBloqueNuevosCelu = document.createElement("div");
bloqueOriginalCelu.parentNode.insertBefore(contenedorBloqueNuevosCelu,bloqueOriginalCelu.nextSibling);

bloqueOriginalCelu.style.display = "none";

cantidadReservaCelu.addEventListener("change",actualizarBloqueRepetitivoCelu);

function actualizarBloqueRepetitivoCelu(){
    contenedorBloqueNuevosCelu.innerHTML = "";

    const cantidadLugares = parseInt(cantidadReservaCelu.value) || 0;

    for(let i=0;i<cantidadLugares;i++){
        const clonBloque = bloqueOriginalCelu.cloneNode(true);
        
        clonBloque.style.display = "block";
        const ptexto = document.createElement("p");
        ptexto.textContent = `Persona${i+1}`;
        ptexto.style.textAlign="center";
        ptexto.style.fontWeight="bold"
        ptexto.style.color="white";

        clonBloque.insertBefore(ptexto,clonBloque.firstChild);
        
        contenedorBloqueNuevosCelu.appendChild(clonBloque);
    }
}

//tablet

const cantidadReservaTablet = document.getElementById("NreservasTablet");
const bloqueOriginalTablet = document.getElementById("bloqueRepetitivoTablet");

const contenedorBloqueNuevosTablet = document.createElement("div");
bloqueOriginalTablet.parentNode.insertBefore(contenedorBloqueNuevosTablet,bloqueOriginalTablet.nextSibling);

bloqueOriginalTablet.style.display = "none";

cantidadReservaTablet.addEventListener("change",actualizarBloqueRepetitivoTablet);

function actualizarBloqueRepetitivoTablet(){
    contenedorBloqueNuevosTablet.innerHTML = "";

    const cantidadLugares = parseInt(cantidadReservaTablet.value) || 0;

    for(let i=0;i<cantidadLugares;i++){
        const clonBloque = bloqueOriginalTablet.cloneNode(true);
        
        clonBloque.style.display = "block";
        const ptexto = document.createElement("p");
        ptexto.textContent = `Persona${i+1}`;
        ptexto.style.textAlign="center";
        ptexto.style.fontWeight="bold"
        ptexto.style.color="white";

        clonBloque.insertBefore(ptexto,clonBloque.firstChild);
        
        contenedorBloqueNuevosTablet.appendChild(clonBloque);
    }
}

//pc

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
        const ptexto = document.createElement("p");
        ptexto.textContent = `Persona${i+1}`;
        ptexto.style.textAlign="center";
        ptexto.style.fontWeight="bold"
        ptexto.style.color="white";

        clonBloque.insertBefore(ptexto,clonBloque.firstChild);
        
        contenedorBloqueNuevosPc.appendChild(clonBloque);
    }
}