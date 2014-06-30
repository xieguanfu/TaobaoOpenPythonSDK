#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 根据用户ID获取用户下所有模板
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">根据用户ID获取用户下所有模板</SPAN>
# <UL>
# </UL>
class DeliveryTemplatesGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.delivery.templates.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">需返回的字段列表。 <br/>  <B> 可选值:示例中的值;各字段之间用","隔开 </B> <br/><br/>  <font color=blue> template_id：查询模板ID <br/>  template_name:查询模板名称 <br/>  assumer：查询服务承担放 <br/>  valuation:查询计价规则 <br/>  supports:查询增值服务列表 <br/>  created:查询模板创建时间 <br/>  modified:查询修改时间<br/>  consign_area_id:运费模板上设置的卖家发货地址最小级别ID<br/>  address:卖家地址信息 </font> <br/><br/>  <font color=bule> query_cod:查询货到付款运费信息<br/>  query_post:查询平邮运费信息 <br/>  query_express:查询快递公司运费信息 <br/>  query_ems:查询EMS运费信息<br/>  query_bzsd:查询普通保障速递运费信息<br/>  query_wlb:查询物流宝保障速递运费信息<br/>  query_furniture:查询家装物流运费信息 <font color=blue> <br/><br/> <font color=red>不能有空格</font></SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Field List</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.fields = None
