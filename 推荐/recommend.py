# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:15:24 2019

@author: ASUS
"""
import openpyxl
import random
lists=["韩国菜","韩式烤肉","居酒屋","日本菜","日料自助","日式快餐","日式面条","日式烧烤","日式寿司","日式铁板烧","日式小吃","其他美食"]
for i in lists:
    print("序号：%s  名称：%s"%(lists.index(i)+1,i))
num=eval(input("请选择您想品尝的美食种类！"))
workbook=openpyxl.load_workbook(lists[num-1]+".xlsx")
worksheet=workbook.worksheets[0]#读取第一个工作簿
flag=0
for row in worksheet.rows:
    i=random.randint(1,10)#产生随机数
    if i%2==0 or flag==0:#打印第一行，随机产生打印的行数
        for cell in row:
            print(cell.value,end=" ")#打印单元格
        print()