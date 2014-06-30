#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 增加一个数据模板.只增加基本信息，不会增加Detail详情 必填字段：name,owner,opened 增加数据模板后，数据模板状态:未审核 <br/> 	   名词解释：<br/> <ul> <li> 数据模板：将一系列的指标（AttributeVO）组合在一起，当做指标集合使用。数据模板包含多个数据模板详情，数据模板详情和指标一一对应。  数据模板主要应用在，标签匹配以及数据服务时使用。标明此次调用时，我需要哪些指标。</li> <li>数据模板详情：1个数据模板包含多个详情，一个详情和指标一一对应，用户对模板添加详情即指明此模板需要哪些指标。指标（AttributeVO）中如果包含参数（ParamKeyVO）时，用户可以选择性的添加参数的Value属性（AttributeVO通过其他服务接口获得，如果ParamKeyVO的value在创建DT时不赋值，后续调用其他服务接口时，也可以动态添加）</li> </ul> 使用方法：<br/> {"name":"TESTS__","opened":0,"owner":"TEST"}
# @author wuliang@maimiaotech.com
# @version: 0.0.0

from datetime import datetime
import os
import sys
import time

_jsonEnode = None
try:
    import demjson
    _jsonEnode = demjson.encode
except Exception:
    try:
        import simplejson
    except Exception:
        try:
            import json
        except Exception:
            raise Exception("Can not import any json library")
        else:
            _jsonEnode = json.dumps
    else:
        _jsonEnode = simplejson.dumps

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)


    

## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 增加一个数据模板.只增加基本信息，不会增加Detail详情 必填字段：name,owner,opened 增加数据模板后，数据模板状态:未审核 <br/> 	   名词解释：<br/> <ul> <li> 数据模板：将一系列的指标（AttributeVO）组合在一起，当做指标集合使用。数据模板包含多个数据模板详情，数据模板详情和指标一一对应。  数据模板主要应用在，标签匹配以及数据服务时使用。标明此次调用时，我需要哪些指标。</li> <li>数据模板详情：1个数据模板包含多个详情，一个详情和指标一一对应，用户对模板添加详情即指明此模板需要哪些指标。指标（AttributeVO）中如果包含参数（ParamKeyVO）时，用户可以选择性的添加参数的Value属性（AttributeVO通过其他服务接口获得，如果ParamKeyVO的value在创建DT时不赋值，后续调用其他服务接口时，也可以动态添加）</li> </ul> 使用方法：<br/> {"name":"TESTS__","opened":0,"owner":"TEST"}</SPAN>
# <UL>
# </UL>
class HanoiDatatemplateAddResponse(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的返回信息,包含状态等</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">dict</SPAN>
        # </LI>
        # </UL>
        self.responseStatus = None

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的响应内容</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>        
        self.responseBody = None

        self.code = None

        self.msg = None

        self.sub_code = None

        self.sub_msg = None

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">返回数据模板的唯一标识</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.value = None
    
        self.__init(kargs)

    def isSuccess(self):
        return self.code == None and self.sub_code == None
    
    def _newInstance(self, name, value):
        types = self._getPropertyType(name)
        propertyType = types[0]
        isArray = types[1]
        if propertyType == bool:
            if isArray:
                if not value:
                    return []
                return [x for x in value[value.keys()[0]]]
            else:
                return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            if isArray:
                if not value:
                    return []
                return [datetime.strptime(x, format) for x in value[value.keys()[0]]]
            else:
                return datetime.strptime(value, format)
        elif propertyType == str:
            if isArray:
                if not value:
                    return []
                return [x for x in value[value.keys()[0]]]
            else:
                #like taobao.simba.rpt.adgroupbase.get, response.rpt_adgroup_base_list is a json string,but will be decode into a list via python json lib 
                if not isinstance(value, basestring):
                    #the value should be a json string 
                    return _jsonEnode(value)
                return value
        else:
            if isArray:
                if not value:
                    return []
                return [propertyType(x) for x in value[value.keys()[0]]]
            else:
                return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "value": "Number",
        }
        levels = {
            
            "value": "Basic",
        }
        
        nameType = properties[name]
        pythonType = None
        if nameType == "Number":
            pythonType = int
        elif nameType == "String":
            pythonType = str
        elif nameType == 'Boolean':
            pythonType = bool
        elif nameType == "Date":
            pythonType = datetime
        elif nameType == 'Field List':
            pythonType == str
        elif nameType == 'Price':
            pythonType = float
        elif nameType == 'byte[]':
            pythonType = str
        else:
            pythonType = getattr(sys.modules["Domain.%s" % nameType], nameType)
        
        # 是单个元素还是一个对象
        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)

    def __init(self, kargs):
        
        if kargs.has_key("value"):
            self.value = self._newInstance("value", kargs["value"])
        if kargs.has_key("code"):
            self.code = kargs["code"]
        if kargs.has_key("msg"):
            self.msg = kargs["msg"]
        if kargs.has_key("sub_code"):
            self.sub_code = kargs["sub_code"]
        if kargs.has_key("sub_msg"):
            self.sub_msg = kargs["sub_msg"]
