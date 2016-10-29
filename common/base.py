# coding:utf-8
'''
Created on 2016/10/29.

@author: Dxq
'''
import json


def rtjson(code=1, **args):
    '''return json'''
    if code == 1:
        args['status'] = 1
    else:
        args['status'] = 0
        args['error_code'] = code

    # return json.dumps(args)
    return args
