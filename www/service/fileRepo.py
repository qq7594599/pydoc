#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'


import os
import time
import uuid

class FileRepo:
    def __init__(self, uploadedFile):
        self.uploadedFile = uploadedFile
        self.storageId = str(uuid.uuid4()).replace('-', '')

    def _getStoreLocation(self):
        location = '/upload/%s/%s' % (time.strftime("%Y%m%d", time.localtime()), self.storageId[0])
        target = os.path.normpath(os.getcwd() + location)
        if(os.path.exists(target)):
            return location
        else:
            os.makedirs(target)
            return location

    def save(self):
        store_path = os.path.normpath(os.getcwd() + self._getStoreLocation())
        filepath = os.path.join(store_path, self.storageId)
        self.uploadedFile.save(filepath)