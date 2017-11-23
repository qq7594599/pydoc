#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'


import os
import time
import uuid

from www.dataaccess.file_module import FileModule

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
        store_relative_path = self._getStoreLocation()
        store_path = os.path.normpath(os.getcwd() + store_relative_path)
        filepath = os.path.join(store_path, self.storageId)
        self.uploadedFile.save(filepath)

        root, ext = os.path.splitext(self.uploadedFile.filename)
        obj = {
            'file_name': root,
            'file_ext': ext,
            'storage_name': self.storageId,
            'location': store_relative_path
        }

        module = FileModule()
        module.new_file(obj)

        return self.storageId
