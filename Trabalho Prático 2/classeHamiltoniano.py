from itertools import chain, combinations
import copy
from collections import deque

class VerticeHamiltoniano():
    def __init__(self, vertices, v):
        self.vertices = vertices
        self.vertice = v
        self.visitado = False
        self.adjacentes = []

    def inserir(self, v):
        if len(self.adjacentes) >= self.vertices:
            print("Lista Cheia!")
        else:
            self.adjacentes.append(v)

    def remover(self, u):
        comparacoes = 0

        for i in range(len(self.adjacentes)):
            comparacoes += 1
            if self.adjacentes[i] == u:
                self.adjacentes.pop(i)
                break

        return comparacoes

class Hamiltoniano():
    def __init__(self, vertices):
        self.MAX = vertices
        self.vertices = []

        for i in range(self.MAX):
            self.vertices.append(VerticeHamiltoniano(self.MAX, i))

    def inserir(self, u, v):
        self.vertices[u].inserir(v)
        self.vertices[v].inserir(u)

    def removerVertice(self, v):
        comparacoes = 0

        for i in range(self.MAX):
            comparacoes += 1
            if self.vertices[i].vertice == v:
                self.vertices.pop(i)
                break

        self.MAX = len(self.vertices)

        for i in range(self.MAX):
            comparacoes += self.vertices[i].remover(v)

        return comparacoes
    
    def imprimirGrafo(self):
        for i in range(self.MAX):
            print("Vértice %d: " % self.vertices[i].vertice, end=" ")
            for j in range(len(self.vertices[i].adjacentes)):
                print(self.vertices[i].adjacentes[j], end=" ")
            print()

    def buscaLargura(self, visitado, v, vertice):
        fila = deque([])
        fila.append(v)
        visitado[v] = True
        comparacoes = 0

        while len(fila) > 0:
            u = fila.popleft()

            for i in range(len(self.vertices[u].adjacentes)):
                pos = 0

                for j in range(len(vertice)):
                    comparacoes += 1
                    if vertice[j] == self.vertices[u].adjacentes[i]:
                        pos = j
                        break

                if visitado[pos] == False:
                    visitado[pos] = True
                    fila.append(pos)

        return comparacoes

def componente(grafo, vertices, visitado, vertice):
    contador = 0
    comparacoes = 0

    for i in range(vertices):
        comparacoes += 1
        if visitado[i] == False:
            contador += 1
            comparacoes += grafo.buscaLargura(visitado, i, vertice)

    #print("O grafo possui %d componentes conexas" % contador)
    return contador, comparacoes
    
def subconjuntoProprio(grafo, vertices):
    conjunto = [i for i in range(vertices)]
    comparacoes = 0
    subconjuntos = chain.from_iterable(combinations(conjunto, r) for r in range(len(conjunto)+1))

    for subconjunto in subconjuntos:
        grafoAuxiliar = copy.deepcopy(grafo)

        for j in subconjunto:
            comparacoes += grafoAuxiliar.removerVertice(j)

        vertice = []
        for i in range(grafoAuxiliar.MAX):
            vertice.append(grafoAuxiliar.vertices[i].vertice)
            
        componentes, comparacao = componente(grafoAuxiliar, grafoAuxiliar.MAX, [False]*(grafoAuxiliar.MAX), vertice)
        comparacoes += comparacao

        if componentes > len(subconjunto) and len(subconjunto) > 0 and componentes == grafoAuxiliar.MAX:
            print("O Grafo não tem a Condição Necessária de ser Hamiltoniano!")
            return False, comparacoes
        
    return True, comparacoes
