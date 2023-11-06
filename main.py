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

add_user_to(users_list)
add_user_to(users_list)
add_user_to(users_list)
#posts = input('podaj liczbe postów?')
#users_list.append({'name': name,'posts': posts})
#name = input('podaj imie?')
#posts = input('podaj liczbe postów?')
#users_list.append({'name': name,'posts': posts})
#make it work, make it properly, make it fast

for user in users_list:
   # print(users_list)
    print(f'Twój znajomy {user['name']} dodał {user["posts"]} ')





#print(f'Twój znjaomy{zmienna_na_dane[0]["imie"]} opublikowal {zmienna_na_dane[0]["posts"]} postow!!)
#zmienna_na_imie = input ('Podaj nazwe uzytkownika')
#print (f'TO JEST FACEBOOK {zmienna_na_dane[1]["nick"]} !!!!')



