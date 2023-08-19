#!/usr/bin/python3
""" 2. Filter states by user input """
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

    query = "SELECT * FROM states WHERE name = %s"
    arguments = (STATE,)

    CURSOR.execute(query, arguments)

    result = CURSOR.fetchone()
    print(result)

    CURSOR.close()
    CONNECTION.close()
