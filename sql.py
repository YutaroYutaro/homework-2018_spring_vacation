# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

class SqlFunction(object):
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def create(self,table):
        c = self.conn.cursor()
        create_table = '''create table %s (id int, date varchar(32), charge varchar(32), category varchar(32), notice varchar)'''
        c.execute(create_table % table)

    def insert(self, table, id, date, charge, category, notice):
        c = self.conn.cursor()
        insert_sql = '''insert into %s (id, date, charge, category, notice) values (?,?,?,?,?)'''
        info =  (id, date, charge, category, notice)
        c.execute(insert_sql % table, info)
        self.conn.commit()

    def select(self):
        c = self.conn.cursor()
        select_sql = '''select * from info'''
        for row in c.execute(select_sql):
            print(row)

    def select_id(self, table, id):
        self.conn.row_factory = sqlite3.Row
        c = self.conn.cursor()
        select_id_sql = '''select * from %s where id = ?'''
        rows = c.execute(select_id_sql % table, (id,))
        return rows

    def update(self, table, id, date, charge, category, notice):
        c = self.conn.cursor()
        update_sql = '''update %s set date = ?, charge = ?, category = ?, notice = ? where id = ?'''
        info =  (date, charge, category, notice, id)
        c.execute(update_sql % table, info)
        self.conn.commit()

    def compare(self, table1, table2):
        c1 = self.conn.cursor()
        c2 = self.conn.cursor()
        select1_sql = '''select * from %s'''
        select2_sql = '''select * from %s'''
        c1.execute(select1_sql % table1)
        c2.execute(select2_sql % table2)
        cnt = 0
        while c1.fetchone()[1:4] != c2.fetchone()[1:4]:
            cnt += 1
            print('ng')
            if cnt >= 200:
                cnt = 0
                break

        return cnt

    def delete(self, table):
        c = self.conn.cursor()
        delete_sql = '''delete from %s'''
        c.execute(delete_sql % table)
        self.conn.commit()

    def delete_id(self, table, id):
        c = self.conn.cursor()
        delete_id_sql = '''delete from %s where id = ?'''
        c.execute(delete_id_sql % table, (id,))
        self.conn.commit()

    def drop(self, table):
        c = self.conn.cursor()
        drop_dummy_sql = '''drop table %s'''
        c.execute(drop_dummy_sql % table)
        self.conn.commit()

    def close(self):
        self.conn.close()