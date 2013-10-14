#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 8:31:46 PM Jun 6, 2012
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")

from Common import *
from Response import *
from SdkCommon import *
from decorator import sdk_exception
import logging
logger = logging.getLogger(__name__)
def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

if __getCurrentPath() not in sys.path:
    sys.path.insert(0, __getCurrentPath())

 
#{"simba_rpt_custbase_get_response":{"rpt_cust_base_list":{"code":15,./app/actions/rpt_service/rpt_cust_base_v2.lua:19: error}}}                                                 
def normalize_rawconent(rawContent):
    key_infos = ["""./app/common/common.lua""", """./app/actions/rpt_service/rpt_cust_base_v2.lua"""]
    for key_info in key_infos:
        if key_info in rawContent:
            start = rawContent.find(key_info)
            end = rawContent[start:].find("error") + len("error")
            sick_info = rawContent[start:start+end]
            norm_info = '''"msg":"null","sub_code":"isp.service-unavailable","sub_msg":"maimiao defined"'''
            rawContent = rawContent.replace(sick_info, norm_info)
    return rawContent

class TaobaoClient(object):
    def __init__(self, serverUrl, appKey, appSecret, timeout=180):
        self.serverUrl = serverUrl
        self.appKey = appKey
        self.appSecret = appSecret
        # TODO 目前暂时只支持JSON格式
        self.format = 'json'
        self.signMethod = "md5"
        self.timeout = timeout
        
    @sdk_exception(20)
    def execute(self, request, session=None):
        '''
        执行请求
        @param request: 需要发送的请求,必须是Request下的对象
        @type request: 必须时Request下的对象
        @return: 得到的响应,必然是Reponse下的对象;除非访问时出错了
        @rtype: tuple(response1, response2, ...)
        '''
        sign = self.buildSign(request, session)
        sign = sign.upper()
        # 参数
        # TODO 和原始的Java SDK相比，这里缺少session的传入
        parameters = {
            'sign': sign,
            'format': self.format,
            'app_key': self.appKey,
            'sign_method': self.signMethod,
            'v': '2.0',
            'partner_id': 'top-sdk-java-%s' % SdkVersion,
        }
        parameters.update(self.getRequestParameters(request))
        if session != None:
            parameters["session"] = session
        #print self.serverUrl + "?" + '&'.join("%s=%s" % (x, urllib2.quote(parameters[x])) for x in parameters.keys())
        client = httplib2.Http(timeout=self.timeout)
        headers = {
           'Content-type': 'application/x-www-form-urlencoded',
           'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
           "Accept": "application/x-shockwave-flash, image/gif, image/jpeg, image/pjpeg, image/pjpeg, */*",
           "Accept-Language": "zh-cn",
           "Cache-Control": "no-cache",
           "Connection": "Keep-Alive",
        }
        responseStatus, rawContent = client.request(uri=self.serverUrl, method="POST", 
            body=urllib.urlencode(parameters), headers=headers)
        if responseStatus["status"] != '200':
            print >> sys.stderr, rawContent
            return None
        try:
            if ",," in rawContent:
                rawContent=rawContent.replace(",,",",")
            if """./app/common/common.lua""" in rawContent:
                rawContent=normalize_rawconent(rawContent)
            content = JSONLib.decode(rawContent)
        except Exception,e:
            file_object = open('/home/ops/TaobaoOpenPythonSDK/TaobaoSdk/error_api.txt','a')
            file_object.write('parameters:%s\nrawContent:%s\nEXCEPTION:%s\n---------'%(parameters,rawContent,e))
            file_object.close()
            raise e
        responses = list()
        try:
            for key, value in content.iteritems():
                key = str().join([x.capitalize() for x in key.split("_")])
                ResponseClass = getattr(sys.modules["TaobaoSdk.Response.%s" % key], key)
                response = ResponseClass(value)
                response.responseStatus = responseStatus
                response.responseBody = rawContent
                responses.append(response)
            return tuple(responses)
        except ValueError,e:
            if "does not match format '%Y-%m-%d %H:%M:%S'" in str(e):
                #时间转换
                while(re.search('[a-zA-Z\x80-\xff]+\d{3}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}',rawContent)):
                    match_obj = re.search('[a-zA-Z\x80-\xff]+\d{3}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}',rawContent)
                    match_obj2 = re.search('\D\d{3}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}',rawContent)
                    begin = match_obj.start()
                    end = match_obj2.start()+1
                    rawContent = rawContent[:begin] + '2'+ rawContent[end:]
                #重新生成response
                for key, value in content.iteritems():
                    key = str().join([x.capitalize() for x in key.split("_")])
                    ResponseClass = getattr(sys.modules["TaobaoSdk.Response.%s" % key], key)
                    response = ResponseClass(value)
                    response.responseStatus = responseStatus
                    response.responseBody = rawContent
                    responses.append(response)
                return tuple(responses)
            
        except Exception,e:
            file_object = open('/home/ops/TaobaoOpenPythonSDK/TaobaoSdk/error_api.txt','a')
            file_object.write('parameters:%s\nrawContent:%s\nEXCEPTION:%s\n--------->>>>>>>>>'%(parameters,rawContent,e))
            file_object.close()
            raise e
    
    def buildSign(self, request, session=None):
        '''
        对传入的request进行sign的计算. 
        sign的计算需要format, app_key, sign_method, v, partner_id, 
        appSecret以及request的参数共同拼装成一个字符串,然后
        '''
        parameters = {
            'format': self.format,
            'app_key': self.appKey,
            'sign_method': self.signMethod,
            'v': '2.0',
            'partner_id': 'top-sdk-java-%s' % SdkVersion,
        }
        parameters.update(self.getRequestParameters(request))
        if session != None:
            parameters["session"] = session
        keys = parameters.keys()
        keys.sort()
        query = "%s%s%s" % (self.appSecret,
            str().join('%s%s' % (key, parameters[key]) for key in keys), 
            self.appSecret)
        hash = hashlib.md5(query)
        return hash.hexdigest()
        
    def getRequestParameters(self, request):
        '''
        得到request中所需要进行
        '''
        parameters = dict()
        for key, value in request.__dict__.iteritems():
            if key == 'timestamp':
                value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))
            # TODO 不必须的参数是否需要参与hash的计算
            if value == None:
                continue
            parameters[key] = unicode(value)
        return parameters
            
