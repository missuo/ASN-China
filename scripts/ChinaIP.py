'''
Author: Vincent Young
Date: 2022-11-17 02:14:24
LastEditors: Vincent Young
LastEditTime: 2022-11-17 03:19:20
FilePath: /ASN-China/syncIP.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''

import requests

allChina = "https://raw.githubusercontent.com/cbuijs/ipasn/master/country-asia-china.list"

v4China = "https://raw.githubusercontent.com/cbuijs/ipasn/master/country-asia-china4.list"

v6China = "https://raw.githubusercontent.com/cbuijs/ipasn/master/country-asia-china6.list"

r = requests.get(allChina) 
with open("IP.China.list", "wb") as allChinaIP:
         allChinaIP.write(r.content)

r = requests.get(v4China) 
with open("IPv4.China.list", "wb") as v4ChinaIP:
         v4ChinaIP.write(r.content)

r = requests.get(v6China) 
with open("IPv6.China.list", "wb") as v6ChinaIP:
         v6ChinaIP.write(r.content)
