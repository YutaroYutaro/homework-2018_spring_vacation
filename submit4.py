# -*- coding: utf-8 -*-

import bs4
import requests
from sql import SqlFunction
from shibboleth_login import ShibbolethClient
from twitter import TwitterFunction
import settings
import datetime
from time import sleep

html1 = 'submit1.html'
html4 = 'submit4.html'

dbname = settings.dbname
table1 = settings.table1
table2 = settings.table2
ID = settings.ID
PW = settings.PW
CK = settings.CK
CS = settings.CS
AT = settings.AT
AS = settings.AS

# sql.create(dbname)

while True:
    now = datetime.datetime.now()
    if now.hour == 5 and now.minute == 0:
        with ShibbolethClient(ID, PW) as client:
            res = client.get('https://portal.student.kit.ac.jp/')

            soup = bs4.BeautifulSoup(res.text, "html.parser")

            dates = soup.select('.nl_notice_date')
            charges = soup.select('.nl_div_in_charge')
            categories = soup.select('.nl_category')
            notices = soup.select('.nl_notice')

            twitter = TwitterFunction(CK, CS, AT, AS)

            with SqlFunction(dbname) as table:
                for (i, date, charge, category, notice) in zip(range(1, len(dates)), dates[1:], charges[1:],categories[1:], notices[1:]):
                    table.update(table2, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

                cnt = table.compare(table1, table2)

                if cnt != 0:
                    for i in range(1, cnt + 1):
                        rows = table.select_id(table2, i)

                        for row in rows:
                            str_date = row[1]
                            str_charge = row[2]
                            str_category = row[3]
                            str_notice = row[4]

                        body = '掲載日：' + str_date + '\r\n' + '発信課：' + str_charge + '\r\n' + '概要：' + str_category + '\r\n' + '詳細：' + str_notice
                        print(body)
                        twitter.tweet(body)

                    for (i, date, charge, category, notice) in zip(range(1, len(dates)), dates[1:], charges[1:],
                                                                   categories[1:], notices[1:]):
                        table.update(table1, i, date.get_text(), charge.get_text(), category.get_text(),
                                     notice.get_text())
                else:
                    body = '新たなお知らせはありません。'
                    print(body)
                    twitter.tweet(body)
    else:
        sleep(59)

# with open(html4, 'r') as f:

#     soup = bs4.BeautifulSoup(f, "html.parser")

#     dates = soup.select('.nl_notice_date')
#     charges = soup.select('.nl_div_in_charge')
#     categorys = soup.select('.nl_category')
#     notices = soup.select('.nl_notice')

#     twitter = TwitterFunction(api_key)

#     with SqlFunction(dbname) as table:
#         for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
#             table.update(table2, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())

#         cnt = table.compare(table1, table2)

#         if cnt != 0:
#             for i in range(1,cnt+1):
#                 rows = table.select_id(table2,i)

#                 for row in rows:
#                     str_date = row[1]
#                     str_charge = row[2]
#                     str_category = row[3]
#                     str_notice = row[4]

#                 body = '掲載日：' + str_date + '\r\n' + '発信課：' + str_charge + '\r\n' + '概要：' + str_category + '\r\n' + '詳細：' + str_notice
#                 print(body)
#                 twitter.tweet(body)

#             for (i, date, charge, category, notice) in zip(range(1,len(dates)), dates[1:], charges[1:], categorys[1:], notices[1:]):
#                 table.update(table1, i, date.get_text(), charge.get_text(), category.get_text(), notice.get_text())
#         else:
#             body = '新たなお知らせはありません。'
#             print(body)
#             twitter.tweet(body)
