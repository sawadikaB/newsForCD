# !/usr/bin/env python
# coding=utf8

__version__ = 'v1.0' # 先写个网易的测试一下

import time
import requests
from newsForCD.news_Setting import HEADER_NET

class Crawl():

    def __init__(self):
        self.session = requests.Session()
        headers = HEADER_NET
        self.session.headers.update(headers)

    # 获取页面，private, 内部访问,设置重试5次
    def __get_content(self, url):
        retry = 5
        while retry > 0:
            res = self.session.get(url)
            # print(res.content)
            if res.status_code == 200 or res.status_code == 403 or res.status_code == 404:
                response = res.content.decode('gbk')
                break
            else:
                retry -= 1
                continue
            response = 'no_content'
        return response

    # 网易的
    def page_net(self, url):
        return self.__get_content(url)


