import Classes
from combine_excel import combine

hz = 2.5
cpu = 4  # cpu核数
ram = 16  # ram大小
end = 10  # 测试次数
loop_time = 10  # 每次循环测试次数
save_number = 1  # 最后合并的excel编号 例：1result.csv

for i in range(1, end):
    print(i)
    t = Classes.Test(i, cpu=cpu, ram=ram, hz=hz)
    t.insert_data()
    t.get_sum()
    t.test(loop_time=loop_time)

combine(1, end, save_number)