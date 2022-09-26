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
            if self.li[i] != None:
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

    def menor_distancia(self, v1, v2, rot): ##funcao que le o vetor rot gerado pelo dijkstra e retorna um vetor com o menor caminho
        v = []
        v.append(v2)
        j = v2
        while(rot[j] != v1):
            v.append(rot[j])
            j = rot[j]
        v.append(v1)
        return v[::-1]

    def yen(self, v1, v2, k):
        rot = self.dijkstra(v1)
        A = [{'cost': rot[0][v2], 'path': self.menor_distancia(v1, v2, rot[1])}]
        B = []

        for k in range(1, k):
            for i in range(0, len(A[-1]['path']) - 1) :
                grafo_aux = deepcopy(self)
                spurNode = A[-1]['path'][i]
                rootPath = A[-1]['path'][:i+1]
                
                for path in A:
                    p = path['path']
                    if rootPath == p[:i+1] and len(p) > i and len(grafo_aux.li[spurNode]) != 1:
                        grafo_aux.remove_aresta(p[i], p[i+1])

                saida2 = grafo_aux.dijkstra(spurNode)
                spurPath = grafo_aux.menor_distancia(spurNode, v2, saida2[1])
                total = rootPath[:-1] + spurPath
                totalPath = {'cost': self.custo_caminho(total), 'path': total}
                if totalPath not in B:
                    B.append(totalPath)
            if len(B) == 0:
                break
            B = sorted(B, key = lambda x: x['cost'])
            A.append(B[0])
            B.pop(0)
        return A

    def custo_caminho(self, cam): ##funcao para determinar o custo do caminho
        sum = 0
        v = [] #vetor que guarda os vertices visitados para evitar loops
        for i in range(len(cam) - 1):
            if cam[i] in v:
                    return float('inf')
            v.append(cam[i])
            for aresta in self.li[cam[i]]:
                if aresta.x == cam[i+1]:
                    sum += aresta.peso
                    break
        return sum



