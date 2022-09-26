# -*- coding: utf-8 -*-
from grafo import Grafo


def main():
    print("Grafo 1:")
    grafo1 = Grafo()
    for i in range(6):
        grafo1.insere_vertice()
    grafo1.insere_aresta(0, 1, 1)
    grafo1.insere_aresta(0, 2, 3)
    grafo1.insere_aresta(1, 2, 1)
    grafo1.insere_aresta(1, 3, 1)
    grafo1.insere_aresta(1, 4, 4)
    grafo1.insere_aresta(2, 3, 3)
    grafo1.insere_aresta(2, 4, 2)
    grafo1.insere_aresta(3, 4, -2)
    grafo1.insere_aresta(3, 5, 1)
    grafo1.insere_aresta(4, 5, 2)
    grafo1.print_grafo()

    grafo1.prim(0)
    grafo1.kruskal()

    print("Grafo 2:")
    grafo2 = Grafo()
    for i in range(7):
        grafo2.insere_vertice()
    grafo2.insere_aresta(0, 2, 6)
    grafo2.insere_aresta(2, 1, 3)
    grafo2.insere_aresta(2, 3, 9)
    grafo2.insere_aresta(1, 4, 8)
    grafo2.insere_aresta(1, 5, 3)
    grafo2.insere_aresta(4, 5, 2)
    grafo2.insere_aresta(5, 6, 5)
    grafo2.insere_aresta(5, 2, 1)
    grafo2.insere_aresta(3, 6, 1)

    grafo2.print_grafo()

    grafo2.prim(0)
    grafo2.kruskal()

    print("Grafo 3:")
    grafo3 = Grafo()
    for i in range(6):
        grafo3.insere_vertice()
    grafo3.insere_aresta(0, 1, 3)
    grafo3.insere_aresta(0, 2, 5)
    grafo3.insere_aresta(0, 3, 1)
    grafo3.insere_aresta(1, 4, 4)
    grafo3.insere_aresta(2, 4, 8)
    grafo3.insere_aresta(2, 3, 4)
    grafo3.insere_aresta(3, 5, 3)
    grafo3.insere_aresta(4, 5, 7)

    grafo3.print_grafo()

    grafo3.prim(0)
    grafo3.kruskal()

    
    

    
if __name__ == '__main__':
    main()