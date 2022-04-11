# tuple 数据类型，不可变了
# 识别tuple 的是 小括号里边的 逗号，
# 插入操作，没有，但是可以通过，截取，拼接的方式实现，
#有一个 * 重复操作符 可用
tuple1 = ("小家与", "hahah", "皇子")
print(tuple1)
tuple1 = tuple1[:1] + ("德玛西亚",) + tuple1[1:]
print(tuple1)
