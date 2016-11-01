# coding:utf-8
'''
Created on  2016/3/25

@author:  think
'''

from common import base


class Login(base.BaseHandler):
    '''
    管理员登录
    get()
    post(uname,pwd)
    '''

    def get(self):
        self.clear_all_cookies()

        # m = Manager.get(username='admin')
        # if m is None:
        #     mpwd = hashlib.md5('admin456').hexdigest()
        #     Manager(username='admin', password=mpwd, ctime=int(time.time()), utime=int(time.time()))
        # print m.username
        return self.render('m_manager/login.html')

    def post(self):
        # mpwd = hashlib.md5(self.input('password')).hexdigest()
        # m = Manager.get(username=self.input('username'))
        #
        # if m is None:
        #     # self.write(base.rtjson(0))
        #     return self.finish(base.rtjson(0))
        #
        if not (self.input('username') == 'admin' and self.input('password') == '123'):
            return self.write(base.rtjson(0))

        self.set_secure_cookie('user', self.input('username'))
        return self.write(base.rtjson())


class Logout(base.BaseHandler):
    def get(self):
        self.clear_all_cookies()
        return self.redirect('/m/login')
