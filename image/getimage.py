#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 16:23
# @Author  : 张瑞
# @Site    : 
# @File    : getimage.py
# @Software: PyCharm
import requests
url = 'http://xk1.ahu.cn/CheckCode.aspx'
for i in range(20):
    vcode = requests.get(url)
    with open('code{}.jpg'.format(i), 'wb') as v:
        v.write(vcode.content)