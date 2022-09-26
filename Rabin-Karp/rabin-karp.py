def Rabin_Karp(T,n,P,m): 
    q = 3354393  #Numero primo para evitar colisoes
    d = 32   # tamanho da palavra
    dM = 1 
    for i in range(m-1):  # fazendo dM = d^m-1
        dM = (d*dM)%q
    h1 = 0 
    for i in range(m):  # calculando hash do padrao
        h1 = (h1*d + ord(P[i]))%q
    h2 = 0
    for i in range(m):  # calculando hash da primeira substring de tamanho 'm' do texto
        h2 = (h2*d + ord(T[i]))%q
    i = 0
    cont = 0 #contador de ocorrencias do padrao
    while i < n-m+1:
        if h1 == h2:  # se o hashs forem iguais, incrementa o contador de ocorrencias
            cont +=1
        h2 = (h2 + d*q - ord(T[i])*dM)%q
        if i < n-m:
            h2 = (h2*d + ord(T[i+m]))%q  # calcula o valor de h2 da nova janela do texto
        i += 1
    return cont

def main():
    T = "ABRA KADABRA"
    n = len(T)
    P = "ABRA"
    m = len(P)
    print("Padrao '" + P + "' ocorre "  + str(Rabin_Karp(T, n, P, m)) + " vezes em '" + T + "'")

    T = "A AULA ESTA FICANDO INTERESSANTE"
    n = len(T)
    P = "ESTA"
    m = len(P)
    print("Padrao '" + P + "' ocorre "  + str(Rabin_Karp(T, n, P, m)) + " vezes em '" + T + "'")

    T = "ELA NASCEU DO MAR E O MAR ELA LEVOU NO OLHAR"
    n = len(T)
    P = "MAR"
    m = len(P)
    print("Padrao '" + P + "' ocorre "  + str(Rabin_Karp(T, n, P, m)) + " vezes em '" + T + "'")
    
if __name__ == "__main__":
    main()
