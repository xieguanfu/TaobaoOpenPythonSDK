#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:

<%
import os
import string

def formatDoxygenString(**kargs):
    '''
    为了让doxygen化的文档展示出pretty样式
    '''
    results = list()
    s = string.Template("@$key <SPAN style=\"font-size:16px; font-family:Serif,'Times New Roman',Georgia;\">$value</SPAN>")
    for key, value in kargs.iteritems():
        results.append(s.substitute(key=key, value=value))
    return results

def getElementValue(element, name):
    try:
        return element.getElementsByTagName(name)[0].firstChild.data.strip()
    except Exception:
        return None

# 接口的描述
description = getElementValue(struct, "desc")
if description:
    description = description.replace(os.linesep, str()).replace('\r', str())

# 类名
className = getElementValue(struct, "name").strip()

# 分析需要导入的类
imported = list()
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

'''
% if description:
@brief ${description}
% endif
'''

import os
import sys
import time
import types

__currentPath = os.path.normpath(os.path.realpath(
    os.path.join(os.path.realpath(__file__), os.path.pardir)))
__projectPath = os.path.normpath(os.path.realpath(
    os.path.join(__currentPath, os.path.pardir)))

if __currentPath not in sys.path:
    sys.path.insert(0, __currentPath)
if __projectPath not in sys.path:
    sys.path.insert(0, __projectPath)

from TaobaoObject import TaobaoObject
% for dependencyType in imported:
from ${dependencyType} import ${dependencyType}
% endfor

% if config.enableDoxygen:
    % if description:
\#\# @brief ${description}
    % endif
% endif
class ${className}(TaobaoObject):
    '''
    @brief: ${description}
    '''
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__(kargs)
        % for node in nodes:
        % if config.enableDoxygen:
        \#\#
        % if node.brief:
        # ${formatDoxygenString(brief=node.brief)[0]}
        % endif
        # <UL>
        % for result in formatDoxygenString(**node.addons):
        # <LI>${result}</LI>
        % endfor
        # </UL>
        % endif
        self.${node.name} = None
        '''
        @ivar: ${node.brief}
        @type: ${node.addons['type']}
        '''

        % endfor

    def _getProperties(self):
        '''
        @brief: 得到每一个属性的类型和level信息
        @return: 返回该对象的所有属性的类型和Level
        @todo: 这个方法最好还是别写在这里,domain下的对象应该都更类似数据结构,不适合有这些方法
        '''
        <%
        results = {}
        for node in nodes:
            results[node.name] = (node.addons['type'], node.addons['level'])
        %>
        return ${results}

