
# 这里需要解决重写构造函数的问题。
#1、调用未绑定父类对象的父类方法
# 2、使用super函数

# 多重继承

import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0,10) # 这个randint别写错了
        self.y = r.randint(1,10)
    def move(self):
        print("我的位置是：", self.x, self.y)


class GlodFish(Fish):
    pass
class Carp(Fish):
    pass


# 这里需要解决重写构造函数的问题。
#1、调用未绑定父类对象的父类方法
# 2、使用super函数

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self)   # 1.调用未绑定的父类方法，self是子类对象，而方法是父类的，但是这个方法并没有绑定父类的对象
        super().__init__()  # 2.直接使用super函数
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃获得梦想就是迟迟吃")
            self.hungry = False
        else:
            print("吃不下了")



shark1 = Shark()
print(shark1.move())
fish1 = Fish()
print(fish1.move())


# 多重继承
class Base1:
    def foo1(self):
        print("我是foo1,我为Base1代言....")

class Base2:
    def foo2(self):
        print("我是foo2,我为Base2 代言....")

class C(Base1,Base2):
    pass

c = C()
print(c.foo1())
print(c.foo2())

