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