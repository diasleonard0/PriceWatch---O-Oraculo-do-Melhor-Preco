from DataStorage import DataStorage

class ProductManagement():

    def __init__(self):
        pass

    def addProductsToMonitoring(self, name, url, price):
        # Adicionar os produtos ao monitoramento, solicitando ao usuário o nome, a URL e o preço máximo desejado

        dataStorage = DataStorage()
        dataStorage.enterData(name, url, price)

    def removeProductsFromMonitoring(self, name):
        # Remover produtos do monitoramento, permitindo que o usuário selecione qual produto deseja remover.
        dataStorage = DataStorage()
        dataStorage.removeData(name)

    def displayListOfMonitoredProducts(self, name):
        #  Exibir a lista de produtos atualmente monitorados, mostrando os detalhes de cada um.
        dataStorage = DataStorage()
        dataStorage.viewData(name)