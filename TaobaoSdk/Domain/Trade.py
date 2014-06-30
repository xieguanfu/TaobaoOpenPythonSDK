#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 交易结构
# @author wuliang@maimiaotech.com
# @version: 0.0.0

from copy import deepcopy
from datetime import datetime
import os
import sys
import time
import types

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

if __getCurrentPath() not in sys.path:
    sys.path.insert(0, __getCurrentPath())


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
from Order import Order

                                                                
from PromotionDetail import PromotionDetail

                                                                                                                                                                                        
from ServiceOrder import ServiceOrder

        
from LogisticsTag import LogisticsTag

                                                                                                                                                
## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易结构</SPAN>
class Trade(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.__kargs = deepcopy(kargs)
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家手工调整金额，精确到2位小数，单位：元。如：200.07，表示：200元7分。来源于订单价格修改，如果有多笔子订单的时候，这个为0，单笔的话则跟[order].adjust_fee一样</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.adjust_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家的支付宝id号，在UIC中有记录，买家支付宝的唯一标示，不因为买家更换Email账号而改变。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.alipay_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">支付宝交易号，如：2009112081173831</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.alipay_no = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">创建交易接口成功后，返回的支付url</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.alipay_url = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">淘宝下单成功了,但由于某种错误支付宝订单没有创建时返回的信息。taobao.trade.add接口专用</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.alipay_warn_msg = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">区域id，代表订单下单的区位码，区位码是通过省市区转换而来，通过区位码能精确到区内的划分，比如310012是杭州市西湖区华星路</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.area_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">物流到货时效截单时间，格式 HH:mm</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.arrive_cut_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">物流到货时效，单位天</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.arrive_interval = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">同步到卖家库的时间，taobao.trades.sold.incrementv.get接口返回此字段</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.async_modified = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易中剩余的确认收货金额（这个金额会随着子订单确认收货而不断减少，交易成功后会变为零）。精确到2位小数;单位:元。如:200.07，表示:200 元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.available_confirm_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家支付宝账号</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_alipay_no = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家下单的地区</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_area = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家货到付款服务费。精确到2位小数;单位:元。如:12.07，表示:12元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_cod_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家邮件地址</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_email = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家备注旗帜（与淘宝网上订单的买家备注旗帜对应，只有买家才能查看该字段）红、黄、绿、蓝、紫 分别对应 1、2、3、4、5</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_flag = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家备注（与淘宝网上订单的买家备注对应，只有买家才能查看该字段）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_memo = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家留言</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_message = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家昵称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_nick = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家获得积分,返点的积分。格式:100;单位:个。返点的积分要交易成功之后才能获得。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_obtain_point_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家是否已评价。可选值:true(已评价),false(未评价)。如买家只评价未打分，此字段仍返回false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.buyer_rate = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家可以通过此字段查询是否当前交易可以评论，can_rate=true可以评价，false则不能评价。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.can_rate = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">货到付款服务费。精确到2位小数;单位:元。如:12.07，表示:12元7分。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.cod_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">货到付款物流状态。初始状态 NEW_CREATED,接单成功 ACCEPTED_BY_COMPANY,接单失败 REJECTED_BY_COMPANY,接单超时 RECIEVE_TIMEOUT,揽收成功 TAKEN_IN_SUCCESS,揽收失败 TAKEN_IN_FAILED,揽收超时 TAKEN_TIMEOUT,签收成功 SIGN_IN,签收失败 REJECTED_BY_OTHER_SIDE,订单等待发送给物流公司 WAITING_TO_BE_SENT,用户取消物流订单 CANCELED</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.cod_status = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易佣金。精确到2位小数;单位:元。如:200.07，表示:200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.commission_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">物流发货时效，单位小时</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.consign_interval = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家发货时间。格式:yyyy-MM-dd HH:mm:ss</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.consign_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易创建时间。格式:yyyy-MM-dd HH:mm:ss</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.created = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">使用信用卡支付金额数</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.credit_card_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">建议使用trade.promotion_details查询系统优惠系统优惠金额（如打折，VIP，满就送等），精确到2位小数，单位：元。如：200.07，表示：200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.discount_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易结束时间。交易成功时间(更新交易状态为成功的同时更新)/确认收货时间或者交易关闭时间 。格式:yyyy-MM-dd HH:mm:ss</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.end_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">电子凭证的垂直信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.eticket_ext = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">快递代收款。精确到2位小数;单位:元。如:212.07，表示:212元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.express_agency_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">判断订单是否有买家留言，有买家留言返回true，否则返回false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_buyer_message = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否包含邮费。与available_confirm_fee同时使用。可选值:true(包含),false(不包含)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_post_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">订单中是否包含运费险订单，如果包含运费险订单返回true，不包含运费险订单，返回false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_yfx = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品字符串编号(注意：iid近期即将废弃，请用num_iid参数)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.iid = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">发票抬头</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.invoice_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">发票类型</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.invoice_type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否是3D淘宝交易</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_3D = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">表示是否是品牌特卖（常规特卖，不包括特卖惠和特实惠）订单，如果是返回true，如果不是返回false。当此字段与is_force_wlb均为true时，订单强制物流宝发货。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_brand_sale = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">表示订单交易是否含有对应的代销采购单。 如果该订单中存在一个对应的代销采购单，那么该值为true；反之，该值为false。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_daixiao = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">订单是否强制使用物流宝发货。当此字段与is_brand_sale均为true时，订单强制物流宝发货。此字段为false时，该订单根据流转规则设置可以使用物流宝或者常规方式发货</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_force_wlb = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否保障速递，如果为true，则为保障速递订单，使用线下联系发货接口发货，如果未false，则该订单非保障速递，根据卖家设置的订单流转规则可使用物流宝或者常规物流发货。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_lgtype = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否是多次发货的订单 如果卖家对订单进行多次发货，则为true 否则为false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_part_consign = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">表示订单交易是否网厅订单。 如果该订单是网厅订单，那么该值为true；反之，该值为false。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_wt = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">次日达订单送达时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.lg_aging = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">次日达，三日达等送达类型</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.lg_aging_type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">订单出现异常问题的时候，给予用户的描述,没有异常的时候，此值为空</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.mark_desc = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易修改时间(用户对订单的任何修改都会更新此字段)。格式:yyyy-MM-dd HH:mm:ss</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.modified = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品购买数量。取值范围：大于零的整数,对于一个trade对应多个order的时候（一笔主订单，对应多笔子订单），num=0，num是一个跟商品关联的属性，一笔订单对应多比子订单的时候，主订单上的num无意义。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.num = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品数字编号</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.num_iid = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卡易售垂直表信息，去除下单ip之后的结果</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.nut_feature = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">导购宝=crm</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.o2o = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">导购宝提货方式，inshop：店内提货，online：线上发货</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.o2o_delivery = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">导购员id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.o2o_guide_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">导购员名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.o2o_guide_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">导购员门店id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.o2o_shop_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">导购门店名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.o2o_shop_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">订单列表</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Order</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.orders = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">付款时间。格式:yyyy-MM-dd HH:mm:ss。订单的付款时间即为物流订单的创建时间。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.pay_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">实付金额。精确到2位小数;单位:元。如:200.07，表示:200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.payment = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品图片绝对途径</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.pic_path = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家使用积分,下单时生成，且一直不变。格式:100;单位:个.</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.point_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">邮费。精确到2位小数;单位:元。如:200.07，表示:200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.post_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品价格。精确到2位小数；单位：元。如：200.07，表示：200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.price = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易促销详细信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.promotion = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">优惠详情</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">PromotionDetail</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.promotion_details = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">买家实际使用积分（扣除部分退款使用的积分），交易完成后生成（交易成功或关闭），交易未完成时该字段值为0。格式:100;单位:个</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.real_point_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家实际收到的支付宝打款金额（由于子订单可以部分确认收货，这个金额会随着子订单的确认收货而不断增加，交易成功后等于买家实付款减去退款金额）。精确到2位小数;单位:元。如:200.07，表示:200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.received_payment = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的详细地址</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_address = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的所在城市<br>注：因为国家对于城市和地区的划分的有：省直辖市和省直辖县级行政区（区级别的）划分的，淘宝这边根据这个差异保存在不同字段里面比如：广东广州：广州属于一个直辖市是放在的receiver_city的字段里面；而河南济源：济源属于省直辖县级行政区划分，是区级别的，放在了receiver_district里面<br>建议：程序依赖于城市字段做物流等判断的操作，最好加一个判断逻辑：如果返回值里面只有receiver_district参数，该参数作为城市</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_city = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的所在地区<br>注：因为国家对于城市和地区的划分的有：省直辖市和省直辖县级行政区（区级别的）划分的，淘宝这边根据这个差异保存在不同字段里面比如：广东广州：广州属于一个直辖市是放在的receiver_city的字段里面；而河南济源：济源属于省直辖县级行政区划分，是区级别的，放在了receiver_district里面<br>建议：程序依赖于城市字段做物流等判断的操作，最好加一个判断逻辑：如果返回值里面只有receiver_district参数，该参数作为城市</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_district = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的手机号码</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_mobile = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的姓名</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的电话号码</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_phone = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的所在省份</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_state = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">收货人的邮编</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.receiver_zip = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家支付宝账号</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_alipay_no = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家是否可以对订单进行评价</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_can_rate = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家货到付款服务费。精确到2位小数;单位:元。如:12.07，表示:12元7分。卖家不承担服务费的订单：未发货的订单获取服务费为0，发货后就能获取到正确值。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_cod_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家邮件地址</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_email = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家备注旗帜（与淘宝网上订单的卖家备注旗帜对应，只有卖家才能查看该字段）红、黄、绿、蓝、紫 分别对应 1、2、3、4、5</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_flag = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家备注（与淘宝网上订单的卖家备注对应，只有卖家才能查看该字段）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_memo = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家手机</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_mobile = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家姓名</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家昵称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_nick = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家电话</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_phone = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家是否已评价。可选值:true(已评价),false(未评价)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_rate = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">订单将在此时间前发出，主要用于预售订单</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.send_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">服务子订单列表</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">ServiceOrder</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.service_orders = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">物流标签</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">LogisticsTag</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.service_tags = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">创建交易时的物流方式（交易完成前，物流方式有可能改变，但系统里的这个字段一直不变）。可选值：free(卖家包邮),post(平邮),express(快递),ems(EMS),virtual(虚拟发货)，25(次日必达)，26(预约配送)。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.shipping_type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易快照详细信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.snapshot = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易快照地址</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.snapshot_url = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易状态。可选值:     * TRADE_NO_CREATE_PAY(没有创建支付宝交易)     * WAIT_BUYER_PAY(等待买家付款)     * SELLER_CONSIGNED_PART(卖家部分发货)     * WAIT_SELLER_SEND_GOODS(等待卖家发货,即:买家已付款)     * WAIT_BUYER_CONFIRM_GOODS(等待买家确认收货,即:卖家已发货)     * TRADE_BUYER_SIGNED(买家已签收,货到付款专用)     * TRADE_FINISHED(交易成功)     * TRADE_CLOSED(付款以后用户退款成功，交易自动关闭)     * TRADE_CLOSED_BY_TAOBAO(付款以前，卖家或买家主动关闭交易)     * PAY_PENDING(国际信用卡支付付款确认中)     * WAIT_PRE_AUTH_CONFIRM(0元购合约中)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.status = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">分阶段付款的已付金额（万人团订单已付金额）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.step_paid_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">分阶段付款的订单状态（例如万人团订单等），目前有三返回状态 FRONT_NOPAID_FINAL_NOPAID(定金未付尾款未付)，FRONT_PAID_FINAL_NOPAID(定金已付尾款未付)，FRONT_PAID_FINAL_PAID(定金和尾款都付)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.step_trade_status = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易编号 (父订单的交易编号)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.tid = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">超时到期时间。格式:yyyy-MM-dd HH:mm:ss。业务规则： 前提条件：只有在买家已付款，卖家已发货的情况下才有效 如果申请了退款，那么超时会落在子订单上；比如说3笔ABC，A申请了，那么返回的是BC的列表, 主定单不存在 如果没有申请过退款，那么超时会挂在主定单上；比如ABC，返回主定单，ABC的超时和主定单相同</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.timeout_action_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易标题，以店铺名作为此标题的值。注:taobao.trades.get接口返回的Trade中的title是商品名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.title = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品金额（商品价格乘以数量的总金额）。精确到2位小数;单位:元。如:200.07，表示:200元7分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.total_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易内部来源。 WAP(手机);HITAO(嗨淘);TOP(TOP平台);TAOBAO(普通淘宝);JHS(聚划算) 一笔订单可能同时有以上多个标记，则以逗号分隔</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.trade_from = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易备注。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.trade_memo = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易外部来源：ownshop(商家官网)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.trade_source = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">交易类型列表，同时查询多种交易类型可用逗号分隔。默认同时查询guarantee_trade, auto_delivery, ec, cod的4种交易类型的数据 可选值 fixed(一口价) auction(拍卖) guarantee_trade(一口价、拍卖) auto_delivery(自动发货) independent_simple_trade(旺店入门版交易) independent_shop_trade(旺店标准版交易) ec(直冲) cod(货到付款) fenxiao(分销) game_equipment(游戏装备) shopex_trade(ShopEX交易) netcn_trade(万网交易) external_trade(统一外部交易)step (万人团)nopaid(无付款订单)pre_auth_type(预授权0元购机交易)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">订单的运费险，单位为元</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.yfx_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">运费险支付号</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.yfx_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">运费险类型</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.yfx_type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">在返回的trade对象上专门增加一个字段zero_purchase来区分，这个为true的就是0元购机预授权交易</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.zero_purchase = None
        
        self.__init(kargs)

    def toDict(self, **kargs):
        result = deepcopy(self.__kargs)
        for key, value in self.__dict__.iteritems():
            if key.endswith("__kargs"):
                continue
            if value == None:
                if kargs.has_key("includeNone") and kargs["includeNone"]:
                    result[key] = value
                else:
                    continue
            else:
                result[key] = value
        return result
        
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
                if not isinstance(value, basestring):
                    return _jsonEnode(value)
                else:
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
            
            "adjust_fee": "String",
            
            "alipay_id": "Number",
            
            "alipay_no": "String",
            
            "alipay_url": "String",
            
            "alipay_warn_msg": "String",
            
            "area_id": "String",
            
            "arrive_cut_time": "String",
            
            "arrive_interval": "Number",
            
            "async_modified": "Date",
            
            "available_confirm_fee": "String",
            
            "buyer_alipay_no": "String",
            
            "buyer_area": "String",
            
            "buyer_cod_fee": "String",
            
            "buyer_email": "String",
            
            "buyer_flag": "Number",
            
            "buyer_memo": "String",
            
            "buyer_message": "String",
            
            "buyer_nick": "String",
            
            "buyer_obtain_point_fee": "Number",
            
            "buyer_rate": "Boolean",
            
            "can_rate": "Boolean",
            
            "cod_fee": "String",
            
            "cod_status": "String",
            
            "commission_fee": "String",
            
            "consign_interval": "Number",
            
            "consign_time": "Date",
            
            "created": "Date",
            
            "credit_card_fee": "String",
            
            "discount_fee": "String",
            
            "end_time": "Date",
            
            "eticket_ext": "String",
            
            "express_agency_fee": "String",
            
            "has_buyer_message": "Boolean",
            
            "has_post_fee": "Boolean",
            
            "has_yfx": "Boolean",
            
            "iid": "String",
            
            "invoice_name": "String",
            
            "invoice_type": "String",
            
            "is_3D": "Boolean",
            
            "is_brand_sale": "Boolean",
            
            "is_daixiao": "Boolean",
            
            "is_force_wlb": "Boolean",
            
            "is_lgtype": "Boolean",
            
            "is_part_consign": "Boolean",
            
            "is_wt": "Boolean",
            
            "lg_aging": "String",
            
            "lg_aging_type": "String",
            
            "mark_desc": "String",
            
            "modified": "Date",
            
            "num": "Number",
            
            "num_iid": "Number",
            
            "nut_feature": "String",
            
            "o2o": "String",
            
            "o2o_delivery": "String",
            
            "o2o_guide_id": "String",
            
            "o2o_guide_name": "String",
            
            "o2o_shop_id": "String",
            
            "o2o_shop_name": "String",
            
            "orders": "Order",
            
            "pay_time": "Date",
            
            "payment": "String",
            
            "pic_path": "String",
            
            "point_fee": "Number",
            
            "post_fee": "String",
            
            "price": "String",
            
            "promotion": "String",
            
            "promotion_details": "PromotionDetail",
            
            "real_point_fee": "Number",
            
            "received_payment": "String",
            
            "receiver_address": "String",
            
            "receiver_city": "String",
            
            "receiver_district": "String",
            
            "receiver_mobile": "String",
            
            "receiver_name": "String",
            
            "receiver_phone": "String",
            
            "receiver_state": "String",
            
            "receiver_zip": "String",
            
            "seller_alipay_no": "String",
            
            "seller_can_rate": "Boolean",
            
            "seller_cod_fee": "String",
            
            "seller_email": "String",
            
            "seller_flag": "Number",
            
            "seller_memo": "String",
            
            "seller_mobile": "String",
            
            "seller_name": "String",
            
            "seller_nick": "String",
            
            "seller_phone": "String",
            
            "seller_rate": "Boolean",
            
            "send_time": "String",
            
            "service_orders": "ServiceOrder",
            
            "service_tags": "LogisticsTag",
            
            "shipping_type": "String",
            
            "snapshot": "String",
            
            "snapshot_url": "String",
            
            "status": "String",
            
            "step_paid_fee": "String",
            
            "step_trade_status": "String",
            
            "tid": "Number",
            
            "timeout_action_time": "Date",
            
            "title": "String",
            
            "total_fee": "String",
            
            "trade_from": "String",
            
            "trade_memo": "String",
            
            "trade_source": "String",
            
            "type": "String",
            
            "yfx_fee": "String",
            
            "yfx_id": "String",
            
            "yfx_type": "String",
            
            "zero_purchase": "Boolean",
        }
        levels = {
            
            "adjust_fee": "Basic",
            
            "alipay_id": "Basic",
            
            "alipay_no": "Basic",
            
            "alipay_url": "Basic",
            
            "alipay_warn_msg": "Basic",
            
            "area_id": "Basic",
            
            "arrive_cut_time": "Basic",
            
            "arrive_interval": "Basic",
            
            "async_modified": "Basic",
            
            "available_confirm_fee": "Basic",
            
            "buyer_alipay_no": "Basic",
            
            "buyer_area": "Basic",
            
            "buyer_cod_fee": "Basic",
            
            "buyer_email": "Basic",
            
            "buyer_flag": "Basic",
            
            "buyer_memo": "Basic",
            
            "buyer_message": "Basic",
            
            "buyer_nick": "Basic",
            
            "buyer_obtain_point_fee": "Basic",
            
            "buyer_rate": "Basic",
            
            "can_rate": "Basic",
            
            "cod_fee": "Basic",
            
            "cod_status": "Basic",
            
            "commission_fee": "Basic",
            
            "consign_interval": "Basic",
            
            "consign_time": "Basic",
            
            "created": "Basic",
            
            "credit_card_fee": "Basic",
            
            "discount_fee": "Basic",
            
            "end_time": "Basic",
            
            "eticket_ext": "Basic",
            
            "express_agency_fee": "Basic",
            
            "has_buyer_message": "Basic",
            
            "has_post_fee": "Basic",
            
            "has_yfx": "Basic",
            
            "iid": "Basic",
            
            "invoice_name": "Basic",
            
            "invoice_type": "Basic",
            
            "is_3D": "Basic",
            
            "is_brand_sale": "Basic",
            
            "is_daixiao": "Basic",
            
            "is_force_wlb": "Basic",
            
            "is_lgtype": "Basic",
            
            "is_part_consign": "Basic",
            
            "is_wt": "Basic",
            
            "lg_aging": "Basic",
            
            "lg_aging_type": "Basic",
            
            "mark_desc": "Basic",
            
            "modified": "Basic",
            
            "num": "Basic",
            
            "num_iid": "Basic",
            
            "nut_feature": "Basic",
            
            "o2o": "Basic",
            
            "o2o_delivery": "Basic",
            
            "o2o_guide_id": "Basic",
            
            "o2o_guide_name": "Basic",
            
            "o2o_shop_id": "Basic",
            
            "o2o_shop_name": "Basic",
            
            "orders": "Object Array",
            
            "pay_time": "Basic",
            
            "payment": "Basic",
            
            "pic_path": "Basic",
            
            "point_fee": "Basic",
            
            "post_fee": "Basic",
            
            "price": "Basic",
            
            "promotion": "Basic",
            
            "promotion_details": "Object Array",
            
            "real_point_fee": "Basic",
            
            "received_payment": "Basic",
            
            "receiver_address": "Basic",
            
            "receiver_city": "Basic",
            
            "receiver_district": "Basic",
            
            "receiver_mobile": "Basic",
            
            "receiver_name": "Basic",
            
            "receiver_phone": "Basic",
            
            "receiver_state": "Basic",
            
            "receiver_zip": "Basic",
            
            "seller_alipay_no": "Basic",
            
            "seller_can_rate": "Basic",
            
            "seller_cod_fee": "Basic",
            
            "seller_email": "Basic",
            
            "seller_flag": "Basic",
            
            "seller_memo": "Basic",
            
            "seller_mobile": "Basic",
            
            "seller_name": "Basic",
            
            "seller_nick": "Basic",
            
            "seller_phone": "Basic",
            
            "seller_rate": "Basic",
            
            "send_time": "Basic",
            
            "service_orders": "Object Array",
            
            "service_tags": "Object Array",
            
            "shipping_type": "Basic",
            
            "snapshot": "Basic",
            
            "snapshot_url": "Basic",
            
            "status": "Basic",
            
            "step_paid_fee": "Basic",
            
            "step_trade_status": "Basic",
            
            "tid": "Basic",
            
            "timeout_action_time": "Basic",
            
            "title": "Basic",
            
            "total_fee": "Basic",
            
            "trade_from": "Basic",
            
            "trade_memo": "Basic",
            
            "trade_source": "Basic",
            
            "type": "Basic",
            
            "yfx_fee": "Basic",
            
            "yfx_id": "Basic",
            
            "yfx_type": "Basic",
            
            "zero_purchase": "Basic",

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
            pythonType = getattr(
                sys.modules[os.path.basename(
                os.path.dirname(os.path.realpath(__file__))) + "." + nameType], 
                nameType)

        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)
        
    def __init(self, kargs):
        
        if kargs.has_key("adjust_fee"):
            self.adjust_fee = self._newInstance("adjust_fee", kargs["adjust_fee"])
        
        if kargs.has_key("alipay_id"):
            self.alipay_id = self._newInstance("alipay_id", kargs["alipay_id"])
        
        if kargs.has_key("alipay_no"):
            self.alipay_no = self._newInstance("alipay_no", kargs["alipay_no"])
        
        if kargs.has_key("alipay_url"):
            self.alipay_url = self._newInstance("alipay_url", kargs["alipay_url"])
        
        if kargs.has_key("alipay_warn_msg"):
            self.alipay_warn_msg = self._newInstance("alipay_warn_msg", kargs["alipay_warn_msg"])
        
        if kargs.has_key("area_id"):
            self.area_id = self._newInstance("area_id", kargs["area_id"])
        
        if kargs.has_key("arrive_cut_time"):
            self.arrive_cut_time = self._newInstance("arrive_cut_time", kargs["arrive_cut_time"])
        
        if kargs.has_key("arrive_interval"):
            self.arrive_interval = self._newInstance("arrive_interval", kargs["arrive_interval"])
        
        if kargs.has_key("async_modified"):
            self.async_modified = self._newInstance("async_modified", kargs["async_modified"])
        
        if kargs.has_key("available_confirm_fee"):
            self.available_confirm_fee = self._newInstance("available_confirm_fee", kargs["available_confirm_fee"])
        
        if kargs.has_key("buyer_alipay_no"):
            self.buyer_alipay_no = self._newInstance("buyer_alipay_no", kargs["buyer_alipay_no"])
        
        if kargs.has_key("buyer_area"):
            self.buyer_area = self._newInstance("buyer_area", kargs["buyer_area"])
        
        if kargs.has_key("buyer_cod_fee"):
            self.buyer_cod_fee = self._newInstance("buyer_cod_fee", kargs["buyer_cod_fee"])
        
        if kargs.has_key("buyer_email"):
            self.buyer_email = self._newInstance("buyer_email", kargs["buyer_email"])
        
        if kargs.has_key("buyer_flag"):
            self.buyer_flag = self._newInstance("buyer_flag", kargs["buyer_flag"])
        
        if kargs.has_key("buyer_memo"):
            self.buyer_memo = self._newInstance("buyer_memo", kargs["buyer_memo"])
        
        if kargs.has_key("buyer_message"):
            self.buyer_message = self._newInstance("buyer_message", kargs["buyer_message"])
        
        if kargs.has_key("buyer_nick"):
            self.buyer_nick = self._newInstance("buyer_nick", kargs["buyer_nick"])
        
        if kargs.has_key("buyer_obtain_point_fee"):
            self.buyer_obtain_point_fee = self._newInstance("buyer_obtain_point_fee", kargs["buyer_obtain_point_fee"])
        
        if kargs.has_key("buyer_rate"):
            self.buyer_rate = self._newInstance("buyer_rate", kargs["buyer_rate"])
        
        if kargs.has_key("can_rate"):
            self.can_rate = self._newInstance("can_rate", kargs["can_rate"])
        
        if kargs.has_key("cod_fee"):
            self.cod_fee = self._newInstance("cod_fee", kargs["cod_fee"])
        
        if kargs.has_key("cod_status"):
            self.cod_status = self._newInstance("cod_status", kargs["cod_status"])
        
        if kargs.has_key("commission_fee"):
            self.commission_fee = self._newInstance("commission_fee", kargs["commission_fee"])
        
        if kargs.has_key("consign_interval"):
            self.consign_interval = self._newInstance("consign_interval", kargs["consign_interval"])
        
        if kargs.has_key("consign_time"):
            self.consign_time = self._newInstance("consign_time", kargs["consign_time"])
        
        if kargs.has_key("created"):
            self.created = self._newInstance("created", kargs["created"])
        
        if kargs.has_key("credit_card_fee"):
            self.credit_card_fee = self._newInstance("credit_card_fee", kargs["credit_card_fee"])
        
        if kargs.has_key("discount_fee"):
            self.discount_fee = self._newInstance("discount_fee", kargs["discount_fee"])
        
        if kargs.has_key("end_time"):
            self.end_time = self._newInstance("end_time", kargs["end_time"])
        
        if kargs.has_key("eticket_ext"):
            self.eticket_ext = self._newInstance("eticket_ext", kargs["eticket_ext"])
        
        if kargs.has_key("express_agency_fee"):
            self.express_agency_fee = self._newInstance("express_agency_fee", kargs["express_agency_fee"])
        
        if kargs.has_key("has_buyer_message"):
            self.has_buyer_message = self._newInstance("has_buyer_message", kargs["has_buyer_message"])
        
        if kargs.has_key("has_post_fee"):
            self.has_post_fee = self._newInstance("has_post_fee", kargs["has_post_fee"])
        
        if kargs.has_key("has_yfx"):
            self.has_yfx = self._newInstance("has_yfx", kargs["has_yfx"])
        
        if kargs.has_key("iid"):
            self.iid = self._newInstance("iid", kargs["iid"])
        
        if kargs.has_key("invoice_name"):
            self.invoice_name = self._newInstance("invoice_name", kargs["invoice_name"])
        
        if kargs.has_key("invoice_type"):
            self.invoice_type = self._newInstance("invoice_type", kargs["invoice_type"])
        
        if kargs.has_key("is_3D"):
            self.is_3D = self._newInstance("is_3D", kargs["is_3D"])
        
        if kargs.has_key("is_brand_sale"):
            self.is_brand_sale = self._newInstance("is_brand_sale", kargs["is_brand_sale"])
        
        if kargs.has_key("is_daixiao"):
            self.is_daixiao = self._newInstance("is_daixiao", kargs["is_daixiao"])
        
        if kargs.has_key("is_force_wlb"):
            self.is_force_wlb = self._newInstance("is_force_wlb", kargs["is_force_wlb"])
        
        if kargs.has_key("is_lgtype"):
            self.is_lgtype = self._newInstance("is_lgtype", kargs["is_lgtype"])
        
        if kargs.has_key("is_part_consign"):
            self.is_part_consign = self._newInstance("is_part_consign", kargs["is_part_consign"])
        
        if kargs.has_key("is_wt"):
            self.is_wt = self._newInstance("is_wt", kargs["is_wt"])
        
        if kargs.has_key("lg_aging"):
            self.lg_aging = self._newInstance("lg_aging", kargs["lg_aging"])
        
        if kargs.has_key("lg_aging_type"):
            self.lg_aging_type = self._newInstance("lg_aging_type", kargs["lg_aging_type"])
        
        if kargs.has_key("mark_desc"):
            self.mark_desc = self._newInstance("mark_desc", kargs["mark_desc"])
        
        if kargs.has_key("modified"):
            self.modified = self._newInstance("modified", kargs["modified"])
        
        if kargs.has_key("num"):
            self.num = self._newInstance("num", kargs["num"])
        
        if kargs.has_key("num_iid"):
            self.num_iid = self._newInstance("num_iid", kargs["num_iid"])
        
        if kargs.has_key("nut_feature"):
            self.nut_feature = self._newInstance("nut_feature", kargs["nut_feature"])
        
        if kargs.has_key("o2o"):
            self.o2o = self._newInstance("o2o", kargs["o2o"])
        
        if kargs.has_key("o2o_delivery"):
            self.o2o_delivery = self._newInstance("o2o_delivery", kargs["o2o_delivery"])
        
        if kargs.has_key("o2o_guide_id"):
            self.o2o_guide_id = self._newInstance("o2o_guide_id", kargs["o2o_guide_id"])
        
        if kargs.has_key("o2o_guide_name"):
            self.o2o_guide_name = self._newInstance("o2o_guide_name", kargs["o2o_guide_name"])
        
        if kargs.has_key("o2o_shop_id"):
            self.o2o_shop_id = self._newInstance("o2o_shop_id", kargs["o2o_shop_id"])
        
        if kargs.has_key("o2o_shop_name"):
            self.o2o_shop_name = self._newInstance("o2o_shop_name", kargs["o2o_shop_name"])
        
        if kargs.has_key("orders"):
            self.orders = self._newInstance("orders", kargs["orders"])
        
        if kargs.has_key("pay_time"):
            self.pay_time = self._newInstance("pay_time", kargs["pay_time"])
        
        if kargs.has_key("payment"):
            self.payment = self._newInstance("payment", kargs["payment"])
        
        if kargs.has_key("pic_path"):
            self.pic_path = self._newInstance("pic_path", kargs["pic_path"])
        
        if kargs.has_key("point_fee"):
            self.point_fee = self._newInstance("point_fee", kargs["point_fee"])
        
        if kargs.has_key("post_fee"):
            self.post_fee = self._newInstance("post_fee", kargs["post_fee"])
        
        if kargs.has_key("price"):
            self.price = self._newInstance("price", kargs["price"])
        
        if kargs.has_key("promotion"):
            self.promotion = self._newInstance("promotion", kargs["promotion"])
        
        if kargs.has_key("promotion_details"):
            self.promotion_details = self._newInstance("promotion_details", kargs["promotion_details"])
        
        if kargs.has_key("real_point_fee"):
            self.real_point_fee = self._newInstance("real_point_fee", kargs["real_point_fee"])
        
        if kargs.has_key("received_payment"):
            self.received_payment = self._newInstance("received_payment", kargs["received_payment"])
        
        if kargs.has_key("receiver_address"):
            self.receiver_address = self._newInstance("receiver_address", kargs["receiver_address"])
        
        if kargs.has_key("receiver_city"):
            self.receiver_city = self._newInstance("receiver_city", kargs["receiver_city"])
        
        if kargs.has_key("receiver_district"):
            self.receiver_district = self._newInstance("receiver_district", kargs["receiver_district"])
        
        if kargs.has_key("receiver_mobile"):
            self.receiver_mobile = self._newInstance("receiver_mobile", kargs["receiver_mobile"])
        
        if kargs.has_key("receiver_name"):
            self.receiver_name = self._newInstance("receiver_name", kargs["receiver_name"])
        
        if kargs.has_key("receiver_phone"):
            self.receiver_phone = self._newInstance("receiver_phone", kargs["receiver_phone"])
        
        if kargs.has_key("receiver_state"):
            self.receiver_state = self._newInstance("receiver_state", kargs["receiver_state"])
        
        if kargs.has_key("receiver_zip"):
            self.receiver_zip = self._newInstance("receiver_zip", kargs["receiver_zip"])
        
        if kargs.has_key("seller_alipay_no"):
            self.seller_alipay_no = self._newInstance("seller_alipay_no", kargs["seller_alipay_no"])
        
        if kargs.has_key("seller_can_rate"):
            self.seller_can_rate = self._newInstance("seller_can_rate", kargs["seller_can_rate"])
        
        if kargs.has_key("seller_cod_fee"):
            self.seller_cod_fee = self._newInstance("seller_cod_fee", kargs["seller_cod_fee"])
        
        if kargs.has_key("seller_email"):
            self.seller_email = self._newInstance("seller_email", kargs["seller_email"])
        
        if kargs.has_key("seller_flag"):
            self.seller_flag = self._newInstance("seller_flag", kargs["seller_flag"])
        
        if kargs.has_key("seller_memo"):
            self.seller_memo = self._newInstance("seller_memo", kargs["seller_memo"])
        
        if kargs.has_key("seller_mobile"):
            self.seller_mobile = self._newInstance("seller_mobile", kargs["seller_mobile"])
        
        if kargs.has_key("seller_name"):
            self.seller_name = self._newInstance("seller_name", kargs["seller_name"])
        
        if kargs.has_key("seller_nick"):
            self.seller_nick = self._newInstance("seller_nick", kargs["seller_nick"])
        
        if kargs.has_key("seller_phone"):
            self.seller_phone = self._newInstance("seller_phone", kargs["seller_phone"])
        
        if kargs.has_key("seller_rate"):
            self.seller_rate = self._newInstance("seller_rate", kargs["seller_rate"])
        
        if kargs.has_key("send_time"):
            self.send_time = self._newInstance("send_time", kargs["send_time"])
        
        if kargs.has_key("service_orders"):
            self.service_orders = self._newInstance("service_orders", kargs["service_orders"])
        
        if kargs.has_key("service_tags"):
            self.service_tags = self._newInstance("service_tags", kargs["service_tags"])
        
        if kargs.has_key("shipping_type"):
            self.shipping_type = self._newInstance("shipping_type", kargs["shipping_type"])
        
        if kargs.has_key("snapshot"):
            self.snapshot = self._newInstance("snapshot", kargs["snapshot"])
        
        if kargs.has_key("snapshot_url"):
            self.snapshot_url = self._newInstance("snapshot_url", kargs["snapshot_url"])
        
        if kargs.has_key("status"):
            self.status = self._newInstance("status", kargs["status"])
        
        if kargs.has_key("step_paid_fee"):
            self.step_paid_fee = self._newInstance("step_paid_fee", kargs["step_paid_fee"])
        
        if kargs.has_key("step_trade_status"):
            self.step_trade_status = self._newInstance("step_trade_status", kargs["step_trade_status"])
        
        if kargs.has_key("tid"):
            self.tid = self._newInstance("tid", kargs["tid"])
        
        if kargs.has_key("timeout_action_time"):
            self.timeout_action_time = self._newInstance("timeout_action_time", kargs["timeout_action_time"])
        
        if kargs.has_key("title"):
            self.title = self._newInstance("title", kargs["title"])
        
        if kargs.has_key("total_fee"):
            self.total_fee = self._newInstance("total_fee", kargs["total_fee"])
        
        if kargs.has_key("trade_from"):
            self.trade_from = self._newInstance("trade_from", kargs["trade_from"])
        
        if kargs.has_key("trade_memo"):
            self.trade_memo = self._newInstance("trade_memo", kargs["trade_memo"])
        
        if kargs.has_key("trade_source"):
            self.trade_source = self._newInstance("trade_source", kargs["trade_source"])
        
        if kargs.has_key("type"):
            self.type = self._newInstance("type", kargs["type"])
        
        if kargs.has_key("yfx_fee"):
            self.yfx_fee = self._newInstance("yfx_fee", kargs["yfx_fee"])
        
        if kargs.has_key("yfx_id"):
            self.yfx_id = self._newInstance("yfx_id", kargs["yfx_id"])
        
        if kargs.has_key("yfx_type"):
            self.yfx_type = self._newInstance("yfx_type", kargs["yfx_type"])
        
        if kargs.has_key("zero_purchase"):
            self.zero_purchase = self._newInstance("zero_purchase", kargs["zero_purchase"])
