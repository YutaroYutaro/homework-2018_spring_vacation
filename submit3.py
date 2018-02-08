# -*- coding: utf-8 -*-

import bs4
import requests
import sql
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

#     for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
#         sql.insert(dbname, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

#     sql.update(dbname, 1, 'date', 'charge', 'category', 'notice')

#     sql.delete(dbname)

#     sql.delete_id(dbname, 1)

#     sql.select(dbname)

#     sql.select_id(dbname, 1)

with open('submit1.html', 'r') as f:

    soup = bs4.BeautifulSoup(f, "html.parser")

    dates = soup.select('.nl_notice_date')
    charges = soup.select('.nl_div_in_charge')
    categorys = soup.select('.nl_category')
    notices = soup.select('.nl_notice')

    # for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
    #     sql.insert(dbname, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

    # sql.update(dbname, 1, 'date', 'charge', 'category', 'notice')

    # sql.delete(dbname)

    # sql.delete_id(dbname, 1)

    # sql.select(dbname)

    # sql.select_id(dbname, 2)

