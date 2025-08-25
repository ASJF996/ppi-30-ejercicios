class Operacion:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def suma(self):
        sum=self.x+self.y
        return print(f"la suma de los numeros {self.x} {self.y} es igual a :{sum:.4f}")
    
    def multiplicacion(self):
        mult=self.x*self.y
        return print(f"la multiplicacion de los numeros {self.x} {self.y} es igual a :{mult:.4f}")
    
    def division(self):
        if self.y!=0:
            division=self.x/self.y
        else:
            print(f"la division de {self.x} por {self.y} no es posible")    
        return print(f"la suma de los numeros{self.x} {self.y}es igual a {division:.4f}")
    
 