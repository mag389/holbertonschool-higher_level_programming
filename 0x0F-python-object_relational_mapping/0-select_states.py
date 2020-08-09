#!/usr/bin/python3
""" states script """
import sqlalchemy
import MySQLdb
import sys


if __name__ != '__main__':
    exit()
if len(sys.argv) is not 4:
    print("in if {}".format(len(sys.argv)))
    exit()
# args are: username, passwd, db name
conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
