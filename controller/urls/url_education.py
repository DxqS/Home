# coding:utf-8
'''
Created on 2016/11/3.

@author: Dxq
'''
from controller import education_ctrl

urls = [
    '/edu/cert', education_ctrl.Cert,
    '/edu/wait', education_ctrl.Wait,
    '/edu/edit', education_ctrl.Edit
]
