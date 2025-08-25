from cmath import pi


class Circulo:
    def __init__(self,x,y,R):
        self.x=x
        self.y=y
        self.R=R

    def area(self):
        A=pi*self.R**2
        return A
    
    def perimetro(self):
        P=2*pi*self.R
        return P
    
    def mostrar_propiedades(self):
        
        print(f"El circulo tiene un radio de {self.R:.3f} cm y su centro es{self.x,self.y}\n" 
              f"El perimetro del circulo es:{self.perimetro():.3f}\n" 
              f"El area del circulo es:{self.area()}  ")