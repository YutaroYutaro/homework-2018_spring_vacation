# -*- coding: utf-8 -*-

import bs4
import requests
from shibboleth_login import ShibbolethClient

# ID = input('your username: ')
# PW = input('your passsword: ')

# with ShibbolethClient(ID, PW) as client:
#     res = client.get('https://portal.student.kit.ac.jp/')
    
#     soup = bs4.BeautifulSoup(res.text, "html.parser")
    
#     dates = soup.select('.nl_notice_date')
#     charges = soup.select('.nl_div_in_charge')
#     categorys = soup.select('.nl_category')
#     notices = soup.select('.nl_notice')

#     for (date, charge, category, notice) in zip(dates[1:], charges[1:], categorys[1:], notices[1:]):
#         print(date.get_text())
#         print(charge.get_text())
#         print(category.get_text())
#         print(notice.get_text())

with pen('submit1.html', 'r') as f:

    soup = bs4.BeautifulSoup(f, "html.parser")

    dates = soup.select('.nl_notice_date')
    charges = soup.select('.nl_div_in_charge')
    categorys = soup.select('.nl_category')
    notices = soup.select('.nl_notice')

    for (date, charge, category, notice) in zip(dates[1:], charges[1:], categorys[1:], notices[1:]):
        print(date.get_text())
        print(charge.get_text())
        print(category.get_text())
        print(notice.get_text())

