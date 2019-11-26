# -*- coding: UTF-8 -*-
# 爬取有道翻译
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import urllib.request as url_req # urllib 导包
import urllib.parse as parse # urllib 导包
from myos import myos
url = 'https://tieba.baidu.com/f?kw=dnf%E5%89%91%E5%B8%9D'
header = {}
header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' 
# data = {}
# data['query'] = 'callable'
# data = parse.urlencode(data).encode('utf-8')

# req = url_req.Request(url,data)  # 获取网页内容  data不为空时,默认为post提交否则为get
# req.add_header("User-Agent",'xxx')
# res = url_req.urlopen(req)
# res = url_req.urlopen(url,data,header)
res = url_req.urlopen(url)
html = res.read().decode('utf-8')
print(html)

