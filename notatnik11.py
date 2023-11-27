

import requests
from bs4 import BeautifulSoup
import re
# pobranie strony internetowej
nazwa_miejscowosci = 'Gdańsk'
def get_coordinate_of(city:str)->list[float,float]:
    #city = 'Gdansk'
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    #adres_URL1= f'https://pl.wikipedia.org/wiki/Kuryłówka'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')
    #pobranie współrzednych
    response_html_latitude = response_html.select('.latitude')[1].text # . poniewaz class
    response_html_latitude = float(response_html_latitude.replace(',','.'))
    response_html_longitude = response_html.select('.longitude')[1].text # . poniewaz class
    response_html_longitude = float(response_html_longitude.replace(',','.'))
    #print(response_html_latitude, response_html_longitude)
    return [response_html_latitude, response_html_longitude]
print(get_coordinate_of(nazwa_miejscowosci))