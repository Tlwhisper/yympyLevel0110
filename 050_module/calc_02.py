
import M1.TemperatureConversion as tc  # 通过包来导入模块


print("32摄氏度对应的化石温度是%.2f" % tc.ctf(32))
print("99化石温度对应的摄氏温度是%.2f" % tc.ftc(99))

#print(__name__)  # 这里的__name__ 是__main__
#print(tc.__name__)  # 这里的__name__ 是导入的模块名TemperatureConversion
