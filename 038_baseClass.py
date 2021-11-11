


class Father:
    def hello(self):
        print("正在打印父类的方法")

class Son(Father):
    def hello(self):
        print("正在打印子雷的方法")

a = Father()
print(a.hello())
#b = Son()
#print(b.hello())
