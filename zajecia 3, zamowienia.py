import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'Db7543!#'
DB = 'shop'


INSERT_ORDERS = """
INSERT INTO order_detail (client_id, product_id, quantity, order_date ) VALUE 
(%s, %s, %s, %s);
"""

ORDERS = [
    (1, 1, 3, '2024-03-04'),
    (2, 3, 2, '2024-03-05'),
    (3, 2, 1, '2024-03-06'),
    (1, 4, 2, '2024-03-07'),
    (2, 4, 1, '2024-03-08')
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_ORDERS, ORDERS)
            #obowiązkowo dla DML
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
