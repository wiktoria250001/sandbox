import requests
from bs4 import BeautifulSoup
import folium
from dane import users_list

def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'name': name, 'posts': posts})


def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imie uzykownika do usuniecia: ')
    for user in users_list:
        if user["name"] == name:
            tmp_list.append(user)
    print('Znaleziono użytkowników:')
    print('0: Usuń wszystkich znalezionych użytkowników')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'wybierz numer użytkownika do usuniecia: '))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])


def show_users_from(users_list:list)->None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')

def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('podaj nick użytkownika do modyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono!!!')
            user['name'] = input('podaj nowe imie: ')
            user['nick'] = input('podaj nowa ksywke: ')
            user['posts'] = int(input('podaj liczbe postow: '))
            user['city'] = input('podaj miasto')

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
from dane import users_list
# zwrócic mape z pinezka odnoszczaca sie do uzytkowanika podanego z klawiatury
def get_map_one_user(user:str)->None:
    city = get_coordinate_of(user['city'])
    map = folium.Map(location=get_coordinate_of(city='Zamość'), tiles="OpenStreetMap", zoom_start=15)
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








def gui(users_list:list) -> None:
    while True:
        print(f'MENU: \n'
              f'0: Zakończ program \n'
              f'1: Wyświetl użytkowników \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Modyfikuj użytkownika'
              f'5: Wygeneruj mapę z użytkownikiem'
              f'6: Wygeneruj mapę z uzytkownikami'
              )
        menu_option = input('Podaj funkcję do wywołania')
        print(f'Wybrano funkcję {menu_option}')

        match menu_option:
            case '0':
                print('Kończę pracę')
                break
            case '1':
                print('Wyświetlanie listę użytkowników')
                show_users_from(users_list)
            case '2':
                print('Dodawanie użytkownika')
                add_user_to(users_list)
            case '3':
                print('Usuwanie użytkownika')
                remove_user_from(users_list)
            case '4':
                print('Modyfikuję użytkownika')
                update_user(users_list)
            case '5' :
                print('Rysuję mapę z użytkownikiem')
                user = input('podaj nazwe uzytkownika do modyfikacji')
                for item in users_list:
                    if item['nick'] == user:
                        get_map_one_user(item)
            case '6'  :
                print('Rysuję mapę z użytkownikami')
                get_map_of(users_list)




