class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior is None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def desapilar(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior is None:
            print("No hay ningún elemento en la pila para desapilar")
            return

        print(f"Desapilar {self.superior.data}")
        self.superior = self.superior.siguiente

    def imprimir(self):
        if self.superior is None:
            print("La pila está vacía.")
            return
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal is not None:
            print(f"{nodo_temporal.data}", end=", ")
            nodo_temporal = nodo_temporal.siguiente
        print()
    
    def eliminar_nodo(self, dato_a_eliminar):
        if self.superior is None:
            print("La pila está vacía, no se puede eliminar ningún elemento.")
            return
        
        if self.superior.data == dato_a_eliminar:
            self.superior = self.superior.siguiente
            return
        
        nodo_temporal = self.superior
        while nodo_temporal.siguiente is not None and nodo_temporal.siguiente.data != dato_a_eliminar:
            nodo_temporal = nodo_temporal.siguiente

        if nodo_temporal.siguiente is not None:
            nodo_temporal.siguiente = nodo_temporal.siguiente.siguiente
        else:
            print(f"No se encontró el dato {dato_a_eliminar} en la pila")

pila1 = Pila()
pila1.apilar(4)
pila1.apilar(5)
pila1.apilar(6)
pila1.apilar(7)
pila1.apilar(8)

dato_a_eliminar = int(input("Ingrese el dato a eliminar: "))

pila1.eliminar_nodo(dato_a_eliminar)

pila1.imprimir()




