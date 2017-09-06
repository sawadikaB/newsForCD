# !/usr/bin/env python
# coding=utf8
__version__ = '1.0'

import time
from newsForCD.news_Setting import URL_NET
from newsForCD.news_Crawl import Crawl
from newsForCD.news_Spider import Spider


class Engine():

    def __init__(self):
        self.crwal = Crawl()
        self.spider = Spider()


    def enginer(self):
        content = self.crwal.page_net(URL_NET)
        self.spider.

    def run(self):
        self.enginer()

if __name__ == '__main__':
    i = Engine()
    i.run()