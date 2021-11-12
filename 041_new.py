# 修改不可改变的类str，重写str的__new__方法。

class Cupstr(str):
    def __new__(cls,str1):
        str1 = str1.upper()
        return str.__new__(cls,str1)

a = Cupstr("I love FISHc.Com !")
print(a)

# 析构函数
class C:
    def __init__(self):
        print("我是构造函数")
    def __del__(self):
        print("我是析构函数")

c1 = C()
del c1
