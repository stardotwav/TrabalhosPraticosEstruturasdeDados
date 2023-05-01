# Trabalho Prático 2

Neste trabalho foram apresentados as implementações de estruturas de dados para a representação computacional de grafos, sendo utilizados: matriz de incidência, matriz de adjacência, e a lista de adjacência, e usando dessas estruturas serão feitas verificações para grafos Eulerianos e Hamiltonianos.

### 🔴 Grafo Euleriano

Um grafo Euleriano é aquele que possui um circuito Euleriano, em que devemos visitar todas as arestas exatamente uma única vez, além de que todos os vértices do grafo devem possuir um grau par.

Para a implementação foram utilizadas de três estruturas de dados diferentes entre si, dessa forma, foi criada uma classe de interface, que demonstra as funções que devem ser implementadas em cada uma das classes derivadas, na figura abaixo é apresentado um diagrama que demonstra as classes desenvolvidas e suas funções.

<img src="https://github.com/stardotwav/TrabalhosPraticosEstruturasdeDados/blob/main/Trabalho%20Pr%C3%A1tico%202/Graficos%20Gerados/Grafo.jpg">

Além disso, foi realizada a prova da complexidade dos algoritmos implementados em função das estruturas de dados utilizadas, em que usando da estruturas de matriz de incidência obtivemos uma complexidade de $O(V^{2} * E)$, para a matriz de adjacência a complexidade foi de $O(V * E)$ e, por fim, para a lista de adjacência a complexidade foi também de $O(V * E)$, com o diferencial da sua fórmula fechada ser $V * 2E$, enquanto na matriz de adjacência foi $V * 3E$. Para demonstrar o gasto computacional foi também gerado um gráfico de comparação do número de operações básicas gastas em relação ao número de vértices em cada estrutura, sendo esse gráfico apresentado abaixo.

<img src="https://github.com/stardotwav/TrabalhosPraticosEstruturasdeDados/blob/main/Trabalho%20Pr%C3%A1tico%202/Graficos%20Gerados/graficoGrafoEuleriano.png">


### 🟠 Grafo Hamiltoniano

Um grafo Hamiltoniano é aquele que possui um ciclo Hamiltoniano, ou seja, ao percorrer o grafo devemos visitar todos os vértices exatamente uma única vez, além de que neste caso especial não foram provadas características necessárias e suficientes como apresentado nos grafos Eulerianos, dessa forma, neste trabalho será apresentado a implementação da verificação da principal condição necessária de grafos Hamiltonianos: para qualquer subconjunto próprio não vazio $S \subset V$, sendo $G$ um grafo, vale a relação $\omega(G - S) \leq |S|$.

No caso da implementação para verificação de grafos Hamiltonianos foi utilizado da estrutura de lista de adjacência, usando da lista estática contígua, essa lista foi escolhida pelo fator de facilitar a verificação do nó que estamos analisando, visto que durante a execução das funções de verificação era necessário remover vértices variados em diversos momentos, dessa forma facilitando por exemplo na busca em largura a identificação de qual vértice estava sendo tratando.

Sobre a prova da complexidade, neste caso, pensando que as buscas por subconjuntos próprios se repetem cerca de $2^{V}$, então a complexidade acabou sendo essa, visto que é necessário repetir a verificação de componentes conexas para todas as possibilidades de retirada de vértices. Abaixo temos um gráfico que representa testes feitos com a relação do número de repetições da operação básica em relação ao número de vértices. 

<img src="https://github.com/stardotwav/TrabalhosPraticosEstruturasdeDados/blob/main/Trabalho%20Pr%C3%A1tico%202/Graficos%20Gerados/graficoGrafoHamiltoniano.png">