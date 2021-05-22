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
    table1_sql = 'create table air ' \
                 '( locationId varchar(255) null,' \
                 'location   varchar(255) null,' \
                 'city       varchar(255) null,' \
                 'country    varchar(255) null,' \
                 'utc        varchar(255) null,' \
                 'local      varchar(255) null,' \
                 'parameter  varchar(255) null,' \
                 'value      varchar(255) null,' \
                 'unit       varchar(255) null,' \
                 'latitude   varchar(255) null,' \
                 'longitude  varchar(255) null);'
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
        air_sql = 'create table small' + str(i) + ' ' \
                     '( locationId varchar(255) null,' \
                     'location   varchar(255) null,' \
                     'city       varchar(255) null,' \
                     'country    varchar(255) null,' \
                     'utc        varchar(255) null,' \
                     'local      varchar(255) null,' \
                     'parameter  varchar(255) null,' \
                     'value      varchar(255) null,' \
                     'unit       varchar(255) null,' \
                     'latitude   varchar(255) null,' \
                     'longitude  varchar(255) null);'
        try:
            sql_con.cursor.execute(air_sql)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    sql_con = sql_connect.Sql_c()
    create_table()