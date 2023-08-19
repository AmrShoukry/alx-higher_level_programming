#!/usr/bin/python3
""" 5. All cities by state """
import sys
import MySQLdb


if __name__ == '__main__':
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    DB_PORT = 3306
    STATE = sys.argv[4]

    CONNECTION = MySQLdb.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME
    )

    CURSOR = CONNECTION.cursor()

    query = "SELECT cities.name FROM cities INNER JOIN states ON\
    cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    arguments = (STATE, )
    CURSOR.execute(query, arguments)

    result = CURSOR.fetchall()
    for index, row in enumerate(result):
        if index == 0:
            print(row[0], end='')
        else:
            print(f", {row[0]}", end='')
    print()

    CURSOR.close()
    CONNECTION.close()
