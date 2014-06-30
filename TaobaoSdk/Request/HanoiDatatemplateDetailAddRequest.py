#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 向某个DT批量添加指标关系 注意 不会校验指标关系是否重复 返回的是添加数量 必填字段： <br /> DataTemplateVO: <br /> id <br/> opened<br/> DataTemplateDetailVO:<br /> name--用户可以根据这个name来创建模板<br/> Attr--需要把查询出来的AttributeVO对象放入到Detail中,如果Attr对应有ParamKey，paramKey的value可填入也可不填入，填入后，查询出来的Detail中ParamMap就会包含此信息<br />  用法<br/> DataTemplateVO  {"id":1,"opened":1} <br/> DataTemplateDetailVO  [{"attr":{"code":"SEX","description":"按男、女、男+女、无四个维度","documentId":1219,"id":35666,"params":[{"documentId":null,,"id":7757,"key":"buyerID","name":"buyerID","required":0,"sort":0,"type":3,"value":123}],"title":"性别","typeId":23157,"unit":"","valueType":1},"name":"d0c24612-b0f5-4814-9cf8-8eccb20f2017"}]
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">向某个DT批量添加指标关系 注意 不会校验指标关系是否重复 返回的是添加数量 必填字段： <br /> DataTemplateVO: <br /> id <br/> opened<br/> DataTemplateDetailVO:<br /> name--用户可以根据这个name来创建模板<br/> Attr--需要把查询出来的AttributeVO对象放入到Detail中,如果Attr对应有ParamKey，paramKey的value可填入也可不填入，填入后，查询出来的Detail中ParamMap就会包含此信息<br />  用法<br/> DataTemplateVO  {"id":1,"opened":1} <br/> DataTemplateDetailVO  [{"attr":{"code":"SEX","description":"按男、女、男+女、无四个维度","documentId":1219,"id":35666,"params":[{"documentId":null,,"id":7757,"key":"buyerID","name":"buyerID","required":0,"sort":0,"type":3,"value":123}],"title":"性别","typeId":23157,"unit":"","valueType":1},"name":"d0c24612-b0f5-4814-9cf8-8eccb20f2017"}]</SPAN>
# <UL>
# </UL>
class HanoiDatatemplateDetailAddRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.hanoi.datatemplate.detail.add"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">appName</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.app_name = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">attr: 将AttributeVO转换成JSON格式 name: 详情的名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.data_template_details = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">id:数据模板唯一标识</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.data_template_vo = None
