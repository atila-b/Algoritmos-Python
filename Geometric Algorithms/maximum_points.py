import random

class Ponto:
    def __init__(self, x, y):
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
            if L[i].x > R[j].x:
                arr[k] = L[i]
                i += 1
            elif L[i].x < R[j].x:
                arr[k] = R[j]
                j += 1
            else:
                if L[i].y > R[j].y:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
  
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def pontos_maximos(P, n):
    mergeSort(P)
    maximos = []
    max = P[0]
    maximos.append(P[0])
    for i in range(1, n):
        if max.x >= P[i].x and max.y >= P[i].y:
            if max.x == P[i].x and max.y == P[i].y:
                maximos.pop(len(maximos)-1)
                if len(maximos) > 0:  
                    max = maximos[len(maximos)-1]
                else:    
                    max.x = float('-inf')
                    max.y = float('-inf')
        else:
            maximos.append(P[i])
            max = P[i]
    print_pontos(maximos)

def print_pontos(P):
    print("*------------------------------------------------------------------------------*")
    for i in range(len(P)):
        if P[i] != None:
            print("Ponto " + str(i+1) + " = x: " + str(P[i].x) + "; y: " + str(P[i].y))

def main():
    p1 = Ponto(2, 4)
    p2 = Ponto(4, 4)
    p3 = Ponto(5, 3)
    p4 = Ponto(4, 6)
    p5 = Ponto(5, 4)
    p6 = Ponto(5, 10)
    p7 = Ponto(5, 12)
    p8 = Ponto(4, 2)
    p9 = Ponto(4, 13)
    p10 = Ponto(5, 12)

    V1 = []
    V1.extend([p1, p2, p3]) 
    print("Exemplo 1:")   # exemplo do enunciado
    print_pontos(V1)
    print("Pontos maximos do exemplo 1:")
    pontos_maximos(V1, len(V1))

    print("Exemplo 2:") # o ponto (5, 12) aparece 2 vezes, logo ele nao eh maximal, e o maximal passa a ser (5, 10)
    V2 = [] 
    V2.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])   
    print_pontos(V2)
    print("Pontos maximos do exemplo 2:")
    pontos_maximos(V2, len(V2))

if __name__ == "__main__":
    main()
