import time
import pymysql
import sql_connect
from pandas import DataFrame

if __name__ == '__main__':
    sql_con = sql_connect.Sql_c()
    df = DataFrame([], columns=['sql', 'data_sum', 'time'])
    data_sum = {}
    for i in range(1, 12):
        sql = 'select count(*) from select_data.small' + str(i) + ';'
        sql_con.cursor.execute(sql)
        res = sql_con.cursor.fetchall()
        data_sum[i] = res[0][0]

    for i in range(1, 12):
        print(i)
        for j in range(100):
            sql = 'select sum(value) from select_data.small' + str(i) + ';'
            t1 = time.perf_counter()
            sql_con.cursor.execute(sql)
            t2 = time.perf_counter()
            diff = t2 - t1
            arr = DataFrame([[sql, data_sum[i], diff]], columns=['sql', 'data_sum', 'time'])
            df = df.append(arr, ignore_index=True)
    df.to_csv('sum2.csv', index_label=False)
