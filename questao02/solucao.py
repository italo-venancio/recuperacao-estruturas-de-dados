def solucao(s, t):
    
    def transformar(linha):
        pilha = []
        for caractere in linha:
            # se o caractere atual for uma "#" 
            if caractere == "#":
                # o topo da pilha eh removido, ja que eh o antecessor da "#"
                pilha.pop()
            else:
                pilha.append(caractere)

        saida = "".join(pilha)
        return saida

    s = transformar(s)
    t = transformar(t)    

    if s == t:
        return True
    else:
        return False