#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N) """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # connect to mysql, passing 3 arguments in argv
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306,
                         charset="utf8")

    # cursor object
    cur_obj = db.cursor()

    # select the query
    cur_obj.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    myresult = cur_obj.fetchall()

    for i in myresult:
        print(i)

    # close cursor
    cur_obj.close()

    # close database
    db.close()
