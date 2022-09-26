from aresta import Aresta
from copy import deepcopy
import random
class Grafo(object):
    def __init__(self):
        self.li = []

    def init_completo(self, V):
        for i in range(V):
            self.insere_vertice()
            j=0
            for j in range(i):
                self.insere_aresta(i, j, random.randrange(20,100))


    def insere_vertice(self):
        self.li.append([])

    def insere_aresta(self, x, y, peso):
        arestax = Aresta(y, peso)
        arestay = Aresta(x, peso)
        self.li[x].append(arestax)
        self.li[y].append(arestay)

    def remove_aresta(self, x, y):
        self.li[x].remove(y)
        self.li[y].remove(x)

    def remove_vertice(self, vertice):
        for i in range(len(self.li)):
            while vertice in self.li[i]:
                self.li[i].remove(vertice)
        self.li[vertice] = None

    def print_grafo(self):
        for i in range(len(self.li)):
            if(self.li[i] != None):
                print(str(i) + " -> "),
                for j in range(len(self.li[i])):
                    print(str(self.li[i][j].x) + " -> "),
                print("NULL")
    

    def dijkstra(self, v):
        dt = []
        rot = []
        for i  in range(len(self.li)):
            dt.append(float('inf'))
            rot.append(0)
        dt[v] = 0
        rot[v] = v
        V = []
        for i in range(len(self.li)):
            V.append(i)
        A = deepcopy(V)
        F = []
        while sorted(F) != sorted(V):
            minimo = float('inf')
            for elemento in A:
                if dt[elemento] < minimo:
                    minimo = elemento
            v = minimo
            F.append(v)
            A.remove(v)

            for u in self.li[v]:
                if dt[v] + u.peso < dt[u.x]:
                    dt[u.x] = dt[v] + u.peso
                    rot[u.x] = v

        return dt, rot


