# coding:utf-8
'''
Created on 2016/10/31.

@author: Dxq
'''
import tornado.web
import tornado.ioloop


class handler(tornado.web.RequestHandler):
    def get(self):
        return self.write('hello')


from controller import url_handler


def myApp():
    print url_handler
    return tornado.web.Application(url_handler)


PORT = 10086
if __name__ == "__main__":
    app = myApp()
    app.listen(PORT)
    print "http://localhost:{}/".format(PORT)
    tornado.ioloop.IOLoop.current().start()
