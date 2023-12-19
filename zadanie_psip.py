import sqlalchemy
import psycopg2 as ps
from dane import users_list

db_params = ps.connect(
    database='postgres',
    user='postgres',
    password='wiki3476',
    host='localhost',
    port=5433
)
#engine=sqlalchemy.create_engine(db_params)
#connection=engine.connect()


cursor= db_params.cursor()

def dodaj_uzytkownika(user:str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1 =f"INSERT INTO public.serafin_psip(city, name, nick, posts) VALUES ('{nick['city']}', '{nick['name']}', '{nick['nick']}', '{nick['posts']}');"
            cursor.execute(sql_query_1)
            db_params.commit()
dodaj_uzytkownika(input('dodaj uzytkownika'))
###dodac wszystkich uzytkownikow do tabeli


