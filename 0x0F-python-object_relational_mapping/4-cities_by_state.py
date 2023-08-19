#!/usr/bin/python3
""" 4. Cities by states """
import sys
import MySQLdb


if __name__ == '__main__':
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    DB_PORT = 3306

    CONNECTION = MySQLdb.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME
    )

    CURSOR = CONNECTION.cursor()

    CURSOR.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    result = CURSOR.fetchall()
    for row in result:
        print(row)

    CURSOR.close()
    CONNECTION.close()
