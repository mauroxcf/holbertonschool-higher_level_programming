#!/usr/bin/python3
""" script that lists all cities from the database """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # connect to mysql, passing 4 arguments in argv
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306,
                         charset="utf8")

    # cursor object
    cur_obj = db.cursor()

    # select the query
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id"
    cur_obj.execute(query)

    myresult = cur_obj.fetchall()

    for i in myresult:
        print(i)

    # close cursor
    cur_obj.close()

    # close database
    db.close()
