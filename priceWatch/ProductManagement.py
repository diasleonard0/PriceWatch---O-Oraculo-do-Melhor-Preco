class ProductManagement():

    __name = ''
    __url = ''
    __price = ''

    def __init__(self, name, url, price):
        self.__name = name
        self.__url = url
        self.__price = price

    def addProductsToMonitoring(self):
        # Adicionar os produtos ao monitoramento, solicitando ao usuário o nome, a URL e o preço máximo desejado
        pass

    def removeProductsFromMonitoring(self):
        # Remover produtos do monitoramento, permitindo que o usuário selecione qual produto deseja remover.
        pass

    def displayListOfMonitoredProducts(self):
        #  Exibir a lista de produtos atualmente monitorados, mostrando os detalhes de cada um.
        pass