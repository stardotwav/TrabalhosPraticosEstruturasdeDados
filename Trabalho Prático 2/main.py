from classeGrafo import Grafo
from classeMatrizAdjacencia import MatrizAdjacencia
from classeListaAdjacencia import ListaAdjacencia
from classeMatrizIncidencia import MatrizIncidencia
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# variável para geração do gráfico
comparacao = []
tamanho = []

# verificando o grafos completos
for i in range(5, 46):
    print("Analisando Grafo Completo de %d vértices" % i)

    if i%2 != 0:
        with open("grafo"+str(i)+".txt", "r") as arquivo:
            vertices = int(arquivo.readline())
            tamanho.append(i)
            listaAdjacencia = ListaAdjacencia(vertices)
            
            for linha in arquivo:
                linha = linha.split()
                listaAdjacencia.inserir(int(linha[0])-1, int(linha[1])-1)
                
            # criando a classe de grafo
            grafo = Grafo()

            # chamando a função para o circuito euleriano
            comparacoes = grafo.circuitoEuleriano(listaAdjacencia)
            comparacao.append(comparacoes)

dados = pd.DataFrame.from_dict({'Tamanho': tamanho, 'Comparação': comparacao})
sns.lineplot(x='Tamanho', y='Comparação', data=dados, color="darkviolet", label="Lista de Adjacência")
plt.yscale('log')
plt.savefig('graficoGrafoEulerianoListaAdjacencia.png')

# variável para geração do gráfico
comparacao = []
tamanho = []

# verificando o grafos completos
for i in range(5, 46):
    print("Analisando Grafo Completo de %d vértices" % i)

    if i%2 != 0:
        with open("grafo"+str(i)+".txt", "r") as arquivo:
            vertices = int(arquivo.readline())
            tamanho.append(i)
            matrizAdjacencia = MatrizAdjacencia(vertices)
            
            for linha in arquivo:
                linha = linha.split()
                matrizAdjacencia.inserir(int(linha[0])-1, int(linha[1])-1)
                
            # criando a classe de grafo
            grafo = Grafo()

            # chamando a função para o circuito euleriano
            comparacoes = grafo.circuitoEuleriano(matrizAdjacencia)
            comparacao.append(comparacoes)

dados = pd.DataFrame.from_dict({'Tamanho': tamanho, 'Comparação': comparacao})
sns.lineplot(x='Tamanho', y='Comparação', data=dados, color="royalblue", label="Matriz de Adjacência")
plt.yscale('log')
plt.savefig('graficoGrafoEulerianoMatrizAdjacencia.png')

# variável para geração do gráfico
comparacao = []
tamanho = []

# verificando o grafos completos
for i in range(5, 46):
    print("Analisando Grafo Completo de %d vértices" % i)

    if i%2 != 0:
        with open("grafo"+str(i)+".txt", "r") as arquivo:
            vertices = int(arquivo.readline())
            tamanho.append(i)
            matrizIncidencia = MatrizIncidencia(vertices, len(arquivo.readlines())-1)
            contador = 0
            
            for linha in arquivo:
                linha = linha.split()
                matrizIncidencia.inserir(int(linha[0])-1, int(linha[1])-1, contador)
                contador += 1
                
            # criando a classe de grafo
            grafo = Grafo()

            # chamando a função para o circuito euleriano
            comparacoes = grafo.circuitoEuleriano(matrizIncidencia)
            comparacao.append(comparacoes)

dados = pd.DataFrame.from_dict({'Tamanho': tamanho, 'Comparação': comparacao})
sns.lineplot(x='Tamanho', y='Comparação', data=dados, color="crimson", label="Matriz de Incidência")
plt.yscale('log')
plt.savefig('graficoGrafoEulerianoMatrizIncidencia.png')
