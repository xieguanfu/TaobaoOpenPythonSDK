#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@date: 2012-06-12 20:22
@version: 0.0.0
"""

class ErrorResponseException(Exception):
    def __init__(self, **kargs):
        super(self.__class__, self).__init__()

        self.code = None
        '''
        错误类型
        '''
        
        self.msg = None
        '''
        错误消息
        '''

        self.sub_code = None

        self.sub_msg = None

        self.params = None

        self.rsp = None

        if kargs.has_key("code"):
            self.code = kargs["code"]
        if kargs.has_key("msg"):
            self.msg = kargs["msg"] 
        if kargs.has_key("sub_code"):
            self.sub_code = kargs["sub_code"]
        if kargs.has_key("sub_msg"):
            self.sub_msg = kargs["sub_msg"]
        if kargs.has_key("params"):
            self.params = kargs["params"]
        if kargs.has_key("rsp"):
            self.rsp = kargs["rsp"]

    def __str__(self):
        if self.rsp is None:
            responseBody = None
        else:
            responseBody = self.rsp.responseBody
        return "%s, ErrorCode: %s; SubMsg: %s, SubCode: %s,params:%s,responseBody:%s" % (self.msg, self.code, self.sub_msg, self.sub_code,self.params,responseBody)

