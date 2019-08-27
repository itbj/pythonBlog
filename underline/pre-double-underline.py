

class Test:
    def __init__(self):
        self.one = 1
        self._two = 2
        self.__three = 3

test = Test()
print(dir(test))
print(test.one)
print(test._two)
print(test.__three)


# class ExtendTest(Test):
#     def __init__(self):
#         super().__init__()
#         self.one = 'aa'
#         self._two = 'bb'
#         self.__three = '__cc'
#
#     def get_three(self):
#         return self.__three
#
#
# test = ExtendTest()
# print(dir(test))
# print(test.one)
# print(test._two)
# print('重点看这个值的变量名：', test._ExtendTest__three)
# print('重点看这个值的变量名：', test._Test__three)
# print('调用自身的方法：', test.get_three())