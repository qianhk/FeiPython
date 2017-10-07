#!/usr/bin/env python
# coding=utf-8

import MySQLdb as mysqldb


def store_reldb():
    db = mysqldb.connect(host='localhost', user='root', passwd='Abc', db='TestDb')
    cursor = db.cursor()

    # Create a table
    cursor.execute('drop table if exists verify_info')
    sql = '''
        create table verify_info (
        id int not null auto_increment primary key,
        verify_code char(20)
        )'''
    cursor.execute(sql)

    # Insert data
    f = open('../cache/result.txt', 'rb')
    for line in f:
        verify_code = line.strip()
        sql = 'insert into verify_info(verify_code) values ("%s");' % (verify_code)
        cursor.execute(sql)
    try:
        db.commit()
    except:
        db.rollback()
        f.close()
        print 'Error happened when inserting data'
    f.close()
    db.close()


if __name__ == '__main__':
    store_reldb()
