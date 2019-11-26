import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import urllib.request as url_req # urllib 导包
import urllib.parse as parse # urllib 导包
import re
from myos import myos


url = 'https://www.bilibili.com/'
res = url_req.urlopen(url)
html = res.read().decode('utf-8')
result = re.findall(r'//i1.hdslb.com/bfs/archive/5d0a7cec11993392631e090468fd01491371c179.jpg@160w_100h.jpg',html)
print(html)
print(result)


