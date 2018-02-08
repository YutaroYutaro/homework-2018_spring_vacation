# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

def create(dbname):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table info (id int, date varchar(32), charge varchar(32), category varchar(32), notice varchar)'''
        c.execute(create_table)

def insert(dbname, id, date, charge, category, notice):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        insert_sql = '''insert into info (id, date, charge, category, notice) values (?,?,?,?,?)'''
        info =  (id, date, charge, category, notice)
        c.execute(insert_sql, info)
        conn.commit()

def select(dbname):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        select_sql = '''select * from info'''
        for row in c.execute(select_sql):
            print(row)

def select_id(dbname, id):
    with closing(sqlite3.connect(dbname)) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        select_id_sql = '''select * from info where id = ?'''
        rows = c.execute(select_id_sql, (id,))
        for row in rows:
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])

def update(dbname, id, date, charge, category, notice):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        update_sql = '''update info set date = ?, charge = ?, category = ?, notice = ? where id = ?'''
        info =  (date, charge, category, notice, id)
        c.execute(update_sql, info)
        conn.commit()

def delete(dbname):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        delete_sql = '''delete from info'''
        c.execute(delete_sql)
        conn.commit()

def delete_id(dbname, id):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        delete_id_sql = '''delete from info where id = ?'''
        c.execute(delete_id_sql, (id,))
        conn.commit()
