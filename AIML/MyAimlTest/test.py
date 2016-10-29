# coding:utf-8
'''
Created on 2016/10/4.

@author: Dxq
'''
import aiml
import content_filter

kernel = aiml.Kernel()
kernel.learn('start_up.xml')
kernel.respond("启动")
while True:
    print kernel.respond(raw_input(">"))
