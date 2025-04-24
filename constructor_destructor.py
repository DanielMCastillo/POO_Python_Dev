#Constructores y destructores test
class MiClase():
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Objeto {self.nombre} creado")

    #Destructor
    def __del__(self):
        print(f"Objeto {self.nombre} destruido")

def miFuncion():
    obj_f = MiClase("F")    
    
obj_a = MiClase("A")
obj_b = MiClase("B")
obj_c = MiClase("C")
miFuncion()


        