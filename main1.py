from mysql.connector import connect
from mysql.connector import MySQLConnection

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
with connect(user=USER, password=PASSWORD) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("""CREATE DATABASE shop2;""")

