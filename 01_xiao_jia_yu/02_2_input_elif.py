score = int(input("请输入一个数字"))
if 100 >= score >= 90:
    print("a")
elif 90 > score >= 80:
    print("b")
elif 80 > score >= 70:
    print("c")
elif 70 > score >= 60:
    print("d")
else:
    print("d")
print(score)


# 3目运算符
print("3目运算符")
x = 10
y = 20
z = x if x > y else y
print(z)

assert (3 < 4) # 如果是对的，就接着往后面执行，如果是错的，就会崩调，抛出异常


