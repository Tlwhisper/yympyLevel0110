# else 的新用法
# 2、和while、for循环搭配：如果循环顺序执行完了，没有中途跳出，就执行else语句。
#   如果中途跳出了，那就不执行else的语句。
#   干完了就怎样，没有干万就不能这样。

def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d 最大的约数是%d" % (num,count))
            break
        count -= 1
    else:
        print("%d是素数!" % num)

num = int(input("请输入一个数"))
showMaxFactor(num)


# 3、和try搭配使用
# 如果try中没有出现异常，就执行else的语句。
# 如果出现了异常，就不执行else的语句。
#  没有问题，那就干吧，
try:
    #int('abc')
    int('123')
except ValueError as reason:
    print('出错啦' + str(reason))
else:
    print('没有出现任何异常')

