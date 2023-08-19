#!/usr/bin/python3
import sys
import MySQLdb
# import mysql.connector
""" 1. Filter states """


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
        passwd='dB@200374',
        db=DB_NAME
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id asc")
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
