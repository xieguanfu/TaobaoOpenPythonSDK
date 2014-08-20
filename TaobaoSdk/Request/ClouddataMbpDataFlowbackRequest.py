#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 用户通过此接口向上传表上传数据
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用户通过此接口向上传表上传数据</SPAN>
# <UL>
# </UL>
class ClouddataMbpDataFlowbackRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.clouddata.mbp.data.flowback"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">一、上传单行数据： 1)	形式为column1=value1,column2=value2,...的字符串，列名称只能包含字母数字和下划线，Value如果包含=(半角等号),(半角逗号)\(反斜杠)必须用\转义，没有参数则不选  2)	若想自行指定数据的日期，请在这个字段里追加上"dt=yyyymmdd"字段，如dt=20140605  二、上传多行数据: 1)	形式为:upload-multi-line;column1,column2,column3,dt;11,12,13,20140726;21,,23,20140727;31,,33,20140728...的字符串  2)	每行数据之间使用;(半角分号)隔开 3)	第一行固定是upload-multi-line，标识是多行上传模式 4)	第二行是上传的数据的列名，列名之间使用,（半角逗号）分隔，列名只能是数字、字母和下划线，并且只能以字母开头，列名不能为空 5)	第三列开始是上传的数据，数据都使用,(半角逗号) 分隔，数据顺序与对应列名顺序一致，数据可以为空，但是逗号不能省略，数据中如果包含;(半角分号),(半角逗号)\(反斜杠)必须用\转义 6)	若想自行指定数据的日期，请在列名中加上dt，并在数据列对应位置加上yyyymmdd格式的数据，如20140605，不允许为空，格式必须正确 7)	假如字段类型是boolean，数据请使用0或1，不支持true或者false 8)	由于接口会有超时限制，建议单次上传的数据量不要超过15,000字节</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.data = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">MBP查询表名</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.table_name = None
