class Grafo:
    def __init__(self):
        pass

    # função para inserir um par de vértices
    def inserir(self):
        pass

    # função para remover uma aresta
    def remover(self):
        pass

    # função que implementa busca em profundida para calcular vértices alcançáveis de v
    def contadorBuscaProfundidade(self):
        pass

    # função que verifica a validade de uma aresta no circuito
    def validaAresta(self):
        pass

    # função principal para impressão do circuito euleriano
    def imprimirCircuitoEuleriano(self):
        pass

    # função que verifica se o grafo é euleriano usando do conceito de grau par dos vértices
    def verificaEuleriano(self):
        pass

    # está função é geral, em que ao enviar um grafo construído pelas demais classes 
    def circuitoEuleriano(self, grafo):
        comparacoes = 0
        comparacoes += 1

        resultado, comparacao = grafo.verificaEuleriano()
        comparacoes += comparacao

        # verifica se o grafo é euleriano
        if resultado == True:
            print("== Grafo é Euleriano ==")
            print("Circuito Euleriano: ", end="")
            comparacoes += grafo.imprimirCircuitoEuleriano(0)
            print()
            print()

        else:
            print("== Grafo não é Euleriano ==")
            print()

        return comparacoes