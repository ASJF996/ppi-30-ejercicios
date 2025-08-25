class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
    
    def presentarse(self):
        print(f"Mi nombre es: {self.nombre},tengo {self.edad},pertenesco al genero {self.genero}")
    
    def adulto(self):
        if self.edad>=18:
            return True
        else:
            return False