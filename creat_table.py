import random
import sql_connect


if __name__ == '__main__':
    sql_con = sql_connect.Sql_c()
    front = 0
    back = 500000
    pace = random.randint(100000, 500000)
    for i in range(1, 12):
        sql = 'TRUNCATE TABLE select_data.small' + str(i) + ';'
        sql_con.cursor.execute(sql)
        sql = 'INSERT INTO select_data.small' + str(i) + ' SELECT * FROM unknown_data.air as a WHERE ' \
              'a.id > ' + str(front) + ' and a.id <= ' + str(back) + ';'
        sql_con.cursor.execute(sql)
        print(front, back, pace)
        pace = random.randint(100000, 500000)
        back = back + pace