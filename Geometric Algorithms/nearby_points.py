import math

class Ponto:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
  
        mergeSort(L)
        mergeSort(R)
        merge(arr, L, R)

def merge(arr, L, R):
    i=j=k=0

    while i < len(L) and j < len(R):
            if L[i].x < R[j].x:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
  
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge2(arr, L, R, meio, d):
    i=j=k=0

    while i < len(L) and j < len(R) and k < len(arr):
        flag = 0
        while (L[i].x > meio+d or L[i].x < meio-d):
            i+=1
            if i == len(L):
                flag = 1
                break
        while (R[j].x > meio+d or R[j].x < meio-d): 
            j+=1
            if j == len(R):
                flag = 1
                break
        if flag == 0:
            if L[i].y < R[j].y:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

    while i < len(L) and k < len(arr):
        arr[k] = L[i]
        i += 1
        k += 1
  
    while j < len(R) and k < len(arr):
        arr[k] = R[j]
        j += 1
        k += 1

def distancia(p1, p2):
    return math.sqrt((((p2.x - p1.x)**2) + ((p2.y - p1.y)**2)))

def pontos_proximos(P, esq, dir):
    #casos base
    if len(P) < 2:
        return float('inf'), [None, None]
    if len(P) == 2:
        return distancia(P[0], P[1]), [P[0], P[1]]

    #divisao de particoes 
    X = sorted(P, key = lambda p: p.x)
    Y = sorted(P, key = lambda p: p.y)
    meio = (esq+dir)//2
    Xl = X[:meio]
    Xr = X[meio+1:]
    Yl = []
    Yr = []
    for i in range(len(P)):
        if Y[i].x < X[meio].x:
            Yl.append(Y[i])
        elif Y[i].x == X[meio].x:
            if Y[i].y <= X[meio].y:
                Yl.append(Y[i])
        else:
            Yr.append(Y[i])

    #aplicando HI
    min1 = pontos_proximos(Yl, 0, len(Yl)-1)
    min2 = pontos_proximos(Yr, 0, len(Yr)-1)
    
    #conquista
    if min(min1[0], min2[0]) == min1[0]:
        par_min = min1[1]
        d = min1[0]
    else:
        par_min = min2[1]
        d = min2[0]

    Ym = [None]*(len(Yr) + len(Yl))
    merge2(Ym, Yl, Yr, X[meio].x, d)
    Ym = [p for p in Ym if p != None]

    for i in range(len(Ym)):  #calculando a distancia entre os pontos de Y'
        for j in range(i+1, len(Ym)):
            if Ym[j].y <= Ym[i].y+d:
                dist = distancia(Ym[i], Ym[j])
                if min(d, dist) == dist:
                    par_min = [Ym[j], Ym[i]]
                    d = dist
    
    return d, par_min

def print_pontos(P):
    print("*------------------------------------------------------------------------------*")
    for i in range(len(P)):
        if P[i] != None:
            print("Ponto " + str(P[i].id) + " = x: " + str(P[i].x) + "; y: " + str(P[i].y))
        else:
            print("None")

def main():
    print("Imagens do exemplo implementado disponiveis em: https://github.com/atila-b/L6-PAA-images.git")
    '''
    p1 = Ponto(1, 3, 2)
    p2 = Ponto(2, 3, 8)
    p3 = Ponto(3, 3, 4)
    p4 = Ponto(4, 3, 7)
    p5 = Ponto(5, 6, 6)
    p6 = Ponto(6, 6, 9)
    p7 = Ponto(7, 8, 3)
    p8 = Ponto(8, 8, 13)
    p9 = Ponto(9, 8, 5)
    p10 = Ponto(10, 8, 11)
    p11 = Ponto(11, 3, 5)
    p12 = Ponto(12, 3, 6)
    p13 = Ponto(13, 6, 5)
    p14 = Ponto(14, 6, 8)
    '''
    
    p1 = Ponto(1, 2, 2)
    p2 = Ponto(2, 3, 5)
    p3 = Ponto(3, 6, 7)
    p4 = Ponto(4, 7, 8)
    p5 = Ponto(5, 5, 11)
    p6 = Ponto(6, 3, 9)
    

    P = []
    #P.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14])
    P.extend([p1, p2, p3, p4, p5, p6])
    n = len(P)
    r = pontos_proximos(P, 0, n-1)
    print("Pontos mais proximos: ")
    print_pontos(r[1])
    print("menor distancia entre os pontos = " + str(r[0]))
    #print_pontos(r[1])

if __name__ == "__main__":
    main()
