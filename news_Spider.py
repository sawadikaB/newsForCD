# !/usr/bin/env python
# coding=utf8

__version__ = 'v1.0'

import re
from lxml import etree
import json
from news_Tool import Tool4News

class Spider():

    def __init__(self):
        self.tool = Tool4News()

    def xpather_net(self, content):
        selector = etree.HTML(content)
        res_list = selector.xpath('')

    def re_json(self, content):
        '''网易那边反回来的数据正则拿出所有json并格式化然后取值
        该方法获取的是原始数据，现停用，改用net_get_news
        '''
        pattern = re.compile('{.*?"title".*?"bendi".*?}', re.S)
        res = re.findall(pattern, content)
        for each in res:
            eachjson = json.loads(each)
            eachinfo = '标题:%s^发布时间:%s^链接:%s' % (eachjson['title'], eachjson['time'], eachjson['docurl'])
            self.container_net.append(eachinfo)
        return self.container_net

    def net_get_news(self, content):
        '''获取最新的新闻（按照目前更新机制，为抓取时间一小时内的新闻）'''
        pattern = re.compile('{.*?"title".*?"bendi".*?}', re.S)
        res = re.findall(pattern, content)
        container_net = []
        for each in res:
            now = self.tool.nowtime()
            nowstamp = self.tool.nowtimestamp()
            eachjson = json.loads(each)
            pubtime = eachjson['time']
            pubtimestamp = self.tool.time_timestamp(pubtime)
            if nowstamp - pubtimestamp < 3600:
                eachinfo = '【%s】标题:%s^发布时间:%s^链接:%s' % (now, eachjson['title'], eachjson['time'], eachjson['docurl'])
                container_net.append(eachinfo)
        container_net.append(str(nowstamp))
        return container_net
