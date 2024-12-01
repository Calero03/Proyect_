class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, producto):
        nuevo_nodo = Nodo(producto)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def recorrer(self):
        productos = []
        actual = self.head
        while actual:
            productos.append(actual.producto)
            actual = actual.siguiente
        return productos


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insertar(self, producto):
        key = producto.nombre_producto
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [producto]
        else:
            self.table[index].append(producto)

    def buscar(self, nombre_producto):
        index = self._hash(nombre_producto)
        productos = self.table[index]
        if productos:
            for producto in productos:
                if producto.nombre_producto == nombre_producto:
                    return producto
        return None
