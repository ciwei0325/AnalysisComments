# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:31:03 2019

@author: ASUS
"""

import jieba
jieba.load_userdict("C:/Users/ASUS/Desktop/add_word.txt")#打开文件添加单词
f=open("C:/Users/ASUS/Desktop/ciyun/commenttxt1.txt",encoding="gbk")#打开需要处理的文本文件
str_text=f.read()#读取文件
f.close()#关闭文件
str_load=jieba.cut(str_text,cut_all=False)#对文件进行精确切分
print("after load_userdict:"+"/".join(str_load))#显示精确切分后的文件
