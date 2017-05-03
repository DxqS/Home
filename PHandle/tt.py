# coding:utf-8
'''
Created on 2017/5/2.

@author: chk01
'''
from poster import *

poster = Poster('poster_back.png', 'save_path.jpg')
poster.add_img('mat1.jpg', (313, 71, 120))
poster.add_text('大大大', font='app.ttf', color="#ffffff", position=(200, 300, 100))
poster.save()
