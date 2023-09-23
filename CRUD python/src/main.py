import presentacion.diseño as d

class App:
    def __init__(self) -> None:
        # TODO constructor
        pass
    
    def iniciar(self):
        Miapp = d.Vista()
        Miapp.iniciar()
        
        
    def main(self): 
        self.iniciar()

#inicio programa
programa = App()
programa.main()
