# 实现把./record.txt这个文件按照===分割成不同的对话，
#把双方各自说的话，写入各自的文件，并写入不同的文件

def save(boy, girl, count):  # 把分割之后的 一段对话 保存到两个文件
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(filename): # 分割这个文件
    f = open(filename)
    #f = open('./talk.txt')
    #print(f.read())
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6]!='======':
            (role,spoken) = each_line.split(':', 1)
            if role =='小甲鱼':
                boy.append(spoken)
            if role == '小客服':
                girl.append(spoken)
        else:
            save(boy,girl,count)
            boy.clear()
            girl.clear()
            count += 1
    save(boy,girl,count)  # 最后一次还得保存,

split_file('./record.txt')
