#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 根据操作者ID，返回被查者ID指定时间段内每个帐号的"已接待人数"<br/> 备注：<br/> 1、如果是操作者ID=被查者ID，返回被查者ID的"已接待人数"。<br/> 2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"已接待人数"。<br/> 3、如果操作者是主账户，他可以查询所有子帐号的"已接待人数"。<br/> （注意：这里说的是授权是主帐号，可以查询所有子帐号的数据，具体要查询哪些子账号的数据，需要在service_staff_id具体指定，而不是service_staff_id直接输入主帐号）<br/>  4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>  5、规则：某客服在1天内和同一个客户交流了多次，已回复人数算1。<br/> 6、"已接待人数"定义：买家、卖家彼此发过至少1条消息 ，不论谁先发都可以。<br/>   7、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>   8、开始时间与结束时间之间的间隔不能超过7天<br/>   9、不能查询90天以前的数据<br/>   10、不能查询当天的记录<br/>    11、查询日期精确到日<br/>
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


    
from Domain.ReplyStatOnDay import ReplyStatOnDay



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 根据操作者ID，返回被查者ID指定时间段内每个帐号的"已接待人数"<br/> 备注：<br/> 1、如果是操作者ID=被查者ID，返回被查者ID的"已接待人数"。<br/> 2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"已接待人数"。<br/> 3、如果操作者是主账户，他可以查询所有子帐号的"已接待人数"。<br/> （注意：这里说的是授权是主帐号，可以查询所有子帐号的数据，具体要查询哪些子账号的数据，需要在service_staff_id具体指定，而不是service_staff_id直接输入主帐号）<br/>  4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>  5、规则：某客服在1天内和同一个客户交流了多次，已回复人数算1。<br/> 6、"已接待人数"定义：买家、卖家彼此发过至少1条消息 ，不论谁先发都可以。<br/>   7、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>   8、开始时间与结束时间之间的间隔不能超过7天<br/>   9、不能查询90天以前的数据<br/>   10、不能查询当天的记录<br/>    11、查询日期精确到日<br/></SPAN>
# <UL>
# </UL>
class WangwangEserviceReceivenumGetResponse(object):
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

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">客服回复列表，按天统计，排列</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">ReplyStatOnDay</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.reply_stat_list_on_days = None
    
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
                d_list = []
                for x in value[value.keys()[0]]:
                    #data = propertyType(value)
                    try:
                        data = propertyType(x)
                    except Exception:
                        data = propertyType(value)
                    d_list.append(data)
                return d_list
                #return [propertyType(x) for x in value[value.keys()[0]]]
            else:
                return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "reply_stat_list_on_days": "ReplyStatOnDay",
        }
        levels = {
            
            "reply_stat_list_on_days": "Object Array",
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
        
        if kargs.has_key("reply_stat_list_on_days"):
            self.reply_stat_list_on_days = self._newInstance("reply_stat_list_on_days", kargs["reply_stat_list_on_days"])
        if kargs.has_key("code"):
            self.code = kargs["code"]
        if kargs.has_key("msg"):
            self.msg = kargs["msg"]
        if kargs.has_key("sub_code"):
            self.sub_code = kargs["sub_code"]
        if kargs.has_key("sub_msg"):
            self.sub_msg = kargs["sub_msg"]
