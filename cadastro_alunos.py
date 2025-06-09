# Atividade Funções: Cadastro e análise de notas
# Feito por : Ester Gonçalves & Maria Eduarda Paixão :)


dicionario_alunos = {} # Dicionario criado vazio

def cadastrar_aluno(): # função de cadastrar aluno
    while True:
        try: # tratamento de excessão para o input alfabético
            nome = input("Nome do aluno: ").title() # inputando o nome, e o uso do title pra formatar
            if not nome.isalpha():
                raise ValueError('\nDigite nome com letras do alfabeto')
            break
        except ValueError as e:
            print(e)
    
    notas = [] # criando uma lista de notas vazia
    for i in range(1, 4): # usando a estrutura for para percorrer a lista e inputar as 3 notas

        while True: # tratamento de excessão para o input numérico 
            try:
                nota = float(input(f"Digite a {i}º nota: "))
            except ValueError:
                print("Valor inválido. Digite um número.")

    notas.append(nota) # uso do append pra adicionar a nota na lista
    dicionario_alunos[nome] = notas # adicionando o a chave nome(com o conteúdo do input) e o valor sendo a lista de notas
    print("Aluno cadastrado com sucesso!")

def calcular_media(notas): # função que calcula a média
    return sum(notas) / len(notas) # uso do sum para somar os valores da lista, dividido pelo tamanho (len)

def exibir_media(): # função para exibir a média
    while True: #tratamento de excessão
        try:
            nome = input("Nome do aluno: ").title()
            if not nome.isalpha():
                raise ValueError('\nDigite nome com letras do alfabeto')
            break
        except ValueError as e:
            print(e)
    if nome in dicionario_alunos: # verifica se existe alguma chave referente com o nome inputado, se verdadeiro, executa o bloco de comando. 
        notas = dicionario_alunos[nome] # passa pra variavel 'notas' o conteudo da chave referente ao nome inputado
        media = calcular_media(notas) # calcula a média com o uso da função
        print(f"A média do aluno(a) {nome} foi: {media:.2f}")  # exibe a média do aluno
    else:
        print("Aluno não encontrado.") # caso seja falso, exibe mensagem de erro


def verificar_situacao(media): # função que verifica a situação do aluno
    if media >= 5: # caso a media seja maior que 5, ele está aprovado, caso contrário, reprovado
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_situacao(): # função pra exibir a situação
    while True:#tratamento de excessão
        try:
            nome = input("Nome do aluno: ").title()
            if not nome.isalpha():
                raise ValueError('\nDigite nome com letras do alfabeto')
            break
        except ValueError as e:
            print(e)
    if nome in dicionario_alunos: #verifica se existe alguma chave referente com o nome inputado, se verdadeiro, executa o bloco de comando. 
        notas = dicionario_alunos[nome] # pega a lista de notas correspondente ao nome do aluno
        media = calcular_media(notas) # calcula a média com base nas notas usando a função definida anteriormente
        situacao = verificar_situacao(media) # verifica a situação do aluno com base na média
        print(f"O aluno(a) {nome} está: {situacao}") # exibe o resultado da situação do aluno
    else:
        print("Aluno não encontrado.") # caso o nome não exista no dicionário, exibe mensagem de erro



def exibir_boletim(): # função para exibir o boletim de um aluno específico
    while True: # tratamento de exceção 
        try:
            nome = input("Nome do aluno: ").title() 
            if not nome.isalpha():
                raise ValueError('\nDigite nome com letras do alfabeto')
            break
        except ValueError as e:
            print(e)

    if nome in dicionario_alunos: # verifica se o nome do aluno está no dicionário
        notas = dicionario_alunos[nome] # pega a lista de notas do aluno
        media = calcular_media(notas) # calcula a média com base nas notas
        situacao = verificar_situacao(media) # verifica a situação com base na média
        print(f"\nBoletim de {nome}") 
        print(f"Notas: {notas}") # exibe as notas
        print(f"Média: {media:.2f}") # exibe a média com 2 casas decimais
        print(f"Situação: {situacao}") # exibe a situação (aprovado ou reprovado)
    else:
        print("Aluno não encontrado.") # mensagem de erro caso o nome não esteja no dicionário

def exibir_todos_boletins(): # função para exibir o boletim de todos os alunos cadastrados
    if not dicionario_alunos: # verifica se o dicionário está vazio
        print("Nenhum aluno cadastrado.") # se estiver vazio, exibe mensagem
        return
    for nome, notas in dicionario_alunos.items(): # percorre o dicionário com nome e lista de notas
        media = calcular_media(notas) # calcula a média do aluno
        situacao = verificar_situacao(media) # verifica a situação
        print(f"\nAluno: {nome}") # exibe o nome do aluno
        print(f"Notas: {notas}") # exibe as notas do aluno
        print(f"Média: {media:.2f}") # exibe a média com 2 casas decimais
        print(f"Situação: {situacao}") # exibe a situação (aprovado ou reprovado)

while True: 
    while True: # tratamento de exceção 
        try:
            menu = int(input('\n------MENU-----\n0- Sair\n1- Cadastrar aluno\n2- Calcular média\n3- Verificar sitação\n4- Exibir boletim\n5- Exibir todos os boletins\nEscolha uma das opções acima: '))
            if menu in [0,1,2,3,4,5]: # verifica se a opção escolhida está dentro do menu
                break
            else:
                print('Digite uma das opções acima') 
        except ValueError:
            print('Escolha uma das opções acima!') 

    match menu: # estrutura match-case para executar as funções de acordo com a escolha do menu
        case 0:
            print('Programa Encerrado!') # encerra o programa
            break
        case 1:
            cadastrar_aluno() # chama a função para cadastrar aluno
        case 2: 
            exibir_media() # chama a função para exibir a média
        case 3:
            exibir_situacao() # chama a função para exibir a situação
        case 4 : 
            exibir_boletim() # chama a função para exibir o boletim de um aluno
        case 5 :
            exibir_todos_boletins() # chama a função para exibir todos os boletins

    
           



        


