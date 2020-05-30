# !/usr/bin/env python
# -*- coding:utf8 -*-
"""
    :author: wujiangbin

    :copyright: (c) 2020 - 2021 BeiJing ZhiTuShiKong Technology CO.,Ltd.
    北京星球时空科技有限公司

    All rights reserved.
"""

from flask import Flask
#import upload
from flask_tus import tus_manager

app = Flask(__name__)
tus_manager(app)
app.run("0.0.0.0", 4004)
