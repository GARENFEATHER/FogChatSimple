# -*- coding:utf-8 -*-
import socket

class dataType(object):
	"""docstring for dataType"""
	def __init__(self, arg):
		super(dataType, self).__init__()
		self.arg = arg
		self.anaarg=arg+" test"
		self.inside=233

	def func():
		print "test func"
		
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(2048).decode('utf-8')
dataN=[]
for x in range(0,3):
	data=raw_input("input(%s):" % str(x))
	dataN.append(data)
	s.send(dataN)
	print s.recv(2048).decode('utf-8')
s.send(b'exit')
s.close()