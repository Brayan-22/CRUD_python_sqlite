import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import logica.admin as ad
import logica.cliente as cl
import re
class Vista:
    def __init__(self) -> None:
        # TODO constructor
        self._ventana = tk.Tk()
        self._ventana.resizable(False,False)
        self._ventana.configure(bg="#F4F6F7")
        
    def limpiar_ventana(self):
        for componente in self._ventana.winfo_children():
            componente.destroy()
    
    def registro(self):
        self.limpiar_ventana()
        self._ventana.title("Registro Cliente")
        self._ventana.geometry("280x250")
        botonVolver = tk.Button(self._ventana,text="Volver",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=8,font=("Arial",9),fg="black",command=self.iniciar)
        botonVolver.place(x=190,y=5)
        
        etiquetaNombres = tk.Label(self._ventana,text="Nombres: ",font=("Arial",9))
        etiquetaNombres.place(x=15,y=35)
        campoNombre = tk.Entry(self._ventana)
        campoNombre.place(x=130,y=35)
        
        etiquetaApellidos = tk.Label(self._ventana,text="Apellidos: ",font=("Arial",9))
        etiquetaApellidos.place(x=15,y=65)
        campoApellidos = tk.Entry(self._ventana)
        campoApellidos.place(x=130,y=65)
        
        etiquetaCorreo = tk.Label(self._ventana,text="Correo:",font=("Arial",9))
        etiquetaCorreo.place(x=15,y=95)
        campoCorreo = tk.Entry(self._ventana)
        campoCorreo.place(x=130,y=95)
        
        etiquetaContraseña = tk.Label(self._ventana,text="Contraseña:",font=("Arial",9))
        etiquetaContraseña.place(x=15,y=125)
        campoContraseña = tk.Entry(self._ventana)
        campoContraseña.place(x=130,y=125)
        
        etiquetaTelefono = tk.Label(self._ventana,text="Telefono: ",font=("Arial",9))
        etiquetaTelefono.place(x=15,y=155)
        campoTelefono = tk.Entry(self._ventana)
        campoTelefono.place(x=130,y=155)
        def crear()->None:
            Nombre:str = campoNombre.get()
            Apellido:str = campoApellidos.get()
            Correo:str = campoCorreo.get()
            Contra:str = campoContraseña.get()
            if len(Nombre)==0 or len(Apellido)==0 or len(Correo)==0 or len(Contra)==0 or len(campoTelefono.get())==0:
                messagebox.showwarning("ERROR","No se permite campos vacios")
                self.iniciar()
                
            try:
                Telef:int = int(campoTelefono.get())
            except Exception as e:
                print("ERROR",str(e))
                messagebox.showwarning("ERROR","El campo telefono solo permite digitos")
                self.iniciar()
                
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(pattern,Correo):
                cliente = cl.CreateCliente()
                if cliente.insertarNuevoCliente(Nombre,Apellido,Correo,Contra,Telef):
                    messagebox.showinfo("ERROR","Cliente creado")
                    self.iniciar()
                else:
                    messagebox.showerror("ERROR","Cliente ya existente")
                    self.iniciar()
            else:
                messagebox.showwarning("ERROR","Correo no admitido")
                self.iniciar()
                
        botonOk = tk.Button(self._ventana,text="Crear",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=crear)
        botonOk.place(x=105,y=195)
        self._ventana.mainloop()


    def selectTypeUser(self):
        self._ventana.title("Tipo usuario")
        self.limpiar_ventana()
        etiqueta = tk.Label(self._ventana,text="Como deseas ingresar",font=("Arial",10),bg=self._ventana["background"])
        etiqueta.place(x=90,y=60)
        botonVolver = tk.Button(self._ventana,text="Volver",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=self.iniciar)
        botonVolver.place(x=200,y=10)
        botonAdmin = tk.Button(self._ventana,text="Administrador",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=14,font=("Arial",10),fg="black",command=self.loginAdmin)
        botonAdmin.place(x=100,y=100)
        botonCliente = tk.Button(self._ventana,text="Cliente",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=14,font=("Arial",10),fg="black",command=self.loginCliente)
        botonCliente.place(x=100,y=160)
        
    
    def iniciar(self):
        self.limpiar_ventana()
        self._ventana.title("Bienvenido")
        self._ventana.geometry("300x300")
        botonLogIn = tk.Button(self._ventana,text="Iniciar sesión",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=14,font=("Arial",10),bg="#ECF0F5",fg="black",command=self.selectTypeUser)
        botonLogIn.place(x=100,y=100)
        botonSignUp = tk.Button(self._ventana,text="Registrarse",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=14,font=("Arial",10),bg="#ECF0F5",fg="black",command=self.registro)
        botonSignUp.place(x=100,y=160)
        self._ventana.mainloop()
        
    def ventanaCliente(self):
        self.limpiar_ventana()
        self._ventana.geometry("300x300")
        self._ventana.title("Cliente")   
        botonVolverInicio = tk.Button(self._ventana,text="Volver",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=self.iniciar)
        botonVolverInicio.place(x=210,y=10)
        def cambiarContra():
            ventana_emergente = tk.Toplevel(self._ventana)
            ventana_emergente.title("Cambiar Contraseña")
            ventana_emergente.geometry("280x200")
            ventana_emergente.resizable(False,False)
            etiquetaCorreo = tk.Label(ventana_emergente,text="Correo:",font=("Arial",9))
            etiquetaCorreo.place(x=15,y=15)
            campoCorreo = tk.Entry(ventana_emergente)
            campoCorreo.place(x=130,y=15)
            
            etiquetaCNueva = tk.Label(ventana_emergente,text="Contraseña nueva: ",font=("Arial",9))
            etiquetaCNueva.place(x=15,y=45)
            campoCNueva = tk.Entry(ventana_emergente)
            campoCNueva.place(x=130,y=45)
            
            def cambiar()->None:
                Correo:str = campoCorreo.get()
                ContraNueva:str = campoCNueva.get()
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if len(Correo)==0 and len(ContraNueva)==0: 
                    messagebox.showwarning("ERROR","No se permiten campos vacios")
                    ventana_emergente.destroy()
                else:
                    if re.fullmatch(pattern,Correo):
                        cliente = cl.UpdateCliente()
                        if cliente.actualizarContraseña(Correo,ContraNueva):
                            messagebox.showinfo("OK","Contraseña cambiada")
                            ventana_emergente.destroy()
                        else:
                            messagebox.showwarning("Error","Correo invalido")
                            ventana_emergente.destroy()
                    else:
                        messagebox.showwarning("ERROR","Correo no valido")
                        ventana_emergente.destroy()
                    
            botonOk = tk.Button(ventana_emergente,text="Cambiar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=cambiar)
            botonOk.place(x=105,y=165)
            ventana_emergente.mainloop()
            
        botonCambiarContra = tk.Button(self._ventana,text="Cambiar contraseña",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=18,font=("Arial",9),fg="black",command=cambiarContra)
        botonCambiarContra.place(x=95,y=165)
        
        
    def ventanaAdmin(self):
        self.limpiar_ventana()
        self._ventana.geometry("500x500")
        self._ventana.title("Administrador")
        botonVolverInicio = tk.Button(self._ventana,text="Volver",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=self.iniciar)
        botonVolverInicio.place(x=410,y=10)
        
        def nuevoAdmin()->bool:
                ventana_emergente = tk.Toplevel(self._ventana)
                ventana_emergente.title("Nuevos admin")
                ventana_emergente.geometry("280x200")
                ventana_emergente.resizable(False,False)
                etiquetaNombres = tk.Label(ventana_emergente,text="Nombres: ",font=("Arial",9))
                etiquetaNombres.place(x=15,y=15)
                campoNombre = tk.Entry(ventana_emergente)
                campoNombre.place(x=130,y=15)
                
                etiquetaApellidos = tk.Label(ventana_emergente,text="Apellidos: ",font=("Arial",9))
                etiquetaApellidos.place(x=15,y=45)
                campoApellidos = tk.Entry(ventana_emergente)
                campoApellidos.place(x=130,y=45)
                
                etiquetaCorreo = tk.Label(ventana_emergente,text="Correo: ",font=("Arial",9))
                etiquetaCorreo.place(x=15,y=75)
                campoCorreo = tk.Entry(ventana_emergente)
                campoCorreo.place(x=130,y=75)
                
                etiquetaContraseña = tk.Label(ventana_emergente,text="Contraseña: ",font=("Arial",9))
                etiquetaContraseña.place(x=15,y=105)
                campoContraseña = tk.Entry(ventana_emergente)
                campoContraseña.place(x=130,y=105)
                
                etiquetaNivel = tk.Label(ventana_emergente,text="Nivel: ",font=("Arial",9))
                etiquetaNivel.place(x=15,y=135)
                campoNivel = ttk.Combobox(ventana_emergente)
                elements = ["admin","supervisor"]
                campoNivel['values']=elements
                campoNivel.bind("<<ComboboxSelected>>")
                campoNivel.place(x=130,y=135)
                def crear()->None:
                    Nombres:str = campoNombre.get()
                    Apellidos:str = campoApellidos.get()
                    Correo:str = campoCorreo.get()
                    Contra:str = campoContraseña.get()
                    Nivel:str = campoNivel.get()
                    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    if re.fullmatch(pattern,Correo):
                        admin = ad.CreateAdmin()
                        admin.insertarNuevoAdmin(Nombres,Apellidos,Correo,Contra,Nivel)
                        ventana_emergente.destroy()
                    else:
                        messagebox.showwarning("ERROR","Correo no admitido")
                        ventana_emergente.destroy()
                        
                botonOk = tk.Button(ventana_emergente,text="Crear",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=crear)
                botonOk.place(x=105,y=165)
                ventana_emergente.mainloop()
            
            
        botonNuevoAdmin =tk.Button(self._ventana,text="Crear nuevo admin",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=16,font=("Arial",9),fg="black",command=nuevoAdmin)
        botonNuevoAdmin.place(x=190,y=450)
        etiqueta = tk.Label(self._ventana,text="Clientes: ",font=("Arial",10),bg=self._ventana["background"])
        etiqueta.place(x=220,y=5)
        
        scrollbar = ttk.Scrollbar(self._ventana)
        scrollbar.place(x=475,y=40,height=300)
        
        tabla = ttk.Treeview(self._ventana,yscrollcommand=scrollbar.set)
        tabla.place(x=15,y=40,height=300)
        scrollbar.config(command=tabla.yview)
        tabla["columns"]=("Nombres", "Apellidos","Correo","Contraseña","Telefono")
        
        tabla.column("#0",width=25)
        tabla.column("Nombres",width=85)
        tabla.column("Apellidos",width=85)
        tabla.column("Correo",width=95)
        tabla.column("Contraseña",width=85)
        tabla.column("Telefono",width=75)
        
        tabla.heading("#0",text="ID")
        tabla.heading("Nombres",text="Nombres")
        tabla.heading("Apellidos",text="Apellidos")
        tabla.heading("Correo",text="Correo")
        tabla.heading("Contraseña",text="Contraseña")
        tabla.heading("Telefono",text="Telefono")
        
        def eliminar()->None:
            seleccion = tabla.selection()
            if seleccion:
                fila = seleccion[0]
                valores = tabla.item(fila)["values"]
                cliente = cl.DeleteCliente()
                cliente.eliminarCliente(valores[2])
                tabla.delete(seleccion)
            else:
                messagebox.showwarning
        
        def modificar()->None:
            seleccion = tabla.selection()
            if seleccion:
                fila = seleccion[0]
                valores = tabla.item(fila)["values"]
                cliente = cl.UpdateCliente()
                ventana_emergente = tk.Toplevel(self._ventana)
                ventana_emergente.title("Nuevos datos")
                ventana_emergente.geometry("280x200")
                ventana_emergente.resizable(False,False)
                etiquetaNombres = tk.Label(ventana_emergente,text="Nuevos nombres: ",font=("Arial",9))
                etiquetaNombres.place(x=15,y=15)
                campoNombre = tk.Entry(ventana_emergente)
                campoNombre.place(x=130,y=15)
                campoNombre.insert(0,valores[0])
                
                etiquetaApellidos = tk.Label(ventana_emergente,text="Nuevos apellidos: ",font=("Arial",9))
                etiquetaApellidos.place(x=15,y=45)
                campoApellidos = tk.Entry(ventana_emergente)
                campoApellidos.place(x=130,y=45)
                campoApellidos.insert(0,valores[1])
                
                etiquetaCorreo = tk.Label(ventana_emergente,text="Nuevo correo: ",font=("Arial",9))
                etiquetaCorreo.place(x=15,y=75)
                campoCorreo = tk.Entry(ventana_emergente)
                campoCorreo.place(x=130,y=75)
                campoCorreo.insert(0,valores[2])
                
                etiquetaContraseña = tk.Label(ventana_emergente,text="Nueva contraseña: ",font=("Arial",9))
                etiquetaContraseña.place(x=15,y=105)
                campoContraseña = tk.Entry(ventana_emergente)
                campoContraseña.place(x=130,y=105)
                campoContraseña.insert(0,valores[3])
                
                etiquetaTelefono = tk.Label(ventana_emergente,text="Nuevo telefono: ",font=("Arial",9))
                etiquetaTelefono.place(x=15,y=135)
                campoTelefono = tk.Entry(ventana_emergente)
                campoTelefono.place(x=130,y=135)
                campoTelefono.insert(0,valores[4])
                def modif()->None:
                    correoViejo:str = valores[2]
                    nuevoNombre:str = campoNombre.get()
                    nuevoApellido:str = campoApellidos.get()
                    nuevoCorreo:str = campoCorreo.get()
                    nuevaContra:str = campoContraseña.get()
                    nuevoTelef:int = int(campoTelefono.get())
                    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    if re.fullmatch(pattern,nuevoCorreo):
                        cliente.modificarInfo(correoViejo,nuevoNombre,nuevoApellido,nuevoCorreo,nuevaContra,nuevoTelef)
                        ventana_emergente.destroy()
                    else:
                        messagebox.showwarning("ERROR","Correo no admitido")
                        ventana_emergente.destroy()
                            
                botonOk = tk.Button(ventana_emergente,text="Modificar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=modif)
                botonOk.place(x=105,y=165)
                ventana_emergente.mainloop()
            else:
                messagebox.showwarning("Error","Seleccione una fila que desee modificar")
        
        botonModificar = tk.Button(self._ventana,text="Modificar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=modificar)
        botonModificar.place(x=210,y=400)
        botonModificar.config(state="disabled")
        
        botonEliminar = tk.Button(self._ventana,text="Eliminar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=eliminar)
        botonEliminar.place(x=310,y=400)
        botonEliminar.config(state="disabled")
            
        def listar()->None:
            tabla.delete(*tabla.get_children())
            clientes = cl.ReadCliente().getAllClientes()
            
            for i in clientes:
                tabla.insert(parent="",index="end",iid=i[0],text=i[0],values=i[1:6])
            
            botonEliminar.config(state="active")
            botonModificar.config(state="active")
            self._ventana.mainloop()
            
        botonListar = tk.Button(self._ventana,text="Listar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=listar)
        botonListar.place(x=110,y=400)
        self._ventana.mainloop()
        
        
    def loginAdmin(self):    
        self.limpiar_ventana()
        botonVolver = tk.Button(self._ventana,text="Volver",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=self.selectTypeUser)
        botonVolver.place(x=200,y=10)
        self._ventana.title("Inicio de sesión administradores")
        etiquetaCorreo = tk.Label(self._ventana,text="Correo: ",font=("Arial",10),bg=self._ventana["background"])
        etiquetaCorreo.place(x=50,y=100)
        etiquetaContraseña = tk.Label(self._ventana,text="Contraseña: ",font=("Arial",10),bg=self._ventana["background"])
        etiquetaContraseña.place(x=50,y=150)
        
        campoCorreo = tk.Entry(self._ventana)
        campoCorreo.place(x=130,y=100)
        
        campoContraseña = tk.Entry(self._ventana,show="*")
        campoContraseña.place(x=130,y=150)
        def verificarCredenciales()->None:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(pattern,campoCorreo.get()):
                auth = ad.ReadAdmin()
                if auth.authAdmin(campoCorreo.get(),campoContraseña.get()):
                    self.ventanaAdmin()
                else:
                    campoContraseña.delete("0","end")
                    campoCorreo.delete("0","end")
                    messagebox.showerror("Error","Credenciales no validas")
            else:
                campoContraseña.delete("0","end")
                campoCorreo.delete("0","end")
                messagebox.showerror("Error","Credenciales no validas")
                
        botonIngresar = tk.Button(self._ventana,text="Ingresar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=verificarCredenciales)
        botonIngresar.place(x=120,y=200)
        
        
        
    def loginCliente(self):
        self.limpiar_ventana()
        botonVolver = tk.Button(self._ventana,text="Volver",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=self.selectTypeUser)
        botonVolver.place(x=200,y=10)
        self._ventana.title("Inicio de sesión clientes")
        etiquetaCorreo = tk.Label(self._ventana,text="Correo: ",font=("Arial",10),bg=self._ventana["background"])
        etiquetaCorreo.place(x=50,y=100)
        etiquetaContraseña = tk.Label(self._ventana,text="Contraseña: ",font=("Arial",10),bg=self._ventana["background"])
        etiquetaContraseña.place(x=50,y=150)
        
        campoCorreo = tk.Entry(self._ventana)
        campoCorreo.place(x=130,y=100)
        
        campoContraseña = tk.Entry(self._ventana,show="*")
        campoContraseña.place(x=130,y=150)
        def verificarCredenciales()->None:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(pattern,campoCorreo.get()):
                auth = cl.ReadCliente()
                if auth.authCliente(campoCorreo.get(),campoContraseña.get()):
                    self.ventanaCliente()
                else:
                    campoContraseña.delete("0","end")
                    campoCorreo.delete("0","end")
                    messagebox.showerror("Error","Credenciales no validas")
            else:
                campoContraseña.delete("0","end")
                campoCorreo.delete("0","end")
                messagebox.showerror("Error","Credenciales no validas")
                
        botonIngresar = tk.Button(self._ventana,text="Ingresar",relief=tk.SOLID,highlightthickness=0,borderwidth=1,height=1,width=10,font=("Arial",9),fg="black",command=verificarCredenciales)
        botonIngresar.place(x=120,y=200)
        
        
        