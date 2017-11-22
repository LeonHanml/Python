#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8

#导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread


#读取一个txt文件

text = open('test.txt','r').read()

#读入背景图片

bg_pic = imread('3.png')

#生成词云

wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(text)

image_colors = ImageColorGenerator(bg_pic)
#显示词云图片

plt.imshow(wordcloud)
plt.axis('off')
plt.show()


#保存图片

wordcloud.to_file('test.jpg')