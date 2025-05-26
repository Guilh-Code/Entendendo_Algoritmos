# Função que encontra o índice do menor valor em uma lista
def buscaMenor(arr):
    menor = arr[0]               # Assume que o primeiro elemento é o menor
    menor_indice = 0             # Índice do menor elemento inicializado como 0

    for i in range(1, len(arr)): # Percorre o restante da lista
        if arr[i] < menor:       # Se encontrar um valor menor que o atual
            menor = arr[i]       # Atualiza o menor valor
            menor_indice = i     # Atualiza o índice do menor valor

    return menor_indice          # Retorna o índice do menor valor encontrado


# Função que implementa o algoritmo de ordenação por seleção
def ordenacaoporSelecao(arr):
    novoArr = []                         # Lista que vai armazenar os elementos ordenados

    for i in range(len(arr)):           # Repete o processo até esvaziar a lista original
        menor = buscaMenor(arr)        # Encontra o índice do menor valor na lista atual
        novoArr.append(arr.pop(menor)) # Remove o menor valor da lista original e adiciona na nova lista

    return novoArr                      # Retorna a lista ordenada

# Testa a função com uma lista de exemplo
print(ordenacaoporSelecao([5, 3, 6, 2, 10]))  # Saída esperada: [2, 3, 5, 6, 10]
