#klauzula where

import datetime
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'Db7543!#'
DB = 'shop'

stmt = """SELECT first_name as name, last_name as surname FROM client WHERE id=4;"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(stmt)

            for row in cursor:
                print(row)

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

