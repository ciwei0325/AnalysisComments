# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:17:16 2019

@author: ASUS
"""

import jieba.add_word
f=open("C:/Users/ASUS/Desktop/ciyun/commenttxt1.txt",encoding="gbk")#打开文件读取评论，并以gbk方式解码
str_text=f.read()#读取文件
f.close()#关闭文件
str_jing2=jieba.cut(str_text,cut_all=False)#将句子进行精确的切分
print("before add_word:"+"/".join(str_jing2))#在未添加自定义词之前
jieba.add_word("")#添加自定义词
str_jing3=jieba.cut(str_text,cut_all=False)#将句子进行精确切分
print("after add_word:"+"/".join(str_jing3))#显示添加了自定义词后切分的句子
jieba.suggest_freq("",tune=True)#可调节单个词语的词频，使不被分出来。
str_jing4=jieba.cut(str_text,cut_all=False)#经过调整词典后的结果
print("after suggest_frep:"+"/".join(str_jing4))
