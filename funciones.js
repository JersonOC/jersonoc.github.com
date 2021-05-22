// Mensaje de Bienvenida
function Mostrar(){
    var miDiv = document.getElementById("bienvenido");
    if(miDiv.style.display==="none"){
        //Muestro la etiquena Div
        miDiv.style.display = "block";
    }else{
        //Oculto la etiqueta Div
        miDiv.style.display = "none";
    }
}