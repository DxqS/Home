# coding:utf-8
'''
Created on 2016/11/1.

@author: Dxq
'''
from common import base


class List(base.BaseHandler):
    def get(self):
        return self.render('m_home/list.html')

    def post(self):
        pass
