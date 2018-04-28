#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 下午2:08
# @Author  : Sulong
# @File    : socket_basics.py
# @Software: PyCharm
import socket,sys

# socket() 创建套接字
# socket.socket([family[, type[, proto]]])
# family: 套接字家族可以使AF_UNIX或者AF_INET
# type: # 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# protocol: 一般不填默认为0


# 创建 socket对象
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 获取 本地主机名
host = socket.gethostname()
# print(host)
prot = 9999

# b绑定端口号
serversocket.bind((host,prot))

# 设置最大连接数
serversocket.listen(5)
while True:
	# 建立客户端连接
	clientsocket,addr = serversocket.accept()
	print('链接地址%s'%str(addr))

	msg = '欢迎访问'+ '\r\n'
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()
