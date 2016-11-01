# coding:utf-8
'''
Created on 2016/11/1.

@author: Dxq
'''
from common import base


class List(base.BaseHandler):
    def get(self):
        return self.render('m_poster/poster_list.html')

    def post(self):
        pass


class Add(base.BaseHandler):
    def get(self):
        return self.render('m_poster/poster_add.html')

    def post(self):
        return self.finish(base.rtjson())


class Edit(base.BaseHandler):
    def get(self, _id):
        return self.render('m_poster/poster_edit.html')

    def post(self, _id):
        return self.finish(base.rtjson())
