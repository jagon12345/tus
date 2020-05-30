# !/usr/bin/env python
# -*- coding:utf8 -*-
#
# Copyright (c) 2019 - 2040 BeiJing ZhiTuShiKong Technology CO.,Ltd.
# 北京智图时空科技有限公司
#
# All rights reserved.
#
from flask import Flask, render_template, send_from_directory
from flask_tus import tus_manager
import os

app = Flask(__name__)
tm = tus_manager(app, upload_url='/file-upload', upload_folder='uploads/')

app.run("0.0.0.0", 1080)
