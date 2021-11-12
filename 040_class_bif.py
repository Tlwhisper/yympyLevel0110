# 一些类相关的内置函数
# issubclass( 子类, 父类（父类的列表） ) 1、有继承关系的，第二个参数是一个类的列表。
class A:
    pass

class B(A):
    pass
res = issubclass(B, A)
print(res)

res2 = issubclass(B,B)
print(res2)

res3 = issubclass(B, object)
print(res3)

res4 = issubclass(A, B)  # False
print(res4)


# 检查 对象是否是类（类的元组）的对象
# isinstance(object, classinfo)
# 如果第一个参数不是对象，结果就永远是假的

# 3、先检查有没有这个属性
# hasattr(obj,name)
class C:
    def __init__(self, x = 0):
        self.x = x

c1 = C()
print(hasattr(c1,'x'))
print(hasattr(c1,'z'))

# getattr(obj,name, [ 默认输出信息])
tem = getattr(c1,'x')
print(tem)
tem2 = getattr(c1,'y',"您所访问的属性不存在。。。。")
print(tem2)

# setattr(obj, name,[默认])
setattr(c1,'y',"fish_C")  # 如果存在就修改，如果不存在就生成并初始化。

tem2 = getattr(c1,'y',"您所访问的属性不存在。。。。")
print(tem2)

delattr(c1,'y') # 删除了这个属性
tem2 = getattr(c1,'y',"您所访问的属性不存在。。。。")
print(tem2)


#  property() 加一层控制类内方法的中间层，解耦
class D:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)

d1 = D()
tem = d1.getSize()
print(tem)
print(d1.x)
d1.x = 20
print(d1.x)
print(d1.size)
del d1.x
#print(d1.x)  # 删除之后，再访问会报错
