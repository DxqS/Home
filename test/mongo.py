# coding:utf-8
'''
Created on 2016/11/1.

@author: Dxq
'''
user = {
    '_id': 1,
    'openid': 'ad5ADfsdasfa6686daXas',
    'avatar': '/static/img/1.jpg',
    'nick_name': '环环',
    'sex': 1,
    'user_name': '小款',
    'province': '浙江',
    'city': '杭州',
    'time': 100015,
    'subscribe': 1,
    'mobile': 18768120187,
    'mark': '这是我的水印哦',
    'work_year': 10,
    'title': '学徒大师',
    'salon_name': '沙龙王',
    'salon_position': '浙江杭州大',
    'salon_imgs': ['/static/1.jpg', '/static/2.jpg', '/static/3.jpg'],
    'cut_style': '暴雨梨花剪裁',
    'introduce': '我非常擅长这类裁剪',
    'products': ['/static/1.jpg', '/static/2.jpg', '/static/3.jpg'],
    'qrcode': '/static/qrcode.jpg',
}
group = {
    '_id': 10086,
    'uid': 1,
    'status': 1,
    'sex': 1,
    'grp_imgs': ['/static/1.jpg', '/static/2.jpg', '/static/3.jpg'],
    'grp_logo': '/static/img/1.jpg',
    'grp_type': '映客直播',
    'grp_intro': '这是燕子家机构的介绍',
    'grp_web': 'http://www.baidu.com',
    'grp_address': '浙江杭州大大',
    'grp_mobile': 18768120187,
    'grp_name': '林文杰',
    'grp_title': '燕山正版',
    'founder_mobile': 15700070500,
    'founder_honor': '获得国际大奖无数',
    'founder_titles': ['A比赛第一', 'B比赛第二'],
    'founder_name': '孙大款',
    'founder_cert': '/static/ID/card',
    'founder_IDcard': 330382199301250475,
}
net_red = {
    '_id': 10075,
    'name': '阿明',
    'pic': '/static/img.jpg',
    'uid': 1,
    'mobile': 18768120187,
    'wx_number': 'jck353622088',
    'status': '映客直播',
    'avatar': '/static/img.jpg',
    'wx_name': '小喽啰',
    'titles': ['无敌剪刀手', '剪发大师'],
    'fans': 50,
    'intro': '本网红天下无敌',
    'skill': '技巧很好',
    'course_num': 20,
    'grp_type': '映客直播',
    'stu_num': 15000,
}
bill = {
    '_id': 10075,
    'mode': 'cert_order',  # cert_order, page_order, poster_order, wx_order
    'amount': 50,
    'uid': 1,
    'balance': 50,
    'ctime': 1002512,
    'record_id': 1,
    'record_type': '???',
}
wx_order = {
    '_id': 10075,
    'uid': 1,
    'order_type': 'recharge',
    'order_no': '123123',
    'pay_order_no': '15822',
    'bill': 50,
    'price': 30,
    'ctime': 1002512,
    'utime': 1002512,
    'status': 1,  # 1通过0默认
}
cert_order = {
    '_id': 10075,
    'uid': 1,
    'bill': 50,
    'time': 1002512,
    'status': 1,  # 1通过0默认
}
user_poster = {
    '_id': 10075,
    'uid': 1,
    'temp_id': 1,
    'img': '/static/ok.jpg',
    'name': '开课倒计时',
    'ctime': 10058
}
poster_order = {
    '_id': 10075,
    'uid': 1,
    'bill': 100,
    'temp_id': 1,
    'expireat': 10086,
    'ctime': 10058,
    'status': 1  # 0到期1未到期
}
page_order = {
    '_id': 10075,
    'uid': 1,
    'bill': 100,
    'temp_id': 1,
    'expireat': 10086,
    'ctime': 10058,
    'status': 1  # 0到期1未到期
}
temp_poster = {
    '_id': 10075,
    'img': '/static/img.jpg',
    'title': '海报标题',
    'content': '这是个很好的海报，那个更好',
    'bill': 50,
    'scenes':
        [
            {'s_title': '场景标题1',
             'posters':
                 [
                     {'img': '/static/img1.jpg',
                      'name': '海报名称',
                      'temp_key': 'A1-1'
                      },

                     {'img': '/static/img2.jpg',
                      'name': '海报名称',
                      'temp_key': 'A1-2'
                      }]},

            {'s_title': '场景标题2',
             'posters':
                 [
                     {'img': '/static/img1.jpg',
                      'name': '海报名称',
                      'temp_key': 'B1-1'
                      },
                     {'img': '/static/img2.jpg',
                      'name': '海报名称',
                      'temp_key': 'B1-2'
                      }]}
        ],
    'typ': 'personal',  # personal,salon,group,net_red,grp_off,grp_on,net_on,net_off
    'personal_type': 'as'
}
temp_page = {
    '_id': 10075,
    'img': '/static/img.jpg',
    'title': '海报标题',
    'content': '这是个很好的海报，那个更好',
    'bill': 50,
    'temp_key': 'A20-1',
    'demo_link': '/wx/login',
    'typ': 'personal',  # personal,salon,group,net_red,grp_off,grp_on,net_on,net_off
}
course = {
    '_id': 1,
    'uid': 10025,
    'partner': 'grp',  # grp net
    'pid': 102,
    'advisory': {
        'name': '爱迪生',
        'mobile': 18768120187,
        'content': '详情请拨打咯上电话',
        'qrcode': '/static/qr.code'
    },
    'evaluations': [
        {'content': '这课程很棒',
         'source': '小喽啰'},

        {'content': '这课程棒',
         'source': '大喽啰'}
    ],
    'students': [
        {'img': '/static/img.jpg',
         'name': '小喽啰',
         'intro': '这学员超厉害'},

        {'img': '/static/img.jpg',
         'name': '大喽啰',
         'intro': '这学员厉害'},
    ],
    'stu_imgs': ['/static/i.jpg', '/static/2.jpg'],
    'former_imgs': ['/static/i.jpg', '/static/2.jpg'],
    'talker': {
        'talker_pic': '/static/img',
        'talker_intro': '这人牛',
        'talker_stu': 100,
        'talker_position': '工商大学校长',
        'talker_skill': '教书',
        'talker_name': '蒋'
    },
    'schedule': {
        'day1': {'start': 11111,
                 'end': 11111,
                 'speaker': '蒋'},

        'day2': {'start': 11111,
                 'end': 11111,
                 'speaker': '蒋'}
    },
    'info': {
        'detail_address': '浙江',
        'live_address': '酒店',
        'status': 1,  # 1正常2删除
        'type': 'edu',  # 教育，网红线上，网红线下
        'title': '5分钟速度剪',
        'subtitle': '只要五分钟',
        'intros': ['今天做什么', '明天做什么'],
        'student': '新手',
        'count': 100,
        'time': '2016/01/02-2017-104-01',
        'end_time': '2016-01-25',
        'price': 100,
        'platform': '微信',
        'day': '5天',
        'address': '浙江',
        'qrcode': '/static/qrcode',
        'times': '10次',
        'duration': 10,
        'note': '阿达的法定',
        'advantages': ['这课程很便宜', '非常便宜'],
        'tags': ['新手必备', '大师进阶']
    }
}
