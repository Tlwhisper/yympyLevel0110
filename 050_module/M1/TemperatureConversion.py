# 模块，任何一个程序都是模块，引入模块使用import 模块名，不加后缀
# 在相同一级的目录下使用模块名 + 对应的方法就能调用了
# 1、import 模块名
# 2、from 模块名 import 函数名
# 3、import 模块名 as 新名字


def ctf(cel):
    fah = cel * 1.8 + 32
    return fah
def ftc(fah):
    cel =(fah - 32) / 1.8
    return cel

def test():
    print("测试“0摄氏度 = %.2f 华氏度" % ctf(0))
    print("测试“0华氏度 = %.2f 摄氏度" % ftc(0))


# 2、这里使用这一句：如果是在模块内执行，就调用这个测试程序，如果是在主程序的时候，这里的__main__就是当前模块的模块名，而不必调用这个测试程序。

if __name__ =="__main__":
    test()


# 3、添加模块的导入路径。
import sys
#print(sys.path)
# 是一个列表
tem=['/home/yym/python_code/yympyLevel0110/050_module', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
# 可以添加：
#sys.path.append("/home/yym/Desktop/hahaha")
# 就行了


# 4、包管理模块
# 把一个文件夹变成包：在这个文件夹下 搞一个__init__.py的空文件。就行了
# 把相关的模块搞到这个文件夹下，
# 导入这个包内的具体模块：import 包名.模块名



