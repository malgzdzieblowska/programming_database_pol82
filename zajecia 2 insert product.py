import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'Db7543!#'
DB = 'shop'

INSERT_PRODUCTS = """
INSERT INTO product (name, price, stock_quantity) VALUE
(%s, %s, %s);
"""

PRODUCTS = [
    ('Smartfon', 1500, 35),
    ('Telewizor LED 55"', 3500.50, 10),
    ('Konsola do gier', 1200, 3000),
    ('Słuchawki bezprzewodowe', 200, 5)
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_PRODUCTS, PRODUCTS)
            cnx.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists.")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n", err)
    else:
        print("An error occured\n", err)
else:
    print("Done.")
