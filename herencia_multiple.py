#Herencia Multiple
#En Python se puede heredar de varias clases a la vez
class A:
    def metodo(self):
        print("Metodo de la clase A")   
class B:
    def metodo(self):
        print("Metodo de la clase B")    

class C(A,B):
    def metodo(self):
        print("Metodo de la clase C") 

objeto = C()
objeto.metodo() # Se ejecuta el metodo de la clase A, ya que es la primera clase en la jerarquia de herencia