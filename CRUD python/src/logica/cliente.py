import persistencia.conexionDB as cx

conex = cx.Conexion()
class CreateCliente():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor()   
        
    def insertarNuevoCliente(self,nombres:str,apellidos:str,correo:str,contrasena:str,telefono:str)->bool:
        sql = "INSERT INTO Clientes (nombres,apellidos,correo,contraseña,telefono) VALUES (?,?,?,?,?)"
        values = (nombres,apellidos,correo,contrasena,telefono)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False
        
class ReadCliente():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor()  
    
    def authCliente(self,correo:str,contrasena:str)->bool:
        sql = "SELECT * FROM Clientes WHERE correo=? AND contraseña=?"
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
        
    def getAllClientes(self)->list:
        sql = "SELECT * FROM Clientes"
        try:
            self._cursor.execute(sql)
            resultado = self._cursor.fetchall()
            return resultado
        except Exception as e:
            print("ERROR",str(e))
            resultado = []
            return resultado
            
class UpdateCliente():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor() 
        
    def actualizarContraseña(self,correo:str,nuevaContrasena:str) -> bool:
        sql = "UPDATE Clientes SET contraseña=? WHERE correo=?"
        values = (nuevaContrasena,correo)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False
        
    def actualizarTelefono(self,correo:str,nuevoTelefono:int)->bool:
        sql = "UPDATE Clientes SET telefono=? WHERE correo=?"
        values = (nuevoTelefono,correo)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False
    
    def modificarInfo(self,correoViejo:str,nuevosNombres:str,nuevosApellidos:str,nuevoCorreo:str,nuevaContraseña:str,nuevoTelefono:int)->bool:
        sql = "UPDATE Clientes SET nombres=?,apellidos=?,correo=?,contraseña=?,telefono=? WHERE correo=?"
        values = (nuevosNombres,nuevosApellidos,nuevoCorreo,nuevaContraseña,nuevoTelefono,correoViejo)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("Error",str(e))
            return False
    
class DeleteCliente():
    def __init__(self) -> None:
        # TODO constructor
        self._conexion = conex.connection
        self._cursor = self._conexion.cursor() 
    
    def eliminarCliente(self,correo:str)->bool:
        sql = "DELETE FROM Clientes Where correo=?"
        values = (correo,)
        try:
            self._cursor.execute(sql,values)
            self._conexion.commit()
            return True
        except Exception as e:
            print("ERROR: ",str(e))
            return False

        