class minPilha:
    def __init__(self):
        self.pilha = []
        self.minimo = None

    def top(self):
        if self.pilha == []:
            print("Pilha esta vazia!")
        else:
            return self.pilha[-1]

    def push(self, elemento):
        if self.pilha == []:
            self.minimo = elemento
        else:
            if elemento < self.minimo:
                self.minimo = elemento
        self.pilha.append(elemento)

    def getMin(self):
        return self.minimo

    def pop(self):
        self.pilha.pop()

    def __str__(self):
        saida = str(self.pilha)
        return saida
