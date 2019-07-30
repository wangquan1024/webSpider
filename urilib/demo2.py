from urllib.parse import urlparse

# urlsplit与urlparse相似，不过没有params而已
res = urlparse("http://www.baidu.com/3/?username=qs/#1")
print(res.scheme)
print(res.netloc)
print(res.path)
print(res.params)
print(res.query)
print(res.fragment)