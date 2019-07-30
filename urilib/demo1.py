from urllib.request import urlopen,urlretrieve
from urllib.parse import urlencode,parse_qs

# python3中包含request，error，parse和robotparser4个模块
# res = urlopen("http://www.baidu.com")
# print(res.read().decode('utf-8'))

# retrieve可以直接将网页下载到本地
# urlretrieve('http://www.baidu.com','baidu.html') 

# urlencode对特殊字符进行编码
data = {'name': '刘德华','value': '123'}
qs = urlencode(data)
print(qs)

# parse_qs对编码之后的进行解码
qs2 = parse_qs(qs)
print(qs2)
