import cx_Oracle
import sys

arguments = sys.argv
argument_connection_string = arguments[0]

con = cx_Oracle.connect(argument_connection_string)

print con.version

cur = con.cursor()
cur.execute('select * from dual')

for result in cur:
  print result

cur.close
con.close()
