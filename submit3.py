# -*- coding: utf-8 -*-

import bs4
import requests
from sql import SqlFunction
from shibboleth_login import ShibbolethClient

dbname = 'database.db'

# sql.create(dbname)

# ID = input('your username: ')
# PW = input('your passsword: ')

# with ShibbolethClient(ID, PW) as client:
#     res = client.get('https://portal.student.kit.ac.jp/')
    
#     soup = bs4.BeautifulSoup(res.text, "html.parser")
    
#     dates = soup.select('.nl_notice_date')
#     charges = soup.select('.nl_div_in_charge')
#     categorys = soup.select('.nl_category')
#     notices = soup.select('.nl_notice')

    # table = SqlFunction(dbname)

    # table.create()

    # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
    #     table.insert(i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

    # table.update(1, 'date', 'charge', 'category', 'notice')

    # table.delete()

    # table.delete_id(1)

    # table.select()

    # table.select_id(2)

    # table.close()


    # with SqlFunction(dbname) as table:
    #     table.create()

    #     for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
    #         table.insert(i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

    #     table.update(1, 'date', 'charge', 'category', 'notice')

    #     table.delete()

    #     table.delete_id(1)

    #     table.select()

    #     table.select_id(2)


with open('submit1.html', 'r') as f:

    soup = bs4.BeautifulSoup(f, "html.parser")

    dates = soup.select('.nl_notice_date')
    charges = soup.select('.nl_div_in_charge')
    categorys = soup.select('.nl_category')
    notices = soup.select('.nl_notice')

    # table = SqlFunction(dbname)

    # table.create()

    # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
    #     table.insert(i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

    # table.update(1, 'date', 'charge', 'category', 'notice')

    # table.delete()

    # table.delete_id(1)

    # table.select()

    # table.select_id(2)
    
    # table.close()
    

    # with SqlFunction(dbname) as table:
    #     table.create()

    #     for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
    #         table.insert(i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

    #     table.update(1, 'date', 'charge', 'category', 'notice')

    #     table.delete()

    #     table.delete_id(1)

    #     table.select()

    #     table.select_id(2)


