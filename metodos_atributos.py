#Metodos y atributos de clase
class MiClase:
    contador = 0
    
    def __init__(self):
        MiClase.contador +=1
    
    @classmethod
    def obtener_contador(cls):
        return cls.contador
    
obj1 = MiClase()
print(MiClase.obtener_contador())
obj2 = MiClase()
print(MiClase.obtener_contador())