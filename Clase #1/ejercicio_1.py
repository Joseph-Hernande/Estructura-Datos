class Vehículo:
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
        self.encendido = False

    def encender(self):
        if not self.encendido:
            print("El vehículo esta encendido.")
            self.encendido = True
        else:
            print("El vehículo ya está encendido.")

    def apagar(self):
        if self.encendido:
            print("El vehículo se ha apagado.")
            self.encendido = False
        else:
            print("El vehículo ya está apagado.")

    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}, Encendido: {self.encendido}"



vehiculo1 = Vehículo("Toyota", "Gasolina")
print(vehiculo1) 
vehiculo1.encender()  
print(vehiculo1)  
vehiculo1.apagar()  
print(vehiculo1)  
