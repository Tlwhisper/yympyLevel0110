# 字符串相关

str1 = 'AWFWfewfweafefFEG'
str2 = str1.casefold()  # 变成小写
print(str1)
print(str2)

# find()如果没找到会返回-1
# 而index()如果没找到会返回异常
str3 = str1 + '123'
print(str3.isalnum())

# isalpha()
# isdigit() 只包含数字返回真
# isnumeric()

# islower()
# isupper()

# upper() 小写转大写

# join()
str5 = "FishC"
str6 = '   12   34   '
print(str5.join("1234")) # 使用str5去隔开 1FishC2FishC3FishC4
print(str5)

#split() 参数为空,默认按照空格进行字符串切分，切成列表
tem = " I love read"
print(tem.split())

# strip() # 删除两边的空格
print(str6.strip())
