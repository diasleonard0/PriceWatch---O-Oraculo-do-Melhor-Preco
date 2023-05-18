import DataExtraction

class PriceComparison():
    
    def compareCurrentPriceMaximumPrice(self, name):
        # Preço Atual
        url = '' # Onde o ProductManagement guardar a url, eu vou buscar com o nome do produto a sua url
        currentPrice = DataExtraction.DataExtraction.extractRelevantData(url)

        # Preço Máximo
        maximumPrice = '' # Onde o ProductManagement guardar o preço máximo, eu vou buscar com o nome do produto o seu preço máximo

        # Converter ambos para Float
        currentPrice = float(currentPrice)
        maximumPrice = float(maximumPrice)

        # Resultado
        if currentPrice > maximumPrice:
            return False
        else:
            return True