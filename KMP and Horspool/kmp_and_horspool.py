def ComputaNext(P, m, next):
    next[0] = -1 #casos base
    next[1] = 0
    for i in range(2, m):
        j = next[i-1] + 1
        while P[i-1] != P[j] and j>0:
            j = next[j] + 1
        next[i] = j
    
def KMP(T,n,P,m):
    next = []
    for i in range(m):  # inicializanto tabela next
        next.append(None)
    ComputaNext(P,m,next)
    i = 0
    j = 0
    index = 0
    while i < n:  # percorrendo o texto
        if P[j] == T[i]: #comparando o path e o text
            j += 1
            i += 1
            if j == m:  # caso verdadeiro, o padrao foi achado
                index = i-m
                j = next[j-1] + 1
        else:  # senao busca o proximo apontador
            if j == 0:
                i += 1
            else:
                j = next[j-1] + 1
    return index

def ComputaDeslocamento(P, m):
    D = [m]*256   # inicializa a tabela com o tamanho do alfabeto e insere m em todas as posicoes
    for j in range(m-1):
        D[ord(P[j])] = m-1-j    #altera o deslocamento na posição do caracter
    return D

def Horspool(T, n, P, m):
    D = ComputaDeslocamento(P, m)  #construindo tabela de deslocamento
    i = m-1
    index = -1
    while i < n:
        k = 0
        while k < m and P[m-1-k] == T[i-k]:
            k +=1
        if k == m:
            index = i-m+1
        i = i + D[ord(T[i])]
    return index

def main():
    print("Algoritmo KMP:")

    T = "ABRA KADABRA"
    n = len(T)
    P = "ABRA"
    m = len(P)
    print("Padrao '" + P + "' ocorre pela ultima vez no indice "  + str(KMP(T, n, P, m)) + " da string '" + T + "'")

    T = "A AULA ESTA FICANDO INTERESSANTE"
    n = len(T)
    P = "ESTA"
    m = len(P)
    print("Padrao '" + P + "' ocorre pela ultima vez no indice "  + str(KMP(T, n, P, m)) + " da string '" + T + "'")

    T = "ELA NASCEU DO MAR E O MAR ELA LEVOU NO OLHAR"
    n = len(T)
    P = "MAR"
    m = len(P)
    print("Padrao '" + P + "' ocorre pela ultima vez no indice "  + str(KMP(T, n, P, m)) + " da string '" + T + "'")

    print("Algoritmo Horspool")

    T = "ABRA KADABRA"
    n = len(T)
    P = "ABRA"
    m = len(P)
    print("Padrao '" + P + "' ocorre pela ultima vez no indice "  + str(Horspool(T, n, P, m)) + " da string '" + T + "'")

    T = "A AULA ESTA FICANDO INTERESSANTE"
    n = len(T)
    P = "ESTA"
    m = len(P)
    print("Padrao '" + P + "' ocorre pela ultima vez no indice "  + str(Horspool(T, n, P, m)) + " da string '" + T + "'")

    T = "ELA NASCEU DO MAR E O MAR ELA LEVOU NO OLHAR"
    n = len(T)
    P = "MAR"
    m = len(P)
    print("Padrao '" + P + "' ocorre pela ultima vez no indice "  + str(Horspool(T, n, P, m)) + " da string '" + T + "'")

if __name__ == "__main__":
    main()
