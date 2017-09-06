# !/usr/bin/env python
# coding=utf8

__version__ = 'v1.0'

import re
from lxml import etree

class Spider():

    def __init__(self):
        pass

    def xpather_net(self, content):
        selector = etree.HTML(content)
         = selector.xpath('')

