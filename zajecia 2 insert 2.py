import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'Db7543!#'
DB = 'shop'


INSERT_CLIENT_5 = """
INSERT INTO client (first_name, last_name, email) VALUE 
('David','Jones','david.jones@example.com');
"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(INSERT_CLIENT_1)
            cursor.execute(INSERT_CLIENT_2)
            cursor.execute(INSERT_CLIENT_3)
            cursor.execute(INSERT_CLIENT_4)
            cursor.execute(INSERT_CLIENT_5)
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
