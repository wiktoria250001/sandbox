
import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername="postgres + psycopg2",
    username="postgres",
    password="wiki3476",
    host="localhost",
    database="postgres",
    port=5433
)

engine = sqlalchemy.create_engine(db_params)
connection=engine.connect()
connection.execute(sql_query_1)
#sql_query_1=sqlalchemy.text("select * from public.my_table")
#sql_query_1=sqlalchemy.text("INSERT INTO public.my_table(name) VALUES('kępa');")
user= input('podaj nazwe zawodnika do usuniecia')
#sql_query_1=sqlalchemy.text("delete from public.my_table where name=''{user}';")
kogo_zminiec=input('podaj kogo zmienic')
na_kogo=input('podaj na kogo zamienic')
sql_query_1=sqlalchemy.text(f"update public.my_table set name ='{na_kogo}' where name= '{kogo_zminiec}':")

def dodaj_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text("INSERT INTO public.my_table(name) VALUES('{user}');")
    connection.execute(sql_query_1)
    connection.commit()
#cwok='stasiu'
#dodaj_uzytkownika(cwok)

def usun_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text("INSERT INTO public.my_table(name) VALUES('{user}');")

def