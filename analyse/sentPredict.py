# -*- coding: utf-8 -*-

# Import the necessary modules
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

# 导入字典
with open('F:/word_dict.pk', 'rb') as f:
    word_dictionary = pickle.load(f)
with open('F:/label_dict.pk', 'rb') as f:
    output_dictionary = pickle.load(f)
df = pd.read_csv('F:/comment1.csv')
commentlist=list(df['comment'].unique())
starlist=list(df['star'])

# 加载模型
model_save_path = 'F:/corpus_model.h5'
lstm_model = load_model(model_save_path)
predict=[]
label=[]
highnum = lownum = 0
for m in range(len(commentlist)):
    if starlist[m] == 10 or starlist[m] == 50:
        try:
            # 数据预处理
            input_shape = 180
            x = [[word_dictionary[word] for word in (commentlist[m])]]
            x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)

            # 模型预测
            y_predict = lstm_model.predict(x)
            label_dict = {v: k for k, v in output_dictionary.items()}
            label_predict = label_dict[np.argmax(y_predict)]
            label_true = starlist[m]
            predict.append(label_predict)
            label.append(label_true)
            # 统计评分及情感分析为统一极值的数目方便对商家进行评价
            if starlist[m] == 50 and label_dict[np.argmax(y_predict)] == 50:
                highnum += 1
            if starlist[m] == 10 and label_dict[np.argmax(y_predict)] == 10:
                lownum += 1

            print('输入语句: %s' % commentlist[m])
            print('情感预测结果: %s' % label_dict[np.argmax(y_predict)])
            print('情感真实结果: %s' % label_true)

        except KeyError as err:
            print("您输入的句子有汉字不在词汇表中，请重新输入")
            print("不在词汇表中的单词为：%s." % err)

acc = accuracy_score(predict, label)  # 预测准确率
print('模型在测试集上的准确率为: %s.' % acc)
high = highnum / len(commentlist)
print('该店5分评价综合比例：%s ' % high)
low = lownum / len(commentlist)
print('该店1分评价综合比例：%s' % low)

