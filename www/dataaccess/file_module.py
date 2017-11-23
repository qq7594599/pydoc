#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Charence Wang'


import mysql.connector

class FileModule:
    def __init__(self):
        pass

    def new_file(self, obj):
        cnx = mysql.connector.connect(user='root', password='Welcome1',
                                      host='127.0.0.1',
                                      database='pydocdb')
        cursor = cnx.cursor()

        query = ("INSERT INTO `T_Files` "
                 "(`file_name`, `file_ext`, `storage_name`, `location`, "
                 "`created_by`, `created_on`, `updated_by`, `updated_on`, `is_active`) "
                 "VALUES (%(file_name)s, %(file_ext)s, %(storage_name)s, %(location)s, 'sysadmin', now(), "
                 "'sysadmin', now(), 1)")

        cursor.execute(query, obj)

        cnx.commit()
        cursor.close()
        cnx.close()
