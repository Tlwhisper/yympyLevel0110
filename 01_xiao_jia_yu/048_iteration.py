# 迭代器

links = {'鱼儿':'www.baidu.com','皇子':'的玛西亚','提莫':'艾欧尼亚','人类':'动物世界'}
for each in links:
    print("%s --> %s" % ( each, links[each]))



# 斐波那切数列
class Fibs:
    def __init__(self, n = 10):
        self.a = 0
        self.b = 1
        self.n =n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


fibs = Fibs()
for each in fibs:
    print(each)




