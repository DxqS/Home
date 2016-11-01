# coding:utf-8
'''
Created on 2016/11/1.

@author: Dxq
'''
from common import base


class Cert(base.BaseHandler):
    def get(self, typ):
        if typ == 'edu':
            return self.render('m_cert/edu_list.html')
        else:
            return self.render('m_cert/net_list.html')

    def post(self):
        pass
