#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: ph201805203
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    """
    首页，用户上传图片的展示
    """
    def get(self):
        self.render('index.html')


class ExploreHandler(tornado.web.RequestHandler):
    """
    最近上传的图片页面
    """
    def get(self):
        self.render('explore.html')


class PostHandler(tornado.web.RequestHandler):
    """
    单个图片的详情页面
    """
    def get(self, post_id):
        self.render('post.html', post_id=post_id)