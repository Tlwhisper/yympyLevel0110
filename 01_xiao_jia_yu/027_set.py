# set集合，无序，去重
tem1 = [1 ,1, 3,4,5 ,6,7,8,8,9,9,9,10]
print(tem1)
tem2 = list(set(tem1))
print(tem1)
print(tem2)

tem2.add(11)
print(tem2)
tem2.remove(1)
print(tem2)

num1 = frozenset([1,2,3,4,5])
#num1.add(9)  # 不可变的集合,没有这个方法






