import random


class Dado:
    def __init__(self,puntos=0):
      self.puntos=puntos
        
    def lanzar_dado(self):
        self.puntos=random.randint(1,6)
        return self.puntos
    
    def mostrar_puntos(self):
        return print(f"El número de puntos obtenidos es: {self.puntos}")