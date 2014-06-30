#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 查询指标模板 默认不返回详情（detail）列表。 如果想要返回detail，只查询正常的detail <br /> 必填参数：opened参数必填（opened表示开放策略：0：只根据sellerId开放，1：全网开放 2：只根据ISV开放） <br /> 选填参数：isNeedDetail(如果needDetail为true时会返回attr列表，效率低)<br /> 此接口分页处理。默认分页 每页10条，返回总条数 请设置快关：needRetPage=true,参数为true是critera对象中totalAmount为符合条件的总条数,否则，不返回总条数。<br />  {"currentPage":1,"id":123,"isNeedDetail":false,"needRetPage":false,"opened":1,"pageSize":10,"templateName":"xxx"}
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">查询指标模板 默认不返回详情（detail）列表。 如果想要返回detail，只查询正常的detail <br /> 必填参数：opened参数必填（opened表示开放策略：0：只根据sellerId开放，1：全网开放 2：只根据ISV开放） <br /> 选填参数：isNeedDetail(如果needDetail为true时会返回attr列表，效率低)<br /> 此接口分页处理。默认分页 每页10条，返回总条数 请设置快关：needRetPage=true,参数为true是critera对象中totalAmount为符合条件的总条数,否则，不返回总条数。<br />  {"currentPage":1,"id":123,"isNeedDetail":false,"needRetPage":false,"opened":1,"pageSize":10,"templateName":"xxx"}</SPAN>
# <UL>
# </UL>
class HanoiDatatemplateQueryRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.hanoi.datatemplate.query"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">AppName</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.app_name = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">templateName:String 根据模板的名字查找 isNeedDetail：Boolean 是否返回模板详情 opened:int 开放策略 owner:创建者，填入appkey</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.parameter = None
