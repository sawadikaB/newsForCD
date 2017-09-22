# !/usr/bin/env python
# coding:utf8

import time

class Tool4News():
	'''各种工具'''
	def __init__(self):
		pass

	def time_timestamp(self, nt):
		'''
		:param time: 时间参数
		:return: timestamp 返回一个
		时间戳
		'''
		pattern = [
			'%Y-%m-%d %H:%M:%S',
			'%Y/%m/%d %H:%M:%S',
			'%Y-%m-%d %H:%M',
			'%Y/%m/%d %H:%M',
			'%m-%d-%Y %H:%M:%S',
			'%m-%d-%Y %H:%M',
			'%m/%d/%Y %H:%M:%S',
			'%m/%d/%Y %H:%M',
		]
		for each in pattern:
			try:
				timepat = time.strptime(nt, each)
				break
			except Exception:
				timepat = False
				continue
		res = time.mktime(timepat) if timepat else 'no_data'
		return res

	def nowtime(self):
		'''当前时间'''
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

	def nowtimestamp(self):
		'''当前时间戳'''
		return time.time()