
def upper(text):
    print(text.upper() + '!')


# u1 = upper
# print(id(u1))
# print(id(upper))
# u1('123liudong--u1')
# upper('123liudong--upper')

u2 = upper
print('u2 id:', id(u2))
print('upper id:', id(u2))
del upper
u2('test u2')
upper('test upper') # 会报错