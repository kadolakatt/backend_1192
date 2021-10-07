import os
import yagmail as yagmail

from flask import Flask, request, jsonify
from flask.templating import render_template
from forms import FormContactanos, FormRespuesta
from mensajes import lista_mensajes

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

#INICIO - Funciones CP10
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
#FIN - Funciones CP10

#INICIO - Funciones CP11
@app.route('/api/mensajes/listado',methods=["GET"])
def get_mensajes_json():
    return jsonify(lista_mensajes)


@app.route('/api/mensajes/ver/<id>', methods=["GET"])
def get_mensaje_json(id):
    for i in range(len(lista_mensajes)):
        if (id == lista_mensajes[i]["id"]):
            return jsonify(lista_mensajes[i])
    
    return jsonify({ "error":"No se encontró el mensaje con el id especificado." })


@app.route('/mensajes/listado', methods=["GET"])
def get_listado_mensajes():
    return render_template('listado_mensajes.html', lista=lista_mensajes)

@app.route('/mensajes/ver/<id>', methods=["GET"])
def get_mensaje(id):
    for i in range(len(lista_mensajes)):
        if (id == lista_mensajes[i]["id"]):
            return render_template('ver_mensaje.html',item=lista_mensajes[i])


@app.route('/mensajes/respuesta/<id_mensaje>', methods=["GET", "POST"])
def responder_mensaje(id_mensaje):
    if request.method == "GET":
        formulario = FormRespuesta()
        for i in range(len(lista_mensajes)):
            if (id_mensaje == lista_mensajes[i]["id"]):
                formulario.nombre.data = lista_mensajes[i]["nombre"]
                formulario.correo.data = lista_mensajes[i]["correo"]
                formulario.mensaje_original.data = lista_mensajes[i]["mensaje"]
                return render_template('responder_mensaje.html',id=lista_mensajes[i]["id"], form = formulario)
        
        return render_template('responder_mensaje.html',id=id_mensaje, mensaje="No se encontró un mensaje para el id especificado.")
    else:
        formulario = FormRespuesta(request.form)
        if formulario.validate_on_submit():
            yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
            yag.send(to=formulario.correo.data,subject="Su mensaje ha sido respondido.",
                     contents="Hola {0}. La respuesta a tu mensaje: {1} es: {2}."
                     .format(formulario.nombre.data, formulario.mensaje_original.data, formulario.respuesta.data))
            return render_template('responder_mensaje.html',id=id_mensaje, mensaje="Su respuesta ha sido enviada.")
        
        return render_template('responder_mensaje.html',id=id_mensaje, form=formulario, mensaje="Todos los datos son obligatorios.")
#FIN - Funciones CP11