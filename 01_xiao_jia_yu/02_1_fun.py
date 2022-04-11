# 测试type函数
a = "haha"

# 强制转换类型
a = '1234'
b = int(a)
c = float(a)
d = str( b)
print("a 的数据类型" )
print( type(a))
print("b 的数据类型") 
print( type(b))
print("c的数据类型") 
print( type(c))
print("d 的数据类型")
print( type(d))

print(isinstance(a, str))  # 直接使用这个，给出一个作为参考，返回真假




# 幂运算            **
# 单目运算符 + -
# 算术运算符
# 比较运算符
# 逻辑运算符  not and or 

# 加减乘除 / float 除法   // 地板除法
a = b = c = d = 100
print(a / 3)  # 直接除法 == 33.333333333333336
print (a // 3) # 地板除法 == 33
a = -3 ** 2 # -9 **幂运算符比左边的单目运算符 级别高
b = 3 ** -2 ## 0.11111 ** 幂运算符比右侧的单目运算符 级别低
print(a)
print (b)

# 逻辑操作符
 # and or not 
print(3 < 4  <  5) # 解释成： (3 < 4) and (4 < 5)
