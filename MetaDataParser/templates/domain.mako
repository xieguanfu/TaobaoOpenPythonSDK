#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:

<%
import os

def getElementValue(element, name):
    try:
        return element.getElementsByTagName(name)[0].firstChild.data.strip()
    except Exception:
        return None

imported = list()
description = getElementValue(struct, "desc")
if description:
    description = os.replace(os.linesep, str())
%>
'''
% if description
@brief description
% endif
@author ${config.author}
@date ${time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
@version: ${config.majorVersion}.${config.minorVersion}
'''

import os
import sys
import time
import types

__currentPath = os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
__projectPath = os.path.normpath(os.path.join(__currentPath, os.path.dirname))

if __currentPath not in sys.path:
    sys.path.insert(0, __currentPath)
if __projectPath not in sys.path:
    sys.path.insert(0, __projectPath)

## 导入所依赖的类
<%
properties = struct.getElementsByTagName("prop")
if properties != None:
    for property in properties:
        level = None
        dependencyType = None
        try:
            level = getElementValue(property, "level")
        except Exception:
            pass
        try:
            dependencyType = getElementValue(property, "type")
        except Exception:
            pass
        if level == None or level == "Basic" or level == "Basic Array":
            continue
        if dependencyType == None or dependencyType in imported:
            continue
        else:
            imported.append(dependencyType)
%>
from TaobaoObject import TaobaoObject
% for dependencyType in imported:
from ${dependencyType} import ${dependencyType}
% endfor

<%
def formatDoxygenString(**kargs):
    results = list()
    s = '''@%s <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">%s</SPAN>'''
    for key, value in kargs.iteritems():
        results.append(s % (key, value))
    return results
%>

% if config.enableDoxygen:
    % if description:
\#\# @brief ${description}
    % endif
% endif
<%
className = getElementValue(struct, "name") 
%>
class ${className}(TaobaoObject):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__(kargs)
        <%
        class NodeClass(object):
            def __init__(self):
                self.brief = None
                self.name = None
                self.addons = dict()
        nodes = list()
        for node in properties: 
            nodeObject = NodeClass()
            nodeObject.brief = getElementValue(node, "desc")
            nodeObject.addons['type'] = getElementValue(node, "type")
            nodeObject.addons['level'] = getElementValue(node, "level")
            nodeObject.addons['sample'] = getElementValue(node, "sample")
            nodeObject.addons['private'] = getElementValue(node, "private")
            nodeObject.name = getElementValue(node, "name")
            nodes.append(nodeObject)
        %>
        % for node in nodes:
        % if config.enableDoxygen:
        \#\#
        % if node.brief:
        # ${formatDoxygenString(brief=node.brief)}
        % endif
        # <UL>
        % for result in formatDoxygenString(**node.addons)
        # <LI>${result}</LI>
        % endfor
        # </UL>
        self.${node.name} = None
        % endfor
