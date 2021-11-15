
# URL由3部分组成

# protocol    ://  hostname[:port]  /  path/[;parameters][?query]# fragment

# 1、协议：http, https, ftp, file, ed2k,...
# 2、存放资源的服务器的域名系统或IP地址，（有时候需要加端口号，各传输协议有默认的端口号）
# 3、资源的 具体地址，如目录，或文件名

# urllib 是一个包，有4个模块 
# urllib.request 对服务器的请求，发出，跳转，安全。
# urllib.error
# urllib.parse
# urllib.robotparser

import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")  # 从服务器获取网页：是一个对象
html = response.read()  # 把这个对象 读出来，是二进制的数据
html = html.decode("utf-8")  # 把二进制数据 解码 成 html
print(html)
