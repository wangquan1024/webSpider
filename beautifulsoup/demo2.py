from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 第一个参数是要解析的html文本，第二个参数是使用哪种解析器，
soup = BeautifulSoup(html,'lxml')
plist = soup.find_all('a')
# .string 输出一个类似于字符串的值，
# .strings 输出的是一个迭代器
# for p in plist:
#     print(p.string)

# 获取多个内容，不过需要遍历获取
# for p in soup.strings:
#     print(p)

# 获取多个内容，不过需要遍历获取，.stripped_strings 可以去掉空白内容
for p in soup.stripped_strings:
    print(p)
