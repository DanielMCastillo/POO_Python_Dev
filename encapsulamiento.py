#Encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    #Metodo get - devuelve nombre    
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    
    #Metodo setter - asigna nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self,edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa")
                
persona = Persona("Daniel", 25)
print(persona.get_nombre())

persona.set_nombre("Juan")
print(persona.get_nombre())

persona.set_edad(50)
print(persona.get_edad())

persona.set_edad(-50)
print(persona.get_edad())
