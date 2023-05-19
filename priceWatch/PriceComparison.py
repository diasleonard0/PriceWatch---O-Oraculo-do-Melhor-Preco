from DataExtraction import DataExtraction
from DataStorage import DataStorage

class PriceComparison():
    
    def compareCurrentPriceMaximumPrice(self, name):
        # Achar a URL com o nome do produto
        data = DataStorage()
        url = data.getUrl(name)

        # Preço Atual
        dataExtraction = DataExtraction()
        currentPriceList = dataExtraction.extractRelevantData(url)
        currentPrice = currentPriceList[0]

        # Preço Máximo
        desiredPrice = data.getPrice(name)

        # Converter ambos para Float
        currentPrice = float(currentPrice)
        desiredPrice = float(desiredPrice)

        List = []

        # Resultado
        if currentPrice > desiredPrice:
            List.append(False)
            return List
        else:
            List.append(True)
            total = desiredPrice - currentPrice
            List.append(total)
            return List