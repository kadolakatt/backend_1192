import os
import yagmail as yagmail

from flask import Flask, request
from flask.templating import render_template
from forms import FormContactanos

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/contactanos/', methods=["GET", "POST"])
def contactanos():
    if request.method == "GET":
        formulario = FormContactanos()
        return render_template('contactanos.html', form=formulario)
    else:
        formulario = FormContactanos(request.form)
        if formulario.validate_on_submit():
            yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
            yag.send(to=formulario.correo.data,subject="Su mensaje ha sido recibido.",
                     contents="Hola {0}, hemos recibido tu mensaje. En breve nos comunicaremos contigo.".format(formulario.nombre.data))
            return render_template('contactanos.html',mensaje="Su mensaje ha sido enviado.", form=FormContactanos())

        return render_template('contactanos.html', mensaje="Todos los campos son obligatorios.", form=formulario)