# coding:utf-8
'''
Created on 2016/10/31.

@author: Dxq
'''
import tornado.web


class handler1(tornado.web.RequestHandler):
    def get(self):
        return self.finish('hello')

    def post(self):
        pass


class handler2(tornado.web.RequestHandler):
    def get(self):
        return self.finish('hello')

    def post(self):
        pass


class handler3(tornado.web.RequestHandler):
    def get(self):
        return self.finish('hello')

    def post(self):
        pass
