class Vehiulo:
    def __init__(self,marca,velocidad_inic):
        self.marca=marca
        self.velocidad_inic=velocidad_inic
    def acelerar(self,v):
        self.velocidad_inic+=v
    def desacelerar(self,v):
        self.velocidad_inic-=v
    def mostrar_velocidad(self):
        print(f"Tu velocidad actual es{self.velocidad_inic} km/h")

class coche(Vehiulo):
    def __init__(self, marca, velocidad_inic,bocina="tuuut"):
        super().__init__(marca, velocidad_inic)
        self.bocina=bocina

    def tocar_claxon(self):
        print(self.bocina)