# Define a função 'fat' que calcula o fatorial de um número 'x'
def fat(x):
    # Caso base: se 'x' for 1, retorna 1 (pois 1! = 1)
    if x == 1:
        return 1
    else:
        # Caso recursivo: multiplica 'x' pelo fatorial de 'x - 1'
        return x * fat(x - 1)


# Chama a função 'fat' com o valor 3 e imprime o resultado
print(fat(3))  # Saída esperada: 6 (pois 3 * 2 * 1 = 6)



'''
Explicação da lógica:
A função fat calcula o fatorial de um número, ou seja:

fat(3)
= 3 * fat(2)
= 3 * (2 * fat(1))
= 3 * (2 * 1)
= 6
'''