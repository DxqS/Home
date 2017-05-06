# coding:utf-8
'''
Created on 2017/5/5.

@author: Dxq
'''
from pic import *
import PIL
poster = Poster('poster_back.png', 'save_path.jpg')
poster.add_img('mat1.jpg', (313, 71, 120))
ft = 'app.ttf'
poster.add_text(u'大大大', color="#ffffff", position=(200, 300, 100))
poster.add_mul_text(u'你拆我啊\n发顺丰', color="#ffffff", position=(200, 300, 100), align="center")
poster.save()
