import random
import time

lista_aleatoria = []

cantidad_elementos = 5000

for _ in range(cantidad_elementos):
    numero_aleatorio = random.randint(1, 10000)
    lista_aleatoria.append(numero_aleatorio)

print(lista_aleatoria)

elemento_buscado = int(input("Escriba el dato que desea buscar: "))
inicio = time.time()
if elemento_buscado in lista_aleatoria:
    print(f"{elemento_buscado} está presente en la lista.")
else:
    print(f"{elemento_buscado} no está en la lista.")
fin =time.time()
print("Tiempo de ejecucion: ", fin-inicio)

posicion = lista_aleatoria.index(elemento_buscado)

print("La posición de", elemento_buscado, "en la lista es:", posicion)