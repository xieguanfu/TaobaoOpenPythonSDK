#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief Item(商品)结构
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


                                                                                                
from DeliveryTime import DeliveryTime

                
from DescModuleInfo import DescModuleInfo

                                                
from FoodSecurity import FoodSecurity

                                                                                                                                                                                        
from ItemImg import ItemImg

                                
from LocalityLife import LocalityLife

        
from Location import Location

                
from MpicVideo import MpicVideo

                                                                
from PaimaiInfo import PaimaiInfo

                                                        
from PropImg import PropImg

                                                                        
from Sku import Sku

                                                                        
from Video import Video

                                                
## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Item(商品)结构</SPAN>
class Item(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.__kargs = deepcopy(kargs)
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">售后服务ID,该字段仅在taobao.item.get接口中返回</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.after_sale_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品上传后的状态。onsale出售中，instock库中</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.approve_status = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">天猫订单抽佣比例，为5的倍数，最低0.5%。跟淘客佣金没有关系。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.auction_point = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">代充商品类型。在代充商品的类目下，不传表示不标记商品类型（交易搜索中就不能通过标记搜到相关的交易了）。可选类型： no_mark(不做类型标记) time_card(点卡软件代充) fee_card(话费软件代充)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.auto_fill = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品级别的条形码</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.barcode = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">基础色数据</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.change_prop = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品所属的叶子类目 id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.cid = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">货到付款运费模板ID</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.cod_postage_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Item的发布时间，目前仅供taobao.item.add和taobao.item.get可用</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.created = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">定制工具Id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.custom_made_type_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">下架时间（格式：yyyy-MM-dd HH:mm:ss）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.delist_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">发货时间信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">DeliveryTime</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.delivery_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品描述, 字数要大于5个字符，小于25000个字符</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.desc = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">宝贝描述规范化模块锚点信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">DescModuleInfo</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.desc_module_info = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品描述模块化，模块列表，由List转化成jsonArray存入，后端逻辑验证通过，拼装成模块内容+锚点导航后存入desc中。数据结构具体参见Item_Desc_Module</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.desc_modules = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品url</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.detail_url = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">ems费用,格式：5.00；单位：元；精确到：分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Price</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.ems_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">快递费用,格式：5.00；单位：元；精确到：分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Price</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.express_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">宝贝特征值， 只有在Top支持的特征值才能保存到宝贝上</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.features = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">食品安全信息，包括：生产许可证编号、产品标准号、厂名、厂址等</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">FoodSecurity</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.food_security = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">运费承担方式,seller（卖家承担），buyer(买家承担）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.freight_payer = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">全球购商品采购地信息（地区/国家），代表全球购商品的产地信息。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.global_stock_country = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">全球购商品采购地信息（库存类型），有两种库存类型：现货和代购; 参数值为1时代表现货，值为2时代表代购</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.global_stock_type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">支持会员打折,true/false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_discount = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否有发票,true/false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_invoice = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">橱窗推荐,true/false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_showcase = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否有保修,true/false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.has_warranty = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">加价幅度。如果为0，代表系统代理幅度。 在竞拍中，为了超越上一个出价，会员需要在当前出价上增加金额，这个金额就是加价幅度。卖家在发布宝贝的时候可以自定义加价幅度，也可以让系统自动代理加价。系统自动代理加价的加价幅度随着当前出价金额的增加而增加，我们建议会员使用系统自动代理加价，并请买家在出价前看清楚加价幅度的具体金额。另外需要注意是，此功能只适用于拍卖的商品。 以下是系统自动代理加价幅度表： 当前价（加价幅度 ） 1-40（ 1 ）、41-100（ 2 ）、101-200（5 ）、201-500 （10）、501-1001（15）、001-2000（25）、2001-5000（50）、5001-10000（100） 10001以上         200</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.increment = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用户内店宝贝装修模板id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.inner_shop_auction_template_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用户自行输入的类目属性ID串。结构："pid1,pid2,pid3"，如："20000"（表示品牌） 注：通常一个类目下用户可输入的关键属性不超过1个。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.input_pids = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用户自行输入的子属性名和属性值，结构:"父属性值;一级子属性名;一级子属性值;二级子属性名;自定义输入值,....",如：“耐克;耐克系列;科比系列;科比系列;2K5”，input_str需要与input_pids一一对应，注：通常一个类目下用户可输入的关键属性不超过1个。所有属性别名加起来不能超过 3999字节。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.input_str = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否是3D淘宝的商品</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_3D = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否为达尔文挂接成功了的商品</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_cspu = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否在外部网店显示</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_ex = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">非分销商品：0，代销：1，经销：2</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_fenxiao = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否24小时闪电发货</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_lightning_consignment = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否是线下商品。 1：线上商品（默认值）； 2：线上或线下商品； 3：线下商品。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_offline = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品是否为先行赔付 taobao.items.search和taobao.items.vip.search专用</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_prepay = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否在淘宝显示</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_taobao = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否定时上架商品</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_timing = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">虚拟商品的状态字段</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_virtual = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">标示商品是否为新品。 值含义：true-是，false-否。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_xinpin = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品图片列表(包括主图)。fields中只设置item_img可以返回ItemImg结构体中所有字段，如果设置为item_img.id、item_img.url、item_img.position等形式就只会返回相应的字段</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">ItemImg</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.item_imgs = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">表示商品的体积，用于按体积计费的运费模板。该值的单位为立方米（m3）。 该值支持两种格式的设置：格式1：bulk:3,单位为立方米(m3),表示直接设置为商品的体积。格式2：weight:10;breadth:10;height:10，单位为米（m）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.item_size = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品的重量，用于按重量计费的运费模板。注意：单位为kg</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.item_weight = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">上架时间（格式：yyyy-MM-dd HH:mm:ss）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.list_time = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">本地生活电子交易凭证业务，目前此字段只涉及到的信息为有效期: 如果有效期为起止日期类型，此值为2012-08-06,2012-08-16 如果有效期为【购买成功日 至】类型则格式为2012-08-16 如果有效期为天数类型则格式为3</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">LocalityLife</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.locality_life = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品所在地</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Location</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.location = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品修改时间（格式：yyyy-MM-dd HH:mm:ss）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.modified = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">宝贝主图视频的数据信息，包括：视频ID，视频缩略图URL，视频时长，视频状态等信息。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">MpicVideo</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.mpic_video = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否为新消保法中的7天无理由退货</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.newprepay = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">卖家昵称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.nick = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品数量</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.num = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品数字id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.num_iid = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否淘1站商品</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.one_station = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商家外部编码(可与商家外部系统对接)。需要授权才能获取。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.outer_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用户外店装修模板id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.outer_shop_auction_template_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">用于保存拍卖有关的信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">PaimaiInfo</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.paimai_info = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品主图片地址</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.pic_url = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">平邮费用,格式：5.00；单位：元；精确到：分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Price</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.post_fee = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">宝贝所属的运费模板ID，如果没有返回则说明没有使用运费模板</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.postage_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品价格，格式：5.00；单位：元；精确到：分</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Price</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.price = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">宝贝所属产品的id(可能为空). 该字段可以通过taobao.products.search 得到</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.product_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">消保类型，多个类型以,分割。可取以下值：2：假一赔三；4：7天无理由退换货；taobao.items.search和taobao.items.vip.search专用</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.promoted_service = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品属性图片列表。fields中只设置prop_img可以返回PropImg结构体中所有字段，如果设置为prop_img.id、prop_img.url、prop_img.properties、prop_img.position等形式就只会返回相应的字段</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">PropImg</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.prop_imgs = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">属性值别名,比如颜色的自定义名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.property_alias = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品属性 格式：pid:vid;pid:vid</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.props = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品属性名称。标识着props内容里面的pid和vid所对应的名称。格式为：pid1:vid1:pid_name1:vid_name1;pid2:vid2:pid_name2:vid_name2……(<strong>注：</strong><font color="red">属性名称中的冒号":"被转换为："#cln#";  分号";"被转换为："#scln#"</font>)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.props_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品所属卖家的信用等级数，1表示1心，2表示2心……，只有调用商品搜索:taobao.items.get和taobao.items.search的时候才能返回</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.score = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">秒杀商品类型。打上秒杀标记的商品，用户只能下架并不能再上架，其他任何编辑或删除操作都不能进行。如果用户想取消秒杀标记，需要联系小二进行操作。如果秒杀结束需要自由编辑请联系活动负责人（小二）去掉秒杀标记。可选类型 web_only(只能通过web网络秒杀) wap_only(只能通过wap网络秒杀) web_and_wap(既能通过web秒杀也能通过wap秒杀)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.second_kill = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品卖点信息，天猫商家使用字段，最长150个字符。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.sell_point = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否承诺退换货服务!</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.sell_promise = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品所属的店铺内卖家自定义类目列表</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_cids = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;"><a href="http://open.taobao.com/dev/index.php/Sku">Sku</a>列表。fields中只设置sku可以返回Sku结构体中所有字段，如果设置为sku.sku_id、sku.properties、sku.quantity等形式就只会返回相应的字段</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Sku</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.skus = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品新旧程度(全新:new，闲置:unused，二手：second)</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.stuff_status = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品是否支持拍下减库存:1支持;2取消支持(付款减库存);0(默认)不更改 集市卖家默认拍下减库存; 商城卖家默认付款减库存</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.sub_stock = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品的子标题，给商品增加卖点等描述</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.sub_title = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">页面模板id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.template_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品标题,不能超过60字节</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.title = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品类型(fixed:一口价;auction:拍卖)注：取消团购</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.type = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">有效期,7或者14（默认是7天）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.valid_thru = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">该字段废弃，请勿使用。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.video_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品视频列表(目前只支持单个视频关联)。fields中只设置video可以返回Video结构体中所有字段，如果设置为video.id、video.video_id、 video.url等形式就只会返回相应的字段</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Video</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.videos = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品是否违规，违规：true , 不违规：false</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.violation = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">不带html标签的desc文本信息，该字段只在taobao.item.get接口中返回</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.wap_desc = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">适合wap应用的商品详情url ，该字段只在taobao.item.get接口中返回</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.wap_detail_url = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">无线的宝贝描述</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.wireless_desc = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">预扣库存，即付款减库存的商品现在有多少处于未付款状态的订单</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.with_hold_quantity = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">商品所属的商家的旺旺在线状况， taobao.items.search和taobao.items.vip.search专用</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Boolean</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.ww_status = None
        
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
            
            "after_sale_id": "Number",
            
            "approve_status": "String",
            
            "auction_point": "Number",
            
            "auto_fill": "String",
            
            "barcode": "String",
            
            "change_prop": "String",
            
            "cid": "Number",
            
            "cod_postage_id": "Number",
            
            "created": "Date",
            
            "custom_made_type_id": "String",
            
            "delist_time": "Date",
            
            "delivery_time": "DeliveryTime",
            
            "desc": "String",
            
            "desc_module_info": "DescModuleInfo",
            
            "desc_modules": "String",
            
            "detail_url": "String",
            
            "ems_fee": "Price",
            
            "express_fee": "Price",
            
            "features": "String",
            
            "food_security": "FoodSecurity",
            
            "freight_payer": "String",
            
            "global_stock_country": "String",
            
            "global_stock_type": "String",
            
            "has_discount": "Boolean",
            
            "has_invoice": "Boolean",
            
            "has_showcase": "Boolean",
            
            "has_warranty": "Boolean",
            
            "increment": "String",
            
            "inner_shop_auction_template_id": "Number",
            
            "input_pids": "String",
            
            "input_str": "String",
            
            "is_3D": "Boolean",
            
            "is_cspu": "Boolean",
            
            "is_ex": "Boolean",
            
            "is_fenxiao": "Number",
            
            "is_lightning_consignment": "Boolean",
            
            "is_offline": "String",
            
            "is_prepay": "Boolean",
            
            "is_taobao": "Boolean",
            
            "is_timing": "Boolean",
            
            "is_virtual": "Boolean",
            
            "is_xinpin": "Boolean",
            
            "item_imgs": "ItemImg",
            
            "item_size": "String",
            
            "item_weight": "String",
            
            "list_time": "Date",
            
            "locality_life": "LocalityLife",
            
            "location": "Location",
            
            "modified": "Date",
            
            "mpic_video": "MpicVideo",
            
            "newprepay": "String",
            
            "nick": "String",
            
            "num": "Number",
            
            "num_iid": "Number",
            
            "one_station": "Boolean",
            
            "outer_id": "String",
            
            "outer_shop_auction_template_id": "Number",
            
            "paimai_info": "PaimaiInfo",
            
            "pic_url": "String",
            
            "post_fee": "Price",
            
            "postage_id": "Number",
            
            "price": "Price",
            
            "product_id": "Number",
            
            "promoted_service": "String",
            
            "prop_imgs": "PropImg",
            
            "property_alias": "String",
            
            "props": "String",
            
            "props_name": "String",
            
            "score": "Number",
            
            "second_kill": "String",
            
            "sell_point": "String",
            
            "sell_promise": "Boolean",
            
            "seller_cids": "String",
            
            "skus": "Sku",
            
            "stuff_status": "String",
            
            "sub_stock": "Number",
            
            "sub_title": "String",
            
            "template_id": "String",
            
            "title": "String",
            
            "type": "String",
            
            "valid_thru": "Number",
            
            "video_id": "Number",
            
            "videos": "Video",
            
            "violation": "Boolean",
            
            "wap_desc": "String",
            
            "wap_detail_url": "String",
            
            "wireless_desc": "String",
            
            "with_hold_quantity": "Number",
            
            "ww_status": "Boolean",
        }
        levels = {
            
            "after_sale_id": "Basic",
            
            "approve_status": "Basic",
            
            "auction_point": "Basic",
            
            "auto_fill": "Basic",
            
            "barcode": "Basic",
            
            "change_prop": "Basic",
            
            "cid": "Basic",
            
            "cod_postage_id": "Basic",
            
            "created": "Basic",
            
            "custom_made_type_id": "Basic",
            
            "delist_time": "Basic",
            
            "delivery_time": "Object",
            
            "desc": "Basic",
            
            "desc_module_info": "Object",
            
            "desc_modules": "Basic",
            
            "detail_url": "Basic",
            
            "ems_fee": "Basic",
            
            "express_fee": "Basic",
            
            "features": "Basic",
            
            "food_security": "Object",
            
            "freight_payer": "Basic",
            
            "global_stock_country": "Basic",
            
            "global_stock_type": "Basic",
            
            "has_discount": "Basic",
            
            "has_invoice": "Basic",
            
            "has_showcase": "Basic",
            
            "has_warranty": "Basic",
            
            "increment": "Basic",
            
            "inner_shop_auction_template_id": "Basic",
            
            "input_pids": "Basic",
            
            "input_str": "Basic",
            
            "is_3D": "Basic",
            
            "is_cspu": "Basic",
            
            "is_ex": "Basic",
            
            "is_fenxiao": "Basic",
            
            "is_lightning_consignment": "Basic",
            
            "is_offline": "Basic",
            
            "is_prepay": "Basic",
            
            "is_taobao": "Basic",
            
            "is_timing": "Basic",
            
            "is_virtual": "Basic",
            
            "is_xinpin": "Basic",
            
            "item_imgs": "Object Array",
            
            "item_size": "Basic",
            
            "item_weight": "Basic",
            
            "list_time": "Basic",
            
            "locality_life": "Object",
            
            "location": "Object",
            
            "modified": "Basic",
            
            "mpic_video": "Object",
            
            "newprepay": "Basic",
            
            "nick": "Basic",
            
            "num": "Basic",
            
            "num_iid": "Basic",
            
            "one_station": "Basic",
            
            "outer_id": "Basic",
            
            "outer_shop_auction_template_id": "Basic",
            
            "paimai_info": "Object",
            
            "pic_url": "Basic",
            
            "post_fee": "Basic",
            
            "postage_id": "Basic",
            
            "price": "Basic",
            
            "product_id": "Basic",
            
            "promoted_service": "Basic",
            
            "prop_imgs": "Object Array",
            
            "property_alias": "Basic",
            
            "props": "Basic",
            
            "props_name": "Basic",
            
            "score": "Basic",
            
            "second_kill": "Basic",
            
            "sell_point": "Basic",
            
            "sell_promise": "Basic",
            
            "seller_cids": "Basic",
            
            "skus": "Object Array",
            
            "stuff_status": "Basic",
            
            "sub_stock": "Basic",
            
            "sub_title": "Basic",
            
            "template_id": "Basic",
            
            "title": "Basic",
            
            "type": "Basic",
            
            "valid_thru": "Basic",
            
            "video_id": "Basic",
            
            "videos": "Object Array",
            
            "violation": "Basic",
            
            "wap_desc": "Basic",
            
            "wap_detail_url": "Basic",
            
            "wireless_desc": "Basic",
            
            "with_hold_quantity": "Basic",
            
            "ww_status": "Basic",

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
        
        if kargs.has_key("after_sale_id"):
            self.after_sale_id = self._newInstance("after_sale_id", kargs["after_sale_id"])
        
        if kargs.has_key("approve_status"):
            self.approve_status = self._newInstance("approve_status", kargs["approve_status"])
        
        if kargs.has_key("auction_point"):
            self.auction_point = self._newInstance("auction_point", kargs["auction_point"])
        
        if kargs.has_key("auto_fill"):
            self.auto_fill = self._newInstance("auto_fill", kargs["auto_fill"])
        
        if kargs.has_key("barcode"):
            self.barcode = self._newInstance("barcode", kargs["barcode"])
        
        if kargs.has_key("change_prop"):
            self.change_prop = self._newInstance("change_prop", kargs["change_prop"])
        
        if kargs.has_key("cid"):
            self.cid = self._newInstance("cid", kargs["cid"])
        
        if kargs.has_key("cod_postage_id"):
            self.cod_postage_id = self._newInstance("cod_postage_id", kargs["cod_postage_id"])
        
        if kargs.has_key("created"):
            self.created = self._newInstance("created", kargs["created"])
        
        if kargs.has_key("custom_made_type_id"):
            self.custom_made_type_id = self._newInstance("custom_made_type_id", kargs["custom_made_type_id"])
        
        if kargs.has_key("delist_time"):
            self.delist_time = self._newInstance("delist_time", kargs["delist_time"])
        
        if kargs.has_key("delivery_time"):
            self.delivery_time = self._newInstance("delivery_time", kargs["delivery_time"])
        
        if kargs.has_key("desc"):
            self.desc = self._newInstance("desc", kargs["desc"])
        
        if kargs.has_key("desc_module_info"):
            self.desc_module_info = self._newInstance("desc_module_info", kargs["desc_module_info"])
        
        if kargs.has_key("desc_modules"):
            self.desc_modules = self._newInstance("desc_modules", kargs["desc_modules"])
        
        if kargs.has_key("detail_url"):
            self.detail_url = self._newInstance("detail_url", kargs["detail_url"])
        
        if kargs.has_key("ems_fee"):
            self.ems_fee = self._newInstance("ems_fee", kargs["ems_fee"])
        
        if kargs.has_key("express_fee"):
            self.express_fee = self._newInstance("express_fee", kargs["express_fee"])
        
        if kargs.has_key("features"):
            self.features = self._newInstance("features", kargs["features"])
        
        if kargs.has_key("food_security"):
            self.food_security = self._newInstance("food_security", kargs["food_security"])
        
        if kargs.has_key("freight_payer"):
            self.freight_payer = self._newInstance("freight_payer", kargs["freight_payer"])
        
        if kargs.has_key("global_stock_country"):
            self.global_stock_country = self._newInstance("global_stock_country", kargs["global_stock_country"])
        
        if kargs.has_key("global_stock_type"):
            self.global_stock_type = self._newInstance("global_stock_type", kargs["global_stock_type"])
        
        if kargs.has_key("has_discount"):
            self.has_discount = self._newInstance("has_discount", kargs["has_discount"])
        
        if kargs.has_key("has_invoice"):
            self.has_invoice = self._newInstance("has_invoice", kargs["has_invoice"])
        
        if kargs.has_key("has_showcase"):
            self.has_showcase = self._newInstance("has_showcase", kargs["has_showcase"])
        
        if kargs.has_key("has_warranty"):
            self.has_warranty = self._newInstance("has_warranty", kargs["has_warranty"])
        
        if kargs.has_key("increment"):
            self.increment = self._newInstance("increment", kargs["increment"])
        
        if kargs.has_key("inner_shop_auction_template_id"):
            self.inner_shop_auction_template_id = self._newInstance("inner_shop_auction_template_id", kargs["inner_shop_auction_template_id"])
        
        if kargs.has_key("input_pids"):
            self.input_pids = self._newInstance("input_pids", kargs["input_pids"])
        
        if kargs.has_key("input_str"):
            self.input_str = self._newInstance("input_str", kargs["input_str"])
        
        if kargs.has_key("is_3D"):
            self.is_3D = self._newInstance("is_3D", kargs["is_3D"])
        
        if kargs.has_key("is_cspu"):
            self.is_cspu = self._newInstance("is_cspu", kargs["is_cspu"])
        
        if kargs.has_key("is_ex"):
            self.is_ex = self._newInstance("is_ex", kargs["is_ex"])
        
        if kargs.has_key("is_fenxiao"):
            self.is_fenxiao = self._newInstance("is_fenxiao", kargs["is_fenxiao"])
        
        if kargs.has_key("is_lightning_consignment"):
            self.is_lightning_consignment = self._newInstance("is_lightning_consignment", kargs["is_lightning_consignment"])
        
        if kargs.has_key("is_offline"):
            self.is_offline = self._newInstance("is_offline", kargs["is_offline"])
        
        if kargs.has_key("is_prepay"):
            self.is_prepay = self._newInstance("is_prepay", kargs["is_prepay"])
        
        if kargs.has_key("is_taobao"):
            self.is_taobao = self._newInstance("is_taobao", kargs["is_taobao"])
        
        if kargs.has_key("is_timing"):
            self.is_timing = self._newInstance("is_timing", kargs["is_timing"])
        
        if kargs.has_key("is_virtual"):
            self.is_virtual = self._newInstance("is_virtual", kargs["is_virtual"])
        
        if kargs.has_key("is_xinpin"):
            self.is_xinpin = self._newInstance("is_xinpin", kargs["is_xinpin"])
        
        if kargs.has_key("item_imgs"):
            self.item_imgs = self._newInstance("item_imgs", kargs["item_imgs"])
        
        if kargs.has_key("item_size"):
            self.item_size = self._newInstance("item_size", kargs["item_size"])
        
        if kargs.has_key("item_weight"):
            self.item_weight = self._newInstance("item_weight", kargs["item_weight"])
        
        if kargs.has_key("list_time"):
            self.list_time = self._newInstance("list_time", kargs["list_time"])
        
        if kargs.has_key("locality_life"):
            self.locality_life = self._newInstance("locality_life", kargs["locality_life"])
        
        if kargs.has_key("location"):
            self.location = self._newInstance("location", kargs["location"])
        
        if kargs.has_key("modified"):
            self.modified = self._newInstance("modified", kargs["modified"])
        
        if kargs.has_key("mpic_video"):
            self.mpic_video = self._newInstance("mpic_video", kargs["mpic_video"])
        
        if kargs.has_key("newprepay"):
            self.newprepay = self._newInstance("newprepay", kargs["newprepay"])
        
        if kargs.has_key("nick"):
            self.nick = self._newInstance("nick", kargs["nick"])
        
        if kargs.has_key("num"):
            self.num = self._newInstance("num", kargs["num"])
        
        if kargs.has_key("num_iid"):
            self.num_iid = self._newInstance("num_iid", kargs["num_iid"])
        
        if kargs.has_key("one_station"):
            self.one_station = self._newInstance("one_station", kargs["one_station"])
        
        if kargs.has_key("outer_id"):
            self.outer_id = self._newInstance("outer_id", kargs["outer_id"])
        
        if kargs.has_key("outer_shop_auction_template_id"):
            self.outer_shop_auction_template_id = self._newInstance("outer_shop_auction_template_id", kargs["outer_shop_auction_template_id"])
        
        if kargs.has_key("paimai_info"):
            self.paimai_info = self._newInstance("paimai_info", kargs["paimai_info"])
        
        if kargs.has_key("pic_url"):
            self.pic_url = self._newInstance("pic_url", kargs["pic_url"])
        
        if kargs.has_key("post_fee"):
            self.post_fee = self._newInstance("post_fee", kargs["post_fee"])
        
        if kargs.has_key("postage_id"):
            self.postage_id = self._newInstance("postage_id", kargs["postage_id"])
        
        if kargs.has_key("price"):
            self.price = self._newInstance("price", kargs["price"])
        
        if kargs.has_key("product_id"):
            self.product_id = self._newInstance("product_id", kargs["product_id"])
        
        if kargs.has_key("promoted_service"):
            self.promoted_service = self._newInstance("promoted_service", kargs["promoted_service"])
        
        if kargs.has_key("prop_imgs"):
            self.prop_imgs = self._newInstance("prop_imgs", kargs["prop_imgs"])
        
        if kargs.has_key("property_alias"):
            self.property_alias = self._newInstance("property_alias", kargs["property_alias"])
        
        if kargs.has_key("props"):
            self.props = self._newInstance("props", kargs["props"])
        
        if kargs.has_key("props_name"):
            self.props_name = self._newInstance("props_name", kargs["props_name"])
        
        if kargs.has_key("score"):
            self.score = self._newInstance("score", kargs["score"])
        
        if kargs.has_key("second_kill"):
            self.second_kill = self._newInstance("second_kill", kargs["second_kill"])
        
        if kargs.has_key("sell_point"):
            self.sell_point = self._newInstance("sell_point", kargs["sell_point"])
        
        if kargs.has_key("sell_promise"):
            self.sell_promise = self._newInstance("sell_promise", kargs["sell_promise"])
        
        if kargs.has_key("seller_cids"):
            self.seller_cids = self._newInstance("seller_cids", kargs["seller_cids"])
        
        if kargs.has_key("skus"):
            self.skus = self._newInstance("skus", kargs["skus"])
        
        if kargs.has_key("stuff_status"):
            self.stuff_status = self._newInstance("stuff_status", kargs["stuff_status"])
        
        if kargs.has_key("sub_stock"):
            self.sub_stock = self._newInstance("sub_stock", kargs["sub_stock"])
        
        if kargs.has_key("sub_title"):
            self.sub_title = self._newInstance("sub_title", kargs["sub_title"])
        
        if kargs.has_key("template_id"):
            self.template_id = self._newInstance("template_id", kargs["template_id"])
        
        if kargs.has_key("title"):
            self.title = self._newInstance("title", kargs["title"])
        
        if kargs.has_key("type"):
            self.type = self._newInstance("type", kargs["type"])
        
        if kargs.has_key("valid_thru"):
            self.valid_thru = self._newInstance("valid_thru", kargs["valid_thru"])
        
        if kargs.has_key("video_id"):
            self.video_id = self._newInstance("video_id", kargs["video_id"])
        
        if kargs.has_key("videos"):
            self.videos = self._newInstance("videos", kargs["videos"])
        
        if kargs.has_key("violation"):
            self.violation = self._newInstance("violation", kargs["violation"])
        
        if kargs.has_key("wap_desc"):
            self.wap_desc = self._newInstance("wap_desc", kargs["wap_desc"])
        
        if kargs.has_key("wap_detail_url"):
            self.wap_detail_url = self._newInstance("wap_detail_url", kargs["wap_detail_url"])
        
        if kargs.has_key("wireless_desc"):
            self.wireless_desc = self._newInstance("wireless_desc", kargs["wireless_desc"])
        
        if kargs.has_key("with_hold_quantity"):
            self.with_hold_quantity = self._newInstance("with_hold_quantity", kargs["with_hold_quantity"])
        
        if kargs.has_key("ww_status"):
            self.ww_status = self._newInstance("ww_status", kargs["ww_status"])
