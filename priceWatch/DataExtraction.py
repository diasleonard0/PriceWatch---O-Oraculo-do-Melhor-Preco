import requests
from bs4 import BeautifulSoup


class DataExtraction():
    
    def httpRequests(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Houve um erro de consulta ao site desejado ")

    def extractRelevantData(self, url):
        html = self.httpRequests(url)
        soup = BeautifulSoup(html, "html.parser")

        # Extrair o preço
        if url.find('mercadolivre'):
            price_element_1 = soup.find('span', class_ = 'andes-money-amount__fraction')
            price_element_3 = soup.find('span', class_ = 'andes-money-amount__cents andes-money-amount__cents--superscript-36')

            price = price_element_1.text + "." + price_element_3.text if price_element_1 or price_element_3 else 'Preco não encontrado'

            # Extrair a disponibilidade
            availability_element = soup.find('p', class_ = 'ui-pdp-color--BLACK ui-pdp-size--SMALL ui-pdp-family--SEMIBOLD ui-pdp-stock-information__title')
            availability = availability_element.text if availability_element else 'Não Tem'

        else:
            print('Só aceitamos produtos do Mercado Livre!')

        relevantData = []

        relevantData.append(price)
        relevantData.append(availability)

        print(price)
        print(availability)

        return relevantData
