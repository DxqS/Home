# coding:utf-8
'''
Created on 2016/11/3.

@author: Dxq
'''
from controller import bill_ctrl

urls = [
    '/bill/center', bill_ctrl.Center,
    '/bill/(recharge|buy)/history', bill_ctrl.History
]
