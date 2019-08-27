
class Test:
    def __init__(self):
        self.__one__ = '__one__'

    def __get_some__(self):
        print('__get_some__方法被调用了')


t = Test()
print(t.__one__)
t.__get_some__()
print(dir(t))