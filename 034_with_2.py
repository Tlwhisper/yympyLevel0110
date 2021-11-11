# 可以使用with来，让编译器来自动调用finally语句中的close

try:
    with open('./data.txt','r') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦' + str(reason))

