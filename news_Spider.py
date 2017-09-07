# !/usr/bin/env python
# coding=utf8

__version__ = 'v1.0'

import re
from lxml import etree
import json

class Spider():

    def __init__(self):
        self.container_net = []

    def xpather_net(self, content):
        selector = etree.HTML(content)
        res_list = selector.xpath('')

    def re_json(self, content):
        '''网易那边反回来的数据正则拿出所有json并格式化然后取值'''
        pattern = re.compile('{.*?"title".*?"bendi".*?}', re.S)
        res = re.findall(pattern, content)
        for each in res:
            eachjson = json.loads(each)
            eachinfo = '标题:%s^发布时间:%s^链接:%s' % (eachjson['title'], eachjson['time'], eachjson['docurl'])
            self.container_net.append(eachinfo)
        return self.container_net