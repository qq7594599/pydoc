#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'

from flask import Blueprint, render_template, url_for

homeController = Blueprint('home', __name__, template_folder='templates')

@homeController.route('/')
def index():
    return render_template('index.html')

@homeController.route('/query/<obj>')
@homeController.route('/query/<obj>/<filename>')
def queryUrl(obj, filename=''):
    if(filename):
        return url_for(obj, filename=filename)
    return url_for(obj)
