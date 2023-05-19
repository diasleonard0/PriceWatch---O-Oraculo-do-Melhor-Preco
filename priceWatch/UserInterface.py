class UserInterface():

    def __init__(self):
        pass

    def quit():
        return False

    def response(self):
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

            response = input(">> ").strip().upper()

            if response == '0' or '1' or '2' or '3' or '4':
                if response == '0':
                    return '0'
                elif response == '1':
                    return '1'
                elif response == '2':
                    return '2'
                elif response == '3':
                    return '3'
                elif response == '4':
                    return '4'

            elif response == 'SAIR' or 'ADICIONAR PRODUTO' or 'REMOVER PRODUTO' or 'VISUALIZAR PRODUTO' or 'CONFIGURAR O AGENDAMENTO':
                if response == 'SAIR':
                    return '0'
                elif response == 'ADICIONAR PRODUTO':
                    return '1'
                elif response == 'REMOVER PRODUTO':
                    return '2'
                elif response == 'VISUALIZAR PRODUTO':
                    return '3'
                elif response == 'CONFIGURAR O AGENDAMENTO':
                    return '4'

            else:
                print('Houve algum erro de escolha, por favor digite um número entre 0 e 4, ou, digite corretamente o que deseja!!')
                continue
            