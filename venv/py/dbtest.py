# import psycopg2
import pymysql
# host = '35.243.162.113'
# dbname = 'library'
# user = 'beemo'
# password ='beemo1234'
#
# conn_string = " host='35.243.162.113' dbname = 'library' user ='beemo' password = 'beemo1234'"
# conn = psycopg2.connect(conn_string)
conn = pymysql.connect(host="35.243.162.113", user = 'beemo', password = 'beemo1234',
                       db = 'library', charset='utf8')
curs = conn.cursor()

sql = "select * from testtable"
curs.execute(sql)

rows = curs.fetchall()

print(rows)
for i in rows:
    print(i)



conn.close()

# con =
#
# cur = conn.cursor()

# cur.execute ("select * from testtable")
