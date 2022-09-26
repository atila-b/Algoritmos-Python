from aresta import Aresta
from copy import deepcopy
class Grafo(object):
    def __init__(self):
        self.li = []

    def insere_vertice(self):
        self.li.append([])

    def insere_aresta(self, x, y, peso):
        arestax = Aresta(y, peso)
        arestay = Aresta(x, peso)
        self.li[x].append(arestax)
        self.li[y].append(arestay)

    def remove_aresta(self, x, y):
        for val in self.li[x]:
            if val.x == y:
                self.li[x].remove(val)
        for val in self.li[y]:
            if val.x == x:
                self.li[y].remove(val)

    def remove_vertice(self, vertice):
        for i in range(len(self.li)):
            if self.li[i] != None:
                for v in self.li[i]:
                    if v.x == vertice:
                        self.li[i].remove(v)
        self.li[vertice] = None

    def print_grafo(self):
        for i in range(len(self.li)):
            if(self.li[i] != None):
                print(str(i) + " -> "),
                for j in range(len(self.li[i])):
                    print(str(self.li[i][j].x) + " -> "),
                print("NULL")
    

    def prim(self, i):
        T = []
        T.append(i)
        N = []
        for j in range(len(self.li)):
            N.append(j)
        N.remove(i)
        Tmin = []
        n = len(N)
        while len(T) != n + 1:
            min = float("inf")
            aresta = {}
            for j in T:
                for k in N:
                    try:
                        for ar in self.li[j]:
                            if ar.x == k and ar.peso < min:
                                min = ar.peso
                                aresta = {'x': j, 'y': k, 'peso': ar.peso}
                    except:
                        pass
            T.append(aresta['y'])
            N.remove(aresta['y'])
            Tmin.append(aresta)

        saida = Grafo()  #construindo a saida com o vetor Tmin
        for i in range(len(self.li)):
            saida.insere_vertice()
        for aresta in Tmin:
            saida.insere_aresta(aresta['x'], aresta['y'], aresta['peso'])
        print("Arvore minima do algoritmo de Prim:")
        saida.print_grafo()

    def kruskal(self):
        H=[]
        arestas = []
        for vertice in range(len(self.li)):  #Construindo o vetor de arestas H
            for aresta in self.li[vertice]:
                aresta = {'x': vertice, 'y': aresta.x, "peso": aresta.peso}
                a1 = str(str(aresta['x']) + str(aresta['y']))
                a2 = str(str(aresta['y']) + str(aresta['x']))
                if str(a1) not in arestas and str(a2) not in arestas:
                    H.append(aresta)
                    arestas.append(str(a1))
        H = sorted(H, key = lambda x: x['peso']) #Ordenando crescente
        T = Grafo() 
        for i in range(len(self.li)):
            T.insere_vertice()
        T.insere_aresta(H[0]['x'], H[0]['y'], H[0]['peso'])
        i=1
        j=0
        while j < len(self.li) - 2 and i < len(H) - 1:
            grafo_aux = deepcopy(T)
            grafo_aux.insere_aresta(H[i]['x'], H[i]['y'], H[i]['peso'])
            if grafo_aux.dfs2_recursivo(H[i]['x']) != -1:   #verificando a existencia de ciclos com o dfs
                T.insere_aresta(H[i]['x'], H[i]['y'], H[i]['peso'])
                j += 1
            i +=1
        print("Arvore minima do algoritmo de Kruskal:")
        T.print_grafo()


    def dfs2_recursivo(self, vertice):  ## metodo de encapsulamento do dfs
        visitados = []
        grafo_aux = Grafo()
        v = []
        arestas = []
        for i in range(len(self.li)):
            grafo_aux.insere_vertice()
        return self.dfs_recursivo(grafo_aux, vertice, visitados, v, arestas)
            

    
    def dfs_recursivo(self, grafo, vertice, visitados, v, arestas):
        visitados.append(vertice)
        for i in range(len(self.li[vertice])):
            a1 = '{}{}'.format(self.li[vertice][i].x, vertice)
            a2 = '{}{}'.format(vertice, self.li[vertice][i].x)
            if self.li[vertice][i].x not in visitados:
                arestas.append(str(a1))
                found = self.dfs_recursivo(grafo, self.li[vertice][i].x, visitados, v, arestas)
                if found:
                    return found
            else:
                if str(a1) not in arestas and str(a2) not in arestas:
                    return -1   #deteccao de ciclo
        




