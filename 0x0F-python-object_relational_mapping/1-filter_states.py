#!/usr/bin/python3
""" 1. Filter states """
import sys
import MySQLdb


if __name__ == '__main__':
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    DB_PORT = 3306

    connection = MySQLdb.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
