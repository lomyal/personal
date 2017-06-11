#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################################################################################
#
# Copyright (c) 2017 All Rights Reserved
#
####################################################################################################
"""
主页

Authors:   Wang Shijun 
Date:      2017/03/25 14:53:00
"""

import os
import json
import datetime
import ConfigParser

import flask


conf = ConfigParser.ConfigParser()
cfg_file_path = os.path.join(os.path.dirname(__file__), 'config/info.cfg')
conf.read(cfg_file_path)

site_host = conf.get('site', 'host')
site_port = conf.get('site', 'port')  # 端口号，str 类型，在使用前要转换为 int 型

template_folder = os.path.abspath('./static/src')
app = flask.Flask(__name__, template_folder=template_folder)


@app.route('/')
def index():
    """
    主页入口
    :return:
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(threaded=True, debug=False, host=site_host, port=int(site_port))
