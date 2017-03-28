# 认识WXPY

Bot
------------
`bot=Bot(cache_path=None, console_qr=False)`
--------------------------------------
    cache_path 和console_qr为常用参数
    
    cache_path: 设置当前会话的缓存路径。为None（默认）时，则不开启     设为True时，使用默认缓存路径'wxpy.pkl'

    console_qr:在终端中显示登陆二维码，需要安装 pillow 模块
            * 可为整数(int)，表示二维码单元格的宽度，通常为2(当被为True时，也将在内部当作2)。
            * 也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
            * 例如: 在大部分 Linux 系统中可设为 `True` 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
    

Bot对象可以理解为一个Web微信客户端
它本身的一些常用参数

机器人自身：`bot.self：<Friend: 小喽啰>`：
文件传输助手：`bot.file_helper：<Chat: 文件传输助手>`
机器人的好友：`bot.friends`
机器人的群组：`bot.groups`
机器人的公众号：`bot.mps`
机器人的聊天集合：`bot.charts`
机器人的状态：`bot.alive`

常用：
        `bot.register(chats=None, msg_types=None,
            except_self=True, run_async=True, enabled=True)`
            
            
        装饰器：用于注册消息配置

        :param chats: 消息所在的聊天对象：单个或列表形式的多个聊天对象或聊天类型，为空时匹配所有聊天对象
        :param msg_types:(详见Message) 消息的类型：单个或列表形式的多个消息类型，为空时匹配所有消息类型 (SYSTEM 类消息除外)
        :param except_self: 排除由自己发送的消息
        :param run_async: 是否异步执行所配置的函数：可提高响应速度
        :param enabled: 当前配置的默认开启状态，可事后动态开启或关闭
            
-----------------------------------------
    | 关于发送消息，请参见 :doc:`chats`。
    | 关于消息对象和自动处理，请参见 :doc:`messages`。


初始化/登陆
----------------

    :class:`Bot` 在初始化时便会执行登陆操作，需要手机扫描登陆。

获取聊天对象
----------------
Bot.self

    机器人自身 (作为一个聊天对象)
Bot.file_helper

    文件传输助手

Bot.friends

Bot.groups

Bot.mps

Bot.chats


搜索聊天对象
----------------

    * 通过 `.search()` 获得的搜索结果 **均为列表**
    * 若希望找到唯一结果，可使用 :any:`ensure_one()`

搜索好友:

    # 搜索名称包含 '游否' 的深圳男性好友
    found = bot.friends().search('游否', sex=MALE, city='深圳')
    # [<Friend: 游否>]
    # 确保搜索结果是唯一的，并取出唯一结果
    youfou = ensure_one(found)
    # <Friend: 游否>

搜索群聊:

    # 搜索名称包含 'wxpy'，且成员中包含 `游否` 的群聊对象
    wxpy_groups = bot.groups().search('wxpy', [youfou])
    # [<Group: wxpy 交流群 1>, <Group: wxpy 交流群 2>]

在群聊中搜素:

    # 在刚刚找到的第一个群中搜索
    group = wxpy_groups[0]
    # 搜索该群中所有浙江的群友
    found = group.search(province='浙江')
    # [<Member: 浙江群友 1>, <Group: 浙江群友 2> ...]

搜索任何类型的聊天对象 (但不包含群内成员) :

    # 搜索名称含有 'wxpy' 的任何聊天对象
    found = bot.search('wxpy')
    # [<Friend: wxpy 机器人>, <Group: wxpy 交流群 1>, <Group: wxpy 交流群 2>]

加好友和建群
----------------

    Bot.add_friend

    Bot.accept_friend

自动接受好友请求::

    # 注册好友请求类消息
    @bot.register(msg_types=FRIENDS)
    # 自动接受验证信息中包含 'wxpy' 的好友请求
    def auto_accept_friends(msg):
        # 判断好友请求中的验证文本
        if 'wxpy' in msg.text.lower():
            # 接受好友 (msg.card 为该请求的用户对象)
            new_friend = bot.accept_friend(msg.card)
            # 或 new_friend = msg.card.accept()
            # 向新的好友发送消息
            new_friend.send('哈哈，我自动接受了你的好友请求')
            
---------------------------
    Bot.create_group


更新用户的详细信息
----------------

    Bot.user_details

登出
----------------

    Bot.logout

控制多个微信 (多开)
----------------

仅需初始化多个 :class:`Bot` 对象，即可同时控制多个微信:

    bot1 = Bot()
    bot2 = Bot()
    
堵塞进程，直到结束消息监听 (例如，机器人被登出时)
    
    Bot.join
