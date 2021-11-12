# 如果想定制不可改变的容器：
# 只要定义两个：__len__()和__getitem__()方法就行
# 如果想定制可变容器，还要定义__setitem__()和delitem__()方法

class MyList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]


c1 = MyList(1, 3,5,7,9)
c2 = MyList(2 ,4,6,8,10)
print(c1[1])

c1[1]+c1[2]
print(c1.count)
