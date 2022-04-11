f = open('./record.txt')
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
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy=[]
        girl = []
        count += 1

