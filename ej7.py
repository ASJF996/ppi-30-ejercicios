from ej6 import Persona

class Estudiante(Persona):
    def __init__(self,nombre,edad,genero,nivel):
        super().__init__(nombre,edad,genero)
        self.nivel=nivel
    def inscripcion(self,estudiantes_inscritos):
        estudiante=self.nombre,self.edad,self.genero,self.nivel
        estudiantes_inscritos.append(estudiante)

        return estudiantes_inscritos