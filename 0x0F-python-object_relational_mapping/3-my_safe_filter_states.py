#!/usr/bin/python3
""" 3. SQL Injection... """
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

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    arguments = (STATE, )
         
    CURSOR.execute(query, arguments)

    result = CURSOR.fetchall()
    for row in result:
        print(row)

    CURSOR.close()
    CONNECTION.close()
