# 斐波那切数列
# 递归也是分治思想
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibo(n - 1) + fibo(n - 2))

num = int(input("请输入一个数"))
res = fibo(num)
print("%d 个斐波数字是: %d" % (num,res))

