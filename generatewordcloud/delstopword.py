# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:10:05 2019

@author: ASUS
"""

import jieba
with open("C:/Users/ASUS/Desktop/commenttext.txt","r",encoding="gb18030") as f:#打开需要去除停用词的文件
    str_text=f.read()
stopwords = [line.strip() for line in open("C:\\Users\\ASUS\\Desktop\\stopword.txt", 'r', encoding='utf-8').readlines()]#逐行读取停用词文件得到停用词并将其去除两端空格放入列表
words = jieba.cut(str_text, cut_all = False)#对文本内容进行精确切分
stayed_line = ""
for word in words:#对于文本中的单词，若不属于停用词则保留在stayed_line字符串中
    if word not in stopwords:
        stayed_line += word + " "
print(stayed_line)#打印去除停用词后的文本
