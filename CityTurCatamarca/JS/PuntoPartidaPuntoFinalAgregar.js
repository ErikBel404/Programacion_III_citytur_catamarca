//pc
const puntoPartidaPc = document.getElementById("partidaNuevaPC");
const finalRecorridoPc = document.getElementById("finalNuevoPc");

puntoPartidaPc.addEventListener('change',()=>{
    const partida1 = puntoPartidaPc.value;

    if (finalRecorridoPc.value == partida1){
        finalRecorridoPc.value= "0";
    }

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






//tablet
const puntoPartidaTablet = document.getElementById("partidaNuevaTablet");
const finalRecorridoTablet = document.getElementById("finalNuevoTablet");

puntoPartidaTablet.addEventListener('change',()=>{
    const partida2 = puntoPartidaTablet.value;

    
    if (finalRecorridoTablet.value == partida2){
        finalRecorridoTablet.value= "0";
    }

    Array.from(finalRecorridoTablet.options).forEach(llegadas =>{
        if(llegadas.value === partida2){
            llegadas.disabled=true;
            llegadas.style.color ="red";
        }
        else{
            llegadas.disabled =false;
            llegadas.style.color = "gray"
        }
    })

})

//celu
const puntoPartidaCelu = document.getElementById("partidaNuevaCelu");
const finalRecorridoCelu = document.getElementById("finalNuevoCelu");

puntoPartidaCelu.addEventListener('change',()=>{
    const partida3 = puntoPartidaCelu.value;

    if (finalRecorridoCelu.value == partida3){
        finalRecorridoCelu.value= "0";
    }

    Array.from(finalRecorridoCelu.options).forEach(llegadas =>{
        if(llegadas.value === partida3){
            llegadas.disabled=true;
            llegadas.style.color ="red";
        }
        else{
            llegadas.disabled =false;
            llegadas.style.color = "gray"
        }
    })

})
