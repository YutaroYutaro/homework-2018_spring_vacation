# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing


class SqlFunction(object):

    # テーブルに接続する
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    # テーブル作成
    def create_table(self,table):
        c = self.conn.cursor()
        create_table = 'create table %s (id int, date varchar, charge varchar, category varchar, notice varchar)'
        c.execute(create_table % table)

    # テーブルに要素を挿入
    def insert_into_table(self, table, id, date, charge, category, notice):
        c = self.conn.cursor()
        insert_sql = 'insert into %s (id, date, charge, category, notice) values (?,?,?,?,?)'
        info = (id, date, charge, category, notice)
        c.execute(insert_sql % table, info)
        self.conn.commit()

    # テーブルから行ごとの要素を取り出し，そのリストを返す
    def select_from_table(self):
        c = self.conn.cursor()
        select_sql = 'select * from info'
        rows = c.execute(select_sql)
        return rows

    # idで選択したテーブルの行の要素を取り出して返す
    def select_from_table_id(self, table, id):
        self.conn.row_factory = sqlite3.Row
        c = self.conn.cursor()
        select_id_sql = 'select * from %s where id = ?'
        row = c.execute(select_id_sql % table, (id,))
        return row

    # テーブルの要素を上書きする
    def update_table(self, table, id, date, charge, category, notice):
        c = self.conn.cursor()
        update_sql = 'update %s set date = ?, charge = ?, category = ?, notice = ? where id = ?'
        info = (date, charge, category, notice, id)
        c.execute(update_sql % table, info)
        self.conn.commit()

    # ２つのテーブルを比較し，新たに挿入された要素の数を返す
    def compare(self, table1, table2):
        c1 = self.conn.cursor()
        c2 = self.conn.cursor()
        select1_sql = 'select * from %s'
        select2_sql = 'select * from %s'
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

    # テーブルの要素を全部削除する
    def delete_element(self, table):
        c = self.conn.cursor()
        delete_sql = 'delete from %s'
        c.execute(delete_sql % table)
        self.conn.commit()

    # idで選択したテーブルの行の要素を削除する
    def delete_element_id(self, table, id):
        c = self.conn.cursor()
        delete_id_sql = 'delete from %s where id = ?'
        c.execute(delete_id_sql % table, (id,))
        self.conn.commit()

    # テーブルを削除する
    def drop_table(self, table):
        c = self.conn.cursor()
        drop_dummy_sql = 'drop table %s'
        c.execute(drop_dummy_sql % table)
        self.conn.commit()

    def close(self):
        self.conn.close()
