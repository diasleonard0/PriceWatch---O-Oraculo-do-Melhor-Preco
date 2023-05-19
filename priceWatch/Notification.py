from PriceComparison import PriceComparison

class Notification():
    
    def sendNotifications(self, name):
        priceComparison = PriceComparison()
        
        result = priceComparison.compareCurrentPriceMaximumPrice(name)
        
        if result[0]:
            print(f'O Valor CAIU, porraaaaaaa\nDeu Certo karalho\nO valor caiu R${result[1]:.2f}')