import db

from werkzeug.security import generate_password_hash, check_password_hash

#Clase para manejar los usuarios
class usuario():
    nombre=''
    usuario=''
    correo=''
    contrasena=''

    def __init__(self, pnombre, pusuario, pcorreo, pcontrasena):
        self.nombre = pnombre
        self.usuario = pusuario
        self.correo = pcorreo
        self.contrasena = pcontrasena
    
    #Classmethod para crear instancias de usuario desde la bd.
    @classmethod
    def cargar(cls, p_usuario):
        sql = "SELECT usuario, nombre, correo FROM usuarios WHERE usuario = ?;" 
        obj = db.ejecutar_select(sql, [p_usuario])
        if obj:
            if len(obj)>0:
                return cls(obj[0]["nombre"], obj[0]["usuario"], obj[0]["correo"], '******')

        return None
        
    #Metodo para insertar el usuario en la base de datos
    def insertar(self):
        sql = "INSERT INTO usuarios (usuario, nombre, correo, contrasena) VALUES (?, ?, ?, ?);"
        
        #generate_password_hash crea un hash seguro para almacenar la contraseña del usuario en la bd 
        hashed_pwd = generate_password_hash(self.contrasena, method='pbkdf2:sha256', salt_length=32)
        afectadas = db.ejecutar_insert(sql, [self.usuario, self.nombre, self.correo, hashed_pwd])
        return (afectadas>0)

    #Metodo para verificar el usuario contra la base de datos
    def autenticar(self):
        #Este query es inseguro porque puede permitir una inyección SQL
        #sql = "SELECT * FROM usuarios WHERE usuario = '" + self.usuario + "' AND contrasena = '"  + self.contrasena + "';"    
        #Para mitigar usamos comandos SQL parametrizados
        sql = "SELECT * FROM usuarios WHERE usuario = ?;"
        obj = db.ejecutar_select(sql, [ self.usuario ])
        if obj:
            if len(obj) >0:
                #Agregamos la invocación al metodo check_password_hash
                #para verificar el password digitado contra el hash seguro almacenado en bd.
                if check_password_hash(obj[0]["contrasena"], self.contrasena):
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
