# coding:utf-8
'''
Created on 2016/10/31.

@author: Dxq
'''
from handlers import *

urls = [
    (r"/", handler1),
    (r"/story/([0-9]+)", handler2)
]
print urls
