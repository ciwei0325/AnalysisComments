import jieba
import wordcloud
#from scipy.misc import imread
#jieba.load_userdict("C:/Users/ASUS/Desktop/add_word.txt")


jieba.load_userdict("F:/generatewordcloud/dict.txt")
with open("F:/3.611.txt","r",encoding="utf-8") as f:
    str_text=f.read()
words = jieba.cut(str_text, cut_all=False)






stopwords = [line.strip() for line in open("F:/generatewordcloud/stopword.txt", 'r', encoding='utf-8').readlines()]


stayed_line = ""
for word in words:
    if word not in stopwords:
        if word !='\t':
            stayed_line += word + " "




#mask = imread("cat.png")
ls = jieba.lcut(stayed_line)
txt = " ".join(ls)
print(txt)

w = wordcloud.WordCloud(font_path="msyh.ttc",max_words=30,collocations=False,width=1000, height=700, background_color="white",)
w.generate(txt)
w.to_file("F:/3.61.png")
