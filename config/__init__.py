# coding:utf-8
'''
Created on 15/7/31

@author: shenyufeng
'''

import os
import yaml
import redis
import upyun
import time

from pymongo import MongoClient

from wechatpy import WeChatClient

from wechatpy.session.redisstorage import RedisStorage

ospath = os.path.split(__file__)[0]

run_mode = os.environ.get('RUN_ENV', 'local')

pony = yaml.load(file(os.path.split(__file__)[0] + '/pony.yml', 'r'))[run_mode]

gconf = yaml.load(file(ospath + '/gconf.yml', 'r'))[run_mode]
gconf['uptime'] = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
gconf['run_mode'] = run_mode

srv = yaml.load(file(ospath + '/srv.yml', 'r'))[run_mode]

wx = yaml.load(file(ospath + '/wx.yml', 'r'))[run_mode]

errorDesc = yaml.load(file(ospath + '/errorDesc.yml', 'r'))

upFile = upyun.UpYun(gconf['up_file_bucket'], gconf['up_file_uname'], gconf['up_file_pwd'],
                     timeout=30, endpoint=upyun.ED_AUTO)
msgDict = {}

pool = redis.ConnectionPool(**srv['redis'])
rdb = redis.StrictRedis(connection_pool=pool)

mdb = MongoClient(srv['mongo']['host'], srv['mongo']['port'])
mdb.admin.authenticate(srv['mongo']['uname'], srv['mongo']['pwd'], mechanism='SCRAM-SHA-1')
mdb = mdb[srv['mongo']['db']]

wxclient = WeChatClient(wx['APP_ID'], wx['APP_SECRET'], session=RedisStorage(rdb))
