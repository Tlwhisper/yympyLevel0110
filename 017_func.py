# parameter 形参
# argument 实参
# 查看函数文档
# 返回一个元组，所以可以多个返回值。

# 1 查看函数文档 3 种方式
# 2 关键字参数，避免传参乱序
# 3 默认参数：是在定义参数的时候
# 4 可变参数，个数（收集参数）
# 5 局部、全局变量
#    如果在局部变量去修改一个全剧变量，编译器会在栈空间上重建一个同名的局部变量，
#    当回到全剧变量的时候，这个名字又是之前的全剧变量了
#    如果非要在函数内部修改全剧变量，就使用一个global关键字修饰一下
# 6 函数的嵌套
# 7 闭包：函数式编程
# 8 闭包结构，内部函数也不能修改外层函数的值
#   可以使用关键字：nonlocal


def Myfirst(num1, num2):
    result = num1 + num2
    print(result)

def multi(n1, n2):
    return (n1 * n2)

Myfirst(1,2)

print(multi(4,5))

def add(n1, n2):
    '表示两个数字的加和'
    # 表示两个数字的和
    print(n1 + n2)

# 1、查看函数文档 3 种方式
#add.__doc__
#help(add)
#print.__doc__


# 2关键字参数，避免传参乱序

def Saywhat(name, words):
    print(name +' -> '+ words)

Saywhat('小甲鱼','哈哈')
Saywhat('hahahaha','小甲鱼')
Saywhat(words='hahahaha',name='小甲鱼') #调用的时候iou使用关键字参数

# 3 默认参数：是在定义参数的时候
def Say(name='压缩',words='切碎季风前行'):
    print(name + '->' + words)
Say()
Say('皇子','的玛西亚')

# 4 可变参数，个数（收集参数）
def test(*params):
    print("参数的长度是",len(params))
    print("第2个参数是：",params[1])

test(1,"皇子",2,3,4,5)


# 5局部、全局变量
# 如果在局部变量去修改一个全剧变量，编译器会在栈空间上重建一个同名的局部变量，
# 当回到全剧变量的时候，这个名字又是之前的全剧变量了
# 如果非要在函数内部修改全剧变量，就使用一个global关键字修饰一下
num = 5
print(num)
def Myfun():
    global num
    num = 100
    print(num)
Myfun()
print(num)

# 6、函数的嵌套
def fun1():
    print("调用外层函数")
    def fun2():
        print("调用内层函数")
    fun2()

fun1()

# 7、闭包：函数式编程
def FunX(x):
    def FunY(y):
        return x * y
    return FunY


i = FunX(8)
print(i(5))

print(FunX(10)(3))

# 8、闭包结构，内部函数也不能修改外层函数的值
# 可以使用关键字：nonlocal
#def Fun1():
#    x = 5
#    def Fun2():
#        x *= x  # 这里会出错
#        return x
#    return Fun2()

def Fun1():
    x = 5
    def Fun2():
        nonlocal x
        x *= x
        return x
    return Fun2()

# 调用
tem =Fun1()
print(tem)
