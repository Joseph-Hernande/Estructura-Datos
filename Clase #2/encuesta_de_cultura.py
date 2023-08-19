import pandas as pd


url = input("Ingrese el URL de la encuesta: ").lower()

class CargarDatos:
    name = "Encuesta usuario"
    url = ""

    df = pd.read_csv(url, sep=";")

    def __init__(self, url, name):
        self.url = url
        self.name = name
        


    def CalcularPromedio(self):
        pass


    def CalcularSuma(self):
        pass



  
    

