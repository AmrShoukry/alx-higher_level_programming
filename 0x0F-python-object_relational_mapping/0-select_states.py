#!/usr/bin/python3
import sys
import MySQLdb
# import mysql.connector
""" 0. Get all states """


if __name__ == '__main__':
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]

    connection = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME
    )

    # connection = mysql.connector.connect(
    #     host=DB_HOST,
    #     user=DB_USER,
    #     password=DB_PASS,
    #     database=DB_NAME
    # )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id asc")
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()
