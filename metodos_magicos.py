#Metodos magicos POO
#Los metodos magicos son funciones que se ejecutan automaticamente cuando se realizan ciertas operaciones con los objetos de una clase.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def distancia_al_origen(self):
        return (self.x**2 + self.y**2)**0.5
    
    @staticmethod
    def punto_medio(p1, p2):
        return Punto((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)  
    
    
p1 = Punto(2, 3)
p2 = Punto(4, 5)
p3 = p1 + p2
p4 = p1 - p2
pm = Punto.punto_medio(p1, p2)
print("Suma", p3)
print("Resta", p4)
print(p1 == p2)
print(p1.distancia_al_origen())
print(p2.distancia_al_origen())
print(pm)


