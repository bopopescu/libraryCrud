import pymysql
conn = pymysql.connect(host="", user = '', password = '',
                       db = 'library', charset='utf8')

def getAllData():
    curs = conn.cursor()
    sql = "select * from books"
    curs.execute(sql)
    rows = curs.fetchall()
    curs.close()
    return rows

def deleteData(list):
    curs = conn.cursor()
    for i in list:
        sql = "delete from books where seq = %s"
        curs.execute(sql,i)
        conn.commit()
    curs.close()

def insertData(bookname,author,pub,pubdate,content):
    curs = conn.cursor()
    # sql =
    curs.execute("insert into books values (0, %s, %s, %s, %s)",(bookname,author,pub,pubdate))

    curs.execute("insert into bookdetail (seq, bookinfo) values (0, %s)",content)
    conn.commit()
def getOneData(seq):
    curs = conn.cursor()
    sql = "select * from books where seq=%s"

    curs.execute(sql,seq)
    data1 = curs.fetchall()
    sql= "select bookinfo from bookdetail where seq=%s"
    curs.execute(sql,seq)
    data2=curs.fetchall()
    curs.close()
    list = [data1,data2]
    return list

    # sql = "insert into bookdetail (bookinfo) values (%s)
    # curs.execute(sql, content)

def updateData( bookname,author,pub,pubdate,content,seq):
    curs = conn.cursor()
    curs.execute("update books set bookname=%s, author=%s, pub=%s, pubyear=%s where seq =%s",(bookname,author,pub,pubdate,seq))
    conn.commit()
    curs.execute("update bookdetail set bookinfo=%s where seq=%s",(content,seq))
    conn.commit()
    curs.close()

def getDetailDataALL():
    curs = conn.cursor()
    sql = "select bookinfo from bookdetail"
    curs.execute(sql)
    rows = curs.fetchall()
    curs.close()
    return rows



# curs = conn.cursor()
#
# sql = "select * from testtable"
# curs.execute(sql)
#
# rows = curs.fetchall()
#
# print(rows)
# for i in rows:
#     print(i)
#
#
# conn.close()
