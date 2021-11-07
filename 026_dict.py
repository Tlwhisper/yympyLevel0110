# 字典，dict,使用花括号 {}
# 1 bif内置函数
# 2 成员资格运算符： in not in 
# 3 clear() 清空函数
# 4 copy浅拷贝
# 5 pop(),poptiem()
# 6 update()使用一个字典去更新另外一个字典

dict1 = {'李宁':'一切皆有可能','耐克':'just do it','阿迪':'nothing is impossible'}
print(dict1)
print(dict1['李宁'])

# 1 bif内置函数
dict2 = {}
print(dict2)
# dict2.fromkeys((1,2,3)) # 产生一个新的字典，
print(dict2.fromkeys((1,2,3)))   # 打印这个新的字典，
print(dict2) # 这里还是之前的字典

dict3 = dict2.fromkeys((1,2,3),"哈利波特")
print(dict3)

dict1 = dict1.fromkeys(range(32),'赞')

for eachkey in dict1.keys():
    print(eachkey)

for eachVal in dict1.values():  # .values() ,而不是vals()
    print(eachVal)

for eachItem in dict1.items():
    print(eachItem)


# 2 成员资格运算符： in not in 
print( 32 in dict1)
print( 31 in dict1)

print(dict1.get(32,'没有这个元素'))  # 如果没有，就使用这个默认形参
print(dict1.get(31,'没有这个元素'))  # 如果有就直接打印出来，

# 3 clear() 清空函数
a = dict1
b = a
a = {}
print("直接赋值为空之后：打印b")
print(b)  # 因为还在内存里，可以通过另外的变量名来访问。

print("使用clear()方法,打印b,打印dict1")
a = b
a.clear()
print(b)   # 打印为空
print(dict1)  # 打印为空


# 4 copy浅拷贝
a = {1:'one', 2:'two', 3:'three'}
b = a.copy()
c = a
print(id(a))
print(id(b))
print(id(c))

c[4] = 'four'
print("c[4] = 'four'之后")
print(id(a))
print(id(b))
print(id(c))

print(a)
print(b)  # 浅拷贝，copy()函数之后，并不会更新
print(c)


# 5 pop(),poptiem()
print("弹出1号元素的值")
print(a.pop(1)) # one
print(a) # {2: 'two', 3: 'three', 4: 'four'}

print("随机弹出一个item") #
print(a.popitem()) # 随机弹出一个元素,有的随机，有的是最后一个，版本不同吧
print(a)  # 剩下的: {2: 'two', 3: 'three'}

# 6 update()使用一个字典去更新另外一个字典
a = {1:'one', 2:'two', 3:'three', 4:'four', 5:'皇子'}
print(a)
b = { 3:'小狗', 4:'四'}
a.update(b)  # 使用一个字典去更新另外一个字典
print(a)
