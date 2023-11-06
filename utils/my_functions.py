from newone import users_list

def add_user_to(users_list:list) -> None:
    """
    add object to list
    :param users_list: user list
    :return: None
    """
    name = input('podaj imie?')
    posts = input('podaj liczbe postów?')
    users_list.append({"name": name,"posts": posts})
name = input(' podaj imie uzytkownika do usunecia: ')
def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: List - user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imie uzytkownika do usuniecia:')

    for user in users_list:
        if user["name"]== name:
            print(f'Znaleziono uzytkownika{user}')
            #users_list.remove(user)
            tmp_list.append(user)
    print('Znaleziono nastepujacych uzytkownikow :')
    print("0: Usun wszyskich znalezionych uzytkownikow")
    for numerek,user_to_be_removed in enumerate(tmp_list):
        print( f'{numerek+1}: {user_to_be_removed}')
    numer = int(input(f'wybierz numer uzytkownka do usuniecia: '))
    if numer == 0:
        for user in tmp_list:
            if user['name'] == name:
                users_list.remove(tmp_list[numer-1])
    else:
     users_list.remove(tmp_list[numer-1])

    # print(numer)
    # print(tmp_list[numer-1])
    #   users_list.remove(tmp_list[numer-1])


     remove_user_from(users_list)



#add_user_to(users_list)
#posts = input('podaj liczbe postów?')
#users_list.append({'name': name,'posts': posts})
#name = input('podaj imie?')
#posts = input('podaj liczbe postów?')
#users_list.append({'name': name,'posts': posts})
#make it work, make it properly, make it fast

def show_users_from(users_list:list) -> None:
    for user in users_list:
        print(f'Twój znajomy {user['name']} dodał {user["posts"]} ')


def gui(users_list: list) -> None:
    while True:
        print(f'MENU: \n'
            f'0: Zakoncz program\n'
            f'1: Wyswietl uzytkownka\n'   
            f'2: Podaj uzytkownika\n'
            f'3: Usun uzytkownika\n'
            f'4: Modyfikuj uzytkownika')

        menu_option = input('Podaj funkcję do wywołania: ')
        print(f'Wybrano funkcję {menu_option}')

        if menu_option == '0':
            print('Kończę pracę')
            break
        elif menu_option == '1':
            print('Wyświetlanie listy użytkowników')
            show_users_from(users_list)
        elif menu_option == '2':
            print('Dodawanie użytkowników')
            add_user_to(users_list)
        elif menu_option == '3':
            print('Usuwanie użytkownika')
            remove_user_from(users_list)
        elif menu_option == '4':
            print('Modyfikuj')

gui(users_list)





#print(f'Twój znjaomy{zmienna_na_dane[0]["imie"]} opublikowal {zmienna_na_dane[0]["posts"]} postow!!)
#zmienna_na_imie = input ('Podaj nazwe uzytkownika')
#print (f'TO JEST FACEBOOK {zmienna_na_dane[1]["nick"]} !!!!')



