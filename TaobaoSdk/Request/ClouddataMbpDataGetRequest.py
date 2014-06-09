#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: liumc
@contact: liumingchao@maimiaotech.com
@date: 2014-06-09 13:27
@version: 0.0.0
@license: Copyright Maimiaotech.com
@copyright: Copyright Maimiaotech.com

"""
import os
import sys
import time
def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

__modulePath = os.path.join(__getCurrentPath(), os.path.pardir)
__modulePath = os.path.normpath(__modulePath)
if __modulePath not in sys.path:
    sys.path.insert(0, __modulePath)



class ClouddataMbpDataGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__() 
        self.method = 'taobao.clouddata.mbp.data.get'
        self.session = '620151603c6d2a15d18f0996ZZ0e51a14d1d47350f7c375520500325'
        self.sql_id = None
        self.parameter = None
        self.timestamp = int(time.time())



