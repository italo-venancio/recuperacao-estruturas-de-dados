from decodificacao import decodificacao

s = "3[a]2[bc]"
#s = "3[a2[c]]"
#s = "2[abc]3[cd]ef"

if __name__ == '__main__':
    print(decodificacao(s))