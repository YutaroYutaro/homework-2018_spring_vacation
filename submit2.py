# -*- coding: utf-8 -*-

import bs4
import requests
import re
from shibboleth_login import ShibbolethClient
import settings

# テスト用ファイルをオープン
with open('submit1.html', 'r') as f:

    soup = bs4.BeautifulSoup(f, "lxml")

    notice_list = soup.find_all('dl', class_=re.compile('notice_list_dl clearfix'))

    for notice in notice_list:
        print(notice.get_text().replace("\t", "").replace("\r\n", "").replace("\n", ""))
