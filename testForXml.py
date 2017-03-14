# -*- coding:utf-8 -*-
from xml.dom.minidom import Document

testbmp=open("../../test.bmp","r")

coreContent=Document()

words=coreContent.createElement('words')
words.setAttribute('type','text')
content=coreContent.createTextNode('JUST SAY: ')
words.appendChild(content)
coreContent.appendChild(words)

pic=coreContent.createElement('img')
picCon=coreContent.createTextNode(testbmp.read())
testbmp.close()
pic.appendChild(picCon)
words.appendChild(pic)

afterWords=coreContent.createTextNode(' AND SAY NOTHING')
words.appendChild(afterWords)
print coreContent.toprettyxml(indent='')

double=coreContent.createElement('again')
douCon=coreContent.createTextNode('ISAY: ')
double.appendChild(douCon)
douCon=coreContent.createTextNode('youidot')
double.appendChild(douCon)

print double.toprettyxml(indent='').replace('\n','')