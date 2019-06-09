# -*- coding: utf-8 -*-
#爬取日韩料理排行榜页面店铺id等
import xlrd
import xlwt  #对Excel文件进行操作
import json
import requests
from xlutils.copy import copy

workbook = xlwt.Workbook()#新建文件
workbook.add_sheet('日料')#增加sheet 日料
workbook.save('日料.xls')
list_ = ['商铺', 'ID', '分数', '地址']
for i in range(0, 4):
    workbook = xlrd.open_workbook('日料.xls', encoding_override='utf-8')
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    row_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    new_worksheet.write(0, i, list_[i])#按顺序在表中写入数据
    new_workbook.save('日料.xls')

headers = {"Origin": "https://wh.meituan.com",
           "Referer": "https://wh.meituan.com/s/riliao/",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
for number in range(0, 32):
    print('正在请求第{}页'.format(number + 1))
    response = requests.get(
        'https://apimobile.meituan.com/group/v4/poi/pcsearch/57?uuid=6ef1a63594a645c3ab1b.1558777681.1.0.0&userid=-1&limit=32&offset={}&cateId=-1&q=%E6%97%A5%E6%96%99&sort=rating'.format(
            number * 32),
        headers=headers)
    ret = json.loads(response.content.decode())
#将从网页爬取信息写入xls文件
    for id_ in ret['data']['searchResult']:
        print('正在写入:', id_['title'], '------', id_['id'], '------', id_['avgscore'], '------', id_['address'])
        workbook = xlrd.open_workbook('日料.xls', encoding_override='utf-8')
        sheets = workbook.sheet_names()
        worksheet = workbook.sheet_by_name(sheets[0])
        row_old = worksheet.nrows
        new_workbook = copy(workbook)
        new_worksheet = new_workbook.get_sheet(0)
        new_worksheet.write(row_old, 0, id_['title'])#店铺名称
        new_worksheet.write(row_old, 1, id_['id'])#店铺ID
        new_worksheet.write(row_old, 2, id_['avgscore'])#店铺评分
        new_worksheet.write(row_old, 3, id_['address'])#店铺地址
        new_workbook.save('日料.xls')
