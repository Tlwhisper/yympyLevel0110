# 异常捕获，
try:
    #int('abc')
    #sum = 1 + '1'
    #f = open('aaa.txt')
    #print(f.read())
    #f.close()
    num = 1
except OSError as reason:
    print('文件出错了！出错的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错了！出错的原因是：' + str(reason))

#except (OSError,TypeError):  # 可以捕获这两种异常
#    print("出错啦")

except:
    print("出错了")



try:
    f = open('bbb.txt', 'w')
    print(f.write("我存在了"))
    sum = 1 + '1'
except (OSError,TypeError):
    print('出错了')
finally:
    f.close()


# 自己搞一个异常
raise ZeroDivisionError('除数为0的异常')


