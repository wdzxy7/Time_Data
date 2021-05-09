import Classes
for i in range(20, 21):
    print(i)
    t = Classes.Test(i, cpu=4, ram=5)
    t.insert_data()
    t.get_sum()
    t.test(loop_time=1000)