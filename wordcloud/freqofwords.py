# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:07:33 2019

@author: ASUS
"""

import jieba
f=open("C:/Users/ASUS/Desktop/ciyun/commenttxt1.txt",encoding="gbk")
str_text=f.read()
f.close()
words = jieba.cut(str_text, cut_all = False)
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x: x[1], reverse = True)
max_number = int(input(u"需要前多少位高频词？ "))
for word, freq in freq_word[: max_number]:
    print(word, freq)