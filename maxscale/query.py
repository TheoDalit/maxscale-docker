#!/usr/bin/env python3 
import mariadb
import sys

# https://stackoverflow.com/questions/37261665/using-python-to-query-multiple-sql-databases-on-different-servers
# Connect to MariaDB Platform https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
try:
    conn1 = mariadb.connect(
        user="maxuser",
        password="maxpwd",
        host="127.0.0.1",
        port=4000,

    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn1.cursor()


print('The last 10 rows from zipcodes_one')
cur.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10")
result1 = cur.fetchall()
for row in result1:
    print (row)

print('The first 10 rows from zipcodes_two')
cur.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")
result2 = cur.fetchall()
for row in result2:
    print (row)

print('The largest zipcode from zipcodes_one')
cur.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY zipcode DESC LIMIT 1")
result3 = cur.fetchall()
print(result3)

print('The smallest zipcode from zipcodes_two')
cur.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY zipcode LIMIT 1")
result4 = cur.fetchall()
print(result4)

conn1.close()
