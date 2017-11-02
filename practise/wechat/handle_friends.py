# -*- coding: utf-8 -*-

# with open('wechatplay.py','r','utf-8') as file:
#     for line in file:
#         print(line)


import codecs
data = open("test.txt").read()
if data[:3] == codecs.BOM_UTF8:
    data = data[3:]
    print(data.decode("utf-8"))