# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:58:11 2019

@author: ASUS
"""

import jieba
import wordcloud
with open("C:\\Users\\ASUS\\Desktop\\allcommenttxt.txt","r",encoding="gb18030") as f:
    str_text=f.read()
stopwords = [line.strip() for line in open("C:\\Users\\ASUS\\Desktop\\stopword.txt", 'r', encoding='utf-8').readlines()]

words = jieba.cut(str_text, cut_all = False)
stayed_line = ""
for word in words:
    if word not in stopwords:
        stayed_line += word + " "

ls = jieba.lcut(stayed_line)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc",max_words=50,collocations=False,width=500, height=350, background_color="white",)
w.generate(txt)
w.to_file("all.png")
