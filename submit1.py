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

#res = requests.get('https://portal.student.kit.ac.jp/')
print(res.text)
client.close()
