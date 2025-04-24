#Abstraccion Test
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return (3.14 * (self.radio**2))
    def perimetro(self):
        return (3.14*2) * self.radio
    
    
circulo = Circulo(5)
print("Area del circulo:", circulo.area())
print("Périmetro del circulo:", circulo.perimetro())
