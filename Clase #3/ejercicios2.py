def division_por_restas(dividendo, divisor):

    cociente = 0
    
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    if divisor < 0:
        dividendo = -dividendo
        divisor = -divisor

    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

    return cociente

try:
    print("-"*60)
    dividendo = float(input("Ingrese el dividendo: "))
    print("-"*60)
    divisor = float(input("Ingrese el divisor: "))
    print("-"*60)
    resultado = division_por_restas(dividendo, divisor)
    
    print(f"El resultado de {dividendo} / {divisor} es {resultado}")
except ValueError as e:
    print(f"Error: {e}")
