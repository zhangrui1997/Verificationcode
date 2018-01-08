#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 19:15
# @Author  : 张瑞
# @Site    :
# @File    : treateimage.py
# @Software: PyCharm

from PIL import Image
import os
from image import getimage
import time
count = 0
def getimgpath():
    """
    获取训练图片的路径
    :return: 路径列表
    """
    imgpath = []
    for img in os.listdir('../image/'):
        if img.endswith('.jpg'):
            thispath = '../image/'+img
            imgpath.append(thispath)
    return imgpath


def rgb2binary(imgpath):
    """
     将验证码图片二值化
    """
    # 读取图片
    im = Image.open(imgpath)
    # 获取图片大小，生成一张白底255的图片
    im2 = Image.new("P", im.size, 255)
    for y in range(im.size[1]):
        # 获得y坐标
        for x in range(im.size[0]):

            # 获得坐标(x,y)的RGB值
            pix = im.getpixel((x, y))

            # 这些是要得到的数字
            # 220灰色，227红色
            if pix == 43:
                # if pix == 220 or pix == 227:
                # 将黑色0填充到im2中
                im2.putpixel((x, y), 0)
    return im2


def cutimg(im2):
    """
    切割图片
    x代表图片的宽，y代表图片的高 对图片进行纵向切割
    纵向切割
    找到切割的起始和结束的横坐标
    """
    inletter = False
    foundletter = False
    start = 0
    end = 0
    letters = []
    for x in range(im2.size[0]):
        for y in range(im2.size[1]):
            pix = im2.getpixel((x, y))
            if pix != 255:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = x

        if foundletter == True and inletter == False:
            foundletter = False
            end = x
            letters.append((start, end))

        inletter = False
    return letters


def saveimg(letters, im2):
    global count
    for letter in letters:
        # (切割的起始横坐标，起始纵坐标，切割的宽度，切割的高度)
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
        # 更改成用时间命名
        im3.save("%s.png" % (time.strftime('%Y%m%d%H%M%S', time.localtime())))
        count += 1
    # 可以看到保存下来的4个字段
    return


def buildvector(im):
    """
    将图片转换为矢量
    :param im: 图片
    :return: 每个点的像素值
    形如{0: 255, 1: 255, 2: 255, 3: 255, 4: 255, 5: 255, 6: 255...}的字典
    """
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


def main():
    getimage.getimg()
    imgpath = getimgpath()
    for img in imgpath:
        # 二值化
        binaryimg = rgb2binary(img)
        letters = cutimg(binaryimg)
        if len(letters) == 4:
            saveimg(letters, binaryimg)

if __name__ ==  '__main__':
    main()





