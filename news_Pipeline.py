# !/usr/bin/env python
# coding:utf-8

import os
from newsForCD.news_Setting import PATH_NET
class Pipeline():

    def __init__(self):
        self.__data_isdir()

    def __data_isdir(self):
        if not os.path.exists(os.path.abspath('DATA')):
            os.mkdir(os.path.abspath('DATA'))

    def __save_text(self, savecontent, savepath):
        '''
        :param savecontent: 存储内容[list]
        :param savepath: 存储路径[string]
        :return:
        '''
        pass

    def run(self):
        self.__save_text(PATH_NET)

if __name__ == '__main__':
    i = Pipeline()
    i.run()