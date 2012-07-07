#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors:
@date: 11:46:48 PM Jun 4, 2012
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from copy import deepcopy
from datetime import datetime
import os
import sys
import time

__currentPath = os.path.normpath(os.path.join(os.path.realpath(__file__),
    os.path.pardir))
__libraryPath = os.path.normpath(os.path.realpath(os.path.join(__currentPath,
    'libs', 'pytoolkit.zip')))
if not os.path.exists(__libraryPath):
    raise Exception("%s 不存在, 请检查" % __libraryPath)
if __libraryPath not in sys.path:
    sys.path.insert(0, __libraryPath)

# 非Python自带的模块
import JSONLib

class TaobaoObject(object):
    def __init__(self, kargs=dict()):
        # TODO 这里是否可以不用深拷贝,可以试验一下
        self.__kargs = deepcopy(kargs)

        self.__initKargs()

    def toDict(self, **parameters):
        '''
        将该对象中的属性转换成dict格式
        @param includeNone: 如果设置为True,返回结果中将包含属性是None的属性
        @type includeNone: bool
        '''
        includeNone = parameters.has_key("includeNone") and \
            parameters["includeNone"]

        results = self.__kargs
        for key, value in self.__dict__.iteritem():
            # TODO 这里的判断其实也不太合理阿
            if key.endswith("__kargs"):
                continue
            if value == None:
                if includeNone:
                    results[key] = value
                else:
                    continue
        return  results

    # TODO 这里方法其实和Response中的是相同的,需要合并成一个
    def __newInstance(self, name, value):
        properties = self._getProperties()
        if not properties.has_key(name):
            raise Exception("没有找到 %s 的属性信息" % name)
        property = properties[name]
        theType = property[0]
        theConstructor = self.__getPropertyConstructor(theType)
        theLevel = property[1]
        isArray = "Array" in theLevel

        # 为了解决返回结果的list是None的问题
        if not value:
            if isArray:
                return list()
            else:
                return value
        if theConstructor == bool:
            # TODO 为什么要取第一个元素:[0],还是坑爹的淘宝API阿,返回格式太奇怪了,比如taobao.users.get下的response中的users属性
            return isArray and [x for x in value[value.keys()[0]]] or value
        if theConstructor == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            return isArray and \
                [datetime.strptime(x, format) for x in value[value.keys()[0]]] \
                or datetime.strptime(value, format)
        if theConstructor == str:
            if isArray:
                return [x for x in value[value.keys()[0]]]
            else:
                # TODO 这里TAOBAO API的元数据有bug,有些对象明明是Array,但元数据中表情的level却是String
                return not isinstance(value, basestring) and \
                    JSONLib.encode(value) or value
        else:
            pass



    def __getPropertyConstructor(self, theType):
        if theType == "Number":
            return int
        if theType == "String":
            return str
        if theType == "Boolean":
            return bool
        if theType == "Date":
            return datetime
        if theType == "Field List":
            return str
        if theType == "Price":
            return float
        if theType == "byte[]":
            return str
        else:
            print sys.modules
            return None

    def __initKargs(self):
        '''
        初始化__init__()中的kargs参数,将它们动态赋值到本对象中
        '''
        for key, value in self.__kargs.iteritem():
            setattr(self, key, value)

    def _getProperties(self):
        '''
        得到每一个属性的类型和level信息.在这里,这个方法其实是一个抽象参数,需要在Domain下的各个基类中去实现
        '''
        pass