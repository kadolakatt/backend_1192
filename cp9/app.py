import yagmail as yagmail

from flask import Flask, render_template, request, redirect, url_for
from utils import * # isEmailValid
#import utils utils.isEmailValid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/registro/covid', methods=['GET','POST'])
def registro_covid(): 
    if request.method == "GET":
        return render_template('registro.html')
    else:
        if request.form:
            nombre = request.form['nombre']
            usuario = request.form['usuario']
            sexo = request.form['sexo']
            email = request.form['email']
            contrasena = request.form['contrasena']
            declaracion = request.form['declaracion']

            errores = ""
            exito = ""

            if len(nombre) <= 0:
                errores+= "Debe escribir un nombre válido. "
            
            if not isUsernameValid(usuario):
                errores+= "Debe escribir un nombre de usuario válido. "
            
            if not isEmailValid(email):
                errores+= "Debe escribir un email válido. "
            
            if not isPasswordValid(contrasena):
                errores+= "La contraseña no cumple con los requisitos de seguridad. "
            
            if declaracion != "S":
                errores+= "Debe aceptar los terminos legales. "

            if not errores:
                exito = "Su cuenta ha sido registrada"
                yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
                yag.send(to=email, subject=exito,
                contents="Bienvenido {0}, Haz clic aqui para verificar tu cuenta.".format(nombre))
                return redirect(url_for('login'))
            else:
                return render_template('registro.html', error=errores)
