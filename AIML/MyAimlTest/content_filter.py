# coding:utf-8
'''
Created on 2016/10/4.

@author: Dxq
'''

import re


def ss(content):
    if re.search("[a-zA-Z0-9]", content, flags=re.IGNORECASE):
        res = 'WEIGHT FOUR TWO'
    elif re.search("你是谁", content, flags=re.IGNORECASE):
        res = '你是谁'
    elif re.search("你究竟是谁", content, flags=re.IGNORECASE):
        res = '你究竟是谁'
    elif re.search("多大了", content, flags=re.IGNORECASE):
        res = '多大了'
    else:
        res = '其他'
    return res
