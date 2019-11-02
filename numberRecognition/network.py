from keras import Sequential
from keras.engine.saving import load_model
from keras.layers import Dense
import numpy as np


class MyModel:
    def __init__(self, input_size=784, output_size=10):
        self.model = Sequential()
        self.model.add(Dense(80, activation='relu'))
        self.model.add(Dense(output_size, activation='softmax'))
        self.train = False

    def fit(self, x_train, y_train):
        '''
        拟合传入的训练数据
        :param x_train:　输入，shape为(n, 784)
        :param y_train: 输出标签，　shape为(n, 10),其中使用了one-hot表示输出的分类
        :return: 保存模型到本地的 model.h5文件中
        '''
        # 使用了adam梯度下降法，损失函数为交叉熵误差，需要评估的指标是精确度
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        # x_train和y_train就是训练所需的数据，batch_size表示同时训练多少条数据，一个epoch等于使得n*batch_size>=总训练数据条数的n
        history = self.model.fit(x_train, y_train, batch_size=32, epochs=6)
        self.model.save('model.h5')
        self.train = True
        return history

    def predict(self, x_test):
        '''
        对某一个图片进行预测
        :param x_test: 输入形状为 (784,)
        :return: 所属类别，这里返回图片表示的数字
        '''
        if not self.train:
            return 'no model, and you need to call fit method to train a model'
        self.model = load_model('model.h5')
        data = np.asarray([x_test,])
        result = self.model.predict(data)[0]
        return np.argmax(result)
