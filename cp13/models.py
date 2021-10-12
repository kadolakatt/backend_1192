import db

#Clase para manejar los usuarios
class usuario():
    id=0
    nombre=''
    usuario=''
    correo=''
    contrasena=''

    def __init__(self, pid, pnombre, pusuario, pcorreo, pcontrasena):
        self.id = pid
        self.nombre = pnombre
        self.usuario = pusuario
        self.correo = pcorreo
        self.contrasena = pcontrasena
    
    #Metodo para verificar el usuario contra la base de datos
    def autenticar(self):
        #Este query es inseguro porque puede permitir una inyección SQL
        #sql = "SELECT * FROM usuarios WHERE usuario = '" + self.usuario + "' AND contrasena = '"  + self.contrasena + "';"    
        #Para mitigar usamos comandos SQL parametrizados
        sql = "SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?;"
        obj = db.ejecutar_select(sql, [ self.usuario, self.contrasena ])
        if obj:
            if len(obj) >0:
                return True
        
        return False

class mensaje():
    id=0
    nombre=''
    correo=''
    mensaje=''
    respuesta=''
    estado=''

    def __init__(self, pid, pnombre, pcorreo, pmensaje, prespuesta='',pestado='S'):
        self.id = pid
        self.nombre = pnombre
        self.correo = pcorreo
        self.mensaje = pmensaje
        self.respuesta = prespuesta
        self.estado = pestado

    @classmethod
    def cargar(cls, pid):
        sql = "SELECT * FROM mensajes WHERE id = ?;"
        resultado = db.ejecutar_select(sql, [ pid ])
        if resultado:
            if len(resultado)>0:
                return cls(pid, resultado[0]["nombre"], 
                resultado[0]["correo"], resultado[0]["mensaje"],
                resultado[0]["respuesta"], resultado[0]["estado"])
        
        return None
    
    def insertar(self):
        sql = "INSERT INTO mensajes (nombre, correo, mensaje, estado) VALUES (?,?,?,?);"
        afectadas = db.ejecutar_insert(sql, [ self.nombre, self.correo, self.mensaje, 'S' ])
        return ( afectadas > 0 )

    def eliminar(self):
        sql = "DELETE mensajes WHERE id = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.id ])
        return ( afectadas > 0 )

    def responder(self):
        sql = "UPDATE mensajes SET respuesta = ?, estado = 'R' WHERE id = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.respuesta, self.id ])
        return ( afectadas > 0 )

    @staticmethod
    def listado():
        sql = "SELECT * FROM mensajes ORDER BY id;"
        return db.ejecutar_select(sql, None)
    
    @staticmethod
    def listado_paginado(filas_por_pagina, numero_pagina):
        #Utiliza la sentencia LIMIT para extraer los registros paginados.
        sql = "SELECT * FROM mensajes ORDER BY id LIMIT " + str((numero_pagina-1)*filas_por_pagina) + ", " + str(filas_por_pagina) + ";"
        return db.ejecutar_select(sql, None)
