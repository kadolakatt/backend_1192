/*
El evento DOMContentLoaded ocurre cuando se termina de procesar
la estructura del documento HTML quiere decir que todos los elementos 
se encuentra procesados. Generalmente lo utilizamos para 
colocar aqui nuestros controladores de evento.
*/
var ruta_img;

window.addEventListener('DOMContentLoaded', function () {
   var img = document.getElementById('imgPassword');
   var password = document.getElementById("txtPassword");
    
   //el evento keyup ocurre cuando el usuario presiona y levanta una tecla
   //en la caja de texto. Aqui podemos colocar una función que evalue 
   //la fortaleza del password.
   //(NOTA: el nombre del evento es keyup no onkeyup como se colocó inicialmente.)
   password.addEventListener('keyup', function (event) {
        sp = document.getElementById('passwordStrength');
        if (password.value == "a") {
            sp.innerHTML="El password es débil..."
        }
   });
   
   //Se controla el evento mouse over de la imagen
   img.addEventListener('mouseover', (event) => {
       var password = document.getElementById("txtPassword");
       var img2 = document.getElementById('imgPassword2');

       password.type = 'text'; //cambiamos el tipo del input
       ruta_img = img.src;
       img.src = img2.value; //cambiamos la imagen a mostrar
   });
   //Controlamos el evento mouse out de la imagen
   img.addEventListener('mouseout', (event) => {
    var password = document.getElementById("txtPassword");
    password.type = 'password'; //cambiamos el tipo del input a password
    img.src = ruta_img; //cambiamos la imagen a mostrar
   });

   
});

function validar_formulario() {
    //var nombre = documento.formRegistro.txtNombre;
    var nombre = document.getElementById("txtNombre");
    var email = document.getElementById("txtEmail");
    var password = document.getElementById("txtPassword");
    var apellidos = document.getElementById("txtApellidos");
    var errores = document.getElementById("errores");
    var hay_errores = false;

    errores.innerHTML = "";
    if (nombre.value.length == 0 || nombre.value.length < 8) {
        //alert('El nombre es un campo requerido y debe tener más de 8 caracteres.');
        errores.innerHTML += 'El nombre es un campo requerido y debe tener más de 8 caracteres. <br/>';
        nombre.className = "form-control border-danger";
        hay_errores = true;
        //return false;
    }

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (!email.value.match(formato_email)) {
        //alert('Debe especificar un correo electrónico válido.');
        errores.innerHTML += 'Debe especificar un correo electrónico válido. <br/>';
        email.className = "form-control border-danger";
        hay_errores = true;
        //return false;
    }

    if (password.value.length == 0 || password.value.length < 8) {
        //alert('La contraseña es un campo requerido y debe tener más de 8 caracteres.');
        errores.innerHTML += 'La contraseña es un campo requerido y debe tener más de 8 caracteres.<br/>'
        password.className = "form-control border-danger";
        hay_errores = true;
        //return false;
    }

    if (apellidos.value.length == 0 || apellidos.value.length < 8) {
        //alert('El nombre es un campo requerido y debe tener más de 8 caracteres.');
        errores.innerHTML += 'El nombre es un campo requerido y debe tener más de 8 caracteres.<br/>'
        apellidos.className = "form-control border-danger";
        hay_errores = true;
        //return false;
    }

    return !hay_errores;

}