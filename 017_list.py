a = ' I love fish.c'
a = list(a)
print (a)

b = tuple(a)
print(b)
t = max(b)
print(t)

n = len(b)
print(n)
list1 = [1, 2,3,4]
a = str(list1)
print(a)

#sorted() # 函数 返回排好序的列表
#reversed() # 函数， 返回一个迭代器
number = [ 4, 3,5,6 ,7,3,1, 8,10]
tem = list(reversed(number))
print(tem)

# enumerate 枚举，返回迭代器
tem2 = list(enumerate(number))
print(tem2)

# zip() 成对函数
a = [ 1,2,3,4,5,6,7]
b = [ 4,5,6,7]
c = list(zip(a,b))
print(c)
