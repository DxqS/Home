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

from PIL import Image, ImageDraw, ImageFont

im = Image.open('poster_back.png')

image1 = Image.open('mat1.jpg').convert("RGBA")
image2 = Image.open('2.jpg').convert("RGBA")
image3 = Image.open('mat1.jpg').convert("L")
print image1
print image2
# image3.show()
# print Image.blend(image1, image2, .3).show()
print Image.composite(image1, image2, image3).show()
im.show()
font = 'app.ttf'
size = 50
text = u'a大法官ffff'
ft = ImageFont.truetype(font, size) if font else None
ss = ImageDraw.ImageDraw(im)
print ss.getfont()
sss = ss.textsize(text, font=ft)[0]
print sss

draw = ImageDraw.Draw(im)

ft = ImageFont.truetype(font, size)
# 以下[210,558]为用户名名字显示初始位置
# pattern = re.compile(u'[\u4e00-\u9fa5]')
# len_c = len(pattern.findall(unicode(user_name)))
# len_o = len(user_name) - len_c
#
# user_name_x = int(375 - float(size * len_c + size * len_o / 2) / 2)
draw.text([320 - sss / 2, 198], text, font=ft)
text2 = u'$$我爱你%\nv环环a'
draw.multiline_text([320 - sss / 2, 250], text2, font=ft, align="center")
im.save('1.jpg')
