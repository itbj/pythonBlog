
def outter(a):
    def in1(b):
        print(a + b + ' in1 be called')

    in1('----'+a+'----')
    print('outter方法最后一步')

outter('123liudong')

# outter.in1('test in1') #直接报错
# in1('in1 test')


def outter2():
    def in2():
        print('内部方法')
    return in2


# 返回了in2()内部方法
inner_method = outter2()
# 调用in2方法
inner_method()


def bibao(text):

    def test_bibao(x):
        print(text + '  ' + x)

    return test_bibao

in_bibao = bibao('返回嵌套函数')
in_bibao('内部函数test_bibao被调用了')
in_bibao('test2')