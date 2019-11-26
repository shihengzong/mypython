# -*- coding: UTF-8 -*-
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import urllib.request as req # urllib 导包
from myos import myos

res = req.urlopen("http://placekitten.com/g/500/500")  # 获取网页内容
print(res)

cat_img = res.read()
dir_name = './spider/spider_result'
file_name = 'cat_500_500.jpg'
result = myos.saveFile(dir_name,file_name,cat_img)
if result == 0 :
    print("写入失败,写入位数为:",result)

res_info = res.info()
print(res_info)
# Date: Wed, 16 Oct 2019 07:49:36 GMT
# Content-Type: image/jpeg
# Transfer-Encoding: chunked
# Connection: close
# Set-Cookie: __cfduid=d13a12beecd8e187cf5764f17a307e1441571212176; expires=Thu, 15-Oct-20 07:49:36 GMT; path=/; domain=.placekitten.com; HttpOnly
# Access-Control-Allow-Origin: *
# Cache-Control: public, max-age=86400
# Expires: Thu, 17 Oct 2019 07:49:36 GMT
# CF-Cache-Status: HIT
# Age: 49724
# Vary: Accept-Encoding
# Server: cloudflare
# CF-RAY: 52686fe51bd9dbf3-LHR