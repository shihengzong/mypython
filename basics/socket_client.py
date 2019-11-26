# -*- coding: UTF-8 -*-
# 文件名：client.py
 
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
host = '127.0.0.1'
port = 12345                # 设置端口号
 
s.connect((host, port))
receive_bytes = s.recv(1024)
receive_str = receive_bytes.decode("utf-8")
print (receive_str)
s.close()