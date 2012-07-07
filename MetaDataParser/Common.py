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

import os
import sys
import warnings
warnings.filterwarnings("ignore")

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__),
        os.path.pardir))

__libraryPath = os.path.normpath(
    os.path.join(__getCurrentPath(), os.path.pardir, "libs", 'pytoolkit.zip'))
if not os.path.exists(__libraryPath):
    raise Exception("%s 不存在, 请检查" % __libraryPath)

from ArgumentParser import ArgumentParser
import chardet
from Colorful import *
import copy
import hashlib
import httplib2
import JSONLib
from mako.template import Template
import re
if float(sys.version[:3]) <= 2.4:
    from sets import Set as set
import shutil
import subprocess
import tarfile
import tempfile
import threading
import time
import urllib
import urllib2
import urlparse
import yaml
import xml.dom.minidom
