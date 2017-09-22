# !/usr/bin/env python
# coding=utf8
__version__ = '1.0'

import time
from news_Setting import URL_NET
from news_Crawl import Crawl
from news_Spider import Spider
from news_Pipeline import Pipeline
from news_Setting import PATH_NET
import time
import json
import re



class Engine():

    def __init__(self):
        self.crwal = Crawl()
        self.spider = Spider()
        self.pipeline = Pipeline()



    def enginer(self):
        '''实现每个小时抓取一次'''
        while True:
            net_js = 'http://sc.news.163.com/special/04268EVT/xinxiliu.js'
            '''网易新闻的js链接，数据从这返回，目前参数有两个，初步判定一个为固定参数，另一个为类似时间戳'''
            nowtime = int(time.time()*1000)
            params = {'callback': 'data_callback', '_': nowtime}
            content = self.crwal.page_net(net_js, params)
            container = self.spider.re_json(content)
            self.pipeline.run(container, 'News_NET.txt')
            time.sleep(3600)

    # 数据入库
    def insertData(self):
        '''tempNews_NET.txt
            News_NET.txt
        '''
        oldlist = []
        newlist = []
        old = self.pipeline.read_text('News_NET.txt')
        new = self.pipeline.read_text('tempNews_NET.txt')
        for each in old:
            oldlist.append(each.split('^')[2])

        for each in new:
            if each.split('^')[2] > min(oldlist):
                newlist.append(each.strip())
            else:
                print('已入库')
        self.pipeline.run(newlist, 'test.txt', 'a')
        # self.pipeline.dealfile(delfile, crefile) 处理新旧文件



    def enginer_database(self):
        '''第一次使用的抓原始数据的脚本，包含翻页，现停止使用，采取每小时更新方式'''
        n = 1
        while n < 10:
            net_js = 'http://sc.news.163.com/special/04268EVT/xinxiliu.js'
            if n >= 2:
                net_js = 'http://sc.news.163.com/special/04268EVT/xinxiliu_0%s.js' % n
            '''网易新闻的js链接，数据从这返回，目前参数有两个，初步判定一个为固定参数，另一个为类似时间戳'''
            nowtime = int(time.time() * 1000)
            params = {'callback': 'data_callback', '_': nowtime}
            pagecode = 'gbk'
            content = self.crwal.page_net(net_js, params)
            container = self.spider.re_json(content)
            self.pipeline.run(container[-1:], './NET.log')
            self.pipeline.run(container[:-1], PATH_NET)
            n += 1
            time.sleep(2)

    def run(self):
        self.insertData()


if __name__ == '__main__':
    i = Engine()
    i.run()