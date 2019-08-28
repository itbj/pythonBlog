
def add(x):
    return x+1


def upper(text):
    return text.upper()


mylist = [add, upper]
print(mylist)

result = mylist[0](2) #调用了add函数
print(result)

result2 = mylist[1]("are you ok?")
print(result2)