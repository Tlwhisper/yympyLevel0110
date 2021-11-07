# lambda表达式
# 过滤器filter
# 2 map 映射，传入一个映射关系，和一个数（组），把这个数，根据前边的映射关系搞一个新的数（组）
# 3 python3设置递归层数
# import sys
# sys.setrecursionlimit(100)

g = lambda x : x * 2 + 1
tem = g(1)
print(tem)

# 过滤器filter
def odd(x): # 定义过滤器的标准函数 返回奇数
    return x % 2

tem = range(10)
show = filter(odd,tem) # show 返回的是一个迭代器
print(list(show)) 

#lambda一行实现
show = filter(lambda x : x % 2, tem)
print(list(show))

# 2 map 映射，传入一个映射关系，和一个数（组），把这个数，根据前边的映射关系搞一个新的数（组）
res = list(map(lambda x : x * 2,range(10)) )
print(res)


# 3 python3设置递归层数
# import sys
# sys.setrecursionlimit(100)

# 求阶层：
def recurMulti(num):
    if num == 1:
        return 1
    else:
        return num * recurMulti(num - 1)

number = int(input("请输入一个正整数 "))
result = recurMulti(number)
print("%d 的阶乘是 %d" % (number,result))
        

