
class C:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    def __getattr__(self, name):
        print("getattr")
    def __setattr__(self,name, value):
        print("setattr")
        super().__setattr__(name,value)
    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)

c = C()
#c.x

c.x = 1

c.x

del c.x

# 死循环陷阱
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # self.name = value
            super().__setattr__(name, value)
    def getArea(self):
        return self.width * self.height


c1 = Rectangle(4 , 5)
print(c1.getArea())

