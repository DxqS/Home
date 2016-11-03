# coding:utf-8
'''
Created on 2016/11/3.

@author: Dxq
'''
from controller import home_ctrl

urls = [
    '/home/index', home_ctrl.Index,
    '/home/edit', home_ctrl.Edit,
    '/home/page/list', home_ctrl.PageList
]
