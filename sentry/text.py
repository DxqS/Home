# coding:utf-8
'''
Created on 2017/4/5.

@author: chk01
'''
from raven import Client

dsn = 'https://61b0d7a50a1649188ec705e618adccdd:c1eed98b2aea4a2082328b30724b6a41@sentry.io/155338'

client = Client(dsn=dsn, raise_send_errors=False, transport=None,
                install_sys_hook=True, install_logging_hook=True,
                hook_libraries=None, enable_breadcrumbs=True, site="Dxq_test")
try:
    1 / 0
except ZeroDivisionError:
    ident = client.get_ident(client.captureException())
    print "Exception caught; reference is %s" % ident
