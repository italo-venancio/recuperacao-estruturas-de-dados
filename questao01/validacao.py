def validacao(entrada):
    pilha = []
    fechamentos = [")", "]", "}"]

    # funcao para retornar a abertura correspondente ao fechamento
    def abertura(caractere):
        if caractere == ")":
            return "("
        elif caractere == "]":
            return "["
        elif caractere == "}":
            return "{"

    # percorrer a string de entrada
    for caractere in entrada:
        # se o caractere atual for um fechamento
        if caractere in fechamentos: 
            # se a pilha nao estiver vazia E se o ultimo elemento adicionado na pilha for a abertura correspondente
            if pilha != [] and pilha[-1] == abertura(caractere): 
                # entao a abertura sera removida da pilha
                pilha.pop() 
            else:
                return False

        # se o caractere atual for uma abertura
        else:
            # o caractere vai ser adicionado ao topo da pilha
            pilha.append(caractere) 

    if pilha == []: # se a pilha estiver vazia, retorna-se True
        return True
    else:
        return False
    