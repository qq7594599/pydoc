#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'

from flask import Blueprint, request
from www.service.fileRepo import FileRepo

fileUploadController = Blueprint('fileUpload', __name__)

@fileUploadController.route('/')
def index():
    return '''
    <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post action='/api/fileUpload' enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
    '''

@fileUploadController.route('/fileUpload', methods=['GET', 'POST'])
def fileUpload():
    fileRepo = FileRepo(request.files['file'])
    fileRepo.save()
    return 'ok'

