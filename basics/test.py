# -*- coding: UTF-8 -*-
send_china = '上邪,我欲与君相知,长命无绝衰,山无陵,江水为竭,冬雷震震,夏雨雪,天地合,乃敢与君绝.'
bytes_str = send_china.encode('utf-8')
# print(bytes_str)


import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
# print(host)

import package_test.hello as hello
hello.hello()
