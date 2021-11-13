# 模块，任何一个程序都是模块，引入模块使用import 模块名，不加后缀
# 在相同一级的目录下使用模块名 + 对应的方法就能调用了
# 1、import 模块名
# 2、from 模块名 import 函数名
# 3、import 模块名 as 新名字



import TemperatureConversion
import TemperatureConversion as tc

print("32摄氏度对应的化石温度是%.2f" % TemperatureConversion.ctf(32))
print("99化石温度对应的摄氏温度是%.2f" % TemperatureConversion.ftc(99))

print("32摄氏度对应的化石温度是%.2f" % tc.ctf(32))
print("99化石温度对应的摄氏温度是%.2f" % tc.ftc(99))

#print(__name__)  # 这里的__name__ 是__main__
#print(tc.__name__)  # 这里的__name__ 是导入的模块名TemperatureConversion
