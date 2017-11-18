#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'

from flask import Flask
from www.controllers.homeController import homeController

app = Flask('www')
app.register_blueprint(homeController)
