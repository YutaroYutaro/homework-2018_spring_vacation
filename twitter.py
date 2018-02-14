#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

class TwitterFunction(object):
    def __init__(self, CK, CS, AT, AS):
        self.CK = CK    # Consumer Key
        self.CS = CS    # Consumer Secret
        self.AT = AT    # Access Token
        self.AS = AS    # Accesss Token Secert

    def tweet(self,body):
        # ツイート投稿用のURL
        url = "https://api.twitter.com/1.1/statuses/update.json"
        # ツイート本文
        params = {"status": body}
        # OAuth認証で POST method で投稿
        twitter = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        req = twitter.post(url, params = params)

        # レスポンスを確認
        if req.status_code == 200:
            print ("OK")
        else:
            print ("Error: %d" % req.status_code)