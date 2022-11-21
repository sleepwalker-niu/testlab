import  pymysql
from datetime import datetime
db = pymysql.connect(host="localhost", user="root", password="123456", database="fishproject", charset="utf8")

dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(dt)
print("===================================================================")
cursor = db.cursor()
    # print("db1******************************************************************\n")
sql = "insert into video_save_info(time, path, size_len, size_height, num_LtoR, num_RtoL, type, flag_pos, speed) values ('%s', '%s', '%d', '%d', '%d', '%d',\
                                                                 '%d','%d', '%d')" % (
    dt, 'save_path1', 1, 1, 0, 0, 0, 3, 0)

cursor.execute(sql)
db.commit()



cursor1 = db.cursor()
    # print("db1******************************************************************\n")
sql1 = "insert fish_num(data_time, daq) values ('%s', '%d')" % (dt, 1)

cursor1.execute(sql1)
db.commit()



db.close()

