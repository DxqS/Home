# coding:utf-8
'''
Created on 2016/10/29.

@author: Dxq
'''
import os
import tornado.web
import tornado.ioloop

from common import base

# 端口号
PORT = 8080

settings = dict(
    blog_title=u"Tornado Blog",
    template_path=os.path.join(os.path.dirname(__file__), "views"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
)


class Handler(tornado.web.RequestHandler):
    def get(self):
        return self.render('AIML/aiml.html')

    def post(self):
        ask = self._get_argument('ask', default=None, source=self.request.arguments, strip=True)
        print ask
        respond = 1
        return self.finish(base.rtjson(respond=respond))


def make_app():
    return tornado.web.Application([('/aiml', Handler)], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print "http://localhost:{}/".format(PORT)
    tornado.ioloop.IOLoop.current().start()
