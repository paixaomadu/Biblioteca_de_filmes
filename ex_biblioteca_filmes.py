usuarios_filmes= {}
lista_filmes= []

while True:
    while True:
        try:
            menu = int(input('\n------MENU-----\n0- Sair\n1- Adicionar filme\n2- Remover filme\n3- Ver filmes de um usúario\n4- Ver todos os filmes\n Escolha uma das opções acima: '))
            if menu in [0,1,2,3,4]:
                break
            else:
                print('Digite uma das opções acima')
        except ValueError:
            print('Escolha uma das opções acima!')

    match menu:
        case 0:
            break
        case 1:
            while True:
                try:
                    nome= input('\nDigite o nome do usuário: ').title()
                    if not nome.isalpha():
                            raise ValueError('Digite apenas letras!')
                    break
                except ValueError as e:
                        print(e)    
            while True:
                try:
                    filme= input('\nDigite um filme: ').title()
                    if not filme.isalpha():
                            raise ValueError('Digite apenas letras!')
                    break
                except ValueError as e:
                        print(e)
            if nome not in usuarios_filmes:
                usuarios_filmes[nome] = []

            usuarios_filmes[nome].append(filme)
            print('Filme adicionado com sucesso!')
        case 2:
            while True:
                try:
                    nome= input('\nDigite o nome do usuário: ').title()
                    if not nome.isalpha():
                            raise ValueError('Digite apenas letras!')
                    break
                except ValueError as e:
                        print(e)    
            while True:
                try:
                    filme= input('\nDigite um filme: ').title()
                    if not filme.isalpha():
                            raise ValueError('Digite apenas letras!')
                    break
                except ValueError as e:
                        print(e)    
            lista_filmes.remove(filme)
            usuarios_filmes[nome]= lista_filmes
            print('Filme removido com sucesso!')
        case 3:
            while True:
                try:
                    nome= input('\nDigite o nome do usuário: ').title()
                    if not nome.isalpha():
                            raise ValueError('Digite apenas letras!')
                    break
                except ValueError as e:
                        print(e) 
            f= usuarios_filmes.get(nome, 'Essa chave não existe')
            if f != 'Essa chave não existe':
               print(f'Filmes assistidos: {f}')
        case 4:
            if usuarios_filmes:
                for c,v in usuarios_filmes.items():
                    print(f'{c}: {v}')
            else:
                print('Nenhum filme cadastrado ainda.')
        case _:
            print('Essa opção não é válida!')