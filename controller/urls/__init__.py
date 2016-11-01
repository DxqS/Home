# coding:utf-8
'''
Created on 2016/11/1.

@author: Dxq
'''

'''
加载目录下的所有url配置文件。
url配置文件是一个python源代码文件，以url_开头，里面定义了urls（list类型）变量。
interceptor:后面定义了当前url的拦截器
'''

import os

urls = []
ctrls = []

for f in os.listdir(os.path.split(__file__)[0]):
    module_name, ext = os.path.splitext(f)
    if module_name.startswith('url_') and ext == '.py':
        module = __import__(__name__ + '.' + module_name, fromlist=module_name)
        for i, url in enumerate(module.urls):
            if i % 2:
                ctrls.append((module.urls[i - 1], url))
                urls.append((module.urls[i - 1]))
                urls.append(url.__module__ + '.' + url.__name__)
