#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 17:05
# @Author  : 张瑞
# @Site    : 
# @File    : imagematrix.py
# @Software: PyCharm
from PIL import Image

im = Image.open('iconset/0/3.png')
for i in range(im.size[0]):
    for j in range(im.size[1]):
        pix = im.getpixel((i, j))
        # print(pix, end='---')
        print('%-3d  ' % pix, end='')
    print('')