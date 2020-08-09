#!/usr/bin/python3
""" states script """
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    state = sys.argv[4]
    if len(state) > 15:
        exit()
    command = "SELECT cities.name \
              FROM cities LEFT JOIN states \
              ON cities.state_id = states.id \
              WHERE states.name LIKE BINARY '{}' \
              ORDER BY cities.id ASC".format(state)
    cur.execute(command)
    query_rows = cur.fetchall()
    counter = 0
    for row in query_rows:
        if counter is 1:
            print(", ", end="")
        print(row[0], end="")
        counter = 1
    print("")
    cur.close()
    conn.close()
