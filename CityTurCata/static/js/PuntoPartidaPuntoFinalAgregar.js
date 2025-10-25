//pc
const puntoPartidaPc = document.getElementById("partidaNuevaPC");
const finalRecorridoPc = document.getElementById("finalNuevoPc");


puntoPartidaPc.addEventListener('change',()=>{
    const partida1 = puntoPartidaPc.value;

    console.log("¡El evento change se ha disparado!"); // <-- Usa console.log
    console.log("El valor seleccionado es:", partida1);
    Array.from(finalRecorridoPc.options).forEach(llegadas =>{

        if(llegadas.value === partida1){
            llegadas.disabled=true;
            llegadas.style.color ="red";
        }
        else{
            llegadas.disabled =false;
            llegadas.style.color = "gray"
        }
    })

})



