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
    def __get_content(self, url, params, pagecode):
        retry = 5
        while retry > 0:
            res = self.session.get(url, params=params)
            # print(res.headers)
            if res.status_code == 200 or res.status_code == 403 or res.status_code == 404:
                response = res.content.decode(pagecode)
                break
            else:
                retry -= 1
                continue
            response = 'no_content'
        return response

    def __post_content(self, url, data):
        pass

    def __get_likejson(self, url, params):
        retry = 5
        while retry > 0:
            res = self.session.get(url, params=params)
            if res.status_code == 200 or res.status_code == 403 or res.status_code == 404:
                response = res.text
                break
            else:
                retry -= 1
                continue
            response = 'no_data'
        return response


    # 网易的
    def page_net(self, url, params=None):
        return self.__get_likejson(url, params)



