# 文件操作

#f = open('/home/yym/python_code/yympyLevel0110/README.md')
f = open('./README.md')
tem = f.read()
#print(tem)

# seek(offset, from) # from 0:开头。 1 当前位置。2：代表文件末尾。
tem2 = f.read() # 读不到东西，
print(tem2)
print(f.tell())
f.seek(0,0)
print(f.tell())
print(f.readline())  # 打印读出来的一行
tem3 = f.read()
print(tem3)

# 迭代每一行读取
f.seek(0,0)
for each_line in f:
    print(each_line)
