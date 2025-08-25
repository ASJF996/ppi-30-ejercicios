class Empleado:
    def __init__(self,nombre,funcion,salario,horas_trabajadas=0):
        self.nombre=nombre
        self.funcion=funcion
        self.salario=salario
        self.horas_trabajadas=horas_trabajadas

    def trabajar(self,numero_horas):
        self.horas_trabajadas+=numero_horas
        return print(f"El empleado ha trabajado {self.horas_trabajadas} horas")
    def info_sueldo(self):
        print(f"El empleado {self.nombre} recibe un salario de {self.salario} euros")
    def dar_aumento(self,cantidad):
        self.salario+=cantidad
        print(f"El empleado {self.nombre} ha recibido un aumento de {cantidad}, \n"
              f"lo que le da un salario de {self.salario} ")
        
    def info_funcion(self):
        print(f"El empleado {self.nombre} trabaja como {self.funcion}")