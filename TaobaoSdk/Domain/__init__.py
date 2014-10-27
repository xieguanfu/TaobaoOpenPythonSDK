#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 4, 2012 8:24:36 PM
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from Sku import Sku
from TaobaokePayment import TaobaokePayment
from BuyerRefund import BuyerRefund
from VideoItem import VideoItem
from InventorySum import InventorySum
from FavoriteItem import FavoriteItem
from EvalDetail import EvalDetail
from Demographic import Demographic
from GradeEquity import GradeEquity
from TOPPaginator import TOPPaginator
from StaffEvalStatById import StaffEvalStatById
from LimitDiscountDetail import LimitDiscountDetail
from KfcSearchResult import KfcSearchResult
from Template import Template
from DealerOrderDetail import DealerOrderDetail
from Department import Department
from Group import Group
from TemplateResult import TemplateResult
from PropertyInputDO import PropertyInputDO
from INWordCategory import INWordCategory
from ADGroupCatMatchPage import ADGroupCatMatchPage
from WaitingTimeById import WaitingTimeById
from Brand import Brand
from ProductSpec import ProductSpec
from SegmentInfo import SegmentInfo
from HotelImage import HotelImage
from ProductImg import ProductImg
from RoomImage import RoomImage
from RefundBill import RefundBill
from ArticleSub import ArticleSub
from CampaignSchedule import CampaignSchedule
from WlbProcessStatus import WlbProcessStatus
from OrderMessage import OrderMessage
from LoginLog import LoginLog
from WlbMessage import WlbMessage
from PromotionInShop import PromotionInShop
from TravelItemsSku import TravelItemsSku
from Refund import Refund
from TravelItemsLocalityLife import TravelItemsLocalityLife
from ItemTemplate import ItemTemplate
from Keyword import Keyword
from SubUserPermission import SubUserPermission
from PromotionRange import PromotionRange
from IdsModule import IdsModule
from Shipping import Shipping
from ReturnBill import ReturnBill
from DiscountDetail import DiscountDetail
from SelectedItem import SelectedItem
from TopSpm import TopSpm
from WlbAuthorization import WlbAuthorization
from TravelItemsPropValue import TravelItemsPropValue
from Receiver import Receiver
from RefundItem import RefundItem
from CreativeRecord import CreativeRecord
from LotteryWangcaiPresentStat import LotteryWangcaiPresentStat
from PicUrl import PicUrl
from CouponDetail import CouponDetail
from Shop import Shop
from FenxiaoPdu import FenxiaoPdu
from ADGroupCatmatch import ADGroupCatmatch
from OutEntityItem import OutEntityItem
from ADGroupPage import ADGroupPage
from HotelOrder import HotelOrder
from PolicyDetail import PolicyDetail
from FenxiaoImage import FenxiaoImage
from Qscore import Qscore
from Coupon import Coupon
from ChannelOption import ChannelOption
from TravelItems import TravelItems
from WlbOrder import WlbOrder
from VideoPlayInfo import VideoPlayInfo
from PaimaiInfo import PaimaiInfo
from Distributor import Distributor
from Duty import Duty
from RefundBaseResponse import RefundBaseResponse
from IpcInventoryDetailDo import IpcInventoryDetailDo
from ParameterVO import ParameterVO
from WordList import WordList
from ModularDescInfo import ModularDescInfo
from TravelItemsImg import TravelItemsImg
from CatBrandSaleProp import CatBrandSaleProp
from NotifyRefund import NotifyRefund
from TargetSearchTopResult import TargetSearchTopResult
from Area import Area
from CarriageDetail import CarriageDetail
from StreamWeight import StreamWeight
from WlbItemInventoryLog import WlbItemInventoryLog
from ItemProp import ItemProp
from ParamKeyVO import ParamKeyVO
from INWordBase import INWordBase
from PurchaseOrder import PurchaseOrder
from UserCredit import UserCredit
from Location import Location
from Cooperation import Cooperation
from UrlList import UrlList
from EbookSignStatus import EbookSignStatus
from WlbOrderDetail import WlbOrderDetail
from SinglePayDetail import SinglePayDetail
from PropImg import PropImg
from Picture import Picture
from AndroidVlowUrl import AndroidVlowUrl
from ADGroup import ADGroup
from DeliveryTemplate import DeliveryTemplate
from Permission import Permission
from SubPurchaseOrder import SubPurchaseOrder
from BrandCatControlInfo import BrandCatControlInfo
from ProductPropImg import ProductPropImg
from AddressResult import AddressResult
from SubUserFullInfo import SubUserFullInfo
from GroupMember import GroupMember
from RangeVO import RangeVO
from AreaOption import AreaOption
from Tag import Tag
from INCategoryAnalysis import INCategoryAnalysis
from OnlineTimeById import OnlineTimeById
from MicroPayOrderDetail import MicroPayOrderDetail
from BasicMember import BasicMember
from Itinerary import Itinerary
from RefundRemindTimeout import RefundRemindTimeout
from WidgetSku import WidgetSku
from Subscription import Subscription
from ArticleBizOrder import ArticleBizOrder
from PartnerDetail import PartnerDetail
from INCategoryBase import INCategoryBase
from SellerCat import SellerCat
from ADGroupPlace import ADGroupPlace
from TmallMinisite import TmallMinisite
from Bill import Bill
from ActionInfo import ActionInfo
from TaobaokeItemDetail import TaobaokeItemDetail
from FenxiaoItemRecord import FenxiaoItemRecord
from ItemPromotion import ItemPromotion
from Range import Range
from Requisition import Requisition
from Place import Place
from LogisticsCompany import LogisticsCompany
from AfterSale import AfterSale
from WlbInventory import WlbInventory
from OrderAmount import OrderAmount
from LotteryWangcaiSellerGoodsInfo import LotteryWangcaiSellerGoodsInfo
from RecommendWord import RecommendWord
from KeywordPage import KeywordPage
from ProductCat import ProductCat
from CollectItem import CollectItem
from TransitStepInfo import TransitStepInfo
from Campaign import Campaign
from ErrorMessage import ErrorMessage
from SubUserInfo import SubUserInfo
from Trade import Trade
from ScoreResult import ScoreResult
from RankedItem import RankedItem
from UserInfo import UserInfo
from RecommendWordPage import RecommendWordPage
from NonReplyStatOnDay import NonReplyStatOnDay
from WlbItemInventory import WlbItemInventory
from ScItem import ScItem
from ReplyStatById import ReplyStatById
from PromotionDisplayTop import PromotionDisplayTop
from ScItemMap import ScItemMap
from AppCustomer import AppCustomer
from SubwayItemPartition import SubwayItemPartition
from SpmResult import SpmResult
from WordCountList import WordCountList
from WaitingTimesOnDay import WaitingTimesOnDay
from Hotel import Hotel
from INCategoryChildTop import INCategoryChildTop
from DeliveryTime import DeliveryTime
from Promotion import Promotion
from FavoriteShop import FavoriteShop
from DealerOrder import DealerOrder
from CampaignBudget import CampaignBudget
from ItemDescModule import ItemDescModule
from AlipayAccount import AlipayAccount
from AlipayContract import AlipayContract
from Creative import Creative
from TradeRecord import TradeRecord
from ReplyStatOnDay import ReplyStatOnDay
from NotifyTrade import NotifyTrade
from TmallSearchItem import TmallSearchItem
from StaffEvalStatOnDay import StaffEvalStatOnDay
from TravelItemsProp import TravelItemsProp
from ArticleUserSubscribe import ArticleUserSubscribe
from Store import Store
from AttributeVO import AttributeVO
from TravelItemsAreaNode import TravelItemsAreaNode
from RoomType import RoomType
from RdsDbInfo import RdsDbInfo
from TmallTmCat import TmallTmCat
from TmallBrand import TmallBrand
from FenxiaoSku import FenxiaoSku
from AlipayUserDetail import AlipayUserDetail
from RefundDetail import RefundDetail
from ExtraAttributes import ExtraAttributes
from Meal import Meal
from InnerLabel import InnerLabel
from Discount import Discount
from LocalityLife import LocalityLife
from INCategoryTop import INCategoryTop
from TopFee import TopFee
from ShopCat import ShopCat
from CampaignArea import CampaignArea
from TaobaokeItem import TaobaokeItem
from SubwayItem import SubwayItem
from TradeRate import TradeRate
from User import User
from TradeAmount import TradeAmount
from KeywordForecast import KeywordForecast
from CampaignPlatform import CampaignPlatform
from PromotionInItem import PromotionInItem
from CertTxtInfo import CertTxtInfo
from SubAccountInfo import SubAccountInfo
from DiscardInfo import DiscardInfo
from Feature import Feature
from EbookItem import EbookItem
from ADGroupCatMatchForecast import ADGroupCatMatchForecast
from NonreplyStatById import NonreplyStatById
from AccountFreeze import AccountFreeze
from TradeContact import TradeContact
from INWordAnalysis import INWordAnalysis
from LogisticsPartner import LogisticsPartner
from INCategoryProperties import INCategoryProperties
from Label import Label
from SearchOrderResult import SearchOrderResult
from BrandCatControl import BrandCatControl
from ImprItemDO import ImprItemDO
from Subtask import Subtask
from DemographicSetting import DemographicSetting
from MsgList import MsgList
from OnlineTimesOnDay import OnlineTimesOnDay
from GradePromotion import GradePromotion
from HanoiLabelGroup import HanoiLabelGroup
from SellerAuthorize import SellerAuthorize
from CreativePage import CreativePage
from BaseInfo import BaseInfo
from TaobaokeShop import TaobaokeShop
from TaobaokeEliteItem import TaobaokeEliteItem
from Video import Video
from WlbItemBatchInventory import WlbItemBatchInventory
from FenxiaoGrade import FenxiaoGrade
from FenxiaoProduct import FenxiaoProduct
from LotteryWangcaiPresent import LotteryWangcaiPresent
from TmallSearchTmItem import TmallSearchTmItem
from MjsPromotion import MjsPromotion
from ProductExtraInfo import ProductExtraInfo
from WlbPartnerContact import WlbPartnerContact
from WlbConsignMent import WlbConsignMent
from Passerger import Passerger
from InventoryAuthorizeInfo import InventoryAuthorizeInfo
from DocumentVO import DocumentVO
from CertPicInfo import CertPicInfo
from ItemCat import ItemCat
from ItemImg import ItemImg
from TOPSearchResult import TOPSearchResult
from WlbSellerSubscription import WlbSellerSubscription
from Task import Task
from WidgetSkuProps import WidgetSkuProps
from Policy import Policy
from DistributorArchive import DistributorArchive
from WlbOrderScheduleRule import WlbOrderScheduleRule
from EbookLib import EbookLib
from NotifyItem import NotifyItem
from TravelItemsPriceCalendar import TravelItemsPriceCalendar
from RefundMessage import RefundMessage
from OrderGuest import OrderGuest
from WlbItemBatch import WlbItemBatch
from ImprFeedInfoDO import ImprFeedInfoDO
from Product import Product
from WlbOrderItem import WlbOrderItem
from KeywordQscore import KeywordQscore
from CorpInfo import CorpInfo
from BookBill import BookBill
from BatchPolicy import BatchPolicy
from WlbReplenish import WlbReplenish
from WlbItem import WlbItem
from PromotionDetail import PromotionDetail
from FoodSecurity import FoodSecurity
from ServiceOrder import ServiceOrder
from UnfreezeOrderDetail import UnfreezeOrderDetail
from Role import Role
from LotteryType import LotteryType
from Function import Function
from TaobaokeAuthorize import TaobaokeAuthorize
from Room import Room
from PictureCategory import PictureCategory
from TipInfo import TipInfo
from DistributorItemFlow import DistributorItemFlow
from QueryPagination import QueryPagination
from WlbTmsOrder import WlbTmsOrder
from WlbPartnerAddress import WlbPartnerAddress
from ImprFeedIdDO import ImprFeedIdDO
from Item import Item
from PropValue import PropValue
from TmallCat import TmallCat
from Activity import Activity
from TypeVO import TypeVO
from Chatpeer import Chatpeer
from CrmMember import CrmMember
from PageResult import PageResult
from Order import Order
from AtOrder import AtOrder
from LimitDiscount import LimitDiscount
from LoginUser import LoginUser
from WidgetItem import WidgetItem
from Account import Account
from INRecordBase import INRecordBase
from TmcMessage import TmcMessage
from UserTag import UserTag
from ShopScore import ShopScore
from EbookOrder import EbookOrder
from TradeConfirmFee import TradeConfirmFee
from GradeDiscount import GradeDiscount
from TmallRefundMessage import TmallRefundMessage
from DescModuleInfo import DescModuleInfo
from TravelItemsCombo import TravelItemsCombo
from TradeMonitor import TradeMonitor
from CouponResult import CouponResult
from Evaluation import Evaluation
from InsightWordDataDTO import InsightWordDataDTO 
