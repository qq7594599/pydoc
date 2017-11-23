#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'

from flask import Flask, url_for
from www.controllers.homeController import homeController
from www.controllers.api.fileUploadController import fileUploadController

app = Flask('www')

app.secret_key = '\xba\x99\xe6\xbc\x0b\xb8pW5\x08u\xc9\x01\xcc\xba\xb5o\x97\xdf7q;\xcc\x90'

app.register_blueprint(homeController)
app.register_blueprint(fileUploadController, url_prefix='/api')


