# property
# 描述符类
# 描述符 就是将某种特殊类型的类的实例，指派给另一个类的属性

# 练习题
# 写一个摄氏温度和华氏温度
# 定义一个温度类，然后定义两个描述符类，描述摄氏度和华氏度两个属性
# 要求两个属性会自动转换，也就是你给华氏度这个属性赋值，可以打印摄氏度的值

class MyDescriptor:
    def __get__(self, instance, owner):
        print("getting...",self, instance, owner)

    def __set__(self, intstance, value):
        print("setting...",self, instance, value)

    def __delete__(self, instance):  # 这里没有缩写
        print("deleting...",self,instance)


class Test:
    x = MyDescriptor()


test = Test()
test.x

print(test)

print(Test)




class MyProperty:
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self,instance, value):
        self.fset(instance, value)

    def __delete__(self,instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x =MyProperty(getX, setX, delX)


c1 = C()
c1.x = 'X-man'
print(c1.x)
print(c1._x)


# 写一个摄氏温度和华氏温度
# 定义一个温度类，然后定义两个描述符类，描述摄氏度和华氏度两个属性
# 要求两个属性会自动转换，也就是你给华氏度这个属性赋值，可以打印摄氏度的值

class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self,instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self,instance,owner):
        #return self.value
        return instance.cel * 1.8 +32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


temp = Temperature()
temp.cel = 30
print(temp.fah)

temp.fah = 100
print(temp.cel)
