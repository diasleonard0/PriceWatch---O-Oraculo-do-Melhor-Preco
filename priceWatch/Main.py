from DataStorage import DataStorage
from UserInterface import UserInterface
from ProductManagement import ProductManagement
from Scheduling import Scheduling

'''
Upgrade

- Tentar colocar uma alternativa para ver todos os produtos que foram adicionados no Banco de Dados
'''

class Main():
    
    def startMonitoring(self):
        # Iniciar monitoramento de preços
        pass

    def startScheduling(self):
        # Iniciar Agendamento de Verificação
        pass
        

    def start(self):
        while True:

            dataStorage = DataStorage()
            response = UserInterface().response()

            if (dataStorage.checkDatabase()): # Se tiver algo no BD ele inicia o monitoramento
                self.startMonitoring()
            else: # Caso contrário ele cria um db e uma tabela
                dataStorage.createTheTable()
            
            if response == '0':
                print('Encerrando programa...')
                break
            
            elif response == '1':
                name = input("Nome do Produto: ").strip()
                price = input("Preço Desejado: ").strip()
                url = input("URL do Produto: ").strip()

                addProduct = ProductManagement()
                addProduct.addProductsToMonitoring(name, url, price)

            elif response == '2':
                name = input("Nome do Produto que deseja Remover: ").strip()
                
                removeProduct = ProductManagement()
                removeProduct.removeProductsFromMonitoring(name)

            elif response == '3':
                name = input("Nome do Produto que você deseja Visualiar: ").strip()

                viewProduct = ProductManagement()
                viewProduct.displayListOfMonitoredProducts(name)

            elif response == '4':
                # Configurar o Agendamento, ou seja, aqui eu quero que ele fique vendo automaticamente
                name = input('Nome do Produto: ').strip()
                print('Formas de Agendamento:\nm - Por minuto\nh - Por hora\nd - Por dia')
                toSchedule = input('>> ').strip().lower()

                if toSchedule in ['m', 'h', 'd']:
                    schedule = Scheduling()
                    schedule.configureSchedule(toSchedule, name)
                else:
                    print("Você digitou uma letra errado, é 'm', 'h' ou 'd'")
                    continue

Main().start()
