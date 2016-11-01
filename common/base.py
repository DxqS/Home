# coding:utf-8
'''
Created on 2016/10/29.

@author: Dxq
'''
from tornado.web import RequestHandler
import config
import hashlib
import time


def rtjson(code=1, **args):
    '''
    给键值对统一增加status属性及一些错误code给出相应的错误信息
    '''
    if code == 1:
        args['status'] = 1
    else:
        args['status'] = 0
        args['error_code'] = code
        # args['msg'] = errorDesc.get(code)
    # return json.dumps(args)
    return args


class Storage(dict):
    """
    转化字典表现形式
    f[key]->f.key
    """

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("uid")

    def input(self, name, default=None, strip=True):
        return self._get_argument(name, default, self.request.arguments, strip)

    def get_template_namespace(self):
        namespace = super(BaseHandler, self).get_template_namespace()
        # namespace.update(myfilter.filters)
        namespace['gconf'] = config.gconf
        namespace['session'] = {'uname': self.get_current_user()}
        #
        aa = [config.gconf['up_safe_token'], str(int(time.time()) + 5 * 3600), '/']
        ss = hashlib.md5('&'.join(aa)).hexdigest()
        self.set_cookie('_upt', ss[12:20] + aa[1], '.yanshanpk.com')

        return namespace
