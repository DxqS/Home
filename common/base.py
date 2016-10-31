# coding:utf-8
'''
Created on 2016/10/29.

@author: Dxq
'''


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


def aa():
    pass
