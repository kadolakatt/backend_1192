import db

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
    