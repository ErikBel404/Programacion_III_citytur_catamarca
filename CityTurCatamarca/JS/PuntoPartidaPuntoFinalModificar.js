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
/*
finalRecorridoPc.addEventListener('change',()=>{
    const final = finalRecorridoPc.value;

    Array.from(puntoPartidaPc.options).forEach(partidas =>{
        if(partidas.value === final){
            partidas.disabled=true;
            partidas.style.color ="red";
        }
        else{
            partidas.disabled =false;
            partidas.style.color = "gray"
        }
    })
})*/

//tablet
const puntoPartidaTablet = document.getElementById("partidaNuevaTablet");
const finalRecorridoTablet = document.getElementById("finalNuevoTablet");

puntoPartidaTablet.addEventListener('change',()=>{
    const partida2 = puntoPartidaTablet.value;

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
/*
finalRecorridoTablet.addEventListener('change',()=>{
    const final = finalRecorridoTablet.value;

    Array.from(puntoPartidaTablet.options).forEach(partidas =>{
        if(partidas.value === final){
            partidas.disabled=true;
            partidas.style.color ="red";
        }
        else{
            partidas.disabled =false;
            partidas.style.color = "gray"
        }
    })
})
*/

//celu
const puntoPartidaCelu = document.getElementById("partidaNuevaCelu");
const finalRecorridoCelu = document.getElementById("finalNuevoCelu");

puntoPartidaCelu.addEventListener('change',()=>{
    const partida3 = puntoPartidaCelu.value;

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

/*
finalRecorridoCelu.addEventListener('change',()=>{
    const final = finalRecorridoCelu.value;

    Array.from(puntoPartidaCelu.options).forEach(partidas =>{
        if(partidas.value === final){
            partidas.disabled=true;
            partidas.style.color ="red";
        }
        else{
            partidas.disabled =false;
            partidas.style.color = "gray"
        }
    })
})
    
*/