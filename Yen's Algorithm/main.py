# -*- coding: utf-8 -*-
from grafo import Grafo

def ler_saida(A):
    print("Caminhos mais curtos:")
    for i in range(len(A)):
        print(str(i + 1) + "- " + str(A[i]['path']) + " custo: " + str(A[i]['cost']))

def main():

    print("Teste do algoritmo de Yen:")
    print("Grafo 1:")

    grafo1 = Grafo()
    for i in range(10):
        grafo1.insere_vertice()
    grafo1.insere_aresta(0, 1, 60)
    grafo1.insere_aresta(0, 2, 54)
    grafo1.insere_aresta(0, 3, 42)
    grafo1.insere_aresta(1, 3, 71)
    grafo1.insere_aresta(2, 3, 56)
    grafo1.insere_aresta(5, 3, 52)
    grafo1.insere_aresta(4, 3, 26)
    grafo1.insere_aresta(6, 3, 87)
    grafo1.insere_aresta(1, 5, 29)
    grafo1.insere_aresta(2, 4, 67)
    grafo1.insere_aresta(5, 6, 20)
    grafo1.insere_aresta(4, 6, 70)
    grafo1.insere_aresta(7, 6, 36)
    grafo1.insere_aresta(8, 6, 59)
    grafo1.insere_aresta(9, 6, 32)
    grafo1.insere_aresta(4, 8, 73)
    grafo1.insere_aresta(5, 7, 25)
    grafo1.insere_aresta(7, 9, 25)
    grafo1.insere_aresta(8, 9, 26)
    grafo1.print_grafo()
    v1 = 0
    print("K = 4:")
    ler_saida(grafo1.yen(v1, 9, 4))
    print("K = 5:")
    ler_saida(grafo1.yen(v1, 9, 5))

    print("Grafo 2:")
    grafo2 = Grafo()
    for i in range(6):
        grafo2.insere_vertice()
    grafo2.insere_aresta(0, 1, 3)
    grafo2.insere_aresta(0, 2, 2)
    grafo2.insere_aresta(1, 2, 1)
    grafo2.insere_aresta(1, 3, 4)
    grafo2.insere_aresta(2, 3, 2)
    grafo2.insere_aresta(2, 4, 3)
    grafo2.insere_aresta(4, 3, 2)
    grafo2.insere_aresta(5, 3, 1)
    grafo2.insere_aresta(5, 4, 2)
    grafo2.insere_aresta(5, 0, 6)
    grafo2.print_grafo()
    print("K = 3:")
    ler_saida(grafo2.yen(v1, 5, 3))
    print("K = 4:")
    ler_saida(grafo2.yen(v1, 5, 4))

    print("Grafo 3:")
    grafo3 = Grafo()
    for i in range(7):
        grafo3.insere_vertice()
    grafo3.insere_aresta(0, 1, 6)
    grafo3.insere_aresta(0, 2, 4)
    grafo3.insere_aresta(0, 3, 3)
    grafo3.insere_aresta(1, 3, 2)
    grafo3.insere_aresta(1, 6, 7)
    grafo3.insere_aresta(2, 3, 3)
    grafo3.insere_aresta(2, 4, 5)
    grafo3.insere_aresta(3, 5, 3)
    grafo3.insere_aresta(3, 4, 5)
    grafo3.insere_aresta(4, 5, 1)
    grafo3.insere_aresta(4, 6, 2)
    grafo3.insere_aresta(5, 6, 2)
    grafo3.print_grafo()
    print("K = 4:")
    ler_saida(grafo3.yen(v1, 6, 4))
    print("K = 5:")
    ler_saida(grafo3.yen(v1, 6, 5))

    
    

    
if __name__ == '__main__':
    main()