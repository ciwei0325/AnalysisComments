# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:31:50 2019

@author: ASUS
"""

import csv#导入处理CSV文件的库
csv_file=csv.reader(open("C:\\Users\\ASUS\\Desktop\\美团爬取\\4-comments\\3.4 comment0.csv","r"))#读取CSV文件
print(csv_file)#打印读取的CSV文件内容
f=open("C:\\Users\\ASUS\\Desktop\\lowstar9.txt","w")#打开目标TXT文件
for stu in csv_file:#逐行读取CSV文件中的评论列
    f.write(stu[2])#将读取内容写入TXT文件中
f.close()#关闭TXT文件
