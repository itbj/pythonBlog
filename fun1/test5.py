
class A:
    def __init__(self):
        self.n = 'test object can be a function'

    def __call__(self, *args, **kwargs):
        print(self.n)


a = A()
a() #a是对象，但目前就如同函数一样。

print(callable(A))
print(callable('strings'))