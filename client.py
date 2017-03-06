# -*- coding:utf-8 -*-
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(2048).decode('utf-8')
for x in range(0,3):
	data=raw_input("input(%s):" % str(x))
	s.send(data)
	print s.recv(2048).decode('utf-8')
s.send(b'exit')
s.close()