#!/usr/bin/python3
""" script that lists all states from the database """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # connect to mysql, passing 3 arguments in argv
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    cur_obj = db.cursor() # cursor object

    cur_obj.execute("SELECT * FROM states") # select the query

    myresult = cur_obj.fetchall()

    for i in myresult:
        print(i)

    cur_obj.close() #close cursor
    db.close() #close database
