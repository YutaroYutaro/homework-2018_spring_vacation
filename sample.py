# name_list = ["Jhon", "Mike", "Bob"]
# age_list = [23, 31, 28]

# for (name, age) in zip(name_list, age_list):
#     print(name)
#     print(age)

# import sqlite3
# from contextlib import closing

# dbname = 'database.db'

# id = 1
# date = 'date'
# charge = 'charge'
# category = 'category'
# notice = 'notice'

# with closing(sqlite3.connect(dbname)) as conn:
#     c = conn.cursor()
#     # sql = 'insert into info (id, date, charge, category, notice) values (?,?,?,?,?)'
#     # info =  (id, date, charge, category, notice)
#     # c.execute(sql, info)
#     # conn.commit()

#     sql = 'delete from info where id=?'
#     c.execute(sql, (1,))
#     conn.commit()

#     select_sql = 'select * from info'
#     for row in c.execute(select_sql):
#      print(row)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from requests_oauthlib import OAuth1Session

# CK = 'mkcHlMdLfmZvscaLUWibbUlKX'                             # Consumer Key
# CS = 'jC9XC4OJK7Ne2zISx69zd7P2FQ8eYoxGmFIqgfVZCtMviCwwFv'         # Consumer Secret
# AT = '962172337134084096-OJeMSd75evbKPuPidoOv9EyRQaIzndS' # Access Token
# AS = '7j2Jss9vwugAN4bexBKWrF0sAhj7a1Pw9JWOpw0FCU48E'         # Accesss Token Secert

# # ツイート投稿用のURL
# url = "https://api.twitter.com/1.1/statuses/update.json"

# # ツイート本文
# params = {"status": "Hello, World!"}

# # OAuth認証で POST method で投稿
# twitter = OAuth1Session(CK, CS, AT, AS)
# req = twitter.post(url, params = params)

# # レスポンスを確認
# if req.status_code == 200:
#     print ("OK")
# else:
#     print ("Error: %d" % req.status_code)

# -*- coding: utf-8 -*-

import datetime

now = datetime.datetime.now() # 現在の日時を取得

print(now.year)           # 年： 2016
print(now.month)          # 月： 2
print(now.day)            # 日： 23
print(type(now.hour))           # 時： 11
print(now.minute)         # 分： 53
print(now.second)         # 秒： 42
print(now.microsecond)    # マイクロ秒： 728665