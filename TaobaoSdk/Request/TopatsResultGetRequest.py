#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 获取异步任务结果。 <br/>异步API使用方法，请查看：<a href="http://open.taobao.com/doc/detail.htm?id=30">异步API使用说明</a> <br/>1. 只能获取AppKey自身创建的异步任务结果 <br/>2. 如果任务状态为done，则返回任务结果（如taobao.topats.trades.fullinfo.get）或下载地址（如taobao.topats.trades.sold.get） <br/>3. 任务结果下载地址只能使用一次，需要重复下载可重新调用此接口获取下载地址
# @author wuliang@maimiaotech.com
# @version: 0.0.0

import os
import sys
import time



def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

__modulePath = os.path.join(__getCurrentPath(), os.path.pardir)
__modulePath = os.path.normpath(__modulePath)
if __modulePath not in sys.path:
    sys.path.insert(0, __modulePath)


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取异步任务结果。 <br/>异步API使用方法，请查看：<a href="http://open.taobao.com/doc/detail.htm?id=30">异步API使用说明</a> <br/>1. 只能获取AppKey自身创建的异步任务结果 <br/>2. 如果任务状态为done，则返回任务结果（如taobao.topats.trades.fullinfo.get）或下载地址（如taobao.topats.trades.sold.get） <br/>3. 任务结果下载地址只能使用一次，需要重复下载可重新调用此接口获取下载地址</SPAN>
# <UL>
# </UL>
class TopatsResultGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.topats.result.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">任务id号，创建任务时返回的task_id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.task_id = None
