//pc
const puntoPartidaPc = document.getElementById("partidaNuevaPC");
const finalRecorridoPc = document.getElementById("finalNuevoPc");

puntoPartidaPc.addEventListener('change',()=>{
    const partida1 = puntoPartidaPc.value;

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







