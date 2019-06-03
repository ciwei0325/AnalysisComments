# -*- coding: utf-8 -*-
import jieba
import wordcloud
#from scipy.misc import imread
#jieba.load_userdict("C:/Users/ASUS/Desktop/add_word.txt")


jieba.load_userdict("add_word.txt")#导入自定义添加的词典
# 打开要生成词云的文本
with open("test.txt","r",encoding="utf-8") as f:
    str_text=f.read()

#  读取停用词
stopwords = [line.strip() for line in open("F:/generatewordcloud/stopword.txt", 'r', encoding='utf-8').readlines()]

#  分词
words = jieba.cut(str_text, cut_all=False)

#  去掉停用词
stayed_line = ""
for word in words:
    if word not in stopwords:
        if word !='\t':
            stayed_line += word + " "

#  再分词及生成词云
ls = jieba.lcut(stayed_line)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc",max_words=30,collocations=False,width=1000, height=700, background_color="white",)
w.generate(txt)
w.to_file("F:/3.61.png")
