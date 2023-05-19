class UserInterface():

    def quit():
        return False

    print("Seja Bem-Vindo\n")

    while True:
        print(
            "Escolha uma opção:\n" +
            "0 - Sair\n" +
            "1 - Adicionar Produto\n" +
            "2 - Remover Produto\n" +
            "3 - Visualizar Produto\n" +
            "4 - Configurar o Agendamento\n"
        )

        response = input(">> ").strip().lower()

        if response == '0' or '1' or '2' or '3' or '4':
            if response == '0':
                break
            elif response == '1':
                pass
            elif response == '2':
                pass
            elif response == '3':
                pass
            elif response == '4':
                pass

        if response == 'ADICIONAR PRODUTO' or 'REMOVER PRODUTO' or 'VISUALIZAR PRODUTO' or 'CONFIGURAR O AGENDAMENTO':
            if response == 'ADICIONAR PRODUTO':
                pass
            elif response == 'REMOVER PRODUTO':
                pass
            elif response == 'VISUALIZAR PRODUTO':
                pass
            elif response == 'CONFIGURAR O AGENDAMENTO':
                pass
            else:
                print()

        else:
            print('Houve algum erro de escolha, por favor digite um número entre 0 e 4, ou, digite corretamente o que deseja!!')
    
    quit()