# coding:utf-8
'''
Created on 2017/1/11.

@author: chk01
'''

from PIL import Image, ImageDraw, ImageFont

back = 'avatar.jpg'

ttfont = ImageFont.truetype("shuang.ttf", 70)

ttfont2 = ImageFont.truetype("kai.ttf", 120)
ttfont3 = ImageFont.truetype("hei.ttf", 50)
im = Image.open(back)
draw = ImageDraw.Draw(im)
draw.text((50, 40), u'双  望  桥  沙  场', fill=(255, 0, 0), font=ttfont)
draw.text((120, 180), u'陈 建 双', fill=(6, 15, 70), font=ttfont2)
draw.text((80, 350), u'地址：翁垟镇镇西北路', fill=(196, 124, 76), font=ttfont3)
draw.text((80, 400), u'手机：', fill=(196, 124, 76), font=ttfont3)
draw.text((230, 400), u'13587457295', fill=(255, 76, 17), font=ttfont3)
draw.text((230, 450), u'13806608363', fill=(255, 76, 17), font=ttfont3)
draw.text((230, 500), u'15868079299', fill=(255, 76, 17), font=ttfont3)

# draw.text((690, 550), u'     13587457295', fill=(255, 144, 48), font=ttfont3)
#
#
# draw.text((40, 600), u'      13806608363', fill=(255, 144, 48), font=ttfont3)
# draw.text((690, 600), u'     15868079299', fill=(255, 144, 48), font=ttfont3)
# im.show()
im.save('end1.jpg')
