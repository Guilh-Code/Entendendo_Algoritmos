def regressiva(i):
    print(i)  # Imprime o valor atual de 'i'
    
    # === CASO BASE ===
    if i <= 1:
        return  # Encerra a recursão quando atinge 1 ou menos
    
    # === CASO RECURSIVO ===
    else:
        regressiva(i - 1)  # Chama a função novamente com i - 1

regressiva(3)

'''
Fluxo quando regressiva(3) é chamada:

3  → recursiva com 2
2  → recursiva com 1
1  → entra no caso base e para
'''