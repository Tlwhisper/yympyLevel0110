item = [1,2,3,4,['xingxing','shuzu'],'tianshi',"stringing"]
print item

#append()
item.append('linghucong')
print item

#extend
item.extend(['xiaoxiaoniao','tianshidechibang'])
print(item)

# insert
item.insert(1,'yangyanmeng_i')
print item


# remove() 
item.remove(2)
print item

#del
del item[3]
print item


# 3.pop
item.pop()
tem = item.pop()
item.pop(2)


#copy
item2 = item[1:3]
itme3 = item[4:]
item4 = item[:3]
itme5 = item[:]

dir(list)
flag = 'xiaojiayu' in item
print flag

# count
item.count('xiaojiayu')

# index
item.index('xiaojayu')
item.index('xiaojuayu',3,11)

# reverse()
item.reverse()

# sort()
item66 = [ 3,4,6,7,8,99,80,12,43,32]
item66.sort()
print(item66)

item66.sort(reverse=True)
print(item66)
