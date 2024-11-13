import pymysql
from datetime import datetime

registro = {}

def conectarse()->None:
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Contraseña@123',
        db='bd_practica'
    )

def incio(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"Fecha y hora de incio de sesion: ":now}