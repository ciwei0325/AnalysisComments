# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:08:11 2019

@author: ASUS
"""

import jieba.analyse
import math
f=open("C:/Users/ASUS/Desktop/ciyun/commenttxt1.txt",encoding="gbk")#打开需处理的文件
str_text=f.read()#读取文件
f.close()#关闭文件
keywords1=jieba.analyse.extract_tags(str_text)#关键词提取
print("关键词提取"+"/".join(keywords1))
keywords_top=jieba.analyse.extract_tags(str_text,topK=3)#返回关键词的数量，重要性从高到低排序
print('关键词topk'+"/".join(keywords_top))
print('总词数{}'.format(len(list(jieba.cut(str_text)))))#文件中的总词数
total=len(list(jieba.cut(str_text)))
get_cnt=math.ceil(total*0.1)  #向上取整
print('从%d 中取出%d 个词'% (total,get_cnt))
keywords_top1=jieba.analyse.extract_tags(str_text,topK=get_cnt)
print('关键词topk'+"/".join(keywords_top1))
