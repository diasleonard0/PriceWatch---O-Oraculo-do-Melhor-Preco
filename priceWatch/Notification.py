import PriceComparison

class Notification():
    
    def sendNotifications(self, nome):
        if PriceComparison.PriceComparison.compareCurrentPriceMaximumPrice(nome):
            print('O VALOOOOOOOOOOOOOOOR\nCAIUUUUUUUUUUUUUUUUUUUUUUUUUUUUU')