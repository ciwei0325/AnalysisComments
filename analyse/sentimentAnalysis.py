# -*- coding: utf-8 -*-

import pickle
import numpy as np
import pandas as pd
from keras.utils import np_utils, plot_model # 实现神经网络可视化
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences # 填充 实现文本预处理
from keras.layers import LSTM, Dense, Embedding, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score # 模型评估
from keras.models import load_model # 保存和加载模型
# graphviz安装不顺利，添加安装graphviz的路径
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Bell599/graphviz/bin'



# 导入数据
# 文件的数据中，特征为comment, 类别为star.
def load_data(filepath, input_shape=20):
    df = pd.read_csv(filepath)

    # 标签及词汇表
    labels, vocabulary = list(df['star'].unique()), list(df['comment'].unique())

    # 构造字符级的特征
    string = ''
    for word in vocabulary:
        string += word

    vocabulary = set(string)

    # 字典列表
    word_dictionary = {word: i+1 for i, word in enumerate(vocabulary)} # 列出可遍历的索引序列
    with open('F:/word_dict.pk', 'wb') as f:
        pickle.dump(word_dictionary, f) # 将序列化后的对象以二进制写入文件
    inverse_word_dictionary = {i+1: word for i, word in enumerate(vocabulary)} # 反向

    label_dictionary = {label: i for i, label in enumerate(labels)}
    with open('F:/label_dict.pk', 'wb') as f:
        pickle.dump(label_dictionary, f)
    output_dictionary = {i: labels for i, labels in enumerate(labels)}

    vocab_size = len(word_dictionary.keys()) # 词汇表大小
    label_size = len(label_dictionary.keys()) # 标签类别数量

    # 序列填充，按input_shape填充，长度不足的按0补充，预处理
    x = [[word_dictionary[word] for word in sent] for sent in df['comment']]
    x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)
    y = [[label_dictionary[sent]] for sent in df['star']]
    y = [np_utils.to_categorical(label, num_classes=label_size) for label in y] # 将类别向量转换为二进制（只有0和1）的矩阵类型表示
    y = np.array([list(_[0]) for _ in y])

    return x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary

# 创建深度学习模型
def create_LSTM(n_units, input_shape, output_dim, filepath):
    x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary = load_data(filepath)
    model = Sequential()
    # 使用add来堆叠模型
    # input_dim即字典长度=输入数据最大下标+1，output_dim为全连接嵌入的维度
    model.add(Embedding(input_dim=vocab_size + 1, output_dim=output_dim,
                        input_length=input_shape, mask_zero=True))
    model.add(LSTM(n_units, input_shape=(x.shape[0], x.shape[1])))
    model.add(Dropout(0.2)) # 每轮迭代时每五个输入值就会被随机抛弃一个。
    model.add(Dense(label_size, activation='softmax'))
    # 配置学习过程
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    plot_model(model, to_file='F:/model_lstm.png', show_shapes=True)
    model.summary()
    return model

# 模型训练
def model_train(input_shape, filepath, model_save_path):

    # 将数据集分为训练集和测试集比例为9:1

    x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary = load_data(filepath, input_shape)
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.1, random_state = 42)

    # 模型输入参数
    n_units = 100
    batch_size = 32 # 通常取2的n次方
    epochs = 5 # 一个epoch等于使用全部样本训练一次
    output_dim = 20

    # 模型训练
    lstm_model = create_LSTM(n_units, input_shape, output_dim, filepath)
    lstm_model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1)

    # 模型保存
    lstm_model.save(model_save_path)

    N = test_x.shape[0]  # 测试的条数
    predict = []
    label = []
    for start, end in zip(range(0, N, 1), range(1, N+1, 1)):
        sentence = [inverse_word_dictionary[i] for i in test_x[start] if i != 0]
        y_predict = lstm_model.predict(test_x[start:end])
        label_predict = output_dictionary[np.argmax(y_predict[0])]
        label_true = output_dictionary[np.argmax(test_y[start:end])]
        print(''.join(sentence), label_true, label_predict) # 输出预测结果
        predict.append(label_predict)
        label.append(label_true)

    acc = accuracy_score(predict, label) # 预测准确率
    print('模型在测试集上的准确率为: %s.' % acc)

if __name__ == '__main__':
    filepath = 'F:/hebing.csv'
    input_shape = 180
    model_save_path = 'F:/corpus_model.h5'
    model_train(input_shape, filepath, model_save_path)