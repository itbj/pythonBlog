from numberRecognition.dataDeal import get_datas, show_img
from numberRecognition.network import MyModel


def train():
    model = MyModel()
    (x_train, y_train), (x_test, y_test) = get_datas()
    his = model.fit(x_train, y_train)
    print('训练完毕!相关信息如下:')
    print('模型识别精度为:', his.history['acc'][-1])
    print('--'*24)
    print('开始使用模型进行预测:')
    img = x_test[0]
    print(img.shape)
    show_img(img)
    print('测试集第一张图片属于　', model.predict(img))


train()
