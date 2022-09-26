# -*- coding: utf-8 -*-
import time
from grafo import Grafo

def ler_saida(v1, dt, rot):
    for i in range(len(dt)):
        if i != v1:
            print("Menor distancia entre " + str(v1) +" e " + str(i) + " = " + str(dt[i]))

    for i in range(len(rot)):
        if i != v1:
            v = rot[i]
            print("Menor caminho entre " + str(v1) +" e "+ str(i) + ": "  + str(i) + " -"),
            j = int(i)
            while(rot[j] != v1):
                print(str(rot[j]) + " -"),
                j = rot[j]

            print(str(v1))

def main():
    #Verificando tempo de execucao com um numero arbitrario de vertices

    start_time = time.time()

    grafo_teste = Grafo()
    grafo_teste.init_completo(100)  #criando grafo completo
    saida1 = grafo_teste.dijkstra(0)  #aplicando dijkstra no grafo
 

    end_time = time.time()
    print(str((end_time - start_time)) + " segundos")
    
    #Testando o algoritmo com grafo apresentado em aula:

    print("Teste do algoritmo:")
    print("Grafo:")

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
    saida = grafo1.dijkstra(v1)
    ler_saida(v1, saida[0], saida[1])
    
    

    
if __name__ == '__main__':
    main()