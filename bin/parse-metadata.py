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

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
sys.path.insert(0, os.path.join(__getCurrentPath(), os.path.pardir, "libs", 'pytoolkit.zip'))
sys.path.insert(0, os.path.join(__getCurrentPath(), os.path.pardir))

from ArgumentParser import ArgumentParser
from Colorful import *
from MetaDataParser import *
from MetaDataParser.Settings import *

MAJOR_VERSION = "0.1"
MINOR_VERSION = "0"
try:
    from mercurial import ui, hg
    MINOR_VERSION = hg.repository(ui.ui(), '.').changelog.headrevs()[0]
except Exception:
    pass

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--metadata", type=str, dest='metadata', 
        required=True)
    parser.add_argument("--output", type=str, dest="output", required=True)
    parser.add_argument("--enableDoxygen", action="store_true", default=False,
        dest="enableDoxygen")
    parser.add_argument("--version", action="store_true", default=False,
        dest="version")
    argument = parser.parse_args()
    argument.version = "%s.%s" % (MAJOR_VERSION, MINOR_VERSION)

    if argument.version:
        printColorful("blue", "Version: %s" % argument.version)
        sys.exit(1)

    if not os.path.exists(argument.metadata):
        printColorful("red", "%s 不存在" % argument.metadata)
        sys.exit(1)
        
    if not os.path.exists(argument.output):
        os.makedirs(argument.output)
    
    root = xml.dom.minidom.parse(argument.metadata)
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
