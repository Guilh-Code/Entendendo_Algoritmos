numeros = [2, 3, 7, 8, 10]
# Essa é a lista base.
# Cada número vai ser usado para multiplicar todos os outros, um por um.


for multiplicador in numeros:
    # Loop externo: vamos pegar cada número da lista, um por um
    # e chamar esse número de "multiplicador"
    # Ele será a "linha" da nossa tabela de multiplicação

    linha = [multiplicador * n for n in numeros]
    # Loop interno com list comprehension:
    # Para cada número 'n' da lista,
    # multiplica 'multiplicador * n' e guarda esse valor na lista 'linha'.
    # No fim, 'linha' terá os resultados da tabuada do número atual.

    print(f"{multiplicador} x todos = {linha}")
    # Mostra no terminal o resultado da linha.
    # Exemplo:
    # Se o multiplicador for 2 → mostra: 2 x todos = [4, 6, 14, 16, 20]


'''
Repetição mental:
“Para cada número, crie a tabuada dele com todos os outros da lista.”

Regra:
   Loop fora escolhe o fixo (linha).
   Loop dentro faz a conta com todos os outros.


O loop externo (for multiplicador) define quem faz a tabuada.

O loop interno (for n) é com quem ele multiplica.

A multiplicação está toda aqui: multiplicador * n
'''