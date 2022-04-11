# oo,面向对象，oop面向对象编程。封装继承多肽。
# 多肽：不同对象对同一方法具有不同的响应。
# ooa 面向对象分析
# ood，面向对象设计:
# 类名首字母大写，方法都是小写字母，权限问题：__双下划线是私有，没下划线是共有。_单下划线是不想被外部访问，但是也可以被访问到

class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouse = '大嘴'
    # 方法
    def climb(self):
        print("我正在往前帕")
    def run(self):
        print("我正在奔跑")
    def bite(self):
        print("咬死")
    def sleep(self):
        print("困了困了")

tt = Turtle()
tt.bite()
tt.climb()

class Mylist(list):
    pass  # 占位符
list2 = Mylist()
list2.append(4)
list2.append(1)
list2.append(8)
list2.append(0)
list2.sort()
print(list2)
