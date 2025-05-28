def quicksort(array):
    # Define uma função chamada quicksort que recebe uma lista chamada array.
    # O objetivo é ordenar essa lista de forma recursiva usando o algoritmo quicksort.

    if len(array) < 2:
        # Caso base da recursão: se a lista tiver 0 ou 1 elemento, ela já está ordenada.
        return array
        # Retorna a própria lista, porque não há mais nada para ordenar.

    else:
        pivo = array[0]
        # Escolhe o primeiro elemento da lista como pivô.
        # O pivô é o elemento que será usado para dividir a lista em duas partes:
        # os menores que ele e os maiores que ele.

        menores = [i for i in array[1:] if i <= pivo]
        # Cria uma nova lista chamada 'menores' com todos os elementos da array (exceto o pivô)
        # que são menores ou iguais ao pivô.
        # array[1:] significa: "todos os elementos da lista, exceto o primeiro".
        # Isso evita comparar o pivô com ele mesmo.

        maiores = [i for i in array[1:] if i > pivo]
        # Cria uma nova lista chamada 'maiores' com todos os elementos da array (exceto o pivô)
        # que são maiores que o pivô.

        return quicksort(menores) + [pivo] + quicksort(maiores)
        # Aqui acontece a mágica da recursão:
        # 1. Ordena recursivamente os 'menores' (quicksort(menores))
        # 2. Junta com o pivô (que já está na posição correta)
        # 3. Ordena recursivamente os 'maiores' (quicksort(maiores))
        # O resultado final é uma nova lista, completamente ordenada.



print(quicksort([10, 5, 2, 3]))
# Chama a função quicksort com a lista [10, 5, 2, 3]
# Esperado:
# Passo 1: pivô = 10
# menores = [5, 2, 3]
# maiores = []

# Passo 2 (quicksort dos menores):
# pivô = 5
# menores = [2, 3]
# maiores = []

# Passo 3 (quicksort de [2, 3]):
# pivô = 2
# menores = []
# maiores = [3]

# Reconstruindo:
# [2] + [3] => [2, 3]
# [2, 3] + [5] => [2, 3, 5]
# [2, 3, 5] + [10] => [2, 3, 5, 10]

# Resultado final impresso: [2, 3, 5, 10]
