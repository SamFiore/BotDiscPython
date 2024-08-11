import psycopg2 as db
import dotenv
import sys
import os

# Conectamos con la base de datos
class Conexion:
    _DATABASE = None
    _USERNAME = None
    _PASSWORD = None
    _HOST = None
    _PORT = None
    _conn = None
    _curs = None


    @classmethod
    def obtenerConexion(cls):
        if cls._conn == None:
            try:
                dotenv.load_dotenv('.env')
                cls._DATABASE = os.getenv('DB_NAME')
                cls._USERNAME = os.getenv('DB_USER')
                cls._PASSWORD = os.getenv('DB_PASSWORD')
                cls._HOST = os.getenv('HOST')
                cls._PORT = os.getenv('PORT')
                print('-'.center(20,'-'))
                print(f'''
                DB: {cls._DATABASE}
                USER: {cls._USERNAME}
                PSW: {cls._PASSWORD}
                HOST: {cls._HOST}
                PORT: {cls._PORT}
                ''')
                print('-'.center(20,'-'))
                cls._conn = db.connect(dbname = cls._DATABASE, user = cls._USERNAME, password= cls._PASSWORD, host= cls._HOST, port = cls._PORT)
                return cls._conn
            except Exception as e:
                # Cambiar esto por un mensaje del bot
                print('No se pudó conectar con la base de datos: ' , e)
                sys.exit()
        else:
            return cls._conn

    @classmethod
    def obtenerCursor(cls):
        if cls._curs == None:
            try:
                cls._curs = cls.obtenerConexion().cursor()
                return cls._curs
            except Exception as e:
                # Cambiar esto por un mensaje del bot
                print('No se pudó obtener el cursor: '+e)
                sys.exit()

if __name__ == '__main__':
    Conexion().obtenerConexion()
    Conexion().obtenerCursor()
