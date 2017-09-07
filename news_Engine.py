# !/usr/bin/env python
# coding=utf8
__version__ = '1.0'

import time
from newsForCD.news_Setting import URL_NET
from newsForCD.news_Crawl import Crawl
from newsForCD.news_Spider import Spider
from newsForCD.news_Pipeline import Pipeline
from newsForCD.news_Setting import PATH_NET
import time
import json
import re


class Engine():

    def __init__(self):
        self.crwal = Crawl()
        self.spider = Spider()
        self.pipeline = Pipeline()



    def enginer(self):
        n = 1
        while n < 10:
            net_js = 'http://sc.news.163.com/special/04268EVT/xinxiliu.js'
            if n >= 2:
                net_js = 'http://sc.news.163.com/special/04268EVT/xinxiliu_0%s.js' % n
            '''网易新闻的js链接，数据从这返回，目前参数有两个，初步判定一个为固定参数，另一个为类似时间戳'''
            nowtime = int(time.time()*1000)
            params = {'callback': 'data_callback', '_': nowtime}
            pagecode = 'gbk'
            content = self.crwal.page_net(net_js, params)
            container = self.spider.re_json(content)
            self.pipeline.run(container, PATH_NET)
            n += 1
            time.sleep(2)

    def run(self):
        self.enginer()


if __name__ == '__main__':
    i = Engine()
    i.run()