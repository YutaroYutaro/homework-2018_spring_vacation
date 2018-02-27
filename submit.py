# -*- coding: utf-8 -*-

import bs4
import requests
from shibboleth_login import ShibbolethClient
import settings

# パースするテスト用ファイルをオープン
with open('submit1.html', 'r') as f:

    soup = bs4.BeautifulSoup(f, "lxml")

    # (class="div... cat... notice_list_dl clearfix)毎にパース
    notice_list = soup.find_all('dl', class_=re.compile('notice_list_dl clearfix'))

    # パースしたものを改行と空白を削除して表示
    for notice in notice_list:
        # noticeをタグ毎にパース
        date = notice.find('dd', class_='nl_notice_date')
        charge = notice.find('dd', class_='nl_div_in_charge')
        category = notice.find('dd', class_='nl_category')
        info = notice.find('dd', class_='nl_notice')

        if date:
            print('掲載日：' + date.get_text())

        if charge:
            print('発信課：' + charge.get_text())

        if category:
            print('概要：' + category.get_text())

        if info:
            # infoをタグ毎にパース
            tag_a = info.find('a')
            tag_a_href = info.find('a', href=True)
            notice_info = info.find('p', class_='notice_info')

            if tag_a:
                print(tag_a.get_text().replace("\t", "").replace("\n", ""))
            if tag_a_href:
                print(tag_a_href['href'])
            if notice_info:
                print(notice_info.get_text().replace("\t", ""),)
            # print('詳細：' + info.get_text().replace("\t", ""))

        print('--------------------------------------------------------------------------------------------------------\
----------------------------------------------------------------------------------------')
        # print(notice.get_text().replace("\t", "").replace("\r\n", "").replace("\n", ""))
