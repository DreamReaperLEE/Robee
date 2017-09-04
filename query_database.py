# *_*coding:utf-8 *_*

import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='tuling', port=3306, charset="utf8")
cur = conn.cursor()

#query the message in your database ,and return the result if it's been define
def query_title(msg):
    try:
        cur.execute("select * from own where title like '%s%s%s'" % ('%',msg,'%'))
        rows = cur.fetchall()
        if len(rows)>0:
            result = rows[0][2]
        else:
            result = 'null'
        return result
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])