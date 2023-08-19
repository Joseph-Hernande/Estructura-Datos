class Vehiculo:
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
        self.encendido = False

    def encender(self):
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
        return f"Marca: {self.marca}, Combustible: {self.combustible}, Encendido: {self.encendido}"


class Moto(Vehiculo):
    def __init__(self, marca, combustible, cilindrada):
        super().__init__(marca, combustible)
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Cilindrada: {self.cilindrada}"


class Carro(Vehiculo):
    def __init__(self, marca, combustible, num_puertas):
        super().__init__(marca, combustible)
        self.num_puertas = num_puertas

    def __str__(self):
        return super().__str__() + f", Número de Puertas: {self.num_puertas}"


moto1 = Moto("Honda", "Gasolina", "250cc")
print(moto1)


carro1 = Carro("Toyota", "Gasolina", 4)
print(carro1)
