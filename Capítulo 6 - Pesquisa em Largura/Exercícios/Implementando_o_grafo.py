'''📌 Contexto geral — Busca em Largura (BFS)

É um algoritmo para percorrer grafos em camadas (amigos → amigos dos amigos → etc).

Usa fila (FIFO) para garantir que processa primeiro quem está mais perto.

No exemplo: você quer encontrar um vendedor de manga na sua rede de contatos.

O BFS garante que, se existir, você o encontra no menor número de passos possíveis.'''



from collections import deque  # Importa fila de duas pontas (deque)

# Grafo representado como dicionário (cada nó aponta para seus vizinhos)
grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []

# Critério: vendedor é quem tem nome terminando em "m"
def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    fila_de_pesquisa = deque()       # Cria uma fila
    fila_de_pesquisa += grafo[nome]  # Começa com seus amigos diretos
    verificadas = []                 # Lista para não verificar mesma pessoa duas vezes

    while fila_de_pesquisa:          # Enquanto houver pessoas na fila
        pessoa = fila_de_pesquisa.popleft()  # Pega a primeira pessoa da fila
        if pessoa not in verificadas:        # Se ainda não foi verificada
            if pessoa_e_vendedor(pessoa):    # Verifica se é vendedor
                print(f'{pessoa} é o vendedor de manga!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]  # Adiciona amigos dessa pessoa à fila
                verificadas.append(pessoa)         # Marca como já verificada
    return False  # Se esgotar a fila e não encontrar, retorna False

pesquisa("voce")
