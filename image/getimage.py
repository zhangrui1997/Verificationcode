#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 16:23
# @Author  : 张瑞
# @Site    : 
# @File    : getimage.py
# @Software: PyCharm
import requests
import time
def getimg():
    url = 'http://xk1.ahu.cn/CheckCode.aspx'
    for i in range(20):
        print('正在下载{}张验证码:'.format(i+1))
        vcode = requests.get(url)
        with open('../image/code{}.jpg'.format(i), 'wb') as v:
            v.write(vcode.content)
        time.sleep(1)