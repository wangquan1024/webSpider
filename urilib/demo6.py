#cookiejar

from urllib import request
from urllib import parse
from http import cookiejar

#声明一个cookiejar实例来保存cookie
cookie = cookiejar.CookieJar()
#创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#构建opener
opener = request.build_opener(handler)
res = opener.open("http://www.baidu.com")
for item in cookie:
    print("name="+item.name)
    print("Value="+item.value)