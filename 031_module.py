import os
print(os.getcwd())  # 返回当前的工作目录
print(os.listdir('./'))  # 列举当前目录的东西
#print(os.system('cmd'))


# pickle 把对象搞成二进制格式（字介流），保存到文件
# 一般把字典搞成pickle,泡菜

import pickle
my_list = [1,2,3,'杨',['皇子','盖仑']]
pickle_file = open('my_list.pkl','wb')  # 创建一个二进制文件my_list.pkl，
pickle.dump(my_list,pickle_file)  # 把列表 “倒进” 泡菜坛子：二进制文件
pickle_file.close()  # 这个文件对象关闭

# 重新打开，和读取
pickle_file = open('my_list.pkl','rb')  # 文件对象，
my_list2 = pickle.load(pickle_file)  # pickle包的函数：参数（文件对象）
print(my_list2)  
