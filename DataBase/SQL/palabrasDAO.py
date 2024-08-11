from .connection import Conexion as conn
from .palabras import Palabra

class palabrasDAO:
    _SELECCIONAR = 'SELECT * FROM palabras'
    _INSERTAR = 'INSERT INTO palabras(palabra,definicion) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE palabras SET palabra=%s,definicion=%s WHERE id_word=%s'
    _ELIMINAR = 'DELETE FROM palabras WHERE id_word=%s'

    @classmethod
    def seleccionar(cls):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                curs.execute(cls._SELECCIONAR)
                registros = curs.fetchall()
                palabras = []
                for registro in registros:
                    palabra = Palabra(registro[0],registro[1],registro[2])
                    palabras.append(palabra)
                return palabras
            

    @classmethod
    def insertar(cls,word):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                valores = (word.palabra,word.definicion)
                curs.execute(cls._INSERTAR,valores)

    @classmethod
    def actualizar(cls,word):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                valores = (word.palabra,word.definicion,word.id_palabra)
                curs.execute(cls._ACTUALIZAR,valores)

    @classmethod
    def eliminar(cls,word):
        with conn.obtenerConexion():
            with conn.obtenerCursor() as curs:
                valores = (word.id_palabra,)
                curs.execute(cls._ELIMINAR,valores)

if __name__ == '__main__':
    palabra1 = Palabra(palabra='Thanks',definicion='Significa "gracias", se utiliza cuando manifietas agradecimiento con alguien')
    palabrasDAO.insertar(palabra1)
                
