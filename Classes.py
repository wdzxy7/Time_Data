import time
import random
import sql_connect
from pandas import DataFrame


class Test:
    def __init__(self, runtime, cpu=4, ram=8, hz=2.5):
        self.sql_con = sql_connect.Sql_c()
        self.data_sum = {}
        self.run_time = str(runtime)
        self.cpu = cpu
        self.ram = ram
        self.hz = hz

    def insert_data(self, front=0, back=500000):
        back = random.randint(600000, 900000)
        for i in range(1, 11):
            sql = 'TRUNCATE TABLE select_data.small' + str(i) + ';'
            self.sql_con.cursor.execute(sql)
            sql = 'INSERT INTO select_data.small' + str(i) + ' SELECT * FROM unknown_data.air as a WHERE ' \
                                                             'a.id > ' + str(front) + ' and a.id <= ' + str(back) + ';'
            self.sql_con.cursor.execute(sql)
            pace = random.randint(400000, 900000)
            back = back + pace

    def get_sum(self):
        for i in range(1, 11):
            sql = 'select count(*) from select_data.small' + str(i) + ';'
            self.sql_con.cursor.execute(sql)
            res = self.sql_con.cursor.fetchall()
            self.data_sum[i] = res[0][0]

    def test(self, loop_time=10):
        df = DataFrame([], columns=['hz', 'cpu', 'ram', 'sql', 'data_sum', 'time'])
        for i in range(1, 11):
            print(i)
            for j in range(loop_time):
                sql = 'select sum(value) from select_data.small' + str(i) + ';'
                t1 = time.perf_counter()
                self.sql_con.cursor.execute(sql)
                t2 = time.perf_counter()
                diff = t2 - t1
                arr = DataFrame([[self.hz, self.cpu, self.ram, sql, self.data_sum[i], diff]], columns=['hz', 'cpu', 'ram', 'sql', 'data_sum', 'time'])
                df = df.append(arr, ignore_index=True)
        df.to_csv('result' + self.run_time + '.csv', index=False)
