# -*- coding: utf-8 -*-

import bs4
import requests
from sql import SqlFunction
from shibboleth_login import ShibbolethClient
import settings

# ID = settings.ID
# PW = settings.PW
dbname = settings.dbname
table1 = settings.table1

# sql.create(dbname)

# with ShibbolethClient(ID, PW) as client:
#     res = client.get('https://portal.student.kit.ac.jp/')
    
#     soup = bs4.BeautifulSoup(res.text, "html.parser")
    
#     dates = soup.select('.nl_notice_date')
#     charges = soup.select('.nl_div_in_charge')
#     categorys = soup.select('.nl_category')
#     notices = soup.select('.nl_notice')

    # with SqlFunction(dbname) as table:
        # table.create(table1)

        # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
        #     table.insert(i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())


        # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
        #     table.update(table1, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

        # table.update(1, 'date', 'charge', 'category', 'notice')

        # table.delete(table1)

        # table.delete_id(table1, 1)

        # table.select(table1)

        # rows = table.select_id(table1, 2)



with open('submit1.html', 'r') as f:

    soup = bs4.BeautifulSoup(f, "html.parser")

    dates = soup.select('.nl_notice_date')
    charges = soup.select('.nl_div_in_charge')
    categorys = soup.select('.nl_category')
    notices = soup.select('.nl_notice')

    # with SqlFunction(dbname) as table:
        # table.create(table1)

        # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
        #     table.insert(i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())


        # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
        #     table.update(table1, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

        # table.update(1, 'date', 'charge', 'category', 'notice')

        # table.delete(table1)

        # table.delete_id(table1, 1)

        # table.select(table1)

        # rows = table.select_id(table1, 2)
