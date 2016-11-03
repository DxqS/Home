# coding:utf-8
'''
Created on 2016/11/3.

@author: Dxq
'''
from controller import net_ctrl

urls = [
    '/net/cert', net_ctrl.Cert,
    '/net/wait', net_ctrl.Wait,
    '/net/edit', net_ctrl.Edit
]
