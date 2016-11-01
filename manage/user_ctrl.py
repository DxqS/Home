# coding:utf-8
'''
Created on 16/6/15

@author: cgt
'''

from common import base


class List(base.BaseHandler):
    def get(self):
        return self.render('m_user/user_list.html')
