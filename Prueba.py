class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La cola está vacía"

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items

cola = Cola()

int su= 28

cola.agregar(1)
cola.agregar(2)
cola.agregar(3)

print("Cola actual:", cola.mostrar())
print("Elemento eliminado:", cola.eliminar())
print("Cola actualizada:", cola.mostrar())
print("¿La cola está vacía?", cola.esta_vacia())
print("Tamaño de la cola:", cola.tamano())