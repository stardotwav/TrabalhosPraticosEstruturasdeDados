from classeHamiltoniano import Hamiltoniano, subconjuntoProprio
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# variável para geração do gráfico
comparacao = []
tamanho = []

# verificando o grafos completos
for i in range(5, 19):
    print("Analisando Grafo Completo de %d vértices" % i)
    tamanho.append(i)

    with open("grafoCompleto"+str(i)+".txt", "r") as arquivo:
        vertices = int(arquivo.readline())
        grafo = Hamiltoniano(vertices)
        
        for linha in arquivo:
            linha = linha.split()
            grafo.inserir(int(linha[0]), int(linha[1]))
            
        resultado, comparacoes = subconjuntoProprio(grafo, vertices)
        comparacao.append(comparacoes)
        print("Comparacoes: ", comparacoes)

        if resultado == True:
            print("O Grafo tem a Condição Necessária de ser Hamiltoniano!")
        print()

#dados = pd.DataFrame({'Tamanho': tamanho, 'Comparação': comparacao})
#sns.lineplot(x='Tamanho', y='Comparação', data=dados, color="mediumvioletred")
#plt.savefig('graficoGrafoHamiltoniano.png')