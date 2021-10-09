from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import RadioField, StringField
from wtforms.fields.simple import SubmitField, TextAreaField

class FormContactanos(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)]) 
    correo = StringField('Correo Electrónico', validators=[validators.required(), validators.length(max=150)])
    mensaje = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=500)])
    tipo = RadioField('Tipo de Mensaje', choices=[('P','Pregunta'),('Q','Queja'),('S','Sugerencia')])
    enviar = SubmitField('Enviar Mensaje')

class FormRespuesta(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)]) 
    correo = StringField('Correo Electrónico', validators=[validators.required(), validators.length(max=150)])
    mensaje_original = TextAreaField('Mensaje Original', validators=[validators.required(), validators.length(max=500)])
    respuesta = TextAreaField('Respuesta', validators=[validators.required(), validators.length(max=500)])
    enviar = SubmitField('Enviar Respuesta')
