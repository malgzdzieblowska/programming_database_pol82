import mysql.connector
from mysql.connector import connect, errorcode


USER = 'root'
PASSWORD = 'Db7543!#'

## Otwieranie połączenia do bazy
#with connect(user=USER, password=PASSWORD) as cnx:

## mamy połączenie z serwerem, odpalamy cursor. Cursor to obiekt, na którym możemy wykonywać połączenie do bazy
## na koniec też trzeba go zamknąć
#cursor = cnx.cursor()

## Odpalamy metodę execute
#cursor.execute("""CREATE DATABASE shop;""")

## protokół iteratora - __iter__, __next__

#należy pamiętać o zamknięciu połączenia do bazy, aby nie doszło do "wycieku pamięci" - alokowaniu pamięci, której nie używamy
#cursor.close()
#cnx.close()

## Powyżej wykomentowany pierwszy sposób, ale my będziemy używać menadżera kontekstu
"""
Tak jak poniżej będziemy zawsze tworzyć
wraz z obsługą błędów
To jest dla instrukcji DDL tylko!!!!
"""

CREATE_DATABASE_QUERY = """CREATE DATABASE shop2;"""

try:
    with connect(user=USER, password=PASSWORD) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(CREATE_DATABASE_QUERY)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n",err)
    else:
        print("An Error occured\n", err)
#nie piszemy finally, bo wykonałoby się zawsze. Dajemy else - spróbował, nie było błędów więc Done
else:
    print("Done")