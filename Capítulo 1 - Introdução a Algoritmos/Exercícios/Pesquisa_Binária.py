def pesquisa_binaria(lista, item):
    # Define os limites inferior (baixo) e superior (alto) da busca
    baixo = 0
    alto = len(lista) - 1

    # Continua enquanto ainda houver uma parte da lista para pesquisar
    while baixo <= alto:
        # Calcula o índice do meio da lista
        meio = (baixo + alto) // 2
        chute = lista[meio]  # Pega o valor do meio

        # Verifica se encontrou o item
        if chute == item:
            return meio  # Retorna a posição do item na lista

        # Se o chute for maior que o item, ajusta o limite superior
        if chute > item:
            alto = meio - 1
        else:
            # Se o chute for menor, ajusta o limite inferior
            baixo = meio + 1

    # Se sair do laço, o item não está na lista
    return None

# Lista ordenada para aplicar a pesquisa binária
minha_lista = [1, 3, 5, 7, 9]

# Testa a função com um item que existe (3) → deve retornar 1 (posição na lista)
print(pesquisa_binaria(minha_lista, 3))

# Testa a função com um item que não existe (-1) → deve retornar None
print(pesquisa_binaria(minha_lista, -1))
