#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: ph201805203
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options

# from handlers.main import IndexHandler
from handlers import main

define('port', default='8000', help='Listening port', type=int)
define('debug', default='True', help='Debug mode', type=bool)


class Application(tornado.web.Application):
    def __init__(self, debug=False):
        handlders = [
            (r'/', main.IndexHandler),
            (r'/explore', main.ExploreHandler),
            (r'/post/(?P<post_id>[0-9]+)', main.PostHandler),
        ]
        settings = dict(
            debug=debug,
            template_path='templates',  # 配置模板文件路径
            static_path='statics',  # 配置静态文件路径
            # static_url_prefix='/image/',  # 更改static路由
        )

        super().__init__(handlders, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = Application(debug=options.debug)
    application.listen(options.port)
    print(f"Server start on port {str(options.port)}")
    tornado.ioloop.IOLoop.current().start()  # 启动tornado服务
