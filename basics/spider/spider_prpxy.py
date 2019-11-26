# -*- coding: utf-8 -*-
import urllib.request as url_req

url = 'http://www.whatismyip.com'
ips = {'175.153.23.184:61234'}

proxy_suppert = url_req.ProxyHandler()
opener = url_req.build_opener(proxy_suppert)

url_req.install_opener(opener)
req =  url_req.Request(url)
res = url_req.urlopen(req)
html = res.read().decode('utf-8')
print(html)