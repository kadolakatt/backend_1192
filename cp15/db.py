import sqlite3

from sqlite3 import Error

#Funcion para establecer la conexion a la base de datos
def conectar():
    try:
        conn = sqlite3.connect('db/datos.db')
        return conn
    except Error as err:
        print("Ocurrió un error al establecer la conexión: " + str(err))
        return None

#Funcion para ejecutar SQL de tipo INSERT, UPDATE, DELETE
def ejecutar_insert(_sql, lista_parametros):
    try:
        conn = conectar() #Conectamos a la BD
        if conn:
            #Creamos el objeto cursor para ejecutar SQL
            objeto_cursor = conn.cursor() 
            #Invocamos el metodo execute del cursor para ejecutar el comando
            #rowcount nos devuelve la cantidad de filas afectadas por el comando.
            filas = objeto_cursor.execute(_sql, lista_parametros).rowcount 
            #Cerramos el cursor
            objeto_cursor.close()
            #Confirmamos los cambios realizados por el cursor
            conn.commit()
            #Cerramos la conexion
            conn.close()

            return filas #retornamos la cantidad de filas afectadas.
        else:
            print("No se pudo establecer la conexión. Ver errores previos.")
            return -1
    except Error as err:
        print("Ocurrió un error al intentar ejecutar el comando: " + _sql + " - " + str(err))
        return -1


#Funcion para ejecutar los SQL tipo SELECT
def ejecutar_select(_sql, lista_pametros):
    try:
        #Establecemos la conexión
        conn = conectar()
        if conn:
            #Forzamos la conversión de los resultados de select
            #de lista de tuplas a lista de diccionarios
            conn.row_factory = fabrica_diccionarios

            #Creamos el objeto cursor para ejecutar los comandos
            objeto_cursor = conn.cursor()

            #Si hay parametros invocamos execute con la lista de parametros
            if lista_pametros:
                objeto_cursor.execute(_sql, lista_pametros)
            else:
                #Se ejecuta la instrucción sin parámetros
                objeto_cursor.execute(_sql)

            #Se devuelven las filas de la consulta en una lista
            #se almacenan en la variable filas.
            filas = objeto_cursor.fetchall()

            objeto_cursor.close()
            conn.close()

            return filas

        else:
            print("No se pudo establecer la conexión. Ver errores previos.")
            return None
    except Error as err:
        print("Ocurrió un error al intentar ejecutar el comando: " + _sql + " - " + str(err))
        return None

#Esta función sirve para convertir los resultados de un select
#de lista de tuplas a diccionarios
def fabrica_diccionarios(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d