from classeGrafo import Grafo

class Vertice:
    def __init__(self, vertices):
        self.adjacentes = []
        self.MAX = vertices

    def inserirAresta(self, vertice):
        if len(self.adjacentes) >= self.MAX:
            print("Lista Cheia!")
        else:
            self.adjacentes.append(vertice)

class ListaAdjacencia(Grafo):
    def __init__(self, vertices):
        # definindo estruturas
        self.MAX = vertices
        self.vertices = []

        # preenchendo com listas vazias
        for i in range(self.MAX):
            self.vertices.append(Vertice(self.MAX))

    def inserir(self, u, v):
        # verificando lista cheia
        self.vertices[u].inserirAresta(v)
        self.vertices[v].inserirAresta(u)

    def remover(self, u, v):
        comparacoes = 0

        for indice, chave in enumerate(self.vertices[u].adjacentes):
            comparacoes += 1
            if chave == v:
                self.vertices[u].adjacentes.pop(indice)

        for indice, chave in enumerate(self.vertices[v].adjacentes):
            comparacoes += 1
            if chave == u:
                self.vertices[v].adjacentes.pop(indice)

        return comparacoes

    # função que implementa busca em profundida para calcular vértices alcançáveis de v
    def contadorBuscaProfundidade(self, v, visitado):
        contador = 1
        visitado[v] = True
        comparacoes = 0

        for i in self.vertices[v].adjacentes:
            comparacoes += 1
            if visitado[i] == False:
                contadorAuxiliar, comparacao = self.contadorBuscaProfundidade(i, visitado)
                contador += contadorAuxiliar
                comparacoes += comparacao

        return contador, comparacoes

    # função que verifica a validade de uma aresta no circuito
    def validaAresta(self, u, v):
        comparacoes = 0
        comparacoes +=1 

        if len(self.vertices[u].adjacentes) == 1:
            return True, comparacoes
        else:
            visitado = [False]*(self.MAX)
            contador1, comparacao = self.contadorBuscaProfundidade(u, visitado)
            comparacoes += comparacao

            comparacoes += self.remover(u, v)
            visitado = [False]*(self.MAX)
            contador2, comparacao = self.contadorBuscaProfundidade(u, visitado)
            comparacoes += comparacao

            self.vertices[u].inserirAresta(v)
            self.vertices[v].inserirAresta(u)

            return (False, comparacoes) if contador1 > contador2 else (True, comparacoes)

    # função principal para impressão do circuito euleriano
    def imprimirCircuitoEuleriano(self, u):
        comparacoes = 0

        for v in self.vertices[u].adjacentes:
            comparacoes += 1
            resultado, comparacao = self.validaAresta(u, v)
            comparacoes += comparacao
            
            if resultado == True:
                comparacoes += self.remover(u, v)
                self.imprimirCircuitoEuleriano(v)

        return comparacoes

    # função que verifica se os vértices do grafo possuem grau par
    def verificaEuleriano(self):
        comparacoes = 0

        for i in range(self.MAX):
            comparacoes += 1
            # se possuir grau impar retorna falso
            if len(self.vertices[i].adjacentes)%2 != 0:
                return False, comparacoes
    
        # se possuir grau par retorna verdadeiro
        return True, comparacoes