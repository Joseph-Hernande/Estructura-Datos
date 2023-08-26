edades = [12, 42, 45, 60, 50, 10]

def promedio_edades(edades):
    suma = 0
    for n in edades:
        suma = suma + n
    return suma / len(edades)

promedio = promedio_edades(edades)

print(f"El promedio de las edades es: {promedio}")
