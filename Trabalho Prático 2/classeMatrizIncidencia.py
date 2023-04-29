from classeGrafo import Grafo

class MatrizIncidencia(Grafo):
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas

        # preenchendo com zeros a matriz
        self.grafo = [[0 for i in range(self.arestas)] for i in range(self.vertices)]

    def inserir(self, u, v, aresta):
        # neste caso é inserido 1 na coluna da aresta e na linha dos vértices
        self.grafo[u][aresta] = 1
        self.grafo[v][aresta] = 1

    def remover(self, u, v, aresta):
        self.grafo[u][aresta] = 0
        self.grafo[v][aresta] = 0

    def verificaAdjacente(self, u):
        auxiliar = self.grafo[u]
        adjacentes = []
        arestas = []
        comparacoes = 0

        for i in range(self.vertices):
            for j in range(self.arestas):
                comparacoes += 2
                if(u != i) and (auxiliar[j] == 1) and (self.grafo[i][j] == 1):
                    adjacentes.append(i)
                    arestas.append(j)

        return adjacentes, arestas, comparacoes
    
    def contadorBuscaProfundidade(self, v, visitado):
        contador = 1
        visitado[v] = True
        adjacentes, arestas, comparacao = self.verificaAdjacente(v)
        comparacoes = comparacao

        for i in adjacentes:
            comparacoes += 1
            if visitado[i] == False:
                cont, comparacao = self.contadorBuscaProfundidade(i, visitado)
                contador += cont
                comparacoes += comparacao

        return contador, comparacoes

    def validaAresta(self, u, v):
        adjacentes, arestas, comparacao = self.verificaAdjacente(u)
        comparacoes = comparacao

        comparacoes += 1
        if len(adjacentes) == 1:
            return True, comparacoes
        else:
            visitado = [False]*(self.vertices)
            contador1, comparacao = self.contadorBuscaProfundidade(u, visitado)
            comparacoes += comparacao

            for i in range(len(adjacentes)):
                comparacoes += 1
                if adjacentes[i] == v:
                    self.remover(u, v, arestas[i])
                    break

            visitado = [False]*(self.vertices)
            contador2, comparacao = self.contadorBuscaProfundidade(u, visitado)
            comparacoes += comparacao

            for i in range(len(adjacentes)):
                comparacoes += 1
                if adjacentes[i] == v:
                    self.inserir(u, v, arestas[i])
                    break

            return False, comparacoes if contador1 > contador2 else True, comparacoes
    
    def imprimirCircuitoEuleriano(self, u):
        adjacentes, arestas, comparacao = self.verificaAdjacente(u)
        comparacoes = comparacao

        for i in range(len(adjacentes)):
            comparacoes += 1
            if self.validaAresta(u, adjacentes[i]):
                self.remover(u, adjacentes[i], arestas[i])
                self.imprimirCircuitoEuleriano(adjacentes[i])

        return comparacoes

    def verificaEuleriano(self):
        comparacoes = 0

        for i in range(self.vertices):
            adjacentes, arestas, comparacao = self.verificaAdjacente(i)
            comparacoes += comparacao
            comparacoes += 1
            if len(adjacentes)%2 != 0:
                return False, comparacoes
            
        return True, comparacoes