"""
O que são algoritmos?

- Um algoritmo é um conjunto de instruções claras e finitas que resolvem um problema ou realizam uma tarefa.

- Exemplo simples: uma receita de bolo ou um passo a passo para encontrar um nome em uma lista telefônica.


⚡ Busca Linear vs Busca Binária

- Busca Linear: Verifica item por item até encontrar o que procura. Tempo de execução proporcional ao número de elementos (O(n)).

- Busca Binária: Requer que os dados estejam ordenados. A cada passo, elimina metade da lista. Muito mais eficiente - tempo de execução O(log n).

        Exemplo prático: Achar um número em uma lista com 128 elementos

        Busca linear pode levar até 128 tentativas

        Busca binária leva no máximo 7 tentativas (pois 2⁷ = 128)


⏱️ Notação Big O

- Serve para descrever a eficiência de algoritmos em termos de tempo de execução conforme o tamanho da entrada cresce.

- Exemplos:

    - O(1): Tempo constante (não muda com o tamanho dos dados)

    - O(log n): Logarítmico (muito rápido)

    - O(n): Linear

    - O(n²): Quadrático (piora muito com entradas maiores)


📌 Conclusão do capítulo

- Algoritmos estão por toda parte e são essenciais para resolver problemas de forma eficiente.

- Saber escolher o algoritmo certo pode economizar muito tempo e recursos.

- Busca binária é um exemplo clássico de como um algoritmo eficiente pode superar soluções mais simples.
"""