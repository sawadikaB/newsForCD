# !/usr/bin/env python
# coding:utf-8

import os
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
        with open(os.path.join(os.path.abspath('DATA'), savepath), 'w') as f:
            for each in savecontent:
                f.write(each)
                f.write('\n')

    def run(self, saveconetent, savepath):
        self.__save_text(saveconetent, savepath)

