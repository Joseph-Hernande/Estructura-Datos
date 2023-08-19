class Vehiculo:
    marca= " "
    combustible= " "
    def encender(self):
        return f"se enciende el vehiculo con combustible {self.combustible}"
    def arracar(self):
        pass
    def __init__(self,combustible,marca):
        self.marca = marca 
        self.combustible = combustible
     

carro = Vehiculo("corriente","mazda")
print(carro.marca)
print("="*10)
print(carro.encender())