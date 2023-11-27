

import requests
from bs4 import BeautifulSoup
import folium

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

#for item in nazwy_miejscowosci
#print(get_coordinate_of(item))
# zwrócic mape z pinezka odnoszczaca sie do uzytkowanika podanego z klawiatury
#zwroci mape z wsztystkimi uzytkownikami z danej listy znajomymi



##RYSOWANIE MAPY
city = get_coordinate_of(city='Zamość')
map = folium.Map(location=get_coordinate_of(city='Zamość'), tiles="OpenStreetMap", zoom_start=15)
for item in nazwa_miejscowosci:
    folium.Marker(
        location=city,
        popup='GEOINFORAMTYKA RZĄDZI OU YEEEAAAAAH!'
).add_to(map)

map.save('mapka.html')