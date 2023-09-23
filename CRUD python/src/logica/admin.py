import persistencia.conexionDB as cx

conex = cx.Conexion()
class CreateAdmin():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor()
    
    def insertarNuevoAdmin(self,nombres:str,apellidos:str,correo:str,contrasena:str,nivel:str) -> bool:
        sql = "INSERT INTO Administradores (nombres,apellidos,correo,nivel,contraseña)values (?,?,?,?,?)"
        values = (nombres,apellidos,correo,nivel,contrasena)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("Error: ",str(e))
            return False
        
               
class ReadAdmin():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor()   
         
    def authAdmin(self,correo:str,contrasena:str) -> bool:
        sql = "SELECT * FROM Administradores WHERE correo=? AND contraseña=?"
        values = (correo,contrasena)
        try:
            self._cursor.execute(sql,values)
            resultado = self._cursor.fetchone()
        except Exception as e:
            print("Error", str(e))
        if resultado:
            return True
        else: 
            return False
        
    def getAllAdmins(self)->list:
        sql = "SELECT * FROM Administradores"
        try:
            self._cursor.execute(sql)
            resultado = self._cursor.fetchall()
            return resultado
        except Exception as e:
            print("ERROR:",str(e))
            resultado = []
            return resultado
            
        
            
    
class UpdateAdmin():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor() 
        
    def actualizarContraseña(self,correo:str,nuevaContrasena:str) -> bool:
        sql = "UPDATE Administradores SET contraseña=? WHERE correo=?"
        values = (nuevaContrasena,correo)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False
    
    def cambiarNivel(self,correo:str,contrasena:str,nuevoNivel:str)->bool:
        sql = "UPDATE Administradores SET nivel=? WHERE correo=? AND contraseña=?"
        values = (nuevoNivel,correo,contrasena)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False
        
            
class DeleteAdmin():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor() 
    
    def eliminarAdmin(self,correo:str)->bool:
        sql = "DELETE FROM Administradores Where correo=?"
        values = (correo,)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False