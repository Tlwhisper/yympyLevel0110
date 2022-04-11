try:
    f = open('./data.txt','r')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错啦' + str(reason))
finally:
    if 'f' in locals():  # 这里多加一个判断，就好了:如果文件不存在，就不必关了
        f.close()

