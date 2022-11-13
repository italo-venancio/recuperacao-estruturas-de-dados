def decodificacao(entrada):
    pilha = []
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # percorrer a string de entrada
    for i in range(len(entrada)):
        # os caracteres sao adicionados na pilha ate ser encontrado um "]"
        if entrada[i] != "]":
            pilha.append(entrada[i])
        # foi encontrado um "]"
        else:
            substring = "" # substring vai receber os caracteres ate ser encontrado um "["
            while pilha[-1] != "[":
                substring = pilha.pop() + substring
            pilha.pop() # este pop eh para remover o "[" da pilha

            kdigitos = "" # kdigitos vai receber os numeros que antecedem o "["
            while pilha != [] and pilha[-1] in numeros:
                kdigitos = pilha.pop() + kdigitos
            pilha.append(int(kdigitos) * substring)

    return "".join(pilha)