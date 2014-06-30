#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 查询Detail详情, 根据DataTemplateDetailCriteriaVO信息查询<br/> justQueryParamNotInput 为true时， 则查询出来的Detail详情,只是参数没有填入的列表(（Detail中的Attribute中的ParamKey是调用其他匹配接口必填的值，按照其他接口的规范填入即可）)<br/> 默认分页查询，每页10条记录。如果查询总条数，needRetPage = true<br/> DataTemplateDetailCriteriaVO <ul> <li>attrId(Long):AttributeVO的唯一标识</li> <li>templateId(Long 必填参数):数据模板的唯一标识</li> <li>name(String):数据模板详情的名称</li> <li>id(Long):根据模板唯一标识去查询</li> <li>pageSize:分页大小（最大值30）</li> <li>currentPage:当前页码</li> <li>needRetPage(Boolean 默认False):是否返回总条数</li> <li>justQueryParamNotInput（Boolean 默认False）:是否只查询每天如PK的详情列表</li> </ul>
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">查询Detail详情, 根据DataTemplateDetailCriteriaVO信息查询<br/> justQueryParamNotInput 为true时， 则查询出来的Detail详情,只是参数没有填入的列表(（Detail中的Attribute中的ParamKey是调用其他匹配接口必填的值，按照其他接口的规范填入即可）)<br/> 默认分页查询，每页10条记录。如果查询总条数，needRetPage = true<br/> DataTemplateDetailCriteriaVO <ul> <li>attrId(Long):AttributeVO的唯一标识</li> <li>templateId(Long 必填参数):数据模板的唯一标识</li> <li>name(String):数据模板详情的名称</li> <li>id(Long):根据模板唯一标识去查询</li> <li>pageSize:分页大小（最大值30）</li> <li>currentPage:当前页码</li> <li>needRetPage(Boolean 默认False):是否返回总条数</li> <li>justQueryParamNotInput（Boolean 默认False）:是否只查询每天如PK的详情列表</li> </ul></SPAN>
# <UL>
# </UL>
class HanoiDatatemplateDetailQueryRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.hanoi.datatemplate.detail.query"
        
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
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">attrId(Long):AttributeVO的唯一标识<br/> templateId(Long):数据模板的唯一标识<br/> name(String):数据模板详情的名称<br/> id(Long):根据模板唯一标识去查询<br/> pageSize:分页大小（最大值30）<br/> currentPage:当前页码<br/> needRetPage(Boolean 默认False):是否返回总条数<br/> justQueryParamNotInput（Boolean 默认False）:是否只查询每天如PK的详情列表<br/></SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.parameter = None
