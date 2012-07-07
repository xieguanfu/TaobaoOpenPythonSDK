#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 7, 2012 11:09:53 AM
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

import os
import sys
import shutil
import xml.dom.minidom

MAJOR_VERSION = "0.1"
MINOR_VERSION = "0"

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__),
        os.path.pardir))

__libraryPath = os.path.normpath(
    os.path.join(__getCurrentPath(), os.path.pardir, "libs", 'pytoolkit.zip'))
if not os.path.exists(__libraryPath):
    raise Exception("%s 不存在, 请检查" % __libraryPath)

if __libraryPath not in sys.path:
    sys.path.insert(0, __libraryPath)

__projectPath = os.path.normpath(
    os.path.join(__getCurrentPath(), os.path.pardir))
if __projectPath not in sys.path:
    sys.path.insert(0, __projectPath)

try:
    from ArgumentParser import ArgumentParser
    from Colorful import *
    from MetaDataParser import *
    from MetaDataParser.Settings import *
except ImportError:
    raise ImportError("你的 %s 可能有问题,不能被正确导入" % __libraryPath)

def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("--metadata",
        type=str,
        dest='metadata',
        help="淘宝SDK API 元数据的路径",
        required=True)

    parser.add_argument("--output",
        type=str,
        dest="output",
        help="输出文件的路径",
        required=True)

    parser.add_argument("--enableDoxygen",
        action="store_true",
        default=False,
        help="生成的代码中包含doxygen风格的注释, 默认:False",
        dest="enableDoxygen")

    parser.add_argument("--version",
        action="store_true",
        default=False,
        dest="version")

    argument = parser.parse_args()


    try:
        from mercurial import ui, hg
        MINOR_VERSION = hg.repository(ui.ui(), '.').changelog.headrevs()[0]
    except Exception:
        pass
    if argument.version:
        printColorful("green", "TaobaoOpenPythonSDK Version: %s.%s" % (
            MAJOR_VERSION, MINOR_VERSION))
        sys.exit(0)
    else:
        argument.version = "%s.%s" % (MAJOR_VERSION, MINOR_VERSION)

    if not os.path.exists(argument.metadata):
        printColorful("red", "%s 不存在" % argument.metadata)
        sys.exit(1)

    if not os.path.exists(argument.output):
        try:
            os.makedirs(argument.output)
        except Exception:
            raise Exception("没有mkdir %s的权限" % argument.output)

    return argument

if __name__ == '__main__':
    argument = parseArguments()

    root = None
    try:
        root = xml.dom.minidom.parse(argument.metadata)
    except Exception:
        raise Exception("解析元数据 %s时出错,可能你的元数据格式方面有问题" % argument.metadata)

    domainParser = DomainParser(root, argument)
    domainParser.generateFiles()
    #requestParser = RequestParser(root, argument.output)
    #requestParser.generateFiles()
    #responseParser = ResponseParser(root, argument.output)
    #responseParser.generateFiles()
    #commonParser = SdkCommonParser(root, argument.output)
    #commonParser.generateFiles()
    #shutil.copy(errorResponseTemplate, os.path.join(argument.output, "Response", 
        #errorResponseOutput))
