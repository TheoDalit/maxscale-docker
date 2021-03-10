#!/usr/bin/env python3 
import mariadb
import sys

# Connect to MariaDB Platform https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
try:
    conn1 = mariadb.connect(
        user="maxuser",
        password="maxpwd",
        host="127.0.0.1",
        port=4000,

    )

    conn2 = mariadb.connect(
        user="maxuser",
        password="maxpwd",
        host="127.0.0.1",
        port=4000,

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur1 = conn1.cursor()
cur2 = conn2.cursor()

cur1.execute("SELECT * FROM zipcodes_one.zipcodes_one")
cur2.execute("SELECT * FROM zipcodes_two.zipcodes_two")


result1 = cur1.fetchall()
for row in result1:
    print (row)

result2 = cur2.fetchall()
for row in result2:
    print (row)

conn1.close()
conn2.close()
