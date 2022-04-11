# format
# 下标格式化
tem = "{0} love {1}.{2}".format("I", "Fishc", "com")
print(tem)
# 关键字格式化
tem = "{a} love {b}.{c}".format(a="I", b="Fishc", c="com")
print(tem)

tem1 = '{0:.1f}{1}'.format(27.658,'GB') 
print(tem1) # 27.7GB


tem = '%c %c %c' % (97, 98, 99)
print(tem)

tem = '%o %o %o %o %o %o %o  %o' % (1,3,6,7,8,9,10,11)
print(tem)
tem = '%x %x %x %x %x %x %x %x' % (1,3,6,7,8,9,10,11)
print(tem)
