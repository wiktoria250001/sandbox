

import requests
from bs4 import BeautifulSoup
import folium
from dane import users_list

# pobranie strony internetowej
nazwa_miejscowosci = 'Gdańsk'
def get_coordinates(city:str)->list[float,float]:
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


#for item in nazwy_miejscowosci
#print(get_coordinate_of(item))
#from dane import users_list
# zwrócic mape z pinezka odnoszczaca sie do uzytkowanika podanego z klawiatury
def get_map_of(user:str)->None:
    city = get_coordinates(user['city'])
    map = folium.Map(location=get_coordinate_of(city='Zamość'), tiles="OpenStreetMap", zoom_start=15)
    for user in users_list:
        folium.Marker(
            location=get_coordinate_of(city=user['city']),
            popup=f'Tu rządzi {user["name"]} z geoinforamtyki 2023\n ouu yeeea \n !!!!!!'
        ).add_to(map)

    map.save('mapka.html')

def get_map_of(coordiantes: list, lista_imionn)->None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=15)
    for user in users_list:
        folium.Marker(
            location=get_coordinate_of(city=user['city']),
            popup=f'Tu rządzi {user["name"]} z geoinforamtyki 2023\n ouu yeeea \n !!!!!!'
        ).add_to(map)

    map.save('mapka.html')


#zwroci mape z wsztystkimi uzytkownikami z danej listy znajomymi



##RYSOWANIE MAPY
# city = get_coordinate_of(city='Zamość')
# map = folium.Map(location=get_coordinate_of(city='Zamość'), tiles="OpenStreetMap", zoom_start=7)
# for item in nazwa_miejscowosci:
#     folium.Marker(
#         location=city,
#         popup='GEOINFORAMTYKA RZĄDZI OU YEEEAAAAAH!'
# ).add_to(map)
#
# map.save('mapka.html')
#
# city = get_coordinate_of(users: List) -> None:
#     map = folium.Map(location=get_coordinate_of(city='Zamość'), tiles="OpenStreetMap", zoom_start=7)
#     for item in nazwa_miejscowosci:
#         folium.Marker(
#             location=city,
#             popup='GEOINFORAMTYKA RZĄDZI OU YEEEAAAAAH!'
# ).add_to(map)
#
# map.save('mapka.html')
# from dane import users_list
# get_map_of(users_list)