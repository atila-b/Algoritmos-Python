import random
from copy import deepcopy

def shuffle(arr, n):
    for i in range(n-1, 0, -1):
        j = random.randrange(0, i)
        arr[i], arr[j] = arr[j], arr[i] #swap

def las_vegas(S, n, k, r): # Las Vegas Algorithm
    achou = False

    while achou == False:
        C = []
        for i in range(k):
            shuffle(S, n)
            C.append(deepcopy(S))

        j=0
        while j < k and valida(C, j, r) == True:
            j+=1

        if j == k:
            achou = True
            print(C)
            return C


def valida(C, j, r):
    cont_par = 0
    cont_impar = 0
    for i in range(r):
        if C[j][i] %2 == 0:
            cont_par +=1
            cont_impar = 0
        else:
            cont_impar +=1
            cont_par = 0
        if cont_par >= 3 or cont_impar >=3:
            return False

    return True 

def main():
    S = [1, 4, 8, 9, 3, 5, 6, 2, 10, 7]
    n = len(S)
    random.shuffle(S)
    print("Vetor embaralhado sem 3 números de mesma paridade consecutivos:")
    las_vegas(S, n, 1, n)

if __name__ == "__main__":
    main()
