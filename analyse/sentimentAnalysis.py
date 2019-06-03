import jieba
import numpy as np
import pandas as pd
import joblib
import csv
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from gensim.models.word2vec import Word2Vec

#  读取参考评论集
neg=pd.read_csv('F:/此处为1星评论集',header=None,low_memory=False)
pos=pd.read_csv('F:/此处为5星评论集',header=None,low_memory=False)

#  分词
neg['words']=neg[0].apply(lambda x: jieba.lcut(x))
pos['words']=pos[0].apply(lambda x: jieba.lcut(x))

x=np.concatenate((pos['words'],neg['words']))
y=np.concatenate((np.ones(len(pos)),np.zeros(len(neg))))

#  构造向量空间
w2v=Word2Vec(size=300,min_count=10)
w2v.build_vocab(x)
w2v.train(x,total_examples=w2v.corpus_count,epochs=w2v.iter)
w2v.save('w2v_model.pkl')

#  获取一句话的向量
def total_vec(words):
    vec=np.zeros(300).reshape((1,300))
    for word in words:
        try:
            vec+=w2v.wv[word].reshape((1,300))
        except KeyError:
            continue
    return vec

#  获得结果向量空间
train_vec=np.concatenate([total_vec(words) for words in x])

#  初始化模型
model= SVC(kernel = 'rbf',verbose=True)
#  进行训练
model.fit(train_vec,y)
joblib.dump(model, "svm_model.pkl")
print("done\n")

#对店铺评论进行情感判断
def svm_predict():
    with open("F:/此处为要分析的店铺评论文件", 'r', encoding="gb18030") as csvfile:
        reader = csv.DictReader(csvfile)
        model = joblib.load('svm_model.pkl')
        comment_sentiment = []
        i = num = m = n = h = score = 0
        for row in reader:
            words = jieba.lcut(str(row['comment']))
            words_vec = total_vec(words)
            result = model.predict(words_vec)

            #  comment_sentiment.append('积极' if int(result[0]) else '消极')
            # 实时返回积极消极结果
            
            #  总数统计
            num = num+1
            score+=int(row['star'])
            # 实际积极情感
            if int(row['star'])==50 or int(row['star'])==40 :
                m=m+1
            # 实际消极情感
            if int(row['star'])==10:
                n=n+1
            # 预测积极情感
            if int(result[0]) == 1 :
                i=i+1
                print(row['comment'] + '积极' + row['star'])
                print('\n')
            # 预测消极情感
            elif int(result[0]) == 0:
                h=h+1
                print(row['comment']+'消极'+row['star'])
                print('\n')

    print('情感积极倾向是'+str(m/num))
    print('情感积极倾向预测是'+str(i/num))
    print('平均分是'+str(score/num/50))

svm_predict()