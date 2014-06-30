#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 增加一个数据模板.只增加基本信息，不会增加Detail详情 必填字段：name,owner,opened 增加数据模板后，数据模板状态:未审核 <br/> 	   名词解释：<br/> <ul> <li> 数据模板：将一系列的指标（AttributeVO）组合在一起，当做指标集合使用。数据模板包含多个数据模板详情，数据模板详情和指标一一对应。  数据模板主要应用在，标签匹配以及数据服务时使用。标明此次调用时，我需要哪些指标。</li> <li>数据模板详情：1个数据模板包含多个详情，一个详情和指标一一对应，用户对模板添加详情即指明此模板需要哪些指标。指标（AttributeVO）中如果包含参数（ParamKeyVO）时，用户可以选择性的添加参数的Value属性（AttributeVO通过其他服务接口获得，如果ParamKeyVO的value在创建DT时不赋值，后续调用其他服务接口时，也可以动态添加）</li> </ul> 使用方法：<br/> {"name":"TESTS__","opened":0,"owner":"TEST"}
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">增加一个数据模板.只增加基本信息，不会增加Detail详情 必填字段：name,owner,opened 增加数据模板后，数据模板状态:未审核 <br/> 	   名词解释：<br/> <ul> <li> 数据模板：将一系列的指标（AttributeVO）组合在一起，当做指标集合使用。数据模板包含多个数据模板详情，数据模板详情和指标一一对应。  数据模板主要应用在，标签匹配以及数据服务时使用。标明此次调用时，我需要哪些指标。</li> <li>数据模板详情：1个数据模板包含多个详情，一个详情和指标一一对应，用户对模板添加详情即指明此模板需要哪些指标。指标（AttributeVO）中如果包含参数（ParamKeyVO）时，用户可以选择性的添加参数的Value属性（AttributeVO通过其他服务接口获得，如果ParamKeyVO的value在创建DT时不赋值，后续调用其他服务接口时，也可以动态添加）</li> </ul> 使用方法：<br/> {"name":"TESTS__","opened":0,"owner":"TEST"}</SPAN>
# <UL>
# </UL>
class HanoiDatatemplateAddRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.hanoi.datatemplate.add"
        
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
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">name:String类型，数据模板的名称 opened:int类型，标识此数据模板是否对其他人可见</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.parameter = None
