def multiplicacion_por_sumas(numero1, numero2):

    resultado = 0
    
    if numero2 < 0:
        numero1 = -numero1
        numero2 = -numero2

    for _ in range(numero2):
        resultado += numero1

    return resultado

try:
    print("-"*60)
    numero1 = float(input("Ingrese el primer número: "))
    print("-"*60)
    numero2 = int(input("Ingrese el segundo número: "))
    print("-"*60)
    
    resultado = multiplicacion_por_sumas(numero1, numero2)
    
    print(f"El resultado de {numero1} x {numero2} es {resultado}")
except ValueError:
    print("Por favor, ingrese números válidos.")





