#Propiedades de clase
class MiClase:
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor > 0 :
            self._valor = nuevo_valor
        else:
            print("El valor debe ser mayor que 0")

objeto = MiClase(10) 
print(objeto.valor) # 10
objeto.valor = 20 # Cambia el valor a 20
print(objeto.valor) # 20       