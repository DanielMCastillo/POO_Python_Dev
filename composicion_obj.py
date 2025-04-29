#Composicion de objetos
class Motor:
    def __init__(self):
        self.temperatura = 0
        self.combustible = 100
        
    def encender(self):
        self.temperatura = 90
        self.combustible = 100
        print("Motor encendido")
        
    def apagar(self):
        self.temperatura = 0
        self.combustible = 0
        print("Motor apagado")
    
    def acelerar(self):
        if self.temperatura < 90:
            self.temperatura += 10
            self.combustible -= 10
            print("Acelerando...")
        else:
            print("El motor está caliente, no se puede acelerar más.")
            
class SistemaElectrico:
    def __init__(self):
        self.bateria = 100
        
    def encender(self):
        if self.bateria>5:
            print("Sistema eléctrico encendido")
            self.bateria -= 5
        else:
            print("Batería baja, no se puede encender el sistema eléctrico")
            
    def tocar_claxon(self):
        if self.bateria > 0:
            print("Beep Beep...")
            self.bateria -= 1
        else:
            print("Batería baja, no se puede tocar el claxon.")
        
    def apagar(self):
        self.bateria = 0
        print("Sistema eléctrico apagado")
    
    def cargar(self):
        if self.bateria < 100:
            self.bateria += 10
            print("Cargando batería...")
        else:
            print("La batería está completamente cargada.")
    
    def encender_luces(self):
        if self.bateria > 0:
            print("Luces encendidas")
            self.bateria -= 1
        else:
            print("Batería baja, no se pueden encender las luces.")
            
class Automovil:
    def __init__(self):
        self.motor = Motor()
        self.sistema_electrico = SistemaElectrico()
        self.velocidad = 0
        self.direccion = 0
        self.puertas = 4
        self.asientos = 5
        self.color = "Rojo"
        self.marca = "Kia"
        self.modelo = "K3"
        self.anio = 2023
        self.kilometraje = 10000
        self.precio = 3640000
        self.placa = "ABC123"
        
    
    def arrancar(self):
        self.motor.encender()
        self.sistema_electrico.encender()
        print("Automóvil arrancado")
        
    def detener(self):
        self.motor.apagar()
        self.sistema_electrico.apagar()
        print("Automóvil detenido")
        self.velocidad = 0
        self.direccion = 0
        self.kilometraje += 20
        
    def acelerar(self):
        self.motor.acelerar()
        self.velocidad += 20
        print(f"Velocidad actual: {self.velocidad} km/h")
        
    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 20
            print(f"Frenando... Velocidad actual: {self.velocidad} km/h")
        else:
            print("El automóvil ya está detenido.")
    
    def girar(self, direccion):
        if direccion == "izquierda":
            self.direccion -= 45
            print("Girando a la izquierda")
        elif direccion == "derecha":
            self.direccion += 45
            print("Girando a la derecha")
        else:
            print("Dirección no válida")
    
    def encender_luces(self):
        self.sistema_electrico.encender_luces()
        
    def tocar_claxon(self):
        self.sistema_electrico.tocar_claxon()
        

carro = Automovil()
carro.arrancar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.encender_luces()
carro.tocar_claxon()
carro.girar("izquierda")
carro.frenar()
carro.detener()


