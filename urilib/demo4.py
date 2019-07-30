from urllib import request

# 创建一个代理
handler = request.ProxyHandler({"http":"120.83.100.68:9999"})

# 创建一个opener
opener = request.build_opener(handler)
req = request.Request('http://www.httpbin.org/')
# 使用opener.open请求网页
res = opener.open(req)
print(res.read())
