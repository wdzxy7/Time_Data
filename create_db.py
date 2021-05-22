import sql_connect


def create_table():
    # 创建数据库
    create_db_sql = 'create database unknown_data default character set utf8;'
    try:
        sql_con.cursor.execute(create_db_sql)
    except Exception as e:
        print(e)
    # 建表
    sql = 'use unknown_data;'
    sql_con.cursor.execute(sql)
    table1_sql = 'CREATE TABLE `air` (' \
                 '`locationId` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`location` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`city` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`country` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`utc` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`local` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`parameter` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`value` float(7,3) DEFAULT NULL,' \
                 '`unit` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`latitude` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`longitude` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                 '`id` int(11) NOT NULL AUTO_INCREMENT,' \
                 'PRIMARY KEY (`id`))'
    try:
        sql_con.cursor.execute(table1_sql)
    except Exception as e:
        print(e)
    create_db_sql = 'create database select_data default character set utf8;'
    try:
        sql_con.cursor.execute(create_db_sql)
    except Exception as e:
        print(e)
    sql = 'use select_data;'
    sql_con.cursor.execute(sql)
    for i in range(1, 10):
        air_sql = 'create table small' + str(i) + ' (' \
                  '`locationId` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`location` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`city` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`country` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`utc` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`local` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`parameter` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`value` float(7,3) DEFAULT NULL,' \
                  '`unit` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`latitude` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`longitude` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,' \
                  '`id` int(11) NOT NULL AUTO_INCREMENT,' \
                  'PRIMARY KEY (`id`))'
        try:
            sql_con.cursor.execute(air_sql)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    sql_con = sql_connect.Sql_c()
    create_table()