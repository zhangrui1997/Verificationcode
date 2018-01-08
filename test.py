#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 16:23
# @Author  : 张瑞
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from PIL import Image
import pytesser3
import VectorProcess

im = Image.open("image/code1.jpg")
# im = Image.open("captcha.gif")
his = im.histogram()
values = {}
for i in range(0, 256):
    values[i] = his[i]
# 排序，x:x[1]是按照括号内第二个字段进行排序,x:x[0]是按照第一个字段
temp = sorted(values.items(), key=lambda x: x[1], reverse=True)
# print(temp)

# 将占比最多的10个颜色筛选出来
# 占比最多的10种颜色
# for j, k in temp[:10]:
#     print(j, k)

# 2.构造新的无杂质图片
# 生成一张白底啥都没有的图片
# 获取图片大小，生成一张白底255的图片
im2 = Image.new("P", im.size, 255)
# print(im2.size[1])
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
# 生成了一张黑白二值照片
# im2.show()

# 3.切割图片
# x代表图片的宽，y代表图片的高 对图片进行纵向切割
# 纵向切割
# 找到切割的起始和结束的横坐标
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

'''
count = 0
for letter in letters:
    # (切割的起始横坐标，起始纵坐标，切割的宽度，切割的高度)
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    # 更改成用时间命名
    im3.save("%s.gif" % count)
    count += 1
# 可以看到保存下来的6个字段'''

# 转换验证码图片为向量：
d1 = VectorProcess.buildvector(im)