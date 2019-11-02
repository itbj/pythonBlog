from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import np_utils


def get_datas():
    # 这里直接下载训练数据
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # print('查看一下各个数据的形状:', x_train.shape, y_train.shape, x_test.shape, y_test.shape)
    # 分类的个数
    n_class = 10
    x_train = x_train.reshape((-1, 784))
    y_train = np_utils.to_categorical(y_train, 10)
    x_test = x_test.reshape((-1, 784))
    y_test = np_utils.to_categorical(y_test, n_class)
    print('查看一下各个数据的形状:', x_train.shape, y_train.shape, x_test.shape, y_test.shape)
    return (x_train, y_train), (x_test, y_test)


def show_img(img):
    '''
    展示某个图片
    :param img: shape(28, 28)或者shape(784,)
    :return:
    '''
    if img.shape == (784, ):
        img = img.reshape((28, 28))
    plt.figure()
    plt.imshow(img, cmap='gray')
    plt.show()


# test上面两个方案
# (x_train, y_train), (x_test, y_test) = get_datas()
# show_img(x_train[0])