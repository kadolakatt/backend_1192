from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro/covid')
def registro_covid(): 
    return render_template('registro.html')