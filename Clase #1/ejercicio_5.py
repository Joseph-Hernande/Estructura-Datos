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

    def marchar(self, distancia):
        if not self.encendido:
            print("¡Encienda el vehículo antes de marchar!")
            return

        if self.nivel_combustible == 0:
            print("El vehículo no puede marchar. Nivel de combustible agotado.")
            return

        consumo = 0.1  
        consumo_total = distancia * consumo

        if self.nivel_combustible <= consumo_total:
            print("¡Advertencia! El nivel de combustible es insuficiente. Diríjase a la gasolinera.")
            self.nivel_combustible = 0
        else:
            self.nivel_combustible -= consumo_total
            print(f"El vehículo ha marchado {distancia} km. Nivel de combustible restante: {self.nivel_combustible:.2f} galones")

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



moto1 = Moto("Honda", "Gasolina", "250cc", 0.2)
moto1.encender()
moto1.marchar(50)  
print(moto1)

carro1 = Carro("Toyota", "Gasolina", 4, 0.5)
carro1.encender()
carro1.marchar(100) 
print(carro1)
