# coding:utf-8
'''
Created on 2016/11/1.

@author: Dxq
'''
from manage import poster_ctrl

urls = [
    '/m/poster/list', poster_ctrl.List,
    '/m/poster/add', poster_ctrl.Add,
    '/m/poster/edit/(\d+)', poster_ctrl.Edit
]
