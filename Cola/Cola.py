class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
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
        