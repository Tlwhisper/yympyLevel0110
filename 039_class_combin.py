


# 类进行组合
# 水池里有乌龟和鱼儿

# 绑定概念
# python严格要求方法需要有实例的绑定才能调用。~
# 就是类中定义的方法的第一个形参：self

# 类中定义的属性是静态变量，属性也是一样。即使类对象被删除。实例对象中的也还存在。类中定义的属性,：依然存放在内存中。
class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Poll:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def printNum(self):
        print("我是水池 有乌龟 %d 个，有小鱼 %d 条" % (self.turtle.num,self.fish.num))

poll = Poll(4,20)
print(poll.printNum())


# 绑定概念
# python严格要求方法需要有实例的绑定才能调用。~
# 就是类中定义的方法的第一个形参：self
class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print(self.x, self.y)

dd = CC()
print("dd.__dict__")
print(dd.__dict__)

print("CC.__dict__")
print(CC.__dict__)  # 类对象：通过类名，直接访问的方式，就是类对象，

dd.setXY(5,12)  # 实例对象  通过类，实例化了一个对象
print("dd.__dict__")
print(dd.__dict__)

print("CC.__dict__")
print(CC.__dict__)
# 类中定义的属性是静态变量，属性也是一样。即使类对象被删除。实例对象中的也还存在。类中定义的属性,：依然存放在内存中。

