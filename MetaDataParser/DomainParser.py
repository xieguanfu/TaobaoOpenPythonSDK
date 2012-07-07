#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 12:05:40 AM Jun 5, 2012
@contact: wuliang@maimiaotech.com 
@version: 0.0.0
@deprecated:
@license:
@copyright:

用于解析templates/domain.mako,以生成针对domain下的数据结构
"""

from Common import *
from Settings import *

class DomainParser(object):
    def __init__(self, root, config):
        self.root = root
        self.config = config
        
    def generateFiles(self):
        rootOutput = os.path.join(self.config.output, domainOutput)
        if not os.path.exists(rootOutput):
            os.makedirs(rootOutput)
        imported = set()
        templateFileHandler = open(domainTemplate)

        templateFile = Template(templateFileHandler.read().decode("utf-8"))
        for struct in self.root.getElementsByTagName("struct"):
            rendered = templateFile.render_unicode(
                struct=struct, config=self.config).encode("utf-8")
            rendered = rendered.replace("\\#\\#", "##")
            filename = struct.getElementsByTagName("name")[0].firstChild.data.encode("utf-8")
            imported.add(filename)
            filename += ".py"
            filename = os.path.join(rootOutput, filename)
            printColorful("green", "Generating %s" % (filename))
            fout = open(filename, "w")
            fout.write(rendered)
            fout.close()
        templateFileHandler.close()

        # 生成Domain下的__init__.py文件
        templateFile = Template(open(initTemplate).read().decode("utf-8"))
        rendered = templateFile.render_unicode(imports=imported).encode("utf-8")
        fout = file(os.path.join(rootOutput, "__init__.py"), "w")
        fout.write(rendered)
        fout.close()

