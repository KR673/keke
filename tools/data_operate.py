import sqlite3

def db_exec(sql):
    # 没有加db后缀时, 数据一真插入不了, 但可以那家表. 且没有报错
    con = sqlite3.connect('./db/data.db')
    cur = con.cursor()
    # 使用index()时, 如果没有找到这个值会报错, 所以使用find()代替
    if sql.find(';') >= 0:
        sql_list = sql.split(';')
        for s in sql_list:
            cur.execute(s)
    else:
        cur.execute(sql)
    con.commit()
    con.close()

def db_init():
    sql_enroll = 'CREATE Table enroll(city, department, position, positon_code, apply_num, enroll_num)'
    db_exec(sql_enroll)

if __name__ == '__main__':
    # db_init()
    # db_exec("INSERT INTO enroll (city, department, positon_code, position, enroll_num, apply_num) values ('漯河市', '漯河市郾城区人民法院', '21101011', '五级法官助理', '5', '24');")
    db_init()