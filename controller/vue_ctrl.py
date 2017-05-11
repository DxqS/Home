# coding:utf-8
'''
Created on 2016/11/26.

@author: chk01
'''
from common import base


class Index(base.BaseHandler):
    def get(self):

        return self.render('vue/vue_index.html')

    def post(self):
        pass
