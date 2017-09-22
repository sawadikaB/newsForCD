# !/usr/bin/env python
# coding:utf-8

import os
from news_Tool import Tool4News
import time
class Pipeline():

    def __init__(self):
        self.__data_isdir()
        self.tool = Tool4News()

    def __data_isdir(self):
        if not os.path.exists(os.path.abspath('DATA')):
            os.mkdir(os.path.abspath('DATA'))

    def __save_text(self, savecontent, savepath, type):
        '''
        :param savecontent: 存储内容[list]
        :param savepath: 存储路径[string]
        :param type:写入方式
        :return:
        '''
        with open(os.path.join(os.path.abspath('DATA'), savepath), type, encoding='utf-8') as f:
            for each in savecontent:
                print(each)
                f.write(each)
                f.write('\n')

    # 读文本文件内容
    def read_text(self, path):
        return [each for each in open(os.path.join(os.path.abspath('DATA'), path), 'r', encoding='utf-8')]

    # 处理两个文件
    def dealfile(self):
        os.remove(os.path.join(os.path.abspath('DATA'), 'NEWS_NET.txt'))
        time.sleep(10)
        os.rename(os.path.join(os.path.abspath('DATA'), 'tempNews_NET.txt'), os.path.join(os.path.abspath('DATA'), 'NEWS_NET.txt'))
        pass

    def run(self, saveconetent, savepath, type='a'):
        '''测试时使用的'''
        self.__save_text(saveconetent, savepath, type)

