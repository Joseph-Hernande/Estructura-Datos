class Vehiculo:
    def __init__(self, marca, combustible, tipo, nivel_combustible):
        self.marca = marca
        self.combustible = combustible
        self.encendido = False
        self.tipo = tipo
        self.nivel_combustible = nivel_combustible

    def encender(self):
        if self.nivel_combustible < 0.1:
            print("¡Advertencia! El nivel de combustible es muy bajo. Por favor, vaya a la gasolinera antes de encender el vehículo.")
        else:
            if not self.encendido:
                print("El vehículo se ha encendido.")
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
        return f"Tipo de Vehículo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible}, Encendido: {self.encendido}, Nivel de Combustible: {self.nivel_combustible:.2f} galones"


class Moto(Vehiculo):
    def __init__(self, marca, combustible, cilindrada, nivel_combustible):
        super().__init__(marca, combustible, "Moto", nivel_combustible)
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Cilindrada: {self.cilindrada}"


class Carro(Vehiculo):
    def __init__(self, marca, combustible, num_puertas, nivel_combustible):
        super().__init__(marca, combustible, "Carro", nivel_combustible)
        self.num_puertas = num_puertas

    def __str__(self):
        return super().__str__() + f", Número de Puertas: {self.num_puertas}"



moto1 = Moto("Honda", "Gasolina", "250cc", 0.05)
moto1.encender()  
print(moto1)


carro1 = Carro("Toyota", "Gasolina", 4, 0.2)
carro1.encender()  
print(carro1)
