# -*- coding: utf-8 -*-

import requests
from shibboleth_login import ShibbolethClient
import settings

ID = settings.ID
PW = settings.PW

with ShibbolethClient(ID, PW) as client:
    res = client.get('https://portal.student.kit.ac.jp/')
    f = open('submit1.html', 'w')
    f.write(res.text)
    f.close()
