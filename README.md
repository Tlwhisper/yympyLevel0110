# yympyLevel0110
study notes for myself to review


增加一个type函数，和int()、str()、float()强制转换类型
增加运算符操作 02_01_fun

增加打飞机游戏：

加载背景音乐
播放音乐（单曲循环）
我方飞机诞生
interval = 0
while True:
	if 用户关闭按钮
		退出程序
	interval += 1
	if interval == 50
		interval = 0
		小飞机诞生
	小飞机移动一个位置
	屏幕刷新

	if 用户鼠标移动
		我方飞机中心位置 = 用户鼠标位置
		屏幕刷新
	if 我方飞机与小飞机肢体冲突
		我方挂
		修改我方飞机图案
		打印“game over”
		停止背景音乐




# 02_2_input_elif.py
input输入的变量存起来
条件分支，elif
断言：assert，为真接着执行

010_list.py
列表的
列表的插入，expand(),extand(),insert()
列表的删除：pop(),带参pop()
列表的拷贝：[:]
排序，拷贝

016_format.py
格式化，根据下标指定位置格式化，
	根据变量名格式化
2，8，16进制格式化，
浮点数格式化



017_func.py
	函数相关
	默认参数，关键字参数，可变个数参数
# 查看函数文档
# 返回一个元组，所以可以多个返回值。

# 1 查看函数文档 3 种方式
# 2 关键字参数，避免传参乱序
# 3 默认参数：是在定义参数的时候
# 4 可变参数，个数（收集参数）
# 5 局部、全局变量
#    如果在局部变量去修改一个全剧变量，编译器会在栈空间上重建一个同名的局部变量>，
#    当回到全剧变量的时候，这个名字又是之前的全剧变量了
#    如果非要在函数内部修改全剧变量，就使用一个global关键字修饰一下
# 6 函数的嵌套
# 7 闭包：函数式编程
# 8 闭包结构，内部函数也不能修改外层函数的值
#   可以使用关键字：nonlocal


021_lambda.py
# lambda表达式
# 过滤器filter
# 2 map 映射，传入一个映射关系，和一个数（组），把这个数，根据前边的映射关系搞一
个新的数（组）
# 3 python3设置递归层数
# import sys
# sys.setrecursionlimit(100)


026_dict.py
# 字典，dict,使用花括号 {}
# 1 bif内置函数
# 2 成员资格运算符： in not in 
# 3 clear() 清空函数
# 4 copy浅拷贝
# 5 pop(),poptiem()
# 6 update()使用一个字典去更新另外一个字典


027_set.py
集合操作


030_handle_file.py 
030.1_handle_file.py 
把3段对话，写入6个文件中








