'''
📘 Capítulo 2 – Ordenação por Seleção (Selection Sort)
Livro: Entendendo Algoritmos – Aditya Bhargava



🎯 Objetivo do Capítulo:
Aprender como funciona o algoritmo de ordenação por seleção e introduzir o conceito de eficiência de algoritmos usando a notação Big O.

🧠 Conceito principal: Selection Sort
A ideia da ordenação por seleção é encontrar repetidamente o menor elemento de uma lista e adicioná-lo em uma nova lista ordenada.

Ao final, a nova lista estará totalmente ordenada, e a lista original estará vazia (se você estiver usando pop()).


🔁 Passos do algoritmo:

1 - Encontra o menor valor da lista.

2 - Remove esse valor da lista original.

3 - Adiciona esse valor à nova lista.

4 - Repete até que todos os elementos tenham sido movidos.


📌 Exemplo prático:

Dada a lista: [5, 3, 6, 2, 10]


Passo a passo do selection sort:

- Encontra 2 → remove de original → adiciona à nova lista

- Encontra 3 → remove → adiciona

- Encontra 5 → ...
    → Resultado final: [2, 3, 5, 6, 10]


📏 Análise de desempenho:

- Para ordenar uma lista de n elementos, você precisa fazer cerca de n * (n - 1) / 2 comparações.

- Isso leva à notação Big O = O(n²).

- Selection Sort é ineficiente para listas grandes, mas é bom para aprendizado por ser simples de entender.


🛠️ Código em Python (do livro):

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))


📚 Conceitos-chave aprendidos:

- O que é ordenação.

- Como funciona o algoritmo de seleção.

- Primeira introdução-  à eficiência de algoritmos.

- Introdução à notação Big O (O(n²)).

'''