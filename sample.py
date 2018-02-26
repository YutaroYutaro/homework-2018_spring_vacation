# -*- coding: utf-8 -*-

import bs4
import requests
import re
from shibboleth_login import ShibbolethClient
import settings

with open('submit1.html', 'r') as f:
    soup = bs4.BeautifulSoup(f, "lxml")

    notice_list = soup.find_all('dl', class_=re.compile('notice_list_dl clearfix'))

    for notice in notice_list:
        print(notice.get_text().replace("\t","").replace("\r\n","").replace("\n",""))
    # dates = soup.select('.nl_notice_date')
    # charges = soup.select('.nl_div_in_charge')
    # categories = soup.select('.nl_category')
    # notices = soup.select('.nl_notice')

    # for (date, charge, category, notice) in zip(dates[1:], charges[1:], categories[1:], notices[1:]):
    #     print(date.get_text())
    #     print(charge.get_text())
    #     print(category.get_text())
    #     print(notice.get_text())
