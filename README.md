# Mision TIC 2022
Programacion de Backend con Flask y Python.

Pasos de configuracion de los proyectos:

1. Creamos una carpeta la nombramos con el nombre del proyecto.
2. Abrimos visual studio code y abrimos la carpeta de nuestro proyecto.
3. Abrimos una ventana de terminal en visual studio code
4. ejecutamos python --version
5. ejecutamos pip --version

6. Si el paso 5 devolvió error descargar pip descargando y ejecutando el script de python: https://bootstrap.pypa.io/get-pip.py
   o instalar una versión más reciente de python. El script se ejecuta python get-pip.py.

7. Si la versión de python devuelta en el paso 4 es inferior a 3.7, es recomendable actualizarla a una más reciente. 
   Si no se deberá descargar e instalar virtualenv.

8. Crear el entorno virtual con el comando python -m venv <<nombre_entorno>>

9. Activar el enviroment:
	Si la consola es powershell el comando es <<nombre_entorno>>\scritps\activate.ps1
	Si la consola es cmd el comando es <<nombre_entorno>>\scripts\activate.bat
	Si la consola es de linux o mac source <<nombre_entorno>>/bin/activate

10. Para deactivar el entorno lo hacemos con el comando deactivate

11. Con el entorno virtual activado corremos pip install flask para instalar la versión de flask

12. Para verificar que flask quedó instalado podemos correr pip freeze

13.	Crear el código de la primera aplicación en Flask: diapositivas 11 y 12
    D11:
		from flask import Flask
		app = Flask(__name__)

		@app.route('/')
		def hola_mundo():
			return "Hola, Mundo!"
	
	D12:
		(1) Importar el objeto Flask desde el paquete flask.
		
		(2) Crear instancia de aplicación Flask con el nombre app. Pasa la variable especial __name__ 
		
			que contiene el nombre del módulo Python actual. Se utiliza para indicar a la instancia 
			dónde está ubicada. Necesitará hacerlo porque Flask configura algunas rutas en segundo plano.
			
		(3)  El  decorador  route  de la aplicación (app) es el encargado  de  decirle  a Flask qué URL debe ejecutar su correspondiente función.
		
		(4)  El nombre de la función será usado para generar internamente URLs a partir de dicha función.
		
		(5)  Por último, la  función  retorna  la  respuesta  que  será  mostrada  en el navegador del usuario.
		


14. Vas a configurar VSCode para poder correr nuestro proyecto:
		- En VSCode vamos abrir la paleta de comandos. Buscamos el comando Python: Select Interpreter (Pyton: Seleccionar Interprete)
		- Vamos a elegir la opción que se llame como nuestro entorno virtual creado.
		- Creamos una nueva terminal y esta activará automaticamente el entorno virtual por nosotros.

15. Para configurar el depurador y poder trabajarlo en el desarrollo de nuestra aplicación web. Vamos a irnos al menu de debug a la izquierda.
	Luego ir al menu de Run (ejecutar) y hacer clic en Add Configuration (Añadir Configuración). Esto creará un archivo launch.json donde se agregará
	las configuraciones para correr el debugger. Guardamos la configuración y vamos al menu Run (Ejecutar) y luego clic en Start Debug o iniciar depuración.

		
	 
16. Hay un error en el nombre de la carpeta debe ser templates en lugar de template, enunciado componente practico.