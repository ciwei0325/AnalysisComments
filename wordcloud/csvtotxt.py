# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:31:50 2019

@author: ASUS
"""

import csv
csv_file=csv.reader(open("C:\\Users\\ASUS\\Desktop\\美团爬取\\4-comments\\3.4 comment0.csv","r"))
print(csv_file)
f=open("C:\\Users\\ASUS\\Desktop\\lowstar9.txt","w")
for stu in csv_file:
    f.write(stu[2])
f.close()