from passlib.hash import sha256_crypt
import pymysql
#region conexión
def conectarse()->None:
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Contraseña@123',
        db='bd_practica'
    )
#endregion

#region usuarios
class Usuarios():
    def __init__(self, nombre:str, correo:str, contraseña:str, status:int):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.status = status

def guardarUsuario(nombre:str, correo:str, contraseña:str):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombre, correo, contraseña) VALUES(%s, %s, %s)"),
        (nombre, correo, contraseña)
    conexion.commit()
    conexion.close()

def actualizarEstado(nombre:str, activo:int):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE status SET status = " + "'" + activo + "'" + "WHERE nombre = " + "'" + nombre + "'")
    conexion.commit()
    conexion.close()

def actualizarContraseña(nombre:str, contraseña:str):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE contraseña SET contraseña = " + "'" + contraseña + "'" + "WHERE nombre = " + "'" + nombre + "'")
    conexion.commit()
    conexion.close()
#endregion

#region setDatos
def guardarConvinacionesMulti(multiplexor:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO combinaciones(multiplexor) VALUES (%s)",
                       (multiplexor))
    conexion.commit()
    conexion.close()

def guardarConvinacionesDemulti(demultiplexor:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO combinaciones(demultiplexor) VALUES (%s)",
                       (demultiplexor))
    conexion.commit()
    conexion.close()

#endregion

#region getDatos
def comprobarUsuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario FROM usuarios")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

def getPassword(nombre:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = " + "'" + nombre + "'")
        password = cursor.fetchone()
    conexion.close() 
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas

def getConceptos(materia:str)->str:
    concepts = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        conceptos1 = cursor.execute("SELECT titulo FROM conceptos")
        conceptos1 = cursor.fetchall()
        conceptos2 = cursor.execute("SELECT descripcion FROM conceptos")
        conceptos2 = cursor.fetchall()
    conexion.close() 
    for i in range(len(conceptos1)):
        concepts.append(conceptos1.__getitem__(i))
        concepts.append(conceptos2.__getitem__(i))
    return concepts
#endregion