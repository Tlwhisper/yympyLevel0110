# 列表使用栈结构存储，


item = [1,2,3,4,['xingxing','shuzu'],'tianshi',"stringing"]
print (item)

#append() 在列表中 添加一个元素 一次只能添加一个
item.append('linghucong')
print (item)

#extend 使用一个列表添加到另外一个列表中，参数是“一个” 列表
item.extend(['xiaoxiaoniao','tianshidechibang'])
print(item)

# insert  可以指定位置添加，两个参数
item.insert(0,'yangyanmeng_i')
print(item)


# remove() 成员方法，根据元素名删除
print(item)
print("remove删除tianshi，根据元素名删除")
item.remove("tianshi")
print(item)

#del  bif，内置函数。可以按下标删除，也可以直接删除列表
del item[3]
print(item)


# 3.pop ,又返回值，可以接收，也可以安下标弹出。
item.pop()
tem = item.pop()
item.pop(2) # 按下标弹出


#copy 列表分片slice,
item2 = item[1:3]
itme3 = item[4:]
item4 = item[:3]
itme5 = item[:] # 列表的拷贝
item6 = item  # 这个没有拷贝，只是又搞了一个名字，而已

list1 = [123, 456]
list2 = [234, 561]
print(list1 < list2)
list3 = list1 + list2 # +必须两端都是列表才行
print(list3)

list3 *= 5
print("*5，重复拷贝5遍")
print(list3)

print("小家" not in list3)

print("访问列表中列表的元素")
list4 = [123, 234, ['小家与','牡丹'],453]
print(list4[2][1])

print(dir(list))
item.append('xiaojiayu')
flag = 'xiaojiayu' in item
print (flag)

# count
print("count")
item.count('xiaojiayu')

# index
print("index")
print(item.index('xiaojiayu')) # 从左边开始查找
print(item.index('xiaojiayu',3,11))  # 从给定范围内开始查找

# reverse()
item.reverse()

# sort()
item66 = [ 3,4,6,7,8,99,80,12,43,32]
item66.sort()  # 从小到大排序
print(item66)

item66.sort(reverse=True) # 逆置成从大到小
print(item66)
