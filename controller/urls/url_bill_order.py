# coding:utf-8
'''
Created on 2016/11/3.

@author: Dxq
'''
from controller import bill_order_ctrl

urls = [
    '/bill/order/cert/(net|education)', bill_order_ctrl.CertPay,
    '/bill/order/poster/(\d+)', bill_order_ctrl.PosterPay,
    '/bill/order/page/(\d+)', bill_order_ctrl.PagePay,

]
