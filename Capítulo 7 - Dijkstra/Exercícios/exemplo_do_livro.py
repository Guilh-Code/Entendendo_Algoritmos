# Algoritmo de Dijkstra (exemplo do livro)
# Regras: funciona com pesos >= 0. Se houver peso negativo, use Bellman-Ford.

from math import inf

# 1) Grafo ponderado como dicionário de dicionários
grafo = {}
grafo["inicio"] = {"a": 6, "b": 2}  # arestas e pesos a partir de "inicio"
grafo["a"] = {"fim": 1}
grafo["b"] = {"a": 3, "fim": 5}
grafo["fim"] = {}  # nó final não aponta para ninguém

# 2) Tabela de custos (distâncias mínimas conhecidas a partir de "inicio")
custos = {"a": 6, "b": 2, "fim": inf}

# 3) Tabela de pais (para reconstruir o caminho ótimo)
pais = {"a": "inicio", "b": "inicio", "fim": None}

# 4) Conjunto/lista de nós já processados
processados = []

def encontra_nodo_menor_custo(custos):
    """Retorna o nó com menor custo ainda não processado."""
    menor_custo = inf
    nodo_menor = None
    for nodo, custo in custos.items():
        if custo < menor_custo and nodo not in processados:
            menor_custo = custo
            nodo_menor = nodo
    return nodo_menor

# 5) Loop principal do Dijkstra
nodo = encontra_nodo_menor_custo(custos)
while nodo is not None:
    custo_atual = custos[nodo]
    for vizinho, peso in grafo[nodo].items():
        novo_custo = custo_atual + peso
        # Se achou caminho mais barato até o vizinho, atualiza custo e pai
        if novo_custo < custos.get(vizinho, inf):
            custos[vizinho] = novo_custo
            pais[vizinho] = nodo
    processados.append(nodo)  # marca como processado
    nodo = encontra_nodo_menor_custo(custos)

# 6) Reconstrução do caminho da origem ("inicio") até "fim"
def caminho_ate(pais, destino):
    caminho = [destino]
    while pais.get(caminho[-1]) is not None:
        caminho.append(pais[caminho[-1]])
    caminho.reverse()
    return caminho

caminho = caminho_ate(pais, "fim")
custo_total = custos["fim"]

print("\nCaminho ótimo:", " -> ".join(caminho))
print("Custo total:", custo_total)
