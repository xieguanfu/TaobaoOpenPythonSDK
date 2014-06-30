#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 产品批量添加,传入文件大小限制在1M(一般1w条记录不会超过1M),每五分钟只允许调用一次
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">产品批量添加,传入文件大小限制在1M(一般1w条记录不会超过1M),每五分钟只允许调用一次</SPAN>
# <UL>
# </UL>
class JipiaoPoliciesAddRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.jipiao.policies.add"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">(ZIP压缩UTF-8编码JSON)，压缩前格式为:[{数据结构BatchPolicy的json格式},{数据结构BatchPolicy的json格式},...] 示例： [{ "attributes": "rfc=1;ipt=1;fdtod=0000;ldtod=2359", "source": null, "airline": "CZ", "arrAirports": "CSX,CTU,CAN", "autoHkFlag": true, "autoTicketFlag": true, "cabinRules": "[{\"matcher\":{\"mode\":\"ALL\",\"list\":[\"Y\"]},\"priceStrategy\":{\"mode\":\"DISCOUNT\",\"modeBaseValue\":null,\"retention\":5000,\"rebase\":-5},\"backMatcher\":null}]", "changeRule": null, "dayOfWeeks": "1234", "depAirports": "PEK", "ei": "ei", "excludeDate": null, "firstSaleAdvanceDay": null, "flags": null, "flightInfo": "+CA1234,CZ2345", "lastSaleAdvanceDay": null, "memo": "memoUpdate", "officeId": "RRR003", "outProductId": "46f9b762-ea50-4c71-877b-45fa2936277e", "policyType": 8, "refundRule": null, "reissueRule": null, "saleEndDate": "2013-06-19 00:00:00", "saleStartDate": "2013-06-09 00:00:00", "seatInfo": null, "shareSupport": false, "specialRule": null, "travelEndDate": "2013-06-19 00:00:00", "travelStartDate": "2013-06-09 00:00:00" } ]</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">byte[]</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.compressed_policies = None
