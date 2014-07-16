#encoding=utf8
"""doc string for module"""
__author__ = 'lym liyangmin@maimiaotech.com'

import sys
import logging
import traceback
import inspect

from time import  sleep
from datetime import datetime
from Exceptions.SDKRetryException import SDKRetryException
import simplejson as json

from TaobaoSdk.Exceptions import ErrorResponseException
from Exceptions.HttpStatusException import HttpStatusException

logger = logging.getLogger(__name__)

def sdk_exception(MAX_RETRY_TIMES = 20):
    def _wrapper_func(func,*args,**kwargs):

        def __wrapped_func(*args, **kwargs):
            retry_times = 0
            res = None
            while True:
                try:
                    res =  func(*args, **kwargs)
                except (ImportError,ValueError,HttpStatusException),e:
                    if retry_times == MAX_RETRY_TIMES:
                        logger.error('SDK ERROR,retry %s times,but still failed'%MAX_RETRY_TIMES)
                        raise SDKRetryException
                    retry_times += 1
                    continue
                except Exception,e:
                    logger.exception('sdk error:%s'%e)
                    raise e
                else:
                    if retry_times:
                        logger.info("retry success, total_retry time:%i"%retry_times)
                    return res
        return __wrapped_func

    return _wrapper_func




