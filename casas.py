import requests
from bs4 import BeautifulSoup
import pandas as pd

imobiliarias = [    'https://www.zapimoveis.com.br/venda/casas/sp+mogi-das-cruzes/',    'https://www.vivareal.com.br/venda/sp/mogi-das-cruzes/casa_residencial/',    'https://mogi.olx.com.br/imoveis/venda/casas',    'https://www.imovelweb.com.br/casas-venda-mogi-das-cruzes-sp.html']

prices = []
addresses = []
areas = []
rooms = []
links = []

for url in imobiliarias:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for result in soup.find_all('div', {'class': 'simple-card__info'}):
        price = result.find('p', {'class': 'simple-card__price'}).text
        address = result.find('p', {'class': 'simple-card__address'}).text
        area = result.find('li', {'class': 'feature__item--area'}).text
        room = result.find('li', {'class': 'feature__item--rooms'}).text
        link = result.find('a')['href']
        
        prices.append(price)
        addresses.append(address)
        areas.append(area)
        rooms.append(room)
        links.append(link)

data = {
    'Endereço': addresses,
    'Preço': prices,
    'Área': areas,
    'Número de quartos': rooms,
    'Link': links
}

df = pd.DataFrame(data)
df.to_excel('casas.xlsx', index=False)
