class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:

    def __init__(self):
        self.frente = None
        self.final = None
        self.longitud = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.longitud += 1 

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("No se puede desencolar de una cola vacía")
        valor_desencolado = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.longitud -= 1
        return valor_desencolado

    def ver_frente(self):
        if self.esta_vacia():
            print("Error: Cola vacía")
            return None
        return self.frente.valor
    def obtener_longitud(self):
        return self.longitud

    def mostrar_cola(self):
        print("\nEstado actual de la cola:")
        actual = self.frente
        if not actual:
            print("<vacia>")
        else:
            while actual:
                print(f"[ {actual.valor} ]", end=" -> ")
                actual = actual.siguiente
            print("None")        