# -*- coding:utf-8 -*-
import socket
import threading
import time

def tcplink(sock,addr):
	print "Accept from %s" % str(addr)
	sock.send(b'Welcome')
	while True:
		data=sock.recv(2048)
		time.sleep(1)
		if not data:
			break
		print 'receive %s: %s' % (str(type(data)), data.decode('utf-8'))
		sock.send(('Hello, %s! length: %d' % (str(type(data)), len(str(type(data))))))
	sock.close()
	print "Connection from %s closed" % str(addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(8)
print "Waiting for connection..."
while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink, args=(sock,addr))
	t.start()