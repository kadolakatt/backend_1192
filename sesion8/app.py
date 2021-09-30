#Importamos del módulo flask la clase Flask
#que es la clase principal de nuestra aplicación web
from flask import Flask

#Creamos una nueva instancia de la aplicación Flask
app = Flask(__name__)

#Decorador para establecer la URL mediante la cual 
#el navegador va acceder a esta funcion llamado hola_mundo
@app.route('/') 
def hola_mundo():
    #la instrucción return devuelve los datos o el contenido que el navegador debe mostrar
    return "<h1>Hola Mundo</h1>"

