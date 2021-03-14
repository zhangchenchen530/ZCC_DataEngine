# -*- coding:utf-8 -*-
# 词云展示
from wordcloud import WordCloud
import pandas as pd
import os
import matplotlib.pyplot as plt
%matplotlib inline
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize

# 去掉停用词
def remove_stop_words(f):
	stop_words = ['']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=10, #最高频10个
		width=2000,
		height=1200,)
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# 数据加载
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
# csv转存txt文件
with open('new_data.txt','a+', encoding='utf-8') as f:
    for line in dataset.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\n'))
# 打开文件，读取字符串，转成字符格式
fn = open('new_data.txt','r',encoding='utf-8')
string_data = fn.read()
#print(string_data)
# 生成词云
create_word_cloud(string_data)
