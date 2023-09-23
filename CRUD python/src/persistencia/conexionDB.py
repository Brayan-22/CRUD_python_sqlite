import sqlite3

class Conexion:
    def __init__(self) -> None:
        # TODO constructor
        try:
            self._connection = sqlite3.connect("db\dbUsuarios.db")
        except Exception as e:
            print("Error al conectar con la base de datos: ",str(e))
            
    
    @property
    def connection(self):
        return self._connection
    
    def close_connection(self):
        self._connection.close()
        