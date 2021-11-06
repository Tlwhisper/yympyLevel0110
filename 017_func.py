# parameter 形参
# argument 实参
# 查看函数文档



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

# 查看函数文档 3 种方式
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
