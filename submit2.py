# -*- coding: utf-8 -*-

import bs4
import requests
from shibboleth_login import ShibbolethClient

# ID = input('your username: ')
# PW = input('your passsword: ')

# client = ShibbolethClient(ID, PW)

#try:
# res = client.get('https://portal.student.kit.ac.jp/')
#print(type(res)) # => <class 'requests.models.Response'>
#except Exception:
    # error handling
#finally:
#    client.close()

#res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")

f = open('submit1.html', 'r')
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

f.close()

#client.close()
