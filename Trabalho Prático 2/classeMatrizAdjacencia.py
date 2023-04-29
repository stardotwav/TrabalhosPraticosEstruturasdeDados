from classeGrafo import Grafo

class MatrizAdjacencia(Grafo):
    def __init__(self, vertices):
        self.vertices = vertices
        # preenchendo com zeros a matriz
        self.grafo = [[0 for i in range(vertices)] for i in range(vertices)]

    def inserir(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def remover(self, u, v):
        self.grafo[u][v] = 0
        self.grafo[v][u] = 0

    # função que implementa busca em profundida para calcular vértices alcançáveis de v
    def contadorBuscaProfundidade(self, v, visitado):
        contador = 1
        visitado[v] = True
        comparacoes = 0

        for i in range(self.vertices):
            comparacoes += 1
            if (self.grafo[v][i] != 0) and (visitado[i] == False):
                cont, comparacao = self.contadorBuscaProfundidade(i, visitado)
                contador += cont
                comparacoes += comparacao

        return contador, comparacoes

    # função que verifica a validade de uma aresta no circuito
    def validaAresta(self, u, v):
        contador = 0
        comparacoes = 0

        for i in range(self.vertices):
            comparacoes += 1
            if self.grafo[u][i] == 1:
                contador += 1

        comparacoes += 1
        if contador == 1:
            return True, comparacoes
        else:
            # preenchendo a lista de visitado com valores falsos
            visitado = [False]*(self.vertices)
            contador1, comparacao = self.contadorBuscaProfundidade(u, visitado)
            comparacoes += comparacao

            # remover a borda de u e v, e depois contar novamente os vértices alcançáveis
            self.remover(u, v)
            visitado = [False]*(self.vertices)
            contador2, comparacao = self.contadorBuscaProfundidade(u, visitado)
            comparacoes += comparacao

            # inserindo novamente a conexão dos vértices
            self.inserir(u, v)

            return (False, comparacoes) if contador1 > contador2 else (True, comparacoes)

    # função principal para impressão do circuito euleriano
    def imprimirCircuitoEuleriano(self, u):
        comparacoes = 0

        for v in range(self.vertices):
            if self.grafo[u][v] == 1:
                comparacoes += 1
                resultado, comparacao = self.validaAresta(u, v)
                comparacoes += comparacao

                if resultado == True:
                    self.remover(u, v)
                    self.imprimirCircuitoEuleriano(v)

        return comparacoes

    # função que verifica se os vértices do grafo possuem grau par
    def verificaEuleriano(self):
        comparacoes = 0

        for i in range(self.vertices):
            contador = 0
            for j in range(self.vertices):
                comparacoes += 1
                if self.grafo[i][j] == 1:
                    contador += 1

            if contador%2 != 0:
                return False, comparacoes
        
        return True, comparacoes
