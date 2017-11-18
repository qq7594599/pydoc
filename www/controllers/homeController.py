#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'

from flask import Blueprint, render_template

homeController = Blueprint('home', __name__, template_folder='templates')

@homeController.route('/', defaults={'page': 'index'})
@homeController.route('/<page>')
def index(page):
    return render_template('home/%s.html' % page)

