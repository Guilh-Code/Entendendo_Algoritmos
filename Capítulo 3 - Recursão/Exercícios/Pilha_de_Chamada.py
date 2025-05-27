# Define a função 'sauda' que recebe um parâmetro 'nome'
def sauda(nome):
    print('Olá, ' + nome + '!')  # Imprime uma saudação inicial
    sauda2(nome)  # Chama outra função para perguntar como a pessoa está
    print('preparando para dizer tchau...')  # Mensagem antes da despedida
    tchau()  # Chama a função que imprime a despedida


# Define a função 'sauda2' que também recebe 'nome'
def sauda2(nome):
    print('Como vai ' + nome + '?')  # Imprime uma pergunta


# Define a função 'tchau', que não recebe parâmetros
def tchau():
    print('ok, tchau!')  # Imprime a despedida


# Chama a função principal com o nome 'Guilherme'
sauda('Guilherme')
