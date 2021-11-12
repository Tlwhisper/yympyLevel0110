# 一个作业，实现一个计时器，求时间的和
# 两个魔法方法
class A():
    def __str__(self):
        return "小甲鱼是帅哥"

a = A()
print(a)
a

class B():
    def __repr__(self):
        return "小甲鱼是大哥"


b = B()
print(b)
b

import time as t

class MyTimer():
    def __init__(self):
        self.prompt = "未开始计时"
        self.begin = 0
        self.end = 0
        self.lasted = []
        self.unit = ['年', '月', '天','小时', '分钟', '秒钟']

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) +self.unit[index])
        return prompt

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()停止计时"
        print("计时结束")
    # 停止计时
    def stop(self):
        if not self.begin:
            print("请先调用start开始计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了 "
        for index in range (6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        print(self.prompt)


tt = MyTimer()
tt.start()
t.sleep(4)
tt.stop()
t2 = MyTimer()
t2.start()
t.sleep(2)
t2.stop()
print(tt+t2)
