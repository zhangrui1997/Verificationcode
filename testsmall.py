
import os
from PIL import Image
import numpy
for img in os.listdir('iconset/k/'):
    if img is None:
        print('hahaha')
    im1 = Image.open(img)

# im1 = Image.open('code0.jpg')
# im2 = Image.open('code1.jpg')
# print(im2-im1)
# a=[1, -1, 2]
# b=[2, -3, 4]
# # print([abs(i-j) for i,j in a,b])
# a = numpy.array(a)
# b = numpy.array(b)
# print(a-b)