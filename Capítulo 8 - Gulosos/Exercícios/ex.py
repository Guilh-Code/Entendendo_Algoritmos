# Exemplo do capítulo 8: escolher um conjunto de estações que cubra todos os estados
# usando uma estratégia gulosa (sempre pegar a estação que cobre mais estados
# ainda não cobertos).

# Estados que ainda precisamos cobrir
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# Estações e os estados que cada uma cobre
stations = {
    'kone':  set(['id', 'nv', 'ut']),
    'ktwo':  set(['wa', 'id', 'mt']),
    'kthree':set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az'])
}

final_stations = set()  # conjunto de estações que vamos selecionar (resposta)

# Enquanto houver estados não cobertos, repetimos:
while states_needed:
    best_station = None         # melhor estação desta iteração
    states_covered = set()      # estados que a melhor estação cobre (interseção)

    # Percorremos todas as estações para ver qual cobre mais estados
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # interseção (estados novos cobertos)
        # se essa estação cobre mais estados novos do que a melhor até agora, substitui
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    # Adiciona a melhor estação encontrada ao resultado
    final_stations.add(best_station)
    # Remove os estados já cobertos da lista de estados que faltam
    states_needed -= states_covered

# Resultado final
print("Estações escolhidas:", final_stations)
