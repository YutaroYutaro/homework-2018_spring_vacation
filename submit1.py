# -*- coding: utf-8 -*-

import requests
from shibboleth_login import ShibbolethClient

ID = input('your username: ')
PW = input('your passsword: ')

client = ShibbolethClient(ID, PW)

#try:
res = client.get('https://portal.student.kit.ac.jp/')
#print(type(res)) # => <class 'requests.models.Response'>
#except Exception:
    # error handling
#finally:
#    client.close()

res.raise_for_status()
print(res.text)
# f = open('submit1.html', 'w') # 書き込みモードで開く
# f.write(res.text) # 引数の文字列をファイルに書き込む
# f.close() # ファイルを閉じる
client.close()
