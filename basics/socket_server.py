# -*- coding: UTF-8 -*-
# 文件名：server.py
 
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
host = '127.0.0.1'
print(host)
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
 
s.listen(5)                 # 等待客户端连接
while True:
    c,addr = s.accept()     # 建立客户端连接
    print ('连接地址：', addr)
    send_str = b'hello socket!'
    send_china = '上邪,我欲与君相知,长命无绝衰,山无陵,江水为竭,冬雷震震,夏雨雪,天地合,乃敢与君绝.'
    c.send(send_china.encode('utf-8'))
    c.close()                # 关闭连接