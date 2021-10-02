import yagmail as yagmail

from flask import Flask, render_template, request, redirect, url_for
from utils import *

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/registro', methods=('GET', 'POST'))
def registro():
    if request.method == "GET": 
        return render_template('registro.html')
    elif request.method== "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        email = request.form['email']
        contrasena = request.form['contrasena']
        declaracion = request.form['declaracion']

        errores = ""
        exito = ""

        if len(nombre) <= 0:
            errores += "Debe escribir un nombre válido. "

        if len(apellidos) <=0:
            errores += "Debe digitar un apellido. "

        if not isEmailValid(email):
            errores += "El email es inválido. "
        
        if not isPasswordValid(contrasena):
            errores += "El password no cumple con los requisitos mínimos. "
        
        if not declaracion == "S":
            errores += "Debe aceptar los terminos legales."

        if not errores:
            exito = "Su cuenta ha sido registrada."
            yag = yagmail.SMTP('alertasmisiontic2022@gmail.com', 'prueba123')
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido {0}, usa este link para activar tu cuenta '.format(nombre + ' ' + apellidos))
            return redirect(url_for('login'))
            #return render_template('registro.html', exito=exito)
        else:
            return render_template('registro.html', errores=errores)

        

@app.route('/recuperar/password')
def recuperar_pwd():
    return render_template('recuperar.html')