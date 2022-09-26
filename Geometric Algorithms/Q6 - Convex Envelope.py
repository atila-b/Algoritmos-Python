class Ponto:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.slope = 0

def montaMaxHeap(V, n):
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(V, n, i)

def maxHeapify(V, n, i):
    esq = 2*i + 1
    dir = 2*i + 2

    if esq < n and V[esq].slope > V[i].slope :
        maior= esq 
    else:
        maior = i
    if dir < n and V[dir].slope > V[maior].slope: 
        maior = dir
    if maior != i:
        V[i], V[maior] = V[maior], V[i]  # swap
        maxHeapify(V, n, maior)

def heapSort(V, n):
    montaMaxHeap(V, n)
    for i in range(n-1, 0, -1):
        V[i], V[0]  = V[0], V[i]
        maxHeapify(V, i, 0)

def PontoExtremo(P,n):
    pext = 0
    for i in range(1, n):
        if P[i].x > P[pext].x or (P[i].x == P[pext].x and P[i].y < P[pext].y):
            pext = i
    #print("Ponto extremo: x: " + str(P[pext].x) + "; y: " + str(P[pext].y))
    return pext

def slope(p1, p2):
    return (p2.y-p1.y)/(p2.x-p1.x)


def CalculaSlope(P,n): 
    P[1].slope = slope(P[0], P[1])
    slopeMin = P[1].slope

    for i in range(2, n):
        P[i].slope = slope(P[0], P[i])
        if P[i].slope < slopeMin:
            slopeMin = P[i].slope
    
    return slopeMin

def PoligonoSimples(P, n):
    extremo = PontoExtremo(P, n)
    P[extremo], P[0] = P[0], P[extremo]
    minSlope = CalculaSlope(P, n)
    P[0].slope = minSlope
    heapSort(P, n)
    if P[1].x > P[0].x:
        P[1], P[0] = P[0], P[1]
    #print("Poligono Simples: ")
    #print_pontos(P)

def orientacaoVirada(p, q, r):
    prodVet = (q.x-p.x)*(r.y-p.y)-(r.x-p.x)*(q.y-p.y)
    if prodVet == 0:
        return 0
    elif prodVet > 0:
        return -1
    else:
        return 1

def Graham(P, n):
    PoligonoSimples(P, n)
    H = [None]*n
    H[0] = P[0]
    H[1] = P[1]
    H[2] = P[2]
    m = 2
    for i in range(3, n):
        while orientacaoVirada(H[m-1], H[m], P[i]) == 1:
            m -= 1
        m += 1
        H[m] = P[i]
    #print("Poligono Convexo: ")
    #print_pontos(H)
    return [p for p in H if p != None]

def profundidade(P, n):
    i = 0
    while len(P) > 3:
        H = Graham(P, len(P))
        print("Pontos com profundidade " + str(i) + ":")
        for p in H:
            print(p.id)
            P.remove(p)
        i+=1
    
    if len(P)>0:
        print("Pontos com profundidade " + str(i) + ":")
        for p in P:
            print(p.id)



def print_pontos(P):
    print("*------------------------------------------------------------------------------*")
    for i in range(len(P)):
        if P[i] != None:
            print("Ponto " + str(P[i].id) + " = x: " + str(P[i].x) + "; y: " + str(P[i].y) + "; slope: " + str(P[i].slope))



    

def main():
    print("Imagens do exemplo implementado disponiveis em: https://github.com/atila-b/L6-PAA-images.git")
    #p0 = Ponto(1, 1, 0)
    #p1 = Ponto(2, 1, 3)
    ##p2 = Ponto(3, 4, 3)
    #p3 = Ponto(4, 4, 6)
    #p4 = Ponto(5, 6, 6)
    #p5 = Ponto(6, 6, 3)
    #p6 = Ponto(7, 9, 3)
    #p7 = Ponto(8, 9, 0)
    p1 = Ponto(1, 1, 3)
    p2 = Ponto(2, 5, 3)
    p3 = Ponto(3, 3, 5)
    p6 = Ponto(6, 3, 4)
    p5 = Ponto(5, 3, 2)
    p4 = Ponto(4, 3, 1)
    p8 = Ponto(8, 4, 4)
    p7 = Ponto(7, 3.5, 3.5)
    P = []
    P.extend([p1, p2, p3, p4, p5, p6, p7, p8])
    n = len(P)
    profundidade(P, n)


if __name__ == "__main__":
    main()