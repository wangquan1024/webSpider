# 保存cookie到文件中

from urllib import request
from urllib import parse
from http import cookiejar

# filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例
# cookie = cookiejar.MozillaCookieJar(filename=filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
# ignore_expires的意思是如果cookies已经过期也将它保存并且文件已存在时将覆盖，
# cookie.save(ignore_discard=True,ignore_expires=True)

# cookie的读取
cookie = cookiejar.MozillaCookieJar()
# 读取cookie数据
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
req = request.Request("http://www.baidu.com")
res = opener.open(req)
print(res.read())

