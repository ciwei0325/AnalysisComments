# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:07:33 2019

@author: ASUS
"""

import jieba
f=open("C:/Users/ASUS/Desktop/ciyun/commenttxt1.txt",encoding="gbk")#打开需统计词频的文件
str_text=f.read()#读文件
f.close()#关闭文件
words = jieba.cut(str_text, cut_all = False)#对文本进行精确切分
word_freq = {}#将次数和单词保存入字典
for word in words:
    if word in word_freq:#若单词已出现在字典中则数量直接加1
        word_freq[word] += 1
    else:#否则将单词保存在字典中，并令数量等于1
        word_freq[word] = 1
freq_word = []
for word, freq in word_freq.items():#以列表返回可遍历的(键, 值) 元组数组
    freq_word.append((word, freq))
freq_word.sort(key = lambda x: x[1], reverse = True)#根据次数，降序排列
max_number = int(input(u"需要前多少位高频词？ "))
for word, freq in freq_word[: max_number]:#遍历列表，打印单词及词频
    print(word, freq)
