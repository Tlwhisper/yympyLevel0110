
# 列表，[] 方括号，
# range 从0开始，3个参数
# break,continue
text = "yangyanmeng"
for i in text:
    print(i + ' ')

# 打印在同一行
for i in text:
    print(i, end = ' ')

print(" ")

name = ["jack","tianxia","huangzi","demaxiya"]
for it in name:
    print(it,len(it))

print("next line 0 1 2 3 4 \n") # 这里range从0开始，右边闭区间
for i in range(5):
    print(i)

print("next line 2 3  4 5 6 7 \n")
for i in range(2,8):
    print(i)

print("next line 1 3 5 7 9 \n")
for i in range(1,10,2):
    print(i)

print("next line 5 1 7 3 9 5 11 7 13 9 \n")
for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 5
    print(i)
