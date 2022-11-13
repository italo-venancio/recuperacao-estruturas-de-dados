from minpilha import minPilha

def teste_minpilha():
    pilha = minPilha()
    pilha.push(2)
    pilha.push(4)
    print(pilha.top())
    print(pilha.getMin())
    pilha.pop()
    pilha.push(-1)
    print(pilha.getMin())

if __name__ == '__main__':
    teste_minpilha()