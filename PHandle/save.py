# coding:utf-8
'''
Created on 2017/5/2.

@author: Dxq
'''

def add_img(self, path=None, position=None, **attributes):
        back = self.back
        poster = self.poster
        self_pic = Image.open(path)
        self_wid, self_hei = self_pic.size
        show_wid = 120
        if self_hei > self_wid:
            r = float(self_hei * show_wid) / self_wid
            self_pic = self_pic.resize((show_wid, int(r)), Image.ANTIALIAS)
            box = (313, 71, 313 + show_wid, 71 + int(r))
        else:
            r = float(self_wid * show_wid) / self_hei
            self_pic = self_pic.resize((int(r), show_wid), Image.ANTIALIAS)
            box = (313, 71, 313 + int(r), 71 + show_wid)

        back.paste(self_pic, box)

        r, g, b, a = poster.split()
        back.paste(poster, (0, 0, self.size[0], self.size[1]), mask=a)

        qrcode = Image.open(qrcode)
        qr_size = 165
        qrcode = qrcode.resize((qr_size, qr_size), Image.ANTIALIAS)
        # 二维码大小
        # 100,100为二维码初始点
        qr_box = (292, 863, 292 + qr_size, 863 + qr_size)
        back.paste(qrcode, qr_box)

        draw = ImageDraw.Draw(back)
        font_dp = 'resource/app.ttf'
        size = 28

        ft = ImageFont.truetype(font_dp, size)
        # 以下[210,558]为用户名名字显示初始位置
        pattern = re.compile(u'[\u4e00-\u9fa5]')
        len_c = len(pattern.findall(unicode(user_name)))
        len_o = len(user_name) - len_c

        user_name_x = int(375 - float(size * len_c + size * len_o / 2) / 2)
        draw.text([user_name_x, 198], user_name, font=ft, fill=color)
        back.save(fpath)
        return fpath

        # def add_text(self, path=None, **attributes):
        #     """
        #     在所有类型的聊天对象中进行搜索
        #
        #     :param name: 名称 (可以是昵称、备注等)
        #     :param attributes: 属性键值对，键可以是 sex(性别), province(省份), city(城市) 等。例如可指定 province='广东'
        #     :return: 匹配的聊天对象合集
        #     :rtype: :class:`wxpy.Chats`
        #     """
        #
        #     return self.chats().search(name, **attributes)