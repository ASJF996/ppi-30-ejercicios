class Nota:
    def __init__(self,nota,nombreEstudiante):
        self.nota=nota
        self.nombreEstudiante=nombreEstudiante

    def ha_pasado(self):
        if self.nota>=75:
            print(f"El estudiante {self.nombreEstudiante}ha aprobado")
        else:
            print(f"el estudiante{self.nombreEstudiante} ha reprobado")

