
# __init__ 构造函数


# 权限，共有私有，使用下划线是私有，正常不加下划线是共有都可以访问。
# python的私有是伪私有，可以通过类名访问到

# go语言中，首字母是大写就是共有，所有的包都可见，首字母是小写，只本包可见。
#name = ''  # 这里写不写都行。因为第4行自动使用了

class Ball:
    def setName(self,name):
        self.name = name
    def kick(self):
        print("我叫%s, 该死的，谁踢我" % self.name)


a = Ball()
a.setName('球A')
b = Ball()
b.setName('球B')
c = Ball()
c.setName('土豆')

a.kick()
c.kick()


# __init__ 构造函数
class BaLL:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print("我叫%s, 该死的， 谁踢我" % self.name)


a = BaLL('球A')
a.kick()


# 权限，共有私有，使用下划线是私有，正常不加下划线是共有都可以访问。
# python的私有是伪私有，可以通过类名访问到

# go语言中，首字母是大写就是共有，所有的包都可见，首字母是小写，只本包可见。
class Person:
    name = '小甲鱼'
    __age = 20
    def getAge(self):
        return self.__age

p = Person()
print(p.name)
print(p.getAge())
#print(p.__age)  # 这里会报错
print(p._Person__age) # 这里通过类名也可以访问。 类名前边加一个下划线.
