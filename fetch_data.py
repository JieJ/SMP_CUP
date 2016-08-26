import os
import MySQLdb
import _mysql

# class smp_cup_pipeline(object):
#     def __init__:
#         server = "localhost"
#         user_name = "root"
#         password = "qwert123456"
#         db_name = "smp_cup"
#         self.db = _mysql.connect(server, user_name, password, dbName)

#     def get_user_info():
#         self.db.query("SELECT * FROM user_info WHERE nickname != 'None'")
#         r = self.db.store_result()
#         print type(r)


server = "localhost"
user_name = "root"
password = "qwert123456"
db_name = "smp_cup"
db = _mysql.connect(server, user_name, password, db_name)
db.query("SELECT * FROM user_info WHERE nickname != 'None'")
r = db.store_result()
print type(r)
f = open('data' + os.sep + 'nickname_gender.txt', 'w')
for i in range(10):
    item = r.fetch_row()
    f.write(item[0][2] + '\t' + item[0][4] + '\n')
f.close()

