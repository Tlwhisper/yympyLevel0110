# 生成器
def myGen():
    print("生成器被调用")
    yield 1
    yield 2

myG = myGen()
next(myG)



for i in myGen():
    print(i)


# 实现一个斐波那切数列
def fibs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a
    return a

for each in fibs():
    if each > 100:
        break
    print(each, end=' ')



# 推导式
# 列表推导式
a = [i for i in range(10) if not (i % 2) and (i % 3)]
print(a)

# 字典推导式
b = { i : i % 2 == 0 for i in range(10)}
print(b)

# 没有字符串推导式

# 推导式作为函数参数传进来
tem = sum ( i for i in range(100) if i % 2)
print(tem)
